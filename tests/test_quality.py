"""Beszerzés, minőség és követelmény-nyomonkövetés.

A fő lánc: követelmény (K) → teszteset (T) → átvételi kritérium (AK) →
szerződéses feltétel (Sz). Mellette a beszerzési pontozás, a szállítás közbeni
minőségellenőrzés, az oktatás, az érintettek–RACI–kommunikáció névsora és az
archiválási jegyzék verziói. Minden állításnak abból kell kijönnie, amit a
dokumentumok tételesen tartalmaznak.
"""

from __future__ import annotations

import datetime as dt
import re
from collections import Counter
from pathlib import Path

import pytest

from conftest import ROOT, ft, num, read_doc, section, tables
from test_registers import _acceptance, _kv, _plain
from test_schedule import _tasks

RTM = "docs/2-planning/05-kovetelmeny-matrix.md"
SCOPE = "docs/2-planning/02-hatokor-nyilatkozat.md"
QUALITY = "docs/2-planning/14-minosegterv.md"
TEST_PLAN = "docs/2-planning/16-tesztterv.md"
TESTS = "docs/3-execution/07-tesztjegyzokonyv.md"
UAT = "docs/3-execution/08-uat-elfogadas.md"
HANDOVER = "docs/5-closure/01-atadas-atveteli-jegyzokonyv.md"
AS_BUILT = "docs/3-execution/06-as-built-dokumentacio.md"
QC = "docs/4-monitoring/07-minosegellenorzesi-jegyzokonyv.md"
ISSUES = "docs/3-execution/10-problemanaplo.md"
CRITERIA = "docs/2-planning/13-szallitoertekelesi-szempontrendszer.md"
OFFERS = "docs/3-execution/03-ajanlat-osszehasonlitas.md"
CERTS = "docs/3-execution/05-teljesitesigazolas.md"
FIN_CLOSE = "docs/5-closure/04-penzugyi-zaras.md"
TRAINING_PLAN = "docs/2-planning/17-oktatasi-terv.md"
TRAINING = "docs/3-execution/09-oktatasi-anyag.md"
SCHEDULE = "docs/2-planning/06-utemterv.md"
STAKEHOLDERS = "docs/1-initiation/06-erintettek-nyilvantartasa.md"
POWER = "docs/1-initiation/07-hatalom-erdek-matrix.md"
RACI = "docs/2-planning/09-raci-matrix.md"
COMMS = "docs/2-planning/11-kommunikacios-terv.md"
ARCHIVE = "docs/5-closure/08-archivalasi-jegyzek.md"

YEAR = 2026


def _day(text: str) -> dt.date:
    month, day = re.search(r"(\d\d)\.(\d\d)\.", text).groups()
    return dt.date(YEAR, int(month), int(day))


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


# ---------------------------------------------------------------- követelmény → teszt → AK


def _requirements() -> dict[str, dict]:
    reqs = {}
    for line in read_doc(RTM).splitlines():
        if re.match(r"\| K\d\d \|", line):
            c = _cells(line)
            reqs[c[0]] = {"text": c[1], "pri": c[2], "source": c[3], "test": c[5],
                          "aks": re.findall(r"AK-\d+", c[6]), "status": c[7]}
    return reqs


def _quality_criteria() -> dict[str, list[str]]:
    rows = {}
    for t in tables(section(read_doc(QUALITY), "1. Átvételi kritériumok")):
        for r in t:
            rows[_plain(r[0])] = r
    return rows


def _test_results() -> dict[str, dict]:
    rows = tables(section(read_doc(TESTS), "3. Tesztesetek eredménye"))[0]
    return {r[0]: {"req": r[2], "first": r[3], "retest": r[4], "final": r[5]} for r in rows}


def test_requirement_ids_priorities_and_summary():
    reqs = _requirements()
    assert list(reqs) == [f"K{i:02d}" for i in range(1, len(reqs) + 1)]

    text = read_doc(RTM)
    summary = {_plain(r[0]).split(" ")[0]: int(_plain(r[1])) for r in tables(section(text, "Összesítés"))[0]}
    counts = Counter(r["pri"] for r in reqs.values())
    assert summary["K"] == counts["K"] and summary["F"] == counts["F"] and summary["H"] == counts["H"]
    assert summary["Összesen"] == len(reqs)
    rejected = tables(section(text, "6. Elutasított"))[0]
    assert summary["Elutasítva"] == len(rejected)

    # A változásnapló: az első változat + a később hozzáadott tételek = a mai lista.
    log = tables(section(text, "Változásnapló"))[0]
    initial = int(re.search(r"Első változat, (\d+) követelmény", log[0][1]).group(1))
    added = [r for r in log if re.search(r"K\d\d\** hozzáadva", r[1])]
    assert initial + len(added) == len(reqs)


