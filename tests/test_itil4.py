"""Az ITIL 4-réteg: a szerkezet az ITIL 4 hivatalos felépítését követi, a Xyo-példák a
mintadokumentumok számait és szereplőit használják, az oldal hibátlanul fut."""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

import pytest
from conftest import read_doc, section, tables
from streamlit.testing.v1 import AppTest

from pm_app import content, itil4

PIR = "docs/6-benefits/06-pir.md"
LESSONS = "docs/5-closure/05-tanulsagok-naploja.md"
T0 = "docs/6-benefits/03-t0-baseline-jegyzokonyv.md"
RUNBOOK = "docs/5-closure/02-uzemeltetesbe-adas-runbook.md"

# Az ITIL 4 hivatalos angol nevei (a Foundation-tananyag szerint)
PRINCIPLES = [
    "Focus on value", "Start where you are", "Progress iteratively with feedback",
    "Collaborate and promote visibility", "Think and work holistically",
    "Keep it simple and practical", "Optimize and automate",
]
DIMENSIONS = [
    "Organizations and people", "Information and technology",
    "Partners and suppliers", "Value streams and processes",
]
ACTIVITIES = {
    "plan": "Plan", "improve": "Improve", "engage": "Engage",
    "design_transition": "Design and transition", "obtain_build": "Obtain/build",
    "deliver_support": "Deliver and support",
}
DETAILED = {
    "Continual improvement", "Change enablement", "Incident management", "Problem management",
    "Service request management", "Service desk", "Service level management",
}
PURPOSE_ONLY = {
    "Information security management", "Relationship management", "Supplier management",
    "IT asset management", "Monitoring and event management", "Release management",
    "Service configuration management", "Deployment management",
}


@pytest.fixture(scope="module")
def data():
    return content.load_itil4()


def _texts(node) -> list[str]:
    """A YAML összes szöveges értéke (a beágyazott listákból és szótárakból is)."""
    if isinstance(node, str):
        return [node]
    if isinstance(node, dict):
        return [t for v in node.values() for t in _texts(v)]
    if isinstance(node, list):
        return [t for v in node for t in _texts(v)]
    return []


def _flat(data) -> str:
    return " ".join(" ".join(t.split()) for t in _texts(data))


def _pir() -> dict[str, list[str]]:
    rows = tables(section(read_doc(PIR), "2. A vállalt hasznok"))[0]
    return {r[0]: [c.replace("*", "").strip() for c in r] for r in rows if re.match(r"M\d+$", r[0])}


# ------------------------------------------------------------------ szerkezet

def test_principles_dimensions_and_value_chain_follow_itil4(data):
    assert [p["name_en"] for p in data["principles"]] == PRINCIPLES
    assert [d["name_en"] for d in data["dimensions"]["items"]] == DIMENSIONS
    assert {a["id"]: a["name_en"] for a in data["value_chain"]["activities"]} == ACTIVITIES
    assert [c["name_en"] for c in data["svs"]["components"]] == [
        "Guiding principles", "Governance", "Service value chain", "Practices", "Continual improvement",
    ]
    assert len(data["dimensions"]["external"]["factors"]) == 6  # PESTLE


def test_foundation_has_7_detailed_and_8_purpose_level_practices(data):
    foundation = data["practices"]["foundation"]
    assert {p["name_en"] for p in foundation if p["depth"] == "részletes"} == DETAILED
    assert {p["name_en"] for p in foundation if p["depth"] == "cél"} == PURPOSE_ONLY
    assert len(foundation) == 15


def test_all_34_practices_in_three_groups(data):
    practices = data["practices"]["foundation"] + data["practices"]["others"]
    names = [p["name_en"] for p in practices]
    assert len(names) == len(set(names)) == 34
    count = {g: sum(p["group"] == g for p in practices) for g in data["practices"]["groups"]}
    assert count == {"general": 14, "service": 17, "technical": 3}
    assert "Project management" in names


def test_every_foundation_practice_is_shown_on_the_xyo_with_real_documents(data):
    index = content.load_doc_index()
    for p in data["practices"]["foundation"]:
        assert p["gap"] in itil4.GAP_ICON, p["id"]
        assert p["docs"] and all(d in index for d in p["docs"]), p["id"]
        for field in ("purpose", "xyo", "adds"):
            assert p[field].strip(), (p["id"], field)
    assert content.validate() == []


def test_phase_map_covers_every_phase_once_with_valid_activities(data):
    rows = data["value_chain"]["phase_map"]["rows"]
    assert [r["phase"] for r in rows] == [p["id"] for p in content.load_phases()]
    used = {a for r in rows for a in r["activities"]}
    assert used <= set(ACTIVITIES) and used == set(ACTIVITIES)


def test_value_streams_use_valid_activities_and_real_people(data):
    roster = {r["name"] for r in content.sample_projects()[0]["roles"]}
    for stream in data["value_streams"]["items"]:
        assert stream["steps"]
        for step in stream["steps"]:
            assert step["activity"] in ACTIVITIES, (stream["id"], step["activity"])
            assert any(name in step["who"] for name in roster) or "Service Desk" in step["who"], step["who"]


# ------------------------------------------------------------------ a számok a Xyo-dokumentumokból

def test_kpi_figures_quoted_are_the_pir_figures(data):
    """Minden idézett mérőszám a PIR táblájából jön: T0, eredmény, cél."""
    pir = _pir()
    text = _flat(data)
    t0 = {k: v[2] for k, v in pir.items()}
    result = {k: v[3] for k, v in pir.items()}
    target = {k: v[4] for k, v in pir.items()}
    expected = [
        f"{t0['M5'].replace(' ', '')} munkanap helyett {result['M5']} munkanap alatt áll munkába (M5, PIR)",
        f"T0-ban {t0['M5']} munkanap, a mérési szakasz végén {result['M5']} munkanap (cél {target['M5']})",
        f"{t0['M4']} óráról {result['M4']} órára vitte le (M4)",
        f"{t0['M3']}-ról {result['M3']}-ra (M3)",
        f"{result['M9']}-os rendelkezésre állás (M9)",
        f"rendelkezésre állás {target['M9']} (M9)",
        f"{result['M8']}-os MFA-lefedettség (M8)",
        f"M10: {t0['M10']} → {result['M10']} eset negyedévente",
        f"M6: {result['M6']} a {target['M6']} helyett",
        f"MTTR {target['M2']} óra (M2)",
        f"elégedettség {target['M11']} (M11)",
    ]
    for phrase in expected:
        assert phrase in text, phrase


def test_other_facts_match_the_documents(data):
    text = _flat(data)
    summary = tables(section(read_doc(LESSONS), "6. Összesítés"))
    totals = {r[0].replace("*", ""): r[1].replace("*", "") for t in summary for r in t}
    assert f"{totals['Összesen']} tanulság, {totals['Menet közben rögzítve']} menet közben" in text
    t0_date = re.search(r"\*\*A mérés dátuma:\*\* \*\*(\d{4})\. január (\d+)\.", read_doc(T0))
    assert f"T0 mérés ({t0_date[1]}.01.{t0_date[2]}." in text
    runbook = read_doc(RUNBOOK)
    assert "Kiss Réka + 2 Service Desk munkatárs" in runbook and "Kiss Réka és két munkatárs" in text
    assert re.search(r"távoli hozzáférés-visszavonás \(8 perc\)", runbook)
    assert "kb. 8 perc (runbook 10. eset)" in text


