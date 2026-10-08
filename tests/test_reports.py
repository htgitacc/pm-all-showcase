"""A riportok: státusz-, Steering-, kockázati riport, EVM és a PRINCE2-réteg.

A riport nem termel új adatot: mindent a nyilvántartásokból vesz át (probléma-,
kockázati, eszkalációs napló, hibalista, EVM). Ezért minden riportnak azt kell
mutatnia, ami **a kiadásának napján** a nyilvántartásban állt — se többet
(jövőbeli eseményt), se kevesebbet (lezárt tételt nyitottként).
"""

from __future__ import annotations

import datetime as dt
import re

from conftest import ft, num, read_doc, section, tables
from test_registers import _kv, _plain
from test_schedule import _milestones, _tasks, _workday, _workdays_between

STATUS = "docs/4-monitoring/01-statuszriport.md"
STEERING = "docs/4-monitoring/02-steering-riport.md"
RISK_REPORT = "docs/4-monitoring/05-kockazati-riport.md"
RISKS = "docs/2-planning/10-kockazatnyilvantartas.md"
EVM = "docs/4-monitoring/06-evm-elemzes.md"
ISSUES = "docs/3-execution/10-problemanaplo.md"
ESCALATIONS = "docs/4-monitoring/09-eszkalacios-naplo.md"
TESTS = "docs/3-execution/07-tesztjegyzokonyv.md"
CERTS = "docs/3-execution/05-teljesitesigazolas.md"
BUDGET = "docs/2-planning/07-koltsegvetes.md"
FIN_CLOSE = "docs/5-closure/04-penzugyi-zaras.md"
COMMS = "docs/2-planning/11-kommunikacios-terv.md"
MINUTES = "docs/3-execution/12-meeting-jegyzokonyvek.md"
ARCHIVE = "docs/5-closure/08-archivalasi-jegyzek.md"
LESSONS = "docs/5-closure/05-tanulsagok-naploja.md"
PID = "docs/prince2/01-pid.md"
HIGHLIGHT = "docs/prince2/02-highlight-report.md"
EXCEPTION = "docs/prince2/03-exception-report.md"
END_STAGE = "docs/prince2/04-end-stage-report.md"

YEAR = 2026


def _day(text: str) -> dt.date:
    """`05.29.`, `2026.05.29.` vagy `05.29` → dátum (az évszám elhagyható)."""
    month, day = re.search(r"(?<!\d)(\d\d)\.(\d\d)(?!\d)", re.sub(r"20\d\d\.\s?", "", text)).groups()
    return dt.date(YEAR, int(month), int(day))


def _maybe_day(text: str) -> dt.date | None:
    return _day(text) if re.search(r"\d\d\.\d\d", text) else None


def _schedule_milestones() -> dict[str, dt.date]:
    return {k: v["date"] for k, v in _milestones().items()}


def _steering_sent() -> dt.date:
    return dt.date(YEAR, 5, int(re.search(r"Kiküldve: 2026\. május (\d+)\.", read_doc(STEERING)).group(1)))


def _risk_report_issued() -> dt.date:
    return dt.date(YEAR, 6, int(re.search(r"\*\*Ez a kiadás:\*\* 2026\. június (\d+)\.", read_doc(RISK_REPORT)).group(1)))


def _risk_ids(text: str) -> set[str]:
    return set(re.findall(r"\bR\d+\b", text))


# ---------------------------------------------------------------- nyilvántartási idősorok


def _problems() -> dict[str, tuple[dt.date, dt.date | None]]:
    """P-azonosító → (felmerült, lezárva vagy None)."""
    text = read_doc(ISSUES)
    result = {}
    for m in re.finditer(r"^### (P-\d+) — .*?\n(.*?)(?=^### |^## |\Z)", text, re.S | re.M):
        kv = _kv(m.group(2))
        result[m.group(1)] = (_day(kv["Felmerült"]), _maybe_day(kv.get("Lezárva", "")))
    return result


def _open_problems(on: dt.date) -> set[str]:
    return {p for p, (raised, closed) in _problems().items() if raised <= on and (closed is None or closed > on)}