def test_out_of_scope_references_point_to_scope_exclusions():
    """A K1–K11 hatókör-kizárás nem keverhető a K01–K27 követelménnyel."""
    exclusions = {r[0].strip("*"): r[1] for r in tables(section(read_doc(SCOPE), "4. Ami NINCS"))[0]}
    for r in tables(section(read_doc(RTM), "6. Elutasított"))[0]:
        if "Hatókörön kívül" in r[4]:
            ref = re.search(r"hatókör-kizárás (K\d+)\)", r[4])
            assert ref, r[0]
            assert ref.group(1) in exclusions, r[0]


def test_every_requirement_has_its_test_case():
    reqs = _requirements()
    plan_text = read_doc(TEST_PLAN)
    plan = {r[0]: r for r in tables(section(plan_text, "5. Tesztesetek"))[0]}
    assert sorted(r["test"] for r in reqs.values()) == sorted(plan)
    for rid, r in reqs.items():
        row = plan[r["test"]]
        assert row[2] == rid and row[3] == r["pri"], rid
    mandatory = sum(r["pri"] == "K" for r in reqs.values())
    assert f"Összesen {len(plan)} teszteset**, ebből {mandatory} kötelező (K)" in plan_text
    assert f"mind a {len(reqs)} elfogadott" in plan_text

    results = _test_results()
    assert {t: r["req"] for t, r in results.items()} == {r["test"]: rid for rid, r in reqs.items()}
    ki1 = next(r for r in tables(read_doc(UAT))[1] if r[0] == "KI-1")
    assert ki1[2] == ki1[3] == f"{mandatory}/{mandatory}"


def test_mandatory_requirements_have_acceptance_criteria():
    reqs = _requirements()
    criteria = _quality_criteria()
    assert list(criteria) == [f"AK-{i:02d}" for i in range(1, len(criteria) + 1)]

    mapped = {ak for r in reqs.values() for ak in r["aks"]}
    assert mapped <= set(criteria)
    for rid, r in reqs.items():
        if r["pri"] == "K":
            assert r["aks"], f"{rid}: kötelező követelmény átvételi kritérium nélkül"

    # Ami nem követelményhez tartozik, az a teljes megoldásra szóló kritérium —
    # árva kritérium nincs.
    whole = [r[0] for r in tables(section(read_doc(RTM), "Átvételi kritériumok a teljes"))[0]]
    assert not mapped & set(whole)
    assert mapped | set(whole) == set(criteria)


def test_requirement_status_follows_test_and_acceptance_results():
    reqs, results = _requirements(), _test_results()
    uat = _acceptance(UAT)
    for rid, r in reqs.items():
        passed = "✔" in results[r["test"]]["final"]
        assert r["status"].startswith("teljesült") == passed, rid
        assert r["status"].startswith("**nem teljesült**") == (not passed), rid
        for ak in r["aks"]:
            assert uat[ak] == passed, (rid, ak)
        if not passed:
            assert r["pri"] != "K", f"{rid}: kötelező követelmény nem teljesült, mégis van átvétel"
    failed_aks = {ak for ak, ok in uat.items() if not ok}
    assert failed_aks == {ak for r in reqs.values() if "nem teljesült" in r["status"] for ak in r["aks"]}


def _linked_tests(cell: str) -> list[str]:
    """Egy hiba tesztesetei — a zárójeles megjegyzés (pl. regressziós újrateszt) nélkül."""
    return re.findall(r"T-\d+", cell.split("(")[0])