# ------------------------------------------------------------------ oldal és ábra

def test_value_chain_dot_has_every_activity_phase_and_mapping(data):
    dot = itil4.build_value_chain_dot(data)
    # a fázisok 1-től 6-ig, a tevékenységek a hivatalos sorrendben: egy-egy táblán belül, portokkal
    phase_ports = [dot.index(f'PORT="{p["id"]}"') for p in content.load_phases()]
    assert phase_ports == sorted(phase_ports)
    activity_ports = [dot.index(f'PORT="{a}"') for a in ACTIVITIES]
    assert activity_ports == sorted(activity_ports) and min(activity_ports) > max(phase_ports)
    for phase in content.load_phases():
        assert f'{phase["number"]}. {phase["title_hu"]}</TD>' in dot
    for row in data["value_chain"]["phase_map"]["rows"]:
        for activity in row["activities"]:
            assert f'phases:{row["phase"]}:e -> chain:{activity}:w [style=dashed];' in dot
    assert dot.count("[style=dashed]") == sum(len(r["activities"]) for r in data["value_chain"]["phase_map"]["rows"])


def test_page_renders_with_its_tabs(tmp_progress):
    at = AppTest.from_string("from pm_app import itil4\nitil4.view()\n", default_timeout=60).run()
    assert not at.exception, at.exception
    expected = ["Alapok", "Értéklánc", "Gyakorlatok", "Szerepek és igazodás", "Együtt: PMI + PRINCE2 + ITIL", "Mérhető eredmény", "Haladó szint és ITIL 5", "Összefoglaló és minták"]
    assert itil4.TABS == expected
    assert [t.label for t in at.tabs][: len(expected)] == expected
    assert "ITIL 4" in at.title[0].value
    assert len(at.get("graphviz_chart")) == 1
    assert any("PeopleCert" in c.value for c in at.caption)
    body = " ".join(m.value for m in at.markdown)
    assert "Változásengedélyezés" in body and "Szolgáltatásszint-kezelés" in body


def test_itil4_is_in_the_methodology_menu_after_prince2():
    app = (Path(__file__).resolve().parent.parent / "app.py").read_text(encoding="utf-8")
    menu = app.split('"Módszertan": [', 1)[1].split("],", 1)[0]
    assert 'url_path="itil4"' in menu and menu.index("views.prince2") < menu.index("itil4.view")


def test_validate_reports_broken_itil4_references(data, monkeypatch):
    broken = {**data, "primer_file": "docs/itil4/nincs.md",
              "documents": [{"id": "itil_x", "sample_file": "docs/itil4/nincs-ilyen.md"}],
              "practices": {**data["practices"],
                            "foundation": [{**data["practices"]["foundation"][0], "docs": ["nincs_ilyen_doksi"]}]}}
    monkeypatch.setattr(content, "load_itil4", lambda: broken)
    problems = content.validate.__wrapped__()
    assert any("ITIL 4 `primer_file`" in p for p in problems)
    assert any("ITIL 4 `itil_x`" in p for p in problems)
    assert any("nincs_ilyen_doksi" in p for p in problems)


# ------------------------------------------------------------------ 2. szakasz: szerepek, együtt, hiba útja

ROLLOUT = "docs/6-benefits/07-kiterjesztesi-javaslat.md"
RISKS = "docs/2-planning/10-kockazatnyilvantartas.md"
ISSUES = "docs/3-execution/10-problemanaplo.md"
TESTS = "docs/3-execution/07-tesztjegyzokonyv.md"
SURVEY = "docs/6-benefits/05-felhasznaloi-kerdoiv.md"
SCHEDULE = "docs/2-planning/06-utemterv.md"
STAKEHOLDERS = "docs/1-initiation/06-erintettek-nyilvantartasa.md"
OTHER_ORGS = ("Cloudia Solutions", "Projekt", "független tanácsadó", "Xyo")


def _roster() -> set[str]:
    return {r["name"] for r in content.sample_projects()[0]["roles"]}


NAME_LIKE = re.compile(r"\b(?:dr\. )?[A-ZÁÉÍÓÖŐÚÜŰ][a-záéíóöőúüű]+ [A-ZÁÉÍÓÖŐÚÜŰ][a-záéíóöőúüű]+")
ALLOWED_PAIRS = ("Service Desk", "Cloudia Solutions", "TechLine Zrt")


def _names_ok(text: str) -> bool:
    """Legalább egy ismert szereplő vagy szervezet, és nincs ismeretlen (elírt) személynév:
    a „Nagy Péternél” nem azonos a „Nagy Péter”-rel."""
    if not (any(n in text for n in _roster()) or any(o in text for o in OTHER_ORGS)):
        return False
    rest = text
    for name in sorted(_roster(), key=len, reverse=True) + list(ALLOWED_PAIRS):
        rest = re.sub(re.escape(name) + r"(?![a-záéíóöőúüű])", " ", rest)
    return not NAME_LIKE.search(rest)


def test_roles_are_worn_by_real_people_and_the_concentration_count_is_right(data):
    roles = data["roles"]["items"]
    assert len(roles) == 9
    for r in roles:
        assert _names_ok(r["who"]), r["role"]
    hats = sum("Szabó Márk" in r["who"] for r in roles)
    numbers = {2: "két", 3: "három", 4: "négy", 5: "öt"}
    assert f"Szabó Márk {numbers[hats]} kalapot visel" in _flat(data["roles"])
    risk = re.search(r"### (R\d+) — Belső kapacitáshiány", read_doc(RISKS))
    assert f"({risk[1]} kockázat: belső kapacitáshiány)" in _flat(data["roles"])


def test_new_people_argument_uses_the_rollout_figures(data):
    f4 = section(read_doc(ROLLOUT), "F4 — Service Desk kapacitásbővítés")
    trend = re.search(r"(\d,\d) → (\d,\d) → (\d,\d) ticket/fő", f4).groups()
    text = _flat(data)
    assert f"{trend[0]} → {trend[1]} → {trend[2]} ticket/fő" in text
    assert "+1 fő tartós Service Desk kapacitás" in f4 and "+1 fő tartós Service Desk kapacitást" in text
    for phase in content.load_phases():
        if phase["id"] == "monitoring":
            assert f"{trend[0]} → {trend[1]} → {trend[2]} ticket/fő" in _flat(phase["itil4"])


def test_together_tables_are_complete(data):
    together = data["together"]
    for row in together["layers"]:
        assert all(row[k].strip() for k in ("question", "pmi", "prince2", "itil"))
    assert len(together["concept_map"]) >= 12
    for row in together["concept_map"]:
        assert all(row[k].strip() for k in ("pmi", "prince2", "itil", "note"))
    for h in together["handover_points"]["items"]:
        assert _names_ok(h["from"]) and _names_ok(h["to"]), h["what"]
    assert len(together["conflicts"]) == 4


