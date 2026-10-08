"""A mérési lánc keresztellenőrzése: T0 → havi mérések → kérdőív → PIR → kiterjesztés.

A hatodik fázis azt állítja, hogy a projekt sikeres volt. Ez csak akkor hiteles,
ha a minősítés a mért számokból, az előre rögzített szabállyal kijön.
"""

from __future__ import annotations

import re

from conftest import ft, num, read_doc, section, tables

T0 = "docs/6-benefits/03-t0-baseline-jegyzokonyv.md"
PLAN = "docs/6-benefits/01-haszonrealizalasi-terv-vegleges.md"
MONTHLY = "docs/6-benefits/04-havi-meresi-riportok.md"
SURVEY = "docs/6-benefits/05-felhasznaloi-kerdoiv.md"
PIR = "docs/6-benefits/06-pir.md"
ROLLOUT = "docs/6-benefits/07-kiterjesztesi-javaslat.md"
CBA = "docs/1-initiation/03-koltseg-haszon-elemzes.md"
LESSONS = "docs/5-closure/05-tanulsagok-naploja.md"


def _value(cell: str) -> float:
    """`**74**`, `97,8%`, `12 667 Ft`, `0,75/né` → szám."""
    match = re.search(r"\d[\d  ]*(?:,\d+)?", cell.replace("*", ""))
    return float(match.group(0).replace(" ", "").replace(" ", "").replace(",", "."))


def _meets(value: float, rule: str) -> bool:
    """Célérték vagy küszöb: `≤ 72`, `≥ 40`, `100`, `> 95`, `< 20`."""
    rule = rule.replace("*", "").strip()
    limit = _value(rule)
    if rule.startswith("≤"):
        return value <= limit
    if rule.startswith("≥"):
        return value >= limit
    if rule.startswith(">"):
        return value > limit
    if rule.startswith("<"):
        return value < limit
    return value == limit


def _plan_rows() -> dict[str, list[str]]:
    rows = tables(section(read_doc(PLAN), "2. Mérőszámok"))[0]
    return {r[0]: r for r in rows}  # M#: [#, név, egység, T0, cél, kudarcküszöb, felelős]


def _t3_values() -> dict[str, float]:
    rows = tables(section(read_doc(MONTHLY), "1. Teljes adatsor"))[0]
    return {r[0]: _value(r[5]) for r in rows}


def classify(targets_met: int, below_threshold: int, satisfaction: float) -> str:
    """A Haszonrealizálási terv 3. pontjának döntési szabálya, hézag nélkül."""
    if targets_met >= 9 and below_threshold == 0 and satisfaction >= 4.0:
        return "SIKERES"
    if targets_met < 6 or below_threshold > 2 or satisfaction < 3.5:
        return "NEM SIKERES"
    return "RÉSZBEN SIKERES"


# --------------------------------------------------------------------- T0


def test_t0_availability_arithmetic():
    text = section(read_doc(T0), "M9")
    rows = {r[0]: r[1] for r in tables(text)[0]}
    days, hours = re.search(r"(\d+) munkanap.*× (\d+) óra = ([\d ]+) óra", rows["Elvárt üzemidő"]).groups()[:2]
    expected = int(days) * int(hours)
    assert expected == ft(rows["Elvárt üzemidő"].split("=")[-1].replace("óra", "Ft"))
    outage = _value(rows["Kiesés"].split(",")[1])
    assert round((expected - outage) / expected * 100, 1) == _value(rows["**Rendelkezésre állás**"].split("=")[-1])


def test_t0_satisfaction_is_the_mean_of_the_questions():
    rows = tables(section(read_doc(T0), "M11"))[1]
    questions = [_value(r[1]) for r in rows if not r[0].startswith("**")]
    mean_row = next(r for r in rows if r[0].startswith("**"))
    assert len(questions) == 6
    assert round(sum(questions) / 6, 1) == _value(mean_row[1])


def test_t0_ticket_categories_add_up():
    text = section(read_doc(T0), "M1–M3")
    rows = {r[0]: r[1] for r in tables(text)[0]}
    total = int(_value(rows["Összes ticket"]))
    parts = [int(p) for p in re.findall(r"\((\d+)\)|(\d+) db\)", rows["Kategóriabontás"]) for p in p if p]
    assert sum(parts) == total