def _closed_problems(start: dt.date, end: dt.date) -> set[str]:
    return {p for p, (_, closed) in _problems().items() if closed and start <= closed <= end}


def _ids(text: str, prefix: str) -> set[str]:
    return set(re.findall(rf"{prefix}-\d+", text))


def _risk_baseline() -> dict[str, int]:
    text = read_doc(RISKS)
    scores = {}
    for m in re.finditer(r"^### (R\d+) — .*?\n(.*?)(?=^### |^## |\Z)", text, re.S | re.M):
        scores[m.group(1)] = int(re.search(r"= \*\*(\d)", _kv(m.group(2))["Valószínűség × hatás"]).group(1))
    for heading in ("3. Közepes", "4. Alacsony"):
        for r in tables(section(text, heading))[0]:
            scores[r[0]] = int(re.search(r"= (\d)", next(c for c in r if "×" in c)).group(1))
    return scores


def _risk_changes() -> list[tuple[dt.date, str, int]]:
    """A felülvizsgálati napló átsorolásai: (dátum, kockázat, új besorolás)."""
    changes = []
    for r in tables(section(read_doc(RISKS), "5. Felülvizsgálati napló"))[0]:
        for rid, _, new in re.findall(r"(R\d+) (\d) → (\d)", r[1]):
            changes.append((_day(r[0][5:]), rid, int(new)))
    return changes


def _risk_closures() -> dict[str, dt.date]:
    return {r[0]: _day(r[2]) for r in tables(section(read_doc(RISK_REPORT), "4. Lezárt kockázatok"))[0]}


def _risk_score(rid: str, on: dt.date) -> int:
    score = _risk_baseline()[rid]
    for day, changed, new in sorted(_risk_changes()):
        if changed == rid and day <= on:
            score = new
    return score


def _open_risks(on: dt.date) -> dict[str, int]:
    closed = _risk_closures()
    return {rid: _risk_score(rid, on) for rid in _risk_baseline() if not (rid in closed and closed[rid] <= on)}


def _high_risks(on: dt.date) -> set[str]:
    return {rid for rid, score in _open_risks(on).items() if score >= 6}


def _report_risks(rows: list[list[str]], score_col: int, on: dt.date) -> set[str]:
    """Egy riport kockázati táblája: a besorolásnak a riport napján érvényesnek kell lennie."""
    listed = set()
    for r in rows:
        rid = _plain(r[0])
        if not re.fullmatch(r"R\d+", rid):
            continue
        listed.add(rid)
        cell = r[score_col]
        if "lezárva" in cell:
            assert _risk_closures()[rid] <= on, rid
        else:
            assert int(re.findall(r"\d", _plain(cell))[-1]) == _risk_score(rid, on), (rid, on)
    return listed


# ---------------------------------------------------------------- státuszriport


def _weekly(first: dt.date, last: dt.date, weekday: int) -> list[dt.date]:
    """Heti időpontok; munkaszüneti napon a következő munkanapra csúszik."""
    days, day = [], first
    while day <= last:
        actual = day
        while not _workday(actual):
            actual += dt.timedelta(1)
        days.append(actual)
        day += dt.timedelta(7)
    return days


def test_status_report_log_is_weekly_until_project_close():
    rows = tables(section(read_doc(STATUS), "Riportnapló"))[0]
    entries = [r for r in rows if r[0].replace("*", "").startswith("SR-")]
    first = _day(entries[0][1].split("–")[0] + ".")
    expected = _weekly(first, _schedule_milestones()["M10"], 0)

    colours = []
    for r in entries:
        ids = [int(x) for x in re.findall(r"SR-(\d+)", r[0])]
        days = [_day(d.strip() + ("" if d.strip().endswith(".") else ".")) for d in _plain(r[1]).split("–")]
        assert days[0] == expected[ids[0] - 1] and days[-1] == expected[ids[-1] - 1], r[0]
        colours += [r[2]] * (ids[-1] - ids[0] + 1)
    assert len(colours) == len(expected)

    total = len(expected)
    assert f"{total} riport" in rows[-1][1]
    assert f"Státuszriportok ({total} db)" in read_doc(ARCHIVE)
    red, yellow = sum("🔴" in c for c in colours), sum("🟡" in c for c in colours)
    assert re.search(rf"{total} riportból \*\*{red} piros és\s*>?\s*{yellow} sárga\*\*", read_doc(STATUS))
    assert f"{total} riportból {red} piros és {yellow} sárga" in read_doc(LESSONS)


