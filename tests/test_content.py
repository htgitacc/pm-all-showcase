"""A tartalom szerkezeti épsége: azonosítók, hivatkozások, mintafájlok, README-számok."""

from __future__ import annotations

import itertools
import re

from conftest import ROOT, example_docs, read_doc, sample_docs

from pm_app import content


def _phases():
    return content.load_phases()


def _docs():
    return content.load_doc_index()


def test_app_validation_is_clean():
    assert content.validate() == []


def test_ids_are_unique():
    doc_ids = [d["id"] for p in _phases() for d in p.get("documents", [])]
    item_ids = [i["id"] for p in _phases() for i in p.get("checklist", [])]
    assert len(doc_ids) == len(set(doc_ids))
    assert len(item_ids) == len(set(item_ids))


def test_mandatory_flag_is_explicit():
    """A dokumentumoknál és a checklistnél eltér a kód alapértéke — ezért legyen mindig kiírva."""
    for phase in _phases():
        for entry in phase.get("documents", []) + phase.get("checklist", []):
            assert isinstance(entry.get("mandatory"), bool), entry["id"]


def test_every_document_has_an_existing_sample():
    for doc in _docs().values():
        assert doc.get("sample_file"), doc["id"]
        assert (ROOT / doc["sample_file"]).exists(), doc["sample_file"]


def test_every_mandatory_document_is_on_a_checklist():
    referenced = {
        ref for p in _phases() for item in p.get("checklist", []) for ref in content.doc_refs(item)
    }
    missing = [d["id"] for d in _docs().values() if d.get("mandatory") and d["id"] not in referenced]
    assert missing == []


def test_mandatory_step_has_a_mandatory_output():
    docs = _docs()
    for phase in _phases():
        for item in phase.get("checklist", []):
            refs = content.doc_refs(item)
            if item["mandatory"] and refs:
                assert any(docs[r]["mandatory"] for r in refs), item["id"]


def test_no_orphan_markdown_files():
    prince2 = content.load_prince2()
    referenced = {d["sample_file"] for d in _docs().values()}
    referenced |= {d["sample_file"] for d in prince2.get("documents", [])}
    referenced.add(prince2["primer_file"])
    itil4 = content.load_itil4()
    referenced |= {d["sample_file"] for d in itil4.get("documents", [])}
    referenced.add(itil4["primer_file"])
    for doc in _docs().values():
        referenced |= set((doc.get("examples") or {}).values())
    on_disk = {p.relative_to(ROOT).as_posix() for p in sample_docs() + example_docs("koris")}
    assert on_disk - referenced == set()


def test_readme_status_table_matches_content():
    """A README „Tartalmi állapot" táblája ne mondjon mást, mint a YAML."""
    readme = read_doc("README.md")
    rows = {}
    for line in readme.splitlines():
        m = re.match(r"\| (\d)\. [^|]+\| (\d+) \| (\d+) \| (\d+) \|", line)
        if m:
            rows[int(m.group(1))] = tuple(int(x) for x in m.group(2, 3, 4))
    assert len(rows) == 6
    for phase in _phases():
        docs = phase["documents"]
        expected = (len(docs), sum(d["mandatory"] for d in docs), len(phase["checklist"]))
        assert rows[phase["number"]] == expected, phase["id"]


def test_phase_gate_dates_are_not_before_their_criteria():
    """A Kezdeményezés kapuja nem követelheti meg a kapudöntés után tartott kick-offot."""
    initiation = content.phase_by_id("initiation")
    criteria = " ".join(initiation["gate"]["criteria"]).lower()
    assert "megtartott kick-off" not in criteria


# A YAML-ban a `- Ellenőrizd: minden sorban…` listaelem kettőspont + szóköz miatt
# nem szöveg, hanem egykulcsos szótár lesz, és a felületen `{'Ellenőrizd': …}`
# formában jelenik meg. Ezek a listák csak szöveget tartalmazhatnak.
STRING_LISTS = {"criteria", "contents", "how", "participants", "agenda", "adds",
                "when_prince2", "when_pmi"}


def _colon_trap(node, path, found):
    if isinstance(node, dict):
        for key, value in node.items():
            _colon_trap(value, path + [str(key)], found)
    elif isinstance(node, list):
        has_text = any(isinstance(v, str) for v in node)
        for value in node:
            single = isinstance(value, dict) and len(value) == 1
            if single and (has_text or path[-1] in STRING_LISTS):
                found.append("/".join(path) + f" → {value}")
            _colon_trap(value, path, found)