# ------------------------------------------------------------------ kérdőív


def test_survey_t0_column_matches_t0_record():
    t0_rows = [r for r in tables(section(read_doc(T0), "M11"))[1] if not r[0].startswith("**")]
    survey = [r for r in tables(section(read_doc(SURVEY), "2. Az eredmények"))[0] if r[0].startswith("K")]
    assert [_value(r[1]) for r in t0_rows] == [_value(r[2]) for r in survey]


def test_survey_changes_and_means():
    rows = tables(section(read_doc(SURVEY), "2. Az eredmények"))[0]
    questions = [r for r in rows if r[0].startswith("K")]
    for r in questions:
        assert round(_value(r[3]) - _value(r[2]), 1) == num(r[4].replace("+", "")), r[0]
    mean_row = next(r for r in rows if "ÁTLAG" in r[1])
    t3_mean = round(sum(_value(r[3]) for r in questions) / len(questions), 1)
    assert t3_mean == _value(mean_row[3])
    assert t3_mean == _t3_values()["M11"]


def test_survey_group_split_is_consistent():
    text = read_doc(SURVEY)
    received = int(_value(tables(section(text, "1. A felmérés adatai"))[0][1][2]))
    groups = tables(section(text, "Bontás a home office"))[0]
    respondents = [int(_value(r[2])) for r in groups]
    assert sum(respondents) == received  # csak a beérkezett válaszokból bontható
    k5 = next(r for r in tables(section(text, "2. Az eredmények"))[0] if r[0] == "K5")
    weighted = sum(n * _value(r[3]) for n, r in zip(respondents, groups)) / received
    assert round(weighted, 1) == _value(k5[3])


# ------------------------------------------------------- havi mérés és PIR


def test_monthly_t3_matches_pir():
    pir_rows = tables(section(read_doc(PIR), "2. A vállalt hasznok"))[0]
    t3 = _t3_values()
    for r in pir_rows:
        assert _value(r[3]) == t3[r[0]], r[0]


def test_target_count_and_classification_follow_the_rule():
    plan, t3 = _plan_rows(), _t3_values()
    met = sum(_meets(t3[m], plan[m][4]) for m in plan)
    below = sum(_meets(t3[m], plan[m][5]) for m in plan)
    verdict = classify(met, below, t3["M11"])

    monthly = read_doc(MONTHLY)
    assert f"**Célérték elérve: {met} / 12. Kudarcküszöb alatt: {below}.**" in monthly
    pir = read_doc(PIR)
    assert f"MINŐSÍTÉS: **{verdict}**" in pir
    criteria = {r[0]: r[2] for r in tables(section(pir, "1. A minősítés"))[0]}
    assert f"{met} / 12" in criteria["Célértéket elérő mérőszámok"]
    assert f"{below}" in criteria["Kudarcküszöb alatti mérőszám"]


def test_classification_rule_has_no_gaps():
    """Minden lehetséges eredményre pontosan egy minősítés jut."""
    for met in range(13):
        for below in range(13 - met):
            for m11 in (3.0, 3.5, 3.9, 4.0, 4.5):
                assert classify(met, below, m11) in {"SIKERES", "RÉSZBEN SIKERES", "NEM SIKERES"}
    assert classify(10, 1, 4.2) == "RÉSZBEN SIKERES"  # a régi szabály ezt nem sorolta be
    assert classify(7, 2, 4.0) == "RÉSZBEN SIKERES"  # ahogy ezt sem


def test_t3_percentage_changes():
    rows = tables(section(read_doc(MONTHLY), "Elért célértékek"))[0]
    for r in rows:
        change = r[5].replace("*", "")
        if "%" in change and "pp" not in change and "tervezett" not in change:
            t0, t3 = _value(r[2]), _value(r[3])
            pct = round((t3 - t0) / t0 * 100)
            assert f"{pct:+d}%".replace("-", "−") == change.split()[0], r[0]


def test_home_office_split_matches_m6():
    groups = tables(section(read_doc(PIR), "M6 — Home office"))[0]
    weighted = sum(_value(r[1]) * _value(r[2]) for r in groups) / sum(_value(r[1]) for r in groups)
    assert round(weighted) == _t3_values()["M6"]