def test_status_and_highlight_reports_show_the_problem_log_of_their_day():
    sr10 = read_doc(STATUS).split("# SR-10")[1].split("# SR-05")[0]
    on = dt.date(YEAR, 5, int(re.search(r"# SR-10 — 2026\. május (\d+)\.", read_doc(STATUS)).group(1)))
    listed = _ids(section(sr10, "Nyitott problémák").split("**Lezárva")[0], "P")
    assert listed == _open_problems(on)
    closed = _ids(section(sr10, "Nyitott problémák").split("**Lezárva")[1], "P")
    assert closed == _closed_problems(on - dt.timedelta(7), on - dt.timedelta(1))

    text = read_doc(HIGHLIGHT)
    period = re.search(r"május (\d+) – (\d+)\.", text).groups()
    start, end = dt.date(YEAR, 5, int(period[0])), dt.date(YEAR, 5, int(period[1]))
    problems = section(text, "5. Nyitott problémák")
    assert _ids(problems.split("**Lezárva")[0], "P") == _open_problems(end)
    assert _ids(problems.split("**Lezárva")[1], "P") == _closed_problems(start, end)


# ---------------------------------------------------------------- kockázatok a riportokban


def test_every_high_risk_reaches_the_board_and_scores_are_current():
    steering_day = _steering_sent()
    rows = tables(section(read_doc(STEERING), "5. Kockázatok"))[0]
    assert _high_risks(steering_day) <= _report_risks(rows, 2, steering_day)

    text = read_doc(HIGHLIGHT)
    end = dt.date(YEAR, 5, int(re.search(r"május \d+ – (\d+)\.", text).group(1)))
    rows = tables(section(text, "6. Kockázatok"))[0]
    high = _high_risks(end)
    assert high <= _report_risks(rows, 2, end)
    tolerance = next(r for r in tables(section(text, "2. Tolerancia"))[0] if "Kockázat" in r[0])
    assert f"{len(high)} db 6-os" in tolerance[2] and _risk_ids(tolerance[2]) == high

    sr10 = read_doc(STATUS).split("# SR-10")[1].split("# SR-05")[0]
    sr10_day = dt.date(YEAR, 5, int(re.search(r"# SR-10 — 2026\. május (\d+)\.", read_doc(STATUS)).group(1)))
    _report_risks(tables(section(sr10, "Top 3 kockázat"))[0], 2, sr10_day)


def test_risk_report_overview_matches_the_register():
    on = _risk_report_issued()
    text = read_doc(RISK_REPORT)
    open_now = _open_risks(on)
    listed = {r[0]: r for r in tables(section(text, "5. Nyitott kockázatok"))[0]}
    assert set(listed) == set(open_now)
    for rid, r in listed.items():
        assert int(re.findall(r"\d", _plain(r[2]))[-1]) == open_now[rid], rid

    overview = {_plain(r[0]): r for r in tables(section(text, "1. Összkép"))[0]}
    bucket = lambda scores, lo, hi: sum(lo <= s <= hi for s in scores)
    baseline = dt.date(YEAR, 3, 13)
    for col, day in ((1, baseline), (2, on)):
        scores = _open_risks(day).values()
        assert int(_plain(overview["Nyitott, magas (≥6)"][col])) == bucket(scores, 6, 9)
        assert int(_plain(overview["Nyitott, közepes (3–4)"][col])) == bucket(scores, 3, 4)
        assert int(_plain(overview["Nyitott, alacsony (1–2)"][col])) == bucket(scores, 1, 2)
        closed = sum(d <= day for d in _risk_closures().values())
        assert int(_plain(overview["Lezárva"][col])) == closed
    assert int(_plain(overview["Nyilvántartott kockázat"][2])) == len(_risk_baseline())