def test_error_journey_dates_and_numbers_come_from_the_documents(data):
    journey = data["error_journey"]
    text = _flat(journey)
    # a hiba a tesztjegyzőkönyvben S3-ként
    assert re.search(r"### S3 — zavaró[\s\S]*?\| H-09 \|", read_doc(TESTS))
    assert "H-09, S3" in text
    # a problémanapló dátuma
    p13 = section(read_doc(ISSUES), "P-13")
    day = re.search(r"\| Felmerült \| (\d{4}\.\d\d\.\d\d\.) \|", p13)[1]
    assert any(s["when"] == day for s in journey["steps"])
    # UAT-zárás = a 6.4 vége, üzemeltetésbe adás = a runbook dátuma
    uat_end = re.search(r"\| 6\.4 \| [^|]+ \| \d\d\.\d\d\. \| (\d\d\.\d\d\.) \|", read_doc(SCHEDULE))[1]
    assert any(s["when"].startswith(f"2026.{uat_end}") for s in journey["steps"])
    handover = re.search(r"\*\*Átadás dátuma:\*\* \*\*2026\. június (\d+)\.", read_doc(RUNBOOK))[1]
    assert any(s["when"].startswith(f"2026.06.{handover}.") for s in journey["steps"])
    # a kérdőív: válaszadók, említések, K4
    survey = read_doc(SURVEY)
    responses = re.search(r"\| Beérkezett \| \d+ válasz \| \*\*(\d+) válasz\*\* \|", survey)[1]
    mentions = re.search(r"\| „Néha lassan jön az MFA-értesítés\" \| (\d+) \|", survey)[1]
    k4 = re.search(r"\| T\+3 \| \*\*(\d,\d)\*\*", survey)[1]
    assert f"A {responses} válaszadóból {mentions} említi" in text and f"leggyengébb eredmény ({k4})" in text
    # a PIR dátuma a mérföldkőlistából, és hogy a H-09 maradt egyedül nyitva
    pir_day = re.search(r"\| M11 \| [^|]+ \| (\d{4}\.\d\d\.\d\d\.) \|", read_doc(SCHEDULE))[1]
    assert any(s["when"].startswith(pir_day) for s in journey["steps"])
    assert "Hét nyitott pontból hat lezárva" in read_doc(PIR) and "A hét nyitott pontból egyedül a H-09" in text


def test_kiss_reka_stakeholder_facts(data):
    row = next(line for line in read_doc(STAKEHOLDERS).splitlines() if line.startswith("| E5 | Kiss Réka"))
    assert "kezdetben ellenálló" in row
    initiation = _flat(content.phase_by_id("initiation")["itil4"])
    assert "„kezdetben ellenálló” volt (E5)" in initiation


# ------------------------------------------------------------------ fázisblokkok

def test_every_phase_has_an_itil4_block_matching_the_value_chain_map(data):
    rows = {r["phase"]: r["activities"] for r in data["value_chain"]["phase_map"]["rows"]}
    foundation = {p["id"] for p in data["practices"]["foundation"]}
    others = {p["name_hu"] for p in data["practices"]["others"]}
    for phase in content.load_phases():
        block = phase["itil4"]
        assert block["activities"] == rows[phase["id"]], phase["id"]
        assert set(block["practices"]) <= foundation, phase["id"]
        assert set(block.get("other_practices", [])) <= others, phase["id"]
        assert len(block["adds"]) >= 2 and all(a["what"] and a["why"] for a in block["adds"])
        assert block["who"].startswith("Xyo — ") and _names_ok(block["who"]), phase["id"]


@pytest.mark.parametrize("phase_id", ["initiation", "planning", "execution", "monitoring", "closure", "benefits"])
def test_phase_page_shows_the_itil4_block(phase_id, tmp_progress):
    at = AppTest.from_string(
        f"from pm_app import views\nviews.make_phase_view({phase_id!r})()\n", default_timeout=60
    ).run()
    assert not at.exception, at.exception
    assert any(e.label == "Mi ez a fázis ITIL 4 szerint?" for e in at.expander)
    assert any("ITIL 4" in s.value for s in at.subheader)


# ------------------------------------------------------------------ összefoglaló

def test_primer_covers_the_foundation_syllabus(data):
    primer = " ".join(read_doc(data["primer_file"]).split())
    for name in PRINCIPLES + DIMENSIONS + list(ACTIVITIES.values()):
        assert name in primer, name
    for p in data["practices"]["foundation"]:
        assert p["name_en"] in primer, p["name_en"]
    for term in ("known error", "workaround", "Standard change", "Normal change", "Emergency change",
                 "change authority", "service level agreement", "continual improvement register"):
        assert term in primer, term
    assert "XYO-METH-002" in primer and "XYO-METH-002" not in read_doc("docs/prince2/00-prince2-osszefoglalo.md")


def test_primer_figures_match_the_documents(data):
    primer = " ".join(read_doc(data["primer_file"]).split())
    pir = _pir()
    assert f"0,8 munkanap alatt áll munkába (korábban {pir['M5'][2]})" in primer and pir["M5"][3] == "0,8"
    assert f"{pir['M6'][3]} a {pir['M6'][4]} helyett" in primer
    assert f"{pir['M4'][2]} → {pir['M4'][3]} óra gépbeüzemelés" in primer
    assert f"{pir['M9'][3]} rendelkezésre állás" in primer
    assert "2026.06.04-én bekerült a projekt problémanaplójába (P-13)" in primer
    assert "a 44 válaszadóból 12 említette" in primer
    assert "T0 mérés 2026.01.30-án" in primer


def test_together_tab_search_filters_the_concept_map(tmp_progress):
    at = AppTest.from_string("from pm_app import itil4\nitil4.view()\n", default_timeout=60).run()
    before = sum(len(t.value) for t in at.table)
    at.text_input(key="itil4-fogalom").input("hypercare").run()
    assert not at.exception
    assert sum(len(t.value) for t in at.table) < before


# ------------------------------------------------------------------ 3. szakasz: mintadokumentumok 01–03

SERVICE_DESC = "docs/itil4/01-szolgaltatasleiras.md"
SLA = "docs/itil4/02-sla-ola.md"
CHANGE_MODEL = "docs/itil4/03-valtozasengedelyezes.md"
KPI = "docs/6-benefits/02-kpi-adatlap.md"
MONTHLY = "docs/6-benefits/04-havi-meresi-riportok.md"
CHANGE_LOG = "docs/4-monitoring/04-valtozasnaplo.md"
CHANGE_PROC = "docs/2-planning/15-valtozaskezelesi-eljaras.md"
DECISIONS = "docs/3-execution/11-dontesnaplo.md"
AS_BUILT = "docs/3-execution/06-as-built-dokumentacio.md"
BIDS = "docs/3-execution/03-ajanlat-osszehasonlitas.md"


def _norm(text: str) -> str:
    """Folyó szöveg sortörések és idézetjelek (`> `) nélkül."""
    return " ".join(re.sub(r"^> ?", "", text, flags=re.MULTILINE).split())


def _num(text: str) -> float:
    return float(text.replace("*", "").replace(",", ".").replace(" ", "").strip())


def _runbook_cases() -> dict[str, str]:
    rows = tables(section(read_doc(RUNBOOK), "4. Hibakezelés"))[0]
    return {r[0]: r[1] for r in rows}


def _kpi_targets(metric: str) -> tuple[str, str]:
    card = section(read_doc(KPI), f"{metric} —")
    m = re.search(r"\*\*Cél\*\* ([^·|]+?) · \*\*Kudarcküszöb\*\* ([^|]+?) \|", card)
    return m[1].strip(), m[2].strip()