def test_test_rounds_add_up_and_every_failure_has_a_defect():
    results = _test_results()
    total = len(results)
    first = sum("✔" in r["first"] for r in results.values())
    final = sum("✔" in r["final"] for r in results.values())
    pct = lambda n: f"{n / total * 100:.1f}".replace(".", ",") + "%"

    text = read_doc(TESTS)
    stages = {_plain(r[0]): r[3] for r in tables(section(text, "1. A teszt szakaszai"))[0]}
    assert stages["UAT — 1. kör"] == f"{first}/{total} teszteset megfelelt ({pct(first)})"
    assert f"{final}/{total} megfelelt ({pct(final)})" in stages["UAT — újratesztelés"]
    assert f"{final} / {total} = {pct(final)}" in text

    # Az első kör aránya minden riportban ugyanaz.
    for path in ("docs/4-monitoring/08-merfoldko-riport.md", "docs/prince2/02-highlight-report.md",
                 "docs/prince2/03-exception-report.md"):
        assert f"{first}/{total} teszteset" in read_doc(path), path
    for path in ("docs/4-monitoring/09-eszkalacios-naplo.md", "docs/prince2/02-highlight-report.md",
                 "docs/prince2/03-exception-report.md"):
        assert pct(first) in read_doc(path), path

    # Ami az első körben bukott, ahhoz hiba tartozik, és újrateszt; ami megfelelt,
    # de mégis újratesztelték, az regressziós.
    linked = set()
    linked |= set(_linked_tests(_kv(section(text, "H-01"))["Teszteset"]))
    linked |= set(_linked_tests(_kv(section(text, "H-02"))["Teszteset"]))
    for r in tables(section(text, "S2 — súlyos"))[0]:
        linked |= set(_linked_tests(r[2]))
    failed_first = {t for t, r in results.items() if "✖" in r["first"]}
    assert linked == failed_first
    for t, r in results.items():
        if "✖" in r["first"]:
            assert r["retest"] != "—", t
        elif r["retest"] != "—":
            assert "regressziós" in r["retest"], t


def test_technical_test_starts_when_the_test_machines_arrive():
    text = read_doc(TESTS)
    stage = next(r for r in tables(section(text, "1. A teszt szakaszai"))[0] if r[0].startswith("Technikai teszt"))
    start = _day(stage[1].split("–")[0].strip() + ".")
    task = next(t for t in _tasks() if t["id"] == "6.2")
    assert start == task["start"]
    delivery = _day(_kv(section(read_doc(CERTS), "1. sz. átvételi jegyzőkönyv"))["Szállítás dátuma"])
    assert start >= delivery
    assert f"**Tesztidőszak:** {YEAR}.{start:%m.%d}" in text


# ---------------------------------------------------------------- minőség


def _minutes(text: str) -> int:
    h, m = re.search(r"(\d+) óra (\d+) perc", text).groups()
    return int(h) * 60 + int(m)


def test_autopilot_measurement_follows_the_quality_plan():
    plan = _quality_criteria()["AK-06"]
    machines = int(re.search(r"(\d+) gépen mérve", plan[2]).group(1))

    rows = [r for r in tables(section(read_doc(AS_BUILT), "3.4 Autopilot"))[0] if r[0].startswith("**Javítás után**")]
    assert len(rows) == machines and len({r[1].split(",")[0] for r in rows}) == machines
    values = [_minutes(r[2]) for r in rows]
    average = round(sum(values) / len(values))
    stated = f"{average // 60} óra {average % 60} perc"
    assert f"javítás utáni {machines} mérés" in read_doc(AS_BUILT)
    uat = next(r for t in tables(read_doc(UAT)) for r in t if r[0] == "AK-06")
    assert stated in uat[3] and f"{machines} gép átlaga" in uat[3]

    qc = _kv(section(read_doc(QC), "Feltárt eltérés — QC-02"))
    listed = re.findall(r"(\d):(\d\d)", qc["Újramérés"])
    assert sorted(int(h) * 60 + int(m) for h, m in listed) == sorted(values)
    assert f"{machines} gépen" in qc["Újramérés"]

    # Lezárni csak az újramérés után lehet — a javítás napja nem elég.
    last = max(_day(re.search(r"\((\d\d\.\d\d\.)\)", r[0]).group(1)) for r in rows)
    assert _day(qc["Lezárva"].split("2026.")[1]) >= last
    p06 = _kv(section(read_doc(ISSUES), "P-06"))
    assert _day(p06["Lezárva"].split("2026.")[1]) >= last