def test_risk_register_statuses_follow_the_risk_report():
    register = read_doc(RISKS)
    for rid, closed in _risk_closures().items():
        if f"### {rid} —" in register:
            status = _kv(section(register, f"{rid} —"))["Státusz"]
        else:
            status = next(l for l in register.splitlines() if l.startswith(f"| {rid} |"))
        assert f"lezárva {closed:%m.%d}." in status.replace("*", "").replace("2026.", ""), rid

    occurred = tables(section(read_doc(RISK_REPORT), "3. Bekövetkezett"))[0]
    for r in occurred:
        rid = _plain(r[0])
        line = next(l for l in register.splitlines() if l.startswith(f"| {rid} |"))
        assert f"bekövetkezett {_day(r[2]):%m.%d}." in line, rid

    # A nyilvántartás a riporttal együtt frissül, és az archívum ezt a változatot őrzi.
    last_review = _day(re.search(r"\*\*Utolsó felülvizsgálat:\*\* 2026\.(\d\d\.\d\d\.)", register).group(1))
    assert last_review == _risk_report_issued()
    archived = next(l for l in read_doc(ARCHIVE).splitlines() if "XYO-CP-110" in l)
    assert f"2026.{last_review:%m.%d}." in archived


def test_risk_reviews_agree_across_documents():
    log = tables(section(read_doc(RISK_REPORT), "7. Felülvizsgálati napló"))[0]
    reviews = []
    for r in log:
        reviews += [_day(d.strip()) for d in r[1].split(",") if d.strip()]
    register_days = {_day(r[0][5:]) for r in tables(section(read_doc(RISKS), "5. Felülvizsgálati napló"))[0]}
    assert set(reviews[2:]) <= register_days
    count = len(reviews)
    assert f"a {count}. felülvizsgálat után" in read_doc(RISK_REPORT)
    assert f"Kockázati riportok ({count} db)" in read_doc(ARCHIVE)
    minutes = {_plain(r[0]): int(_plain(r[2])) for r in tables(section(read_doc(MINUTES), "1. Jegyzőkönyv"))[0] if r[2]}
    assert minutes["Kockázat-felülvizsgálat"] == count

    # Ha egy felülvizsgálat eszkalációhoz vezetett, annak a felülvizsgálat után kell jönnie.
    escalations = _escalations()
    for r in log:
        for eid in _ids(r[2], "E"):
            review = _day(r[1])
            assert 0 <= (escalations[eid]["sent"] - review).days <= 3, (eid, review)


def test_ticket_figures_in_the_risk_report_were_known_when_it_was_issued():
    issued = _risk_report_issued()
    waves = {1: "7.1", 2: "7.2", 3: "7.3"}
    starts = {n: next(t for t in _tasks() if t["id"] == wid)["start"] for n, wid in waves.items()}
    impact = {r[0][0]: r for r in tables(section(read_doc("docs/3-execution/09-oktatasi-anyag.md"), "6. Az oktatás hatása"))[0]}
    r12 = _kv(section(read_doc(RISK_REPORT), "R12 — Service Desk"))["Aktuális adat"]
    for wave, value in re.findall(r"(\d)\. hullámnál \**([\d,]+) ticket/fő", r12):
        assert starts[int(wave)] + dt.timedelta(7) <= issued, wave
        assert value == impact[wave][4]


# ---------------------------------------------------------------- Steering, EVM, eszkaláció


def _escalations() -> dict[str, dict]:
    text = read_doc(ESCALATIONS)
    result = {}
    for m in re.finditer(r"^### (E-\d+) — .*?\n(.*?)(?=^### |^## |\Z)", text, re.S | re.M):
        kv = _kv(m.group(2))
        result[m.group(1)] = {"sent": _day(kv["Mikor"]), "closed": _day(kv["Státusz"].split("—")[1])}
    return result