def _doc_names_ok(text: str) -> bool:
    """A folyó szövegben a nevek ragozva állnak („Kiss Rékával”, „Nagy Pétert”). Minden, a
    szereplők vezetéknevével kezdődő névpár egy ismert szereplő ragozott alakja kell legyen: a
    „Nagy Pál” vagy a „Kiss Rita” elírás."""
    people = [n for n in _roster() if not n.endswith((".", "Kft", "Zrt"))]
    surnames = {n.removeprefix("dr. ").split()[0] for n in people}
    given = {n.removeprefix("dr. ").split()[0]: [] for n in people}
    for n in people:
        given[n.removeprefix("dr. ").split()[0]].append(n.split()[-1])
    pattern = re.compile(rf"\b({'|'.join(surnames)}) ([A-ZÁÉÍÓÖŐÚÜŰ][a-záéíóöőúüű]+)")
    for surname, first in pattern.findall(text):
        if not any(first[: len(g) - 1] == g[:-1] for g in given[surname]):
            return False
    return True


def test_sample_documents_are_listed_in_order_with_valid_references(data):
    docs = data["documents"]
    assert [d["order"] for d in docs] == list(range(1, len(docs) + 1))
    assert len({d["id"] for d in docs}) == len(docs)
    index = content.load_doc_index()
    practices = {p["id"] for p in data["practices"]["foundation"]}
    for doc in docs:
        text = read_doc(doc["sample_file"])
        assert f"**Dokumentum azonosítója:** XYO-ITIL-{doc['order']:03d}" in text
        assert set(doc["sources"]) <= set(index) and set(doc["practices"]) <= practices
        assert "ITIL 4-kiegészítés" in text and "Kapcsolódó dokumentumok" in text
        assert _doc_names_ok(text), doc["sample_file"]


def test_validate_reports_broken_itil4_document_refs(data, monkeypatch):
    doc = {**data["documents"][0], "sources": ["nincs_ilyen_forras"], "practices": ["nincs_ilyen_gyakorlat"]}
    monkeypatch.setattr(content, "load_itil4", lambda: {**data, "documents": [doc]})
    problems = content.validate.__wrapped__()
    assert any("nincs_ilyen_forras" in p for p in problems)
    assert any("nincs_ilyen_gyakorlat" in p for p in problems)


def test_summary_tab_lists_and_opens_every_sample(data, tmp_progress):
    at = AppTest.from_string("from pm_app import itil4\nitil4.view()\n", default_timeout=60).run()
    labels = [e.label for e in at.expander]
    for doc in data["documents"]:
        assert any(f"{doc['order']:02d} — {doc['name_hu']}" in label for label in labels)
    at.toggle(key=f"show-{data['documents'][1]['id']}").set_value(True).run()
    assert not at.exception
    assert any("XYO-ITIL-002" in m.value for m in at.markdown)


def _classification() -> dict[str, tuple[str, str]]:
    rows = tables(section(read_doc(SERVICE_DESC), "4. Kéréskatalógus"))[0]
    return {r[0]: (r[1], r[2]) for r in rows}


def test_service_description_classifies_the_runbook_cases(data):
    cases, ours = _runbook_cases(), _classification()
    assert list(ours) == list(cases)  # mind a 15 eset, a Run-book sorrendjében
    for number, (symptom, _) in ours.items():
        assert symptom == cases[number].replace('"', "”"), number
    incidents = [n for n, (_, kind) in ours.items() if kind.startswith("Incidens")]
    requests = [n for n, (_, kind) in ours.items() if "Szolgáltatáskérés" in kind]
    info = [n for n, (_, kind) in ours.items() if "információkérés" in kind]
    assert len(incidents) + len(requests) == len(cases)
    text = read_doc(SERVICE_DESC)
    assert f"A 15 esetből {len(incidents)} incidens és {len(requests)} szolgáltatáskérés." in _norm(text)
    assert f"({info[0]}., {info[1]}.)" in text and len(info) == 2
    assert f"({len(incidents)} incidens, {len(requests)} szolgáltatáskérés)" in _flat(data["documents"][0])
    # a PIR valóban a „hova mentsem?" kérdésekkel magyarázza az M1 elmaradását
    assert "„hova mentsem?\" jellegű használati kérdések" in read_doc(PIR)
    assert f"({_pir()['M1'][3]} a {_pir()['M1'][4].lstrip('≤ ')} helyett)" in _norm(text)


def test_service_description_facts_come_from_the_runbook_and_the_pir():
    text = read_doc(SERVICE_DESC)
    runbook = read_doc(RUNBOOK)
    # a konfigurációs tételek a Run-book 1. pontjából
    items = [(r[0], r[1]) for r in tables(section(runbook, "1. Mit üzemeltetünk"))[0]]
    ours = [(r[0], r[1]) for r in tables(section(text, "6. A szolgáltatás mögötti"))[0]]
    assert ours == items
    # a beszállítói dátumok a Run-book 6. pontjából
    for supplier, until in (("TechLine Zrt.", "2029.05.29."), ("Cloudia Solutions Kft.", "2026.12.19."),
                            ("Microsoft (CSP-n keresztül)", "2027.04.30.")):
        assert re.search(rf"\| {re.escape(supplier)} \| [^|]+ \| \*\*{re.escape(until)}\*\*", runbook)
        assert re.search(rf"\| {re.escape(supplier)} \| [^|]+ \| {re.escape(until)} \|", text)
    # a fajlagos költség a PIR tervezett folyó költségéből
    yearly = re.search(r"\| Folyó költség a 2\. évtől \| ([\d ]+) Ft/év \|", read_doc(PIR))[1]
    per_head = round(int(yearly.replace(" ", "")) / 50 / 12)
    assert f"| Tervezett folyó költség a 2. évtől | {yearly} Ft/év |" in text
    assert f"**{per_head:,} Ft/fő/hó**".replace(",", " ") in text
    # a kizárások a változásnapló hatókörön kívüli kérései
    out_of_scope = {r[0]: r[1] for r in tables(section(read_doc(CHANGE_LOG), "5. Hatókörön kívülre"))[0]}
    for code, subject in (("K9", "Céges mobiltelefon"), ("K10", "Otthoni irodabútor"), ("K11", "Otthoni nyomtatás")):
        assert out_of_scope[code].startswith(subject) and f"({code})" in text
    # elérhetőség, szolgáltatási idő, garanciák
    assert "belső 4200, `servicedesk@xyo.hu`" in runbook and "belső 4200, `servicedesk@xyo.hu`" in text
    assert "H–P 7:30 – 17:00" in read_doc(KPI) and "Munkanapokon 7:30 – 17:00" in text
    assert "(8 perc)" in runbook and "8 percen belül" in text
    assert "| **42 perc** |" in read_doc(AS_BUILT) and "kb. 42 perc" in text
    for metric, phrase in (("M9", "Legalább {} a szolgáltatási időben"), ("M2", "legfeljebb {} munkaóra")):
        target = _kpi_targets(metric)[0].lstrip("≥≤ ")
        assert phrase.format(target + ("%" if metric == "M9" else "")) in text