def test_quality_control_log_summary_and_plan():
    text = read_doc(QC)
    checks = tables(section(text, "1. Ellenőrzési terv"))[0]
    clean = [r for r in checks if "✔" in r[4]]
    deviating = [r for r in checks if "✔" not in r[4]]
    summary = {_plain(r[0]): int(_plain(r[1])) for r in tables(section(text, "8. Összesítés"))[0]}
    assert summary["Elvégzett ellenőrzés"] == len(checks)
    assert summary["Eltérés nélkül megfelelt"] == len(clean)
    assert summary["Eltéréssel (kezelve és lezárva)"] == len(deviating)
    findings = tables(section(text, "8. Összesítés"))[1]
    assert len(findings) == len(deviating) == len(re.findall(r"^### Feltárt (?:eltérés|hiány) — QC-", text, re.M))

    # A minőségterv dátumozott ellenőrzései pontosan így szerepelnek a jegyzőkönyvben.
    planned = {r[0]: r[1] for r in tables(section(read_doc(QUALITY), "3. Minőségellenőrzés"))[0]}
    by_name = {r[1]: r[2] for r in checks}
    for name, when in planned.items():
        if re.fullmatch(r"\d\d\.\d\d\.", when):
            assert by_name[name.replace("Mentés és visszaállítás", "Mentés, megőrzés, visszaállítás")] == when, name


def test_qc02_lead_time_is_measured_to_the_main_rollout():
    found = _day(_kv(section(read_doc(QC), "4. E-03"))["Dátum"].split("2026.")[1])
    wave2 = next(t for t in _tasks() if t["id"] == "7.2")["start"]
    lead = (wave2 - found).days
    for path in (QC, "docs/4-monitoring/08-merfoldko-riport.md", "docs/5-closure/05-tanulsagok-naploja.md",
                 "docs/5-closure/07-eroforras-elengedes.md", "docs/prince2/02-highlight-report.md"):
        assert f"{lead} nappal" in read_doc(path), path
    assert f"{lead} nap volt hátra" in read_doc("docs/4-monitoring/09-eszkalacios-naplo.md")
    for path in ROOT.joinpath("docs").rglob("*.md"):
        assert "teljes élesítés előtt" not in path.read_text(encoding="utf-8"), path


def test_m5_certificate_checks_exactly_the_m5_criteria():
    m5 = {_plain(r[0]) for r in tables(section(read_doc(CERTS), "Ellenőrzött átvételi kritériumok"))[0]}
    planned = {ak for ak, r in _quality_criteria().items() if r[4] == "M5"}
    assert m5 == planned


# ---------------------------------------------------------------- beszerzés


def _weights(heading: str) -> dict[str, float]:
    rows = tables(section(read_doc(CRITERIA), heading))[0]
    return {r[0]: float(r[2].rstrip("%")) for r in rows if r[0]}


def _scores(heading: str) -> tuple[list[str], list[list[str]], list[float]]:
    rows = tables(section(read_doc(OFFERS), heading))[0]
    body = [r for r in rows if not r[0].startswith("**Súlyozott")]
    totals = [num(c) for c in next(r for r in rows if r[0].startswith("**Súlyozott"))[2:]]
    return [r[0] for r in body], body, totals


def _points(cell: str) -> float:
    m = re.search(r"→ ([\d,]+) p", cell)
    return num(m.group(1)) if m else num(cell.replace(" p", ""))


@pytest.mark.parametrize("criteria, offers", [
    ("2. Értékelési szempontok és súlyok — B1", "4. B1"),
    ("3. Értékelési szempontok és súlyok — B2+B3", "5. B2+B3"),
])
def test_supplier_scores_recompute(criteria, offers):
    weights = _weights(criteria)
    assert sum(weights.values()) == 100
    _, body, totals = _scores(offers)
    assert [float(r[1].rstrip("%")) for r in body] == list(weights.values())

    # Ár: a legolcsóbb érvényes ajánlat 100 pont, a többi arányosan.
    prices = [ft(c) for c in body[0][2:]]
    for price, cell in zip(prices, body[0][2:]):
        assert _points(cell) == round(min(prices) / price * 100, 1)

    for col, total in enumerate(totals, start=2):
        weighted = sum(_points(r[col]) * float(r[1].rstrip("%")) / 100 for r in body)
        assert round(weighted, 1) == total


