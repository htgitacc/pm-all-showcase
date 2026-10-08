"""A tartalom szerkezeti épsége: azonosítók, hivatkozások, mintafájlok, README-számok."""

from __future__ import annotations

import re

from conftest import ROOT, read_doc

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
    on_disk = {p.relative_to(ROOT).as_posix() for p in (ROOT / "docs").rglob("*.md")}
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
        for cur, nxt in zip(lines, lines[1:]):
            if cur.startswith("```"):
                in_code = not in_code
            if in_code or not cur.strip() or block.match(cur):
                continue
            if label.match(nxt) and not cur.endswith(("\\", "  ")):
                merged.append(f"{path.name}: {cur[:60]}")
    assert merged == []