def test_sla_series_and_targets_come_from_the_measurements():
    text = read_doc(SLA)
    monthly = {r[0]: r for r in tables(section(read_doc(MONTHLY), "1. Teljes adatsor"))[0]}
    series = {r[1]: r for r in tables(section(text, "3.1 A mért sorozat"))[0]}
    for metric in ("M2", "M9", "M10", "M11"):
        assert [c.replace("*", "") for c in series[metric][2:6]] == [c.replace("*", "") for c in monthly[metric][2:6]]
    # a vállalt célszint és az elfogadhatatlan szint a KPI-adatlap célja és kudarcküszöbe
    targets = tables(section(text, "3.2 A vállalt célszintek"))[0]
    by_name = {r[0].replace("*", "").split(" a ")[0]: r for r in targets}
    for name, metric, unit in (("Rendelkezésre állás", "M9", "%"), ("Átlagos megoldási idő", "M2", " munkaóra"),
                               ("Adatvesztés", "M10", ""), ("Felhasználói elégedettség", "M11", "")):
        goal, fail = _kpi_targets(metric)
        row = by_name[name]
        assert row[1].replace("*", "") == goal + unit, name
        assert row[2].replace("≥ 1 eset", "≥ 1") == fail + unit
    # „mindhárom mért hónapban” és „csak a T+3-ban”: újraszámolva
    m9 = [_num(c) for c in monthly["M9"][3:6]]
    m2 = [_num(c) for c in monthly["M2"][3:6]]
    assert all(v >= 99.5 for v in m9) and "**Mindhárom mért hónapban teljesült**" in text
    assert [v <= 6.0 for v in m2] == [False, False, True] and "**Csak a T+3-ban teljesült**" in text
    # a kérések mért értékei a PIR-ből
    pir = _pir()
    assert f"| {pir['M5'][3]} munkanap | M5 |" in text and f"| {pir['M4'][3]} óra | M4 |" in text


def test_sla_supplier_chain_recomputes():
    text = read_doc(SLA)
    workdays = sum(1 for d in range(1, 31) if dt.date(2026, 9, d).weekday() < 5)  # szeptemberben nincs ünnep
    hours = workdays * 9.5  # 7:30 – 17:00
    assert f"| {workdays} munkanap × 9,5 óra | {hours:.0f} óra |" in text
    budget = hours * 60 * 0.005
    uc = {r[1].split(" (")[0]: _num(r[2].split("%")[0]) for r in tables(section(text, "6.1 A beszállítói"))[0] if "%" in r[2]}
    assert uc == {"Microsoft 365": 99.9, "Microsoft Entra ID": 99.99, "VPN Gateway": 99.95}
    allowances = [30 * 24 * 60 * (100 - v) / 100 for v in uc.values()]

    def hu(x: float) -> str:
        return f"{x:.1f}".replace(".", ",")

    assert f"**{hu(budget)} perc**" in text
    for a in allowances:
        assert f"| {hu(a)} perc |" in text
    total = sum(round(a, 1) for a in allowances)
    assert f"**{hu(total)} perc**" in text and f"({hu(total)} > {hu(budget)} perc)" in text
    assert total > budget  # a lánc határán: a beszállítói keret több, mint a belső
    composite = 100
    for v in uc.values():
        composite *= v / 100
    assert f"≈ **{composite:.2f}%**".replace(".", ",") in _norm(text)
    # a beszállítói dátumok és a Cloudia támogatási pontszáma
    runbook = read_doc(RUNBOOK)
    for until in ("2027.04.30.", "2026.12.19.", "2029.05.29."):
        assert f"**{until}**" in runbook and f"| {until} |" in text
    assert "| Támogatási konstrukció | 10% | 85 p |" in read_doc(BIDS) and "85 pontot kapott" in _norm(text)


def test_sla_priorities_cite_only_incidents_once_each():
    text = read_doc(SLA)
    rows = tables(section(text, "4. Prioritás és célidők"))[0]
    cited = [re.findall(r"(\d+)\. eset", r[4]) for r in rows]
    flat = [c for row in cited for c in row]
    assert len(flat) == len(set(flat))
    kinds = _classification()
    assert all(kinds[c][1].startswith("Incidens") for c in flat)
    assert "10" in cited[0] and "15" in cited[3]  # P1: elveszett gép, P4: kozmetikai
    # a verziók: 1.0 az átadás napján, 1.1 a PIR elfogadása után
    handover = re.search(r"\*\*Átadás dátuma:\*\* \*\*2026\. június (\d+)\.", read_doc(RUNBOOK))[1]
    assert f"| 1.0 | 2026.06.{handover}. |" in text
    pir_day = re.search(r"\*\*Elfogadta:\*\* Projekt Irányító Bizottság — \*\*2026\. október (\d+)\.", read_doc(PIR))[1]
    sla_day = re.search(r"\*\*Dátum:\*\* \*\*2026\. október (\d+)\.", text)[1]
    assert int(sla_day) > int(pir_day) and f"a PIR (2026.10.{int(pir_day):02d}.)" in text


def test_change_model_classifies_the_change_log_rows():
    text = read_doc(CHANGE_MODEL)
    log = tables(section(read_doc(CHANGE_LOG), "4. Amit megvizsgáltunk"))[0]
    ours = tables(section(text, "1. Két eljárás"))[1]
    assert [r[0] for r in ours] == [r[0] for r in log]
    for mine, theirs in zip(ours, log):
        decision = re.search(r"D-\d+", theirs[3])
        assert (decision[0] in mine[2]) if decision else mine[2] == "nem"
        assert mine[1].split(" ")[1] in theirs[1]  # ugyanaz a módosítás
    kinds = [r[3].replace("*", "").split(" ")[0] for r in ours]
    assert kinds == ["Sürgős", "Normál", "Normál", "Normál", "Nem"]
    # a CA-05 döntéshozója a döntésnaplóban
    d14 = next(r for r in tables(read_doc(DECISIONS))[0] if r[0] == "**D-14**")
    assert "Nagy Péter" in d14[3] and "dr. Fekete Zsolt" in d14[3]
    quote = "Biztonsági vonatkozása miatt viszont a szakmai vezető döntött, nem a PM**, DPO-véleménnyel."
    assert quote in read_doc(CHANGE_LOG) and quote.replace("**", "") in _norm(text)


def test_change_model_p05_replay_and_dates_match_the_documents():
    text = read_doc(CHANGE_MODEL)
    p05 = section(read_doc(ISSUES), "P-05")
    assert re.search(r"Eszkalálva \| Nagy Péterhez, 2026\.05\.11\. 10:40", p05) and "| 05.11. 10:40 |" in text
    assert "Lezárva | 2026.05.12." in p05 and "| 05.12. |" in text
    assert "CGNAT" in p05 and "3 tesztelő" in p05 and "**3 tesztelő**" in text
    ca05 = section(read_doc(AS_BUILT), "CA-05")
    assert "05.04–05.08." in ca05 and "| 05.04 – 05.08. |" in text
    assert "2026.05.13–05.22." in ca05 and "| 05.13 – 05.22. |" in text
    # a projekt saját küszöbei és a 24 órás sürgős szabály
    proc = read_doc(CHANGE_PROC)
    assert "**24 órán belül írásban rögzíti**" in proc and "**24 órán belül**" in text
    assert "≤ 1 000 000 Ft, ≤ 3 nap csúszás" in proc and "(1 000 000 Ft, 3 nap," in _norm(text)
    # a szabványos változások Run-book-esetei: a belépő és a kilépő kérés, a többi létező eset
    cases, kinds = _runbook_cases(), _classification()
    standard = tables(section(text, "3. Szabványos változások"))[0]
    refs = {r[0]: re.findall(r"(\d+)\. eset", r[4]) for r in standard}
    assert refs["SV-1"] == ["12"] and refs["SV-2"] == ["13"]
    assert all(c in cases for v in refs.values() for c in v)
    assert "szabványos változással" in kinds["12"][1] and "szabványos változással" in kinds["13"][1]
    # a változási nyilvántartás dátumai a Run-bookból
    runbook = read_doc(RUNBOOK)
    assert "| **A Cloudia Solutions Intune-adminisztrátori joga** | **MEGSZŰNT** | 2026.06.19. |" in runbook
    assert "| Azure előfizetés tulajdonos | Nagy Péter | 2026.06.26. |" in runbook
    assert "(következő: 2026.12.18.)" in runbook and "**2027.02.28-ig**" in runbook
    rows = {r[0]: r for r in tables(section(text, "7. Változási nyilvántartás"))[0]}
    assert rows["CH-001"][1] == "2026.06.19." and rows["CH-002"][1] == "2026.06.26."
    assert rows["CH-003"][1] == "2026.12.18." and rows["CH-004"][1] == "2027.02.28-ig"
    # a Cloudia joga a szerződés szerint az UAT-elfogadással szűnik meg — ez a dokumentum napja
    assert "**2026.06.19-én, az UAT-elfogadással megszűnik**" in read_doc("docs/3-execution/04-szerzodes.md")
    assert "**Dátum:** **2026. június 19.**" in text