def test_steering_report_lists_escalations_as_they_stood():
    sent = _steering_sent()
    part = section(read_doc(STEERING), "4. Eszkalált problémák")
    rows = {r[0]: r for r in tables(part)[0]}
    escalations = _escalations()
    assert set(rows) == {e for e, v in escalations.items() if v["sent"] <= sent}
    for eid, r in rows.items():
        still_open = escalations[eid]["closed"] > sent
        assert ("nyitva" in r[3]) == still_open, eid
    if any(v["sent"] <= sent < v["closed"] for v in escalations.values()):
        assert "Nincs nyitott eszkaláció" not in part


def test_steering_evm_figures_come_from_a_checkpoint_before_it_was_sent():
    sent = _steering_sent()
    rows = tables(section(read_doc(EVM), "4. A javított számok"))[0]
    checkpoints = [(_day(r[0][5:]), r) for r in rows]
    day, latest = max((d, r) for d, r in checkpoints if d <= sent)
    figures = {_plain(r[0]).split(" (")[0]: _plain(r[2]) for r in tables(section(read_doc(STEERING), "2. Számok"))[0]}
    assert num(figures["Ütemhatékonyság"]) == num(latest[4])
    assert num(figures["Költséghatékonyság"]) == num(latest[5])
    assert f"SPI, {day:%m.%d}." in read_doc(STEERING)


# ---------------------------------------------------------------- PRINCE2-réteg


def _pct(part: int, whole: int) -> str:
    return f"{abs(part) / whole * 100:.1f}".replace(".", ",") + "%"


def test_tolerance_figures_recompute():
    totals = {_plain(r[0]): r for t in tables(read_doc(FIN_CLOSE)) for r in t if len(r) >= 4}
    base = ft(totals["Költségbázis összesen"][2])
    contracted = ft(totals["Költségbázis összesen"][3])
    forecast = ft(totals["MINDÖSSZESEN"][3])
    highlight = next(r for r in tables(section(read_doc(HIGHLIGHT), "2. Tolerancia"))[0] if "Költség" in r[0])
    assert f"−{_pct(contracted - base, base)}" in highlight[2]
    assert f"−{_pct(forecast - base, base)}" in highlight[3]
    assert f"{_pct(contracted - base, base)}-kal a költségterv alatt" in read_doc(EXCEPTION)

    # A javítási ablak naptári és munkanapjai.
    window = next(t for t in _tasks() if t["id"].startswith("Hibajavítás"))
    calendar = (window["end"] - window["start"]).days + 1
    work = _workdays_between(window["start"] - dt.timedelta(1), window["end"] + dt.timedelta(1))
    for path in (HIGHLIGHT, EXCEPTION):
        assert re.search(rf"{calendar} naptári nap\s+—\s+Pünkösdhétfő\s+miatt\s+{work}\s+munkanap", read_doc(path)), path


def test_exception_report_counts_match_the_defect_list_and_e04():
    window_start = next(t for t in _tasks() if t["id"].startswith("Hibajavítás"))["start"]
    report = dt.date(YEAR, 5, int(re.search(r"\*\*Dátum:\*\* \*\*2026\. május (\d+)\.", read_doc(EXCEPTION)).group(1)))
    fixed = set()
    text = read_doc(TESTS)
    for line in text.splitlines():
        m = re.match(r"\| (H-\d+) \|.*javítva\** (\d\d\.\d\d)\.", line)
        if m and window_start <= _day(m.group(2) + ".") <= report:
            fixed.add(m.group(1))
    status = {_plain(r[0]): r[1] for r in tables(section(read_doc(EXCEPTION), "4. A helyzet"))[0]}
    assert int(re.match(r"\**(\d+)", status["Javítva 05.29-ig"]).group(1)) == len(fixed)
    assert _ids(status["Javítva 05.29-ig"], "H") == fixed
    e04 = _kv(section(read_doc(ESCALATIONS), "E-04"))["Visszajelzés 05.29-én"]
    assert f"{len(fixed)} javítva ({', '.join(sorted(fixed))})" in e04