def test_yaml_lists_have_no_colon_trap():
    import yaml

    found = []
    for path in sorted((ROOT / "content").rglob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        _colon_trap(data, [path.name], found)
    assert found == []


def test_sample_headers_do_not_merge_into_one_paragraph():
    """Az egymás alatti `**Címke:** érték` sorokat a markdown egy bekezdéssé vonná
    össze — ezért a sor végén kemény sortörés (visszaperjel) kell."""
    label = re.compile(r"\*\*[^*]+:\*\*")
    block = re.compile(r"\s*(\||>|#|- |\* |\d+\. |```)")
    merged = []
    for path in sorted((ROOT / "docs").rglob("*.md")):
        lines = path.read_text(encoding="utf-8").split("\n")
        in_code = False
        for cur, nxt in itertools.pairwise(lines):
            if cur.startswith("```"):
                in_code = not in_code
            if in_code or not cur.strip() or block.match(cur):
                continue
            if label.match(nxt) and not cur.endswith(("\\", "  ")):
                merged.append(f"{path.name}: {cur[:60]}")
    assert merged == []


def test_requirements_are_pinned_exactly():
    # Pontos verziók: a Streamlit Cloud minden Reboot-nál újratelepít,
    # egy csak alsó korlátos sor csendben új főverziót húzna be az élő demó alá.
    for name in ("requirements.txt", "requirements-dev.txt"):
        lines = [l.split("#")[0].strip() for l in read_doc(name).splitlines()]
        reqs = [l for l in lines if l and not l.startswith("-r ")]
        assert reqs, name
        for req in reqs:
            assert re.fullmatch(r"[A-Za-z0-9_.\-]+==[0-9][0-9A-Za-z.]*", req), req


def test_public_demo_hides_tracebacks():
    # A nyilvános demón a hiba ne mutasson tracebacket fájlútvonalakkal (a konzolra így is kiíródik).
    import tomllib

    config = tomllib.loads(read_doc(".streamlit/config.toml"))
    assert config["client"]["showErrorDetails"] in ("type", "none")


# ------------------------------------------------------------------ több mintaprojekt


def test_the_first_sample_project_is_the_complete_one():
    projects = content.sample_projects()
    assert [p["id"] for p in projects] == ["xyo", "koris"]
    assert all(p.get("short_name") and p["name"] and p["idea_doc"] for p in projects)
    # az elsődleges projekt minden dokumentumához van minta (sample_file) — ez az alap
    assert all(d.get("sample_file") for d in _docs().values())


def test_doc_examples_lists_the_primary_first_and_only_existing_files():
    idea = _docs()["project_idea"]
    assert [e["id"] for e in content.doc_examples(idea)] == ["xyo", "koris"]
    planning_doc = _docs()["scope_statement"]
    assert [e["id"] for e in content.doc_examples(planning_doc)] == ["xyo"]   # a Kőrisnek még nincs 2. fázisa
    broken = dict(idea, examples={"koris": "docs/peldak/koris/nincs-ilyen.md"})
    assert [e["id"] for e in content.doc_examples(broken)] == ["xyo"]          # hiányzó fájl nem jelenik meg


def test_validate_reports_a_broken_or_unknown_example(monkeypatch):
    index = {key: dict(value) for key, value in content.load_doc_index().items()}
    index["project_idea"]["examples"] = {"koris": "docs/peldak/koris/nincs-ilyen.md", "ismeretlen": "x.md"}
    monkeypatch.setattr(content, "load_doc_index", lambda: index)
    problems = content.validate.__wrapped__()
    assert any("hiányzó koris-minta" in p for p in problems)
    assert any("ismeretlen mintaprojekt" in p and "ismeretlen" in p for p in problems)


def test_framework_texts_name_the_project_as_an_example():
    # A keret szövegei nem állíthatják általános szabályként, ami csak a Xyo-ra igaz: a Xyo
    # személyneveit csak zárójeles példa mellett, projekt-megjelöléssel használhatjuk.
    text = read_doc("content/phases/1-initiation.yaml")
    for name in ("Nagy Péter", "Kovács Anita", "Kiss Réka", "Varga Eszter", "Balogh Tamás", "Horváth Júlia"):
        for line in text.splitlines():
            if name in line:
                assert "Xyo" in line or "Kőris" in line, f"projektjelölés nélküli név a keretben: {line.strip()}"