# ------------------------------------------------------------------ 4. szakasz: minták 04–06, mérhető eredmény

INCIDENTS = "docs/itil4/04-incidens-problema-ismert-hiba.md"
ACCEPT_ELS = "docs/itil4/05-szolgaltatasi-elfogadas-els.md"
CIR = "docs/itil4/06-folyamatos-fejlesztesi-nyilvantartas.md"
FINAL_ACCEPTANCE = "docs/5-closure/01-atadas-atveteli-jegyzokonyv.md"
WBS_DICT = "docs/2-planning/04-wbs-szotar.md"
RACI = "docs/2-planning/09-raci-matrix.md"
ROLLBACK = "docs/2-planning/20-visszaallasi-terv.md"
COMM = "docs/2-planning/11-kommunikacios-terv.md"


def _hu(x: float, digits: int = 1) -> str:
    return f"{x:.{digits}f}".replace(".", ",")


def test_incident_chain_links_the_same_defect_in_every_document():
    text = read_doc(INCIDENTS)
    chain = tables(section(text, "2. Az azonosítók láncai"))[0]
    tests_doc, issues = read_doc(TESTS), read_doc(ISSUES)
    case_rows = {r[0]: r for r in tables(section(read_doc(RUNBOOK), "4. Hibakezelés"))[0]}
    runbook_open = [r[0] for r in tables(section(read_doc(RUNBOOK), "7. Ismert korlátok"))[0] if r[0].startswith("H-")]
    assert [r[0].split(" ")[0] for r in chain] == runbook_open  # a Run-book nyitott hibái, sorrendben
    for row in chain:
        defect = row[0].split(" ")[0]
        assert re.search(rf"\| {defect} \|", tests_doc)
        if row[1] == "—":
            assert not re.search(rf"\({defect},", issues)
        else:
            assert f"({defect}," in section(issues, row[1])
        if row[2] == "—":
            assert all(defect not in " ".join(r) for r in case_rows.values())
        else:
            assert defect in " ".join(case_rows[row[2].rstrip(".")]), defect
    # az ismert hibák kerülőmegoldása a Run-book „Teendő" oszlopa, a határidő az átadás-átvételi jegyzőkönyvé
    known = {r[0]: r for r in tables(section(text, "3.1 Az átadáskor"))[0]}
    accepted = {r[0]: r for r in tables(section(read_doc(FINAL_ACCEPTANCE), "3. Nyitva maradt hibák"))[0]}
    for row in chain:
        defect, ke = row[0].split(" ")[0], row[3]
        assert known[ke][5] == accepted[defect][4], ke
        if row[2] != "—":
            assert known[ke][3] in (case_rows[row[2].rstrip(".")][3], f"„{case_rows[row[2].rstrip('.')][3]}”")


def test_known_error_status_after_the_pir_matches_the_open_items():
    text = read_doc(INCIDENTS)
    chain = {r[3]: r[0].split(" ")[0] for r in tables(section(text, "2. Az azonosítók láncai"))[0]}
    pir_items = {r[0]: r[3] for r in tables(section(read_doc(PIR), "7. A nyitott pontok"))[0]}
    after = tables(section(text, "3.2 A PIR után"))[0]
    for row in after:
        closed_in_pir = "✔" in pir_items[chain[row[0]]]
        assert ("lezárva" in row[1]) == closed_in_pir, row[0]
    closed = sum("lezárva" in r[1] for r in after)
    numbers = {1: "egy", 2: "kettő", 3: "három", 4: "négy"}
    assert f"**{numbers[len(after)].capitalize()} ismert hibából {numbers[closed]} lezárva, {numbers[len(after) - closed]} nyitva.**" in text
    assert "a 240 000 Ft-os feltételes keret **nem került felhasználásra**" in read_doc(PIR)


def test_problem_record_and_major_incident_facts(data):
    text = read_doc(INCIDENTS)
    flat = _norm(text)
    p13 = section(read_doc(ISSUES), "P-13")
    day = re.search(r"\| Felmerült \| (\d{4}\.\d\d\.\d\d\.) \|", p13)[1]
    assert f"a jelenség {day} óta ismert, P-13" in flat
    survey = read_doc(SURVEY)
    responses = re.search(r"\| Beérkezett \| \d+ válasz \| \*\*(\d+) válasz\*\* \|", survey)[1]
    mentions = re.search(r"\| „Néha lassan jön az MFA-értesítés\" \| (\d+) \|", survey)[1]
    k4 = re.search(r"\| T\+3 \| \*\*(\d,\d)\*\*", survey)[1]
    assert f"a {responses} válaszadóból {mentions} említette" in flat and f"leggyengébb ({k4})" in flat
    # a kiváltó feltétel ugyanaz, mint az „Egy hiba útja" tanulságában
    assert "ha egy hónapban öt ticket" in _flat(data["error_journey"]) and "legalább öt bejelentés" in flat
    # a visszaállási terv küszöbe és a selejtezés dátuma
    assert "**több mint 30%-a** nem tud belépni" in read_doc(ROLLBACK) and "több mint 30%-a nem tud belépni" in flat
    assert "| S1 | Az utolsó élesítési hullám után eltelt 4 hét | 2026.07.10. |" in read_doc(RUNBOOK)
    assert "| NY-2 | Régi gépek selejtezése | 2026.07.10. | ✔ megtörtént |" in read_doc(PIR) and "(2026.07.10.)" in text
    assert "| Szolgáltatáskiesés a hypercare alatt | Érintett felhasználók + Nagy Péter | azonnal | Kiss Réka |" in read_doc(COMM)
    assert "NAIH-bejelentés 72 órán belül" in read_doc(ROLLBACK) and "NAIH-bejelentés 72 órán belül" in text
    # az első napi incidensek és a megoldott probléma
    for issue in ("P-04", "P-05"):
        assert "az élesítés első napján" in section(read_doc(ISSUES), issue)
    assert "**Előszinkronizálás a kiosztás előtt**" in section(read_doc(ISSUES), "P-09")