def test_end_stage_report_knows_only_its_own_stage():
    text = read_doc(END_STAGE)
    stage = re.search(r"Lezárt szakasz:.*\((2026\.\d\d\.\d\d) – (\d\d\.\d\d)\.\)", text)
    start, end = _day(stage.group(1)), _day(stage.group(2))
    risks = tables(section(text, "4. Kockázatok"))[0]
    closed = [r for r in risks if "lezárva" in r[2]]
    for r in risks:
        assert "bekövetkezett" not in r[2], r[0]
        for d in re.findall(r"\d\d\.\d\d\.", r[2]):
            assert _day(d) <= end, (r[0], d)
    for r in closed:
        assert start <= _day(re.search(r"\d\d\.\d\d\.", r[2]).group(0)) <= end
    row = next(r for r in tables(section(text, "1. A szakasz"))[0] if "Kockázat" in r[0])
    assert f"{len(closed)} lezárva" in row[2]
    assert "bekövetkezett nem volt" in row[2]


def test_next_stage_cost_follows_the_contracts():
    pid = {_plain(r[0]): ft(r[1]) for r in tables(section(read_doc(PID), "4.3 Költségterv"))[0]}
    stage3, stage4 = pid["3. Kialakítás és teszt"], pid["4. Élesítés és zárás"]
    phasing = {r[0]: ft(r[1]) for r in tables(section(read_doc(BUDGET), "3. Időbeli elosztás"))[0] if ft(r[1]) is not None}
    assert stage3 + stage4 == phasing["2026. április"] + phasing["2026. május"] + phasing["2026. június"]

    # A szerződött árakkal: a 3. szakaszba (04.20 – 06.19.) eső kifizetések + a májusi mobilnet.
    stage = next(r for r in tables(section(read_doc(PID), "4.1 Irányítási szakaszok"))[0] if r[0] == "3")
    first, last = (_day(d) for d in stage[2].split("–"))
    payments = tables(section(read_doc(CERTS), "Összefoglaló — kifizetések állása"))[0]
    in_stage = sum(ft(r[2]) for r in payments if r[0] and first <= _day(r[3].split("kifizetve ")[1]) <= last)
    schedule = tables(section(read_doc(BUDGET), "3. Időbeli elosztás"))[1]
    may_items = sum(ft(r[3]) for r in schedule if r[1] in {"M5 környezet kész", "Részszállítás (10 gép) átvéve"})
    mobile_may = phasing["2026. május"] - may_items
    plan = _kv(section(read_doc(END_STAGE), "6. A következő szakasz"))["Tervezett költség"]
    assert ft(plan) == in_stage + mobile_may
    assert f"a PID-ben {stage3:,} Ft".replace(",", " ") in plan


# ---------------------------------------------------------------- kommunikáció és jegyzőkönyvek


def test_newsletters_are_fortnightly_and_do_not_run_ahead():
    rows = tables(section(read_doc(COMMS), "2. A pilot hírlevél"))[0]
    days = [_day(r[1][5:]) for r in rows]
    assert all(d.weekday() == 3 for d in days)
    assert all((b - a).days == 14 for a, b in zip(days, days[1:]))
    m7 = _schedule_milestones()["M7"]
    for d, r in zip(days, rows):
        if r[2].startswith("Mindenki élesben"):
            assert d >= m7, r[0]


def test_weekly_meeting_numbers_follow_the_tuesdays():
    text = read_doc(MINUTES)
    register = {_plain(r[0]): int(_plain(r[2])) for r in tables(section(text, "1. Jegyzőkönyv"))[0] if r[2]}
    tuesdays = _weekly(dt.date(YEAR, 3, 17), _schedule_milestones()["M10"], 1)
    assert register["Heti előrehaladási megbeszélés"] == len(tuesdays)
    number = int(re.search(r"\*\*Sorszám:\*\* HE-(\d+)", text).group(1))
    held = dt.date(YEAR, 5, int(re.search(r"\*\*Időpont:\*\* 2026\. május (\d+)\., kedd", text).group(1)))
    assert tuesdays[number - 1] == held