def test_supplier_scales_follow_the_criteria():
    _, b1, _ = _scores("4. B1")
    rows = {r[0]: r for r in b1}
    deadline = {"05.29": 100, "06.05": 60, "06.12": 20}
    for cell in rows["Szállítási határidő"][2:]:
        assert _points(cell) == deadline[re.search(r"\.(\d\d\.\d\d)\.", cell).group(1)]
    refs = {3: 100, 2: 70, 1: 40, 0: 0}
    for cell in rows["Referencia (Autopilot)"][2:]:
        assert _points(cell) == refs[min(int(re.match(r"(\d+)", cell).group(1)), 3)]
    for cell in rows["Kötbérmérték"][2:]:
        rate = num(re.search(r"napi ([\d,]+)%", cell).group(1))
        assert _points(cell) == (100 if rate > 0.5 else 70 if rate == 0.5 else 40)
    _, b23, _ = _scores("5. B2+B3")
    for cell in next(r for r in b23 if r[0].startswith("Referencia"))[2:]:
        assert _points(cell) == refs[min(int(re.match(r"(\d+)", cell).group(1)), 3)]


def test_procurement_savings_and_excluded_offer():
    text = read_doc(OFFERS)
    _, b1, _ = _scores("4. B1")
    _, b23, _ = _scores("5. B2+B3")
    b1_win, b23_win = ft(b1[0][2]), ft(b23[0][2])  # a nyertes az első oszlop
    novacomp = ft(_kv(section(text, "A NovaComp Kft. kizárása"))["Ajánlati ár"])
    assert f"{b1_win - novacomp:,} Ft-tal olcsóbb".replace(",", " ") in text
    azurion = min(ft(c) for c in b23[0][2:])
    assert f"{b23_win - azurion:,} Ft-tal".replace(",", " ") in text

    rows = {r[0].split(" — ")[0].strip("*"): r for r in tables(section(text, "6. Pénzügyi összegzés"))[0]}
    assert ft(rows["B1"][2]) == b1_win and ft(rows["B2+B3"][2]) == b23_win
    for key in ("B1", "B2+B3", "Összesen"):
        assert ft(rows[key][2]) - ft(rows[key][1]) == ft(rows[key][3])
    assert ft(rows["Összesen"][1]) == ft(rows["B1"][1]) + ft(rows["B2+B3"][1])


def test_certificate_payments_match_the_financial_closure():
    summary = tables(section(read_doc(CERTS), "Összefoglaló — kifizetések állása"))[0]
    payments = [r for r in summary if r[0]]
    assert all(r[3].startswith("✔ kifizetve") for r in payments)
    totals = {_plain(r[1]): ft(r[2]) for r in summary if not r[0]}
    assert totals["Kifizetve összesen"] == sum(ft(r[2]) for r in payments)
    assert totals["Hátralévő"] == 0

    vendor_rows = [r for t in tables(read_doc(FIN_CLOSE)) for r in t
                   if len(r) == 6 and r[1] in {"Cloudia Solutions", "TechLine Zrt."}]
    assert sorted((r[1], ft(r[3]), _day(r[5].strip("*")[5:])) for r in vendor_rows) == \
        sorted((r[0], ft(r[2]), _day(r[3].split("kifizetve ")[1])) for r in payments)

    # Az archivált változat dátuma az utolsó kifizetésé.
    last = max(_day(r[3].split("kifizetve ")[1]) for r in payments)
    archived = next(_cells(l) for l in read_doc(ARCHIVE).splitlines() if "XYO-CP-205" in l)
    assert archived[3] == f"{YEAR}.{last:%m.%d}."


# ---------------------------------------------------------------- oktatás


def _training_plan() -> list[dict]:
    rows = tables(section(read_doc(TRAINING_PLAN), "2. Ütemezés"))[0]
    result = []
    for r in rows:
        live = re.search(r"élesítés (\d\d\.\d\d)", r[1])
        if live:
            result.append({"name": _plain(r[0]).replace(" oktatása", ""), "live": _day(live.group(1) + "."),
                           "date": _day(_plain(r[2])[5:])})
    return result


def test_training_happens_two_to_four_days_before_go_live_on_arrived_machines():
    arrivals = {}
    for t in _tasks():
        for count, day in re.findall(r"(\d+) gép \((\d\d\.\d\d\.)\)", t["deps"]):
            arrivals[int(count)] = _day(day)
    groups = _training_plan()
    assert len(groups) == 5
    for g in groups:
        assert 2 <= (g["live"] - g["date"]).days <= 4, g["name"]
        machines = arrivals[10] if g["name"].startswith("UAT") else arrivals[40]
        assert g["date"] >= machines, g["name"]

    # Az 5.2 munkacsomag a 2–5. csoporttól a pótló alkalomig tart.
    task = next(t for t in _tasks() if t["id"] == "5.2")
    makeup = _day(_plain(next(r for r in tables(section(read_doc(TRAINING_PLAN), "2. Ütemezés"))[0]
                              if r[0].startswith("**Pótló"))[2])[5:])
    assert task["start"] == min(g["date"] for g in groups if not g["name"].startswith("UAT"))
    assert task["end"] == makeup