def test_acceptance_criteria_groups_cover_all_26_once():
    text = read_doc(ACCEPT_ELS)
    groups = tables(section(text, "1. Az átvételi kritériumok"))[0]
    criteria = tables(section(read_doc(FINAL_ACCEPTANCE), "2. Az átvételi kritériumok"))[0]
    ids = [r[0].replace("*", "") for r in criteria]
    listed = [c for r in groups[:-1] for c in r[2].split(", ")]
    assert sorted(listed) == sorted(ids) and len(listed) == len(set(listed))
    for row in groups[:-1]:
        assert int(row[3]) == len(row[2].split(", "))
    assert groups[-1][3] == f"**{len(ids)}**"
    sizes = {r[0].split("**")[1]: int(r[3]) for r in groups[:-1]}
    assert f"({sizes['Garancia']} a {sizes['Haszon']}-hoz)" in _norm(text)
    failed = [r[0].replace("*", "") for r in criteria if "NEM FELELT MEG" in r[4]]
    assert failed == ["AK-19"] and "AK-19" in groups[0][2]
    assert f"{len(ids) - 1} kritérium megfelelt, 1 nem felelt meg.**" in read_doc(FINAL_ACCEPTANCE)


def test_service_acceptance_criteria_count_and_evidence():
    text = read_doc(ACCEPT_ELS)
    rows = tables(section(text, "2. Amit az ITIL még kérne"))[0]
    assert [r[0] for r in rows] == [f"SZE-{i:02d}" for i in range(1, len(rows) + 1)]
    ok = sum(r[2] == "✔" for r in rows)
    partial = sum("részben" in r[2] for r in rows)
    open_ = sum("✖" in r[2] for r in rows)
    numbers = {1: "egy", 8: "nyolc", 10: "Tíz"}
    assert ok + partial + open_ == len(rows)
    assert f"**{numbers[len(rows)]} kritériumból {numbers[ok]} teljesült, {numbers[partial]} részben, {numbers[open_]} nyitott.**" in text
    runbook = read_doc(RUNBOOK)
    for who in ("Nagy Péter", "Szabó Márk", "Kiss Réka"):
        assert re.search(rf"\| \**Átvevő[^|]*\| \**{who}", section(runbook, "9. Az átvevő nyilatkozata"))
    assert "| D-20 | Hypercare +1 Service Desk munkatárs (VK-02)" in read_doc(DECISIONS)
    assert "**ellenőrizve: 2026.06.19-én megszűnt**" in read_doc(FINAL_ACCEPTANCE)


def test_hypercare_figures_come_from_the_plan_and_the_t0():
    text = read_doc(ACCEPT_ELS)
    start, end = re.search(r"\| 7\.4 \| Hypercare \(3 hét\) \| (\d\d\.\d\d\.) \| (\d\d\.\d\d\.) \|", read_doc(SCHEDULE)).groups()
    assert f"| 2026.{start[:-1]} – {end} (3 hét" in text
    rule = "a napi új hibabejelentések száma két egymást követő héten a normál szint 150%-a alá"
    assert rule in read_doc(WBS_DICT).replace("**", "") and rule in _norm(text).lower().replace("**", "")
    hypercare = next(r for r in tables(read_doc(RACI))[5] if r[0] == "Hypercare")
    assert hypercare[8] == "**A**" and "Kiss Réka (RACI: „A”)" in text
    yearly = int(re.search(r"\| Összes ticket \| \*\*([\d ]+) db\*\*", read_doc(T0))[1].replace(" ", ""))
    monthly, daily = yearly / 12, yearly / 12 / 21
    assert f"| {yearly:,} db |".replace(",", " ") in text and f"| {_hu(monthly)} db/hó |" in text
    assert f"kb. {_hu(daily)} db/nap" in text and f"**kb. {_hu(daily * 1.5)} db/nap**" in text
    assert "| **Hypercare 07.03-ig** — a kiemelt támogatás aktívan ösztönzi a bejelentést | +12 ticket |" in read_doc(MONTHLY)
    assert "12 tickettel növelte" in _norm(text)
    assert "2 hét hypercare" in read_doc(ROLLOUT) and "2 hét hypercare lesz" in _norm(text)
    assert "✔ lezárva, a kilépési feltétel teljesült" in read_doc(PIR)


def test_cir_lessons_and_priorities_follow_the_rules():
    text = read_doc(CIR)
    log = read_doc(LESSONS)
    titles = dict(re.findall(r"^### (T-\d+) — (.+)$", log, flags=re.MULTILINE))
    total = int(re.search(r"\| \*\*Összesen\*\* \| \*\*(\d+)\*\* \|", log)[1]) + len(re.findall(r"^### T-2[0-9]", log, flags=re.MULTILINE))
    assert total == len(titles) == 23
    service = tables(section(text, "1. Tanulság vagy fejlesztés?"))[1]
    for row in service:
        lesson, title = row[0].split(" — ", 1)
        assert titles[lesson] == title, lesson
    assert f"**A {total} tanulságból {len(service)} érinti a futó szolgáltatást**" in text
    assert f"A többi {total - len(service)} a projektvezetésről szól" in _norm(text)
    # prioritás: magas = kicsi ráfordítás és legalább közepes érték; közepes = nagy érték nagy ráfordítással
    rows = tables(section(text, "2. A nyilvántartás"))[0]
    assert [r[0] for r in rows] == [f"CI-{i:02d}" for i in range(1, len(rows) + 1)]
    for row in rows:
        value, effort, prio = row[3], row[4], row[5].replace("*", "")
        expected = "magas" if effort == "kicsi" and value in ("nagy", "közepes") else "közepes" if (value, effort) == ("nagy", "nagy") else "alacsony"
        assert prio == expected, row[0]
    high = sum(r[5].replace("*", "") == "magas" for r in rows)
    assert f"**{len(rows)} tétel: {high} magas, {len(rows) - high} közepes prioritású.**" in text
    # a kiterjesztési előfeltételek felelősei és határidői
    rollout = read_doc(ROLLOUT)
    for f, ci in (("F1", "CI-09"), ("F4", "CI-11")):
        deadline = re.search(r"\| \*\*Határidő\*\* \| ([\d.]+) \|", section(rollout, f + " —"))[1]
        assert next(r for r in rows if r[0] == ci)[7] == deadline
    for f in ("F2", "F3", "F5"):
        owner = re.search(r"\| \*\*Felelős\*\* \| ([^|]+?) \|", section(rollout, f + " —"))[1].split(" (")[0]
        assert f"| {owner} |" in section(text, "2.1 Ami nem ide tartozik")
    # az 1.0 verzió a tanulságok átadásának napja, a gazda a szerepek szerinti
    handed = re.search(r"\| Nagy Péter, IT osztályvezető \| A teljes napló[^|]+\| ([\d.]+) \|", log)[1]
    assert f"| 1.0 | {handed} |" in text
    owner = next(r for r in content.load_itil4()["roles"]["items"] if r["role_en"] == "Continual improvement")
    assert owner["who"].startswith("Nagy Péter") and "**Gazdája:** Nagy Péter" in text