# ------------------------------------------------------- kapacitás-haszon


def _benefit_table(path: str, heading: str) -> tuple[list[list[str]], int]:
    rows = tables(section(read_doc(path), heading))[0]
    items = [r for r in rows if "Összesen" not in r[0]]
    total = ft(next(r for r in rows if "Összesen" in r[0])[2])
    return items, total


def _multiply(formula: str) -> float:
    factors = re.findall(r"(\d[\d  ]*(?:,\d+)?)", formula)
    result = 1.0
    for f in factors:
        result *= float(f.replace(" ", "").replace(" ", "").replace(",", "."))
    return result


def test_capacity_benefit_tables_multiply_and_add_up():
    for path, heading in ((CBA, "5. A hasznok"), (MONTHLY, "Kapacitás-haszon")):
        items, total = _benefit_table(path, heading)
        for r in items:
            assert round(_multiply(r[1])) == ft(r[2]), (path, r[0])
        assert sum(ft(r[2]) for r in items) == total, path


def test_ticket_volumes_use_the_t0_annual_total():
    """Megtakarított + maradék ticket = a T0 éves 1 240 tickete (mindkét számításban)."""
    annual = 1240
    for path, heading in ((CBA, "5. A hasznok"), (MONTHLY, "Kapacitás-haszon")):
        items, _ = _benefit_table(path, heading)
        saved = _value(items[0][1].split("×")[0])
        remaining = _value(items[1][1].split("×")[0])
        assert saved + remaining == annual, path


def test_pir_quotes_the_actual_capacity_benefit():
    _, actual = _benefit_table(MONTHLY, "Kapacitás-haszon")
    pir_row = next(r for r in tables(section(read_doc(PIR), "6. Költség és haszon"))[0] if r[0] == "Kapacitás-haszon")
    assert ft(pir_row[2]) == actual


# ------------------------------------------------------------ kiterjesztés


def test_rollout_follows_the_pre_agreed_mapping():
    pir = read_doc(PIR)
    rollout = read_doc(ROLLOUT)
    if "MINŐSÍTÉS: **SIKERES**" in pir:
        assert "# ⟹ **SZAKASZOS KITERJESZTÉS" in rollout
        assert "FELTÉTELES KITERJESZTÉS" not in rollout


def test_rollout_costs_add_up():
    text = read_doc(ROLLOUT)
    one_off = tables(section(text, "Egyszeri"))[0]
    items = [r for r in one_off if (not r[0].startswith("**") or r[0].startswith("**F")) and not r[0].startswith("Tartalék")]
    for r in items:
        assert int(_value(r[1])) * ft(r[2]) == ft(r[3]), r[0]
    subtotal = next(r for r in one_off if "Részösszeg" in r[0])
    reserve = next(r for r in one_off if r[0].startswith("Tartalék"))
    total = next(r for r in one_off if "Mindösszesen" in r[0])
    assert sum(ft(r[3]) for r in items) == ft(subtotal[3])
    pct = int(re.search(r"(\d+)%", reserve[0]).group(1))
    assert round(ft(subtotal[3]) * pct / 100) == ft(reserve[3])
    assert ft(subtotal[3]) + ft(reserve[3]) == ft(total[3])
    millions = round(ft(total[3]) / 1_000_000)
    assert f"kb. {millions} M Ft-ot" in text  # a bevezető ugyanazt az összeget mondja

    running = tables(section(text, "Folyó, a 190 főre"))[0]
    assert sum(ft(r[1]) for r in running[:-1]) == ft(running[-1][1])


def test_lessons_referenced_by_pir_exist():
    pir_ids = set(re.findall(r"T-\d\d", section(read_doc(PIR), "9. A mérési szakasz")))
    lessons = read_doc(LESSONS)
    for lesson in sorted(pir_ids):
        assert f"### {lesson} " in lessons, lesson


def test_lessons_header_matches_its_summary():
    text = read_doc(LESSONS)
    total = int(re.search(r"\| \*\*Összesen\*\* \| \*\*(\d+)\*\* \|", text).group(1))
    workshop = int(re.search(r"\| A záró workshopon jött elő \| \*\*(\d+)\*\* \|", text).group(1))
    assert f"**A {total} tanulságból {total - workshop} menet közben került be**" in text
