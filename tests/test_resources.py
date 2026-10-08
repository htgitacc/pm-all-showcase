"""Erőforrás- és felelősségi oldal: WBS-órák, erőforrásterv, RACI, kockázatok."""

from __future__ import annotations

import re

from conftest import read_doc, section, tables

WBS = "docs/2-planning/03-wbs.md"
BUDGET = "docs/2-planning/07-koltsegvetes.md"
RESOURCES = "docs/2-planning/08-eroforrasterv.md"
RACI = "docs/2-planning/09-raci-matrix.md"
REGISTER = "docs/2-planning/10-kockazatnyilvantartas.md"
RISK_REPORT = "docs/4-monitoring/05-kockazati-riport.md"
CLOSURE = "docs/5-closure/03-projektzaro-jelentes.md"


def _int(cell: str) -> int:
    return int(re.search(r"\d[\d  ]*", cell.replace("*", "")).group(0).replace(" ", "").replace(" ", ""))


# ---------------------------------------------------------------- WBS


def _wbs_rows():
    rows = tables(section(read_doc(WBS), "2. Munkacsomagok"))
    packages = [r for r in rows[0] if r[0]]
    total = next(r for r in rows[0] if "Összesen" in r[1])
    split = {r[0]: _int(r[1]) for r in rows[1]}
    return packages, _int(total[3]), split


def test_wbs_table_covers_the_tree():
    text = read_doc(WBS)
    tree = re.findall(r"[├└]── (\d[\d.]*)  ", text)
    leaves = {t for t in tree if not any(o.startswith(t + ".") for o in tree)}
    packages, _, _ = _wbs_rows()
    assert {r[0] for r in packages} == leaves


def test_wbs_hours_add_up_and_split():
    packages, total, split = _wbs_rows()
    by_type: dict[str, int] = {}
    for r in packages:
        kind = r[4].split()[0]
        by_type[kind] = by_type.get(kind, 0) + _int(r[3])
    assert sum(by_type.values()) == total

    note = re.search(r"3\.3\.1: (\d+) \+ (\d+), 3\.4\.2: (\d+) \+ (\d+), 3\.5: (\d+) \+ (\d+), 5\.2: (\d+) \+ (\d+)",
                     read_doc(WBS))
    shares = list(map(int, note.groups()))
    internal_mixed, external_mixed = sum(shares[0::2]), sum(shares[1::2])
    hours = {r[0]: _int(r[3]) for r in packages}
    for wbs, (a, b) in zip(("3.3.1", "3.4.2", "3.5", "5.2"), zip(shares[0::2], shares[1::2])):
        assert a + b == hours[wbs], wbs
    assert internal_mixed + external_mixed == by_type["vegyes"]
    assert split["Belső ráfordítás"] == by_type["belső"] + internal_mixed
    assert split["Külső (Cloudia Solutions)"] == by_type["külső"] + external_mixed


def test_internal_hours_quoted_consistently():
    _, _, split = _wbs_rows()
    internal = split["Belső ráfordítás"]
    assert f"Belső munkaidő ({internal} óra)" in read_doc(BUDGET)
    assert f"A WBS {internal} belső órájához képest" in read_doc(RESOURCES)


# ------------------------------------------------------------ erőforrásterv


def test_resource_plan_adds_up():
    text = read_doc(RESOURCES)
    people = tables(section(text, "1. Belső erőforrások"))[0]
    rows = [r for r in people if r[0]]
    total = _int(next(r for r in people if "Belső összesen" in r[1])[2])
    assert sum(_int(r[2]) for r in rows) == total

    monthly = tables(section(text, "3. Terhelés hónapokra bontva"))[0]
    months = [2, 3, 4, 5, 6, 7]
    per_person = {r[0]: [0 if c in ("—", "") else _int(c) for c in r[1:]] for r in monthly if "összesen" not in r[0]}
    sums = [_int(c) for c in next(r for r in monthly if "összesen" in r[0])[1:]]
    for i in range(len(months)):
        assert sum(v[i] for v in per_person.values()) == sums[i], months[i]
    assert sum(sums) == total

    planned = {r[0].split(" (")[0]: _int(r[2]) for r in rows}
    for name, values in per_person.items():
        key = name.split(" (")[0]
        match = next(k for k in planned if k.split(" (")[0].startswith(key.split()[0]))
        assert sum(values) == planned[match], name

    # akinek egy hónapban órája van, annak az időszaka is fedje le azt a hónapot
    periods = {r[0]: r[3] for r in rows}
    for name, values in per_person.items():
        match = next((k for k in periods if k == name), None)
        if not match:
            continue
        start, end = re.findall(r"(\d\d)\.\d\d", periods[match])[:2]
        for month, hours in zip(months, values):
            if hours:
                assert int(start) <= month <= int(end), (name, month)

    gap = total - _int(re.search(r"A WBS (\d+) belső órájához", text).group(1))
    assert f"{gap} óra a többlet" in text