def test_measurable_kpis_are_the_pir_figures(data):
    measurable = data["measurable"]
    pir = _pir()
    kpis = measurable["kpis"]
    assert [k["id"] for k in kpis] == [f"M{i}" for i in range(1, 13)]

    def digits(value: str) -> str:
        return re.sub(r"[^\d,]", "", value)

    for k in kpis:
        assert digits(k["t0"]) == digits(pir[k["id"]][2]), k["id"]
        assert digits(k["t3"]) == digits(pir[k["id"]][3]), k["id"]
        assert k["kind"] in measurable["kinds"]
    practices = {p["id"] for p in data["practices"]["foundation"]}
    assert all(k["practice"] in practices for k in kpis if "practice" in k)
    assert all(m["practice"] in practices for m in measurable["new_metrics"])
    # a négy SLA-célszint mutatói: amelyeket az SLA vállal
    sla_metrics = [k["id"] for k in kpis if "SLA-célszint" in k["itil"]]
    assert sla_metrics == ["M2", "M9", "M10"] and "M11" in measurable["sla"]
    # a változási célok ugyanazok, mint a változásengedélyezési modellben
    goals = {r[0]: r[1] for r in tables(section(read_doc(CHANGE_MODEL), "8. Mit mérünk"))[0]}
    targets = {m["metric"]: m["target"] for m in measurable["new_metrics"]}
    assert goals["Sikeres változások aránya (nem okozott incidenst, nem kellett visszaállni)"] == "≥ 95%"
    assert targets["Sikeres változások aránya"] == "legalább 95%"
    assert goals["Sürgős változások aránya az összes változáshoz"] == "≤ 10%" and targets["Sürgős változások aránya"] == "legfeljebb 10%"


def test_measurable_tab_renders_counts_and_tables(data, tmp_progress):
    at = AppTest.from_string("from pm_app import itil4\nitil4.view()\n", default_timeout=60).run()
    assert not at.exception
    kinds = data["measurable"]["kinds"]
    counts = {kind: sum(1 for k in data["measurable"]["kpis"] if k["kind"] == kind) for kind in kinds}
    assert counts == {"eredmény": 4, "teljesítmény": 5, "kockázat": 2, "költség": 1}
    caption = next(c.value for c in at.caption if "**eredmény** (" in c.value)
    for kind, n in counts.items():
        assert f"**{kind}** ({n})" in caption
    cells = " ".join(str(v) for t in at.table for v in t.value.to_numpy().ravel())
    assert "17 633 Ft" in cells and "Kérések aránya az összes ticketben" in cells


# ------------------------------------------------------------------ 5. szakasz: haladó szint és ITIL 5

# A Practice Manager csomagjai a PeopleCert ITIL-GYIK-je szerint (ITIL 4 és ITIL 5 azonos)
BUNDLES = {
    "MSF": {"Service desk", "Incident management", "Problem management", "Service request management",
            "Monitoring and event management"},
    "PIC": {"Change enablement", "Deployment management", "Release management",
            "Service configuration management", "IT asset management"},
    "CAI": {"Relationship management", "Supplier management", "Service level management",
            "Continual improvement", "Information security management"},
}


def test_practice_manager_bundles_cover_the_foundation_15_once(data):
    english = {p["id"]: p["name_en"] for p in data["practices"]["foundation"]}
    items = data["advanced"]["practice_bundles"]["items"]
    assert {b["code"]: {english[p] for p in b["practices"]} for b in items} == BUNDLES
    listed = [p for b in items for p in b["practices"]]
    assert sorted(listed) == sorted(english) and len(listed) == len(set(listed)) == 15


def test_itil4_designations_use_the_official_modules(data):
    advanced = data["advanced"]
    codes = {m["code"]: m["name_en"] for m in advanced["itil4_modules"]}
    assert codes == {
        "CDS": "ITIL 4 Specialist: Create, Deliver and Support",
        "DSV": "ITIL 4 Specialist: Drive Stakeholder Value",
        "HVIT": "ITIL 4 Specialist: High-velocity IT",
        "DPI": "ITIL 4 Strategist: Direct, Plan and Improve",
        "DITS": "ITIL 4 Leader: Digital and IT Strategy",
    }
    designations = {d["name"]: set(d["requires"]) for d in advanced["itil4_designations"]}
    assert designations == {
        "ITIL 4 Managing Professional": {"CDS", "DSV", "HVIT", "DPI"},
        "ITIL 4 Strategic Leader": {"DPI", "DITS"},
        "ITIL 4 Practice Manager": {"CDS"},
    }
    assert all(_names_ok(m["who"]) for m in advanced["itil4_modules"])


def test_maturity_follows_the_gap_and_never_aims_above_3(data):
    gaps = {p["id"]: p["gap"] for p in data["practices"]["foundation"]}
    items = data["advanced"]["maturity"]["items"]
    assert sorted(i["practice"] for i in items) == sorted(gaps)
    allowed = {"nagy": {1}, "közepes": {1, 2}, "kicsi": {2, 3}}
    for i in items:
        assert i["now"] in allowed[gaps[i["practice"]]], i["practice"]
        assert i["now"] <= i["target"] <= 3, i["practice"]
    assert [s["level"] for s in data["advanced"]["maturity"]["scale"]] == [1, 2, 3, 4, 5]
    assert "**A cél sehol nem magasabb a 3-as szintnél.**" in data["advanced"]["maturity"]["ceiling"]


def test_itil5_facts_agree_with_the_primer_and_name_their_sources(data):
    itil5 = data["advanced"]["itil5"]
    facts = " ".join(itil5["facts"])
    primer = _norm(read_doc(data["primer_file"]))
    assert "**2027.12.31.**" in facts and "tervezetten 2027.12.31.**" in primer
    languages = re.search(r"kilenc nyelven érhető el \(([^)]+)\)", facts)[1].split(", ")
    assert len(languages) == 9 and "magyar" not in languages and "**magyarul még nem.**" in facts
    assert "kilenc nyelven érhető el — **magyarul még nem**" in primer
    assert [r["name"] for r in itil5["scheme"]] == [
        "ITIL Foundation (Version 5)", "ITIL Practice Manager", "ITIL Managing Professional",
        "ITIL Strategic Leader", "ITIL Master", "ITIL AI Governance",
    ]
    assert all("ITIL Transformation" in r["requires"] for r in itil5["scheme"][1:4])
    assert all(re.search(r"https://www\.(peoplecert\.org|itil\.com)/", s) for s in itil5["sources"])
    assert "https://www.peoplecert.org/help-and-support/faq-itil" in primer


def test_verdict_numbers_come_from_the_documents(data):
    verdict = _norm(data["advanced"]["verdict"])
    rollout = read_doc(ROLLOUT)
    assert "fennmaradó **190 munkatársra**" in rollout and "(190 fő, három hullám, 2027 januártól szeptemberig)" in verdict
    assert "2027.01.11. és 2027.09.30. között" in _norm(rollout)
    assert f"a {['nulla', 'egy', 'kettő', 'három', 'négy', 'öt', 'hat'][len(data['documents'])]} mintadokumentum közül három" in verdict
    assert "négy hónap" in _flat(data["error_journey"]) and "négy hónapig" in verdict


def test_advanced_tab_renders_with_the_maturity_averages(data, tmp_progress):
    at = AppTest.from_string("from pm_app import itil4\nitil4.view()\n", default_timeout=60).run()
    assert not at.exception
    items = data["advanced"]["maturity"]["items"]
    now = f"{itil4.maturity_average(items, 'now'):.1f}".replace(".", ",")
    target = f"{itil4.maturity_average(items, 'target'):.1f}".replace(".", ",")
    assert (now, target) == ("2,1", "2,7")
    assert any(f"**{now}** → reális cél 2027-re: **{target}**" in c.value for c in at.caption)
    cells = " ".join(str(v) for t in at.table for v in t.value.to_numpy().ravel())
    assert "ITIL AI Governance" in cells and "Monitor, Support and Fulfil" in cells