def test_attendance_sheet_adds_up():
    text = read_doc(TRAINING)
    rows = tables(section(text, "3. Jelenléti ív"))[0]
    sessions = [r for r in rows if r[1]]
    total = next(r for r in rows if not r[1])
    for r in sessions:
        assert int(_plain(r[2])) == int(_plain(r[3])) + int(_plain(r[4])), r[0]
    for col in (2, 3, 4):
        assert int(_plain(total[col])) == sum(int(_plain(r[col])) for r in sessions)
    assert f"({len(sessions)} alkalom)" in total[0]

    makeup = next(r for r in sessions if "Pótló" in r[0])
    regular = [r for r in sessions if r is not makeup]
    absent = sum(int(_plain(r[4])) for r in regular)
    assert int(_plain(makeup[2])) == absent
    present = sum(int(_plain(r[3])) for r in sessions)
    assert f"{present}/50" in text and f"egyedi\nrésztvevő {present} fő" in text
    assert f"({present - int(_plain(makeup[3]))} az alkalmon, {int(_plain(makeup[3]))} a pótlón)" in read_doc(UAT)
    assert f"{present}/50 fő, {len(sessions)} alkalom" in read_doc(HANDOVER)

    # A hiányzók tételes pótlása a csoportok hiányzásaiból jön, a dátumok a tervből.
    makeup_rows = tables(section(text, "A hiányzók pótlása"))[0]
    by_date = Counter()
    for r in makeup_rows:
        by_date[_day(r[1])] += int(re.match(r"(\d+)", r[0]).group(1))
    expected = Counter({_day(r[1][5:]): int(_plain(r[4])) for r in regular if int(_plain(r[4]))})
    assert by_date == expected
    planned_dates = {g["date"] for g in _training_plan()}
    assert {_day(r[1][5:]) for r in regular} == planned_dates


def test_training_agenda_is_three_hours_and_the_change_is_documented():
    def blocks(path, heading):
        rows = tables(section(read_doc(path), heading))[0]
        return {r[0]: int(re.match(r"(\d+)", r[1]).group(1)) for r in rows}

    plan = blocks(TRAINING_PLAN, "3. Oktatási tematika")
    final = blocks(TRAINING, "1. Oktatási tematika")
    assert sum(plan.values()) == sum(final.values()) == 180
    changed = {k: (plan[k], final[k]) for k in plan if plan[k] != final[k]}
    assert changed == {"2. Első belépés": (25, 30), "6. Kérdések és szabad gyakorlás": (30, 25)}
    assert "25-ről 30 percre" in read_doc(TRAINING) and "30-ról 25 percre" in read_doc(TRAINING)


# ---------------------------------------------------------------- érintettek, RACI, kommunikáció


def _stakeholders() -> dict[str, list[str]]:
    rows = {}
    for t in tables(read_doc(STAKEHOLDERS)):
        for r in t:
            if re.fullmatch(r"E\d+", r[0]):
                rows[r[0]] = r
    return rows


def test_stakeholder_register_ids_and_change_log():
    rows = _stakeholders()
    assert sorted(rows, key=lambda k: int(k[1:])) == [f"E{i}" for i in range(1, len(rows) + 1)]
    log = tables(section(read_doc(STAKEHOLDERS), "6. Változásnapló"))[0]
    initial = int(re.search(r"(\d+) érintett rögzítése", log[0][1]).group(1))
    added = [r for r in log if "felvétele" in r[1]]
    assert initial + len(added) == len(rows)

    grid = read_doc(POWER).split("```")[1]
    named = set(re.findall(r"E\d+", grid))
    assert named == set(rows)