# ------------------------------------------------------------------- RACI


def _raci_rows():
    text = read_doc(RACI)
    blocks = {}
    for number in re.findall(r"^## (\d)\. ", text, flags=re.M):
        found = tables(section(text, f"{number}. "))
        blocks[number] = found[0] if found else []
    return text, blocks


def test_raci_one_accountable_and_an_executor_per_row():
    text, blocks = _raci_rows()
    expected = {r[0].split(".")[0]: _int(r[1]) for r in tables(section(text, "Ellenőrzés"))[0] if r[0][0].isdigit()}
    for block, rows in blocks.items():
        if block not in expected:
            continue
        assert len(rows) == expected[block], block
        for r in rows:
            cells = [c.replace("*", "") for c in r[1:]]
            assert sum(c in ("A", "A/R") for c in cells) == 1, r[0]
            assert any(c in ("R", "A/R") for c in cells) or "R:" in r[0], r[0]


# ------------------------------------------------------------- kockázatok


def _register():
    text = read_doc(REGISTER)
    risks = {}
    high = section(text, "2. Magas besorolású")
    for block in re.split(r"^### ", high, flags=re.M)[1:]:
        rid = block.split()[0]
        p, i, score = map(int, re.search(r"(\d) × (\d) = \*\*(\d+)", block).groups())
        risks[rid] = ("magas", p, i, score)
    for heading, level in (("3. Közepes", "közepes"), ("4. Alacsony", "alacsony")):
        for r in tables(section(text, heading))[0]:
            vh = next(c for c in r if "×" in c)
            p, i, score = map(int, re.search(r"(\d) × (\d) = (\d+)", vh).groups())
            risks[r[0]] = (level, p, i, score)
    return text, risks


def _level(score: int) -> str:
    return "magas" if score >= 6 else "közepes" if score >= 3 else "alacsony"


def test_register_scores_and_sections():
    _, risks = _register()
    for rid, (level, p, i, score) in risks.items():
        assert p * i == score, rid
        assert _level(score) == level, (rid, score, level)


def test_register_review_log_counts():
    text, risks = _register()
    log = re.search(r"Planning-kapu előtt; (\d+) kockázat: (\d+) nyitott .*?, (\d+) lezárt", text)
    total, open_, closed = map(int, log.groups())
    assert total == len(risks) == open_ + closed


def test_risk_report_overview_matches_its_tables():
    text = read_doc(RISK_REPORT)
    overview = {r[0].replace("*", ""): r for r in tables(section(text, "1. Összkép"))[0]}
    closed = tables(section(text, "4. Lezárt kockázatok"))[0]
    open_rows = tables(section(text, "5. Nyitott kockázatok"))[0]
    occurred = tables(section(text, "3. Bekövetkezett kockázatok"))[0]

    current = [int(re.findall(r"\d+", r[2].replace("*", ""))[-1]) for r in open_rows]
    levels = [_level(s) for s in current]
    now = lambda key: _int(overview[key][2])  # noqa: E731
    assert now("Lezárva") == len(closed)
    assert now("Nyitott, magas (≥6)") == levels.count("magas")
    assert now("Nyitott, közepes (3–4)") == levels.count("közepes")
    assert now("Nyitott, alacsony (1–2)") == levels.count("alacsony")
    assert now("Bekövetkezett") == len(occurred)
    assert len(closed) + len(open_rows) == now("Nyilvántartott kockázat")


def test_closure_risk_statistics_add_up():
    rows = {r[0].replace("*", ""): r[1] for r in tables(section(read_doc(CLOSURE), "7. Kockázatok és problémák"))[0]}
    total = _int(rows["Nyilvántartott kockázat"])
    parts = sum(_int(v) for k, v in rows.items() if k.startswith(("Lezárva", "Nyitva", "Átadva")))
    assert parts == total


def test_schedule_risk_ids_exist_in_register():
    _, risks = _register()
    schedule = read_doc("docs/2-planning/06-utemterv.md")
    for rid in re.findall(r"^\| (R\d+) \|", section(schedule, "6. A legnagyobb ütemkockázatok"), flags=re.M):
        assert rid in risks, rid