def test_named_people_are_registered_stakeholders():
    register = read_doc(STAKEHOLDERS)
    people = set()
    for r in _requirements().values():
        people.add(re.sub(r"\s*\(.*\)", "", r["source"]))
    for path in (UAT, QUALITY):
        for t in tables(section(read_doc(path), "7. Hivatalos" if path == UAT else "5. Az átvétel aláírói")):
            for r in t:
                if "Bizottság" not in r[1]:
                    people.add(_plain(r[1]).split(",")[0])
    people.discard("Üzemi tanács")
    for p in people:
        assert p in register, p


def test_raci_names_the_mandatory_user_signature():
    signer = next(_plain(r[1]).split(",")[0] for r in tables(section(read_doc(QUALITY), "5. Az átvétel aláírói"))[0]
                  if "Felhasználói képviselő" in r[0])
    row = next(_cells(l) for l in read_doc(RACI).splitlines() if l.startswith("| UAT-elfogadás aláírása"))
    assert signer in row[0]


def test_every_stakeholder_has_a_communication_line():
    comms = read_doc(COMMS)
    lines = " ".join(r[0] for r in tables(section(comms, "7. Érintettenkénti"))[0])
    groups = {"E10": "Pilot résztvevők", "E11": "Területvezetők", "E12": "Kimaradó kollégák",
              "E13": "Üzemi tanács", "E14": "Cloudia", "E15": "TechLine", "E16": "mobilszolgáltatók"}
    for sid, r in _stakeholders().items():
        key = groups.get(sid, r[1])
        assert key in lines, sid

    # Az egyszeri kommunikációnak is kell időpont és csatorna, nem csak szándék.
    operational = section(comms, "1. Rendszeres") + section(comms, "3. Eseti")
    assert "E12" in operational and "a névsor előtt" in operational


# ---------------------------------------------------------------- archiválási jegyzék


def _documents() -> dict[str, tuple[Path, str]]:
    docs = {}
    for path in ROOT.joinpath("docs").glob("[1-6]-*/*.md"):
        text = path.read_text(encoding="utf-8")
        docs[re.search(r"XYO-CP-[A-Z0-9-]+", text).group(0)] = (path, text)
    return docs


def _archive_rows() -> list[list[str]]:
    body = read_doc(ARCHIVE).split("## 2. Dokumentumjegyzék")[1].split("### 6.")[0]
    return [_cells(l) for l in body.splitlines() if re.match(r"\| \**XYO-CP-\d", l)]


# Ismert, indokolt eltérések: a költségvetés v1.1-et a VK-04 hozta (06.18.), a
# repóban a v1.0 bázis látszik; a tanulságok naplója a PIR után (10.09.) bővült,
# az archívum a 06.29-i v1.0-t őrzi.
EXPLAINED = {"XYO-CP-107": "Költségvetés v1.1, 2026.06.18.", "XYO-CP-405": "kiegészítve a PIR után"}


def test_archive_versions_match_document_headers():
    docs = _documents()
    for r in _archive_rows():
        doc_id, version = _plain(r[0]), r[2]
        path, text = docs[doc_id]
        if version == "—":
            continue
        header = re.search(r"\*\*Verzió:\*\*\s*([\d.]+)", text)
        found = header.group(1) if header else "1.0"
        if doc_id in EXPLAINED:
            source = read_doc("docs/4-monitoring/03-valtozaskerelem.md") if doc_id == "XYO-CP-107" else text
            assert EXPLAINED[doc_id] in source, doc_id
            continue
        assert found == version, (doc_id, path.name, found, version)


def test_archive_summary_partitions_the_index():
    rows = _archive_rows()
    retention = [_plain(r[4]) for r in rows]

    def bucket(text: str) -> str:
        if "nem selejtezhető" in text:
            return "never"
        if "élettartam" in text:
            return "lifetime"
        years = int(re.search(r"(\d+) év", text).group(1))
        return {3: "3", 5: "5"}.get(years, "8+") if years < 8 else "8+"

    counts = Counter(bucket(t) for t in retention)
    summary = {_plain(r[0]): int(_plain(r[1])) for r in tables(section(read_doc(ARCHIVE), "5. Összesítés"))[0]}
    assert summary["3 év"] == counts["3"] and summary["5 év"] == counts["5"]
    assert summary["8 év vagy hosszabb, rögzített idővel (8 év, a lejárat + 8 év, 10 év)"] == counts["8+"]
    assert summary["A rendszer élettartamához kötött"] == counts["lifetime"]
    assert summary["Nem selejtezhető"] == counts["never"]
    assert summary["Összesen"] == len(rows) == sum(counts.values())
