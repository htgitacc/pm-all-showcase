"""Az ütemterv belső logikája és a dátumok összhangja a dokumentumok között.

Ellenőrzi a naptári napokat, a munkaszüneti napokat, a függőségeket (befejezés–
kezdés és kezdés–kezdés), a kritikus út folytonosságát és azt, hogy a
mérföldkövek és a beszerzési dátumok mindenhol ugyanazok.
"""

from __future__ import annotations

import datetime as dt
import re

import pytest

from conftest import ROOT, read_doc, section, tables

SCHEDULE = "docs/2-planning/06-utemterv.md"
YEAR = 2026

# Magyar munkaszüneti napok a projekt és a mérési szakasz idején (2026).
HOLIDAYS = {
    dt.date(2026, 1, 1), dt.date(2026, 3, 15), dt.date(2026, 4, 3), dt.date(2026, 4, 6),
    dt.date(2026, 5, 1), dt.date(2026, 5, 25), dt.date(2026, 8, 20), dt.date(2026, 10, 23),
}
# A 7.2 és 7.3 hullám közti rés tervezett, jelölt tartalék (5. pont).
DOCUMENTED_BUFFERS = {("7.2", "7.3")}


def _date(text: str) -> dt.date:
    month, day = re.search(r"(\d\d)\.(\d\d)\.", text).groups()
    return dt.date(YEAR, int(month), int(day))


def _workday(day: dt.date) -> bool:
    return day.weekday() < 5 and day not in HOLIDAYS


def _workdays_between(a: dt.date, b: dt.date) -> int:
    """Munkanapok a és b között, a végpontok nélkül."""
    return sum(_workday(a + dt.timedelta(i)) for i in range(1, (b - a).days))


def _milestones() -> dict[str, dict]:
    rows = tables(section(read_doc(SCHEDULE), "1. Mérföldkövek"))[0]
    return {r[0]: {"date": dt.date(*map(int, r[2].strip(".").split("."))), "ku": r[3] == "✔"} for r in rows}


def _tasks() -> list[dict]:
    rows = tables(section(read_doc(SCHEDULE), "2. Ütemterv munkacsomagonként"))[0]
    tasks = []
    for r in rows:
        tasks.append({
            "id": r[0] if r[0] != "—" else r[1].strip("*").split("**")[0].strip(),
            "label": r[1], "start": _date(r[2]), "end": _date(r[3]),
            "days": int(r[4]), "deps": r[5], "ku": r[6] == "✔",
        })
    return tasks


def _resolve(dep: str, tasks: list[dict], milestones: dict) -> tuple[str, dt.date, dt.date, bool]:
    """Egy függőség → (név, kezdés, befejezés, kritikus-e)."""
    dep = dep.strip()
    if dep in milestones:
        m = milestones[dep]
        return dep, m["date"], m["date"], m["ku"]
    explicit = re.search(r"\((\d\d\.\d\d\.)[^)]*\)", dep)
    if explicit:
        day = _date(explicit.group(1))
        return dep, day, day, True
    if dep.endswith(".x"):
        group = [t for t in tasks if t["id"].startswith(dep[:-1])]
        return dep, min(t["start"] for t in group), max(t["end"] for t in group), any(t["ku"] for t in group)
    for t in tasks:
        if t["id"] == dep or dep.lower() in t["label"].lower():
            return t["id"], t["start"], t["end"], t["ku"]
    raise AssertionError(f"Feloldhatatlan függőség: {dep!r}")


def test_calendar_days_match_dates():
    for t in _tasks():
        assert (t["end"] - t["start"]).days + 1 == t["days"], t["id"]


def test_no_task_or_milestone_on_a_day_off():
    for t in _tasks():
        for which in ("start", "end"):
            day = t[which]
            if not _workday(day):
                # csak akkor elfogadható, ha az ütemterv maga jelzi az ünnepet
                assert "Pünkösdhétfő" in t["label"] and day == dt.date(2026, 5, 25), (t["id"], which, day)
    for key, m in _milestones().items():
        assert _workday(m["date"]), key


def test_dependencies_are_respected():
    tasks, milestones = _tasks(), _milestones()
    for t in tasks:
        for raw in re.split(r"[;,]", t["deps"]):
            if not raw.strip():
                continue
            start_to_start = "(KK)" in raw
            name, d_start, d_end, _ = _resolve(raw.replace("(KK)", ""), tasks, milestones)
            if start_to_start:
                assert t["start"] >= d_start, (t["id"], name, "KK")
            elif re.search(r"\(\d\d\.\d\d\.[^)]*\)", raw):
                assert t["end"] >= d_end, (t["id"], name, "a dátumhoz kötött bemenet a feladat vége előtt van")
            else:
                assert t["start"] > d_end, (t["id"], name, "befejezés–kezdés")


def test_critical_path_is_continuous():
    """Egy kritikus feladat legkésőbbi elődje is kritikus, és nincs köztük rejtett rés."""
    tasks, milestones = _tasks(), _milestones()
    for t in (t for t in tasks if t["ku"]):
        preds = []
        for raw in re.split(r"[;,]", t["deps"]):
            if raw.strip() and "(KK)" not in raw:
                preds.append(_resolve(raw, tasks, milestones))
        if not preds:
            continue
        name, _, end, ku = max(preds, key=lambda p: p[2])
        assert ku, (t["id"], f"kritikus, de a döntő elődje ({name}) nem az")
        gap = _workdays_between(end, t["start"])
        if (name, t["id"]) not in DOCUMENTED_BUFFERS:
            assert gap == 0, (t["id"], name, f"{gap} munkanap rejtett tartalék a kritikus úton")


def test_every_critical_task_drives_a_critical_successor():
    """Kritikus az, aminek nincs tartaléka: egy kritikus utódot hézag nélkül hajt,
    vagy egy kritikus mérföldkő napján ér véget."""
    tasks, milestones = _tasks(), _milestones()
    critical_dates = {m["date"] for m in milestones.values() if m["ku"]}
    driving = set()
    for succ in (t for t in tasks if t["ku"]):
        for raw in re.split(r"[;,]", succ["deps"]):
            start_to_start = "(KK)" in raw
            raw = raw.replace("(KK)", "").strip()
            if not raw or raw in milestones:
                continue
            explicit = re.search(r"\((\d\d\.\d\d\.)[^)]*\)", raw)
            if raw.endswith(".x"):
                preds = [t for t in tasks if t["id"].startswith(raw[:-1])]
            elif explicit:
                preds = [t for t in tasks if t["end"] == _date(explicit.group(1))]
            else:
                name = _resolve(raw, tasks, milestones)[0]
                preds = [t for t in tasks if t["id"] == name]
            for pred in preds:
                gap = _workdays_between(pred["end"], succ["start"])
                if start_to_start or gap == 0 or (pred["id"], succ["id"]) in DOCUMENTED_BUFFERS:
                    driving.add(pred["id"])
    for t in (t for t in tasks if t["ku"]):
        assert t["id"] in driving or t["end"] in critical_dates, (t["id"], "kritikusnak jelölve, de van tartaléka")


def test_milestone_report_marks_the_same_critical_milestones():
    rows = tables(section(read_doc("docs/4-monitoring/08-merfoldko-riport.md"), "1. Mérföldkövek"))[0]
    report = {r[0]: r[5] == "✔" for r in rows}
    assert report == {k: m["ku"] for k, m in _milestones().items()}


def test_critical_path_length_to_deadline():
    text = read_doc(SCHEDULE)
    m = _milestones()
    days = (m["M10"]["date"] - m["M3"]["date"]).days
    assert f"Teljes hossz a baseline-tól: {days} naptári nap" in text


def test_milestone_dates_agree_across_documents():
    milestones = _milestones()
    pattern = re.compile(r"\|\s*\**(M\d{1,2})\**\s*\|[^|\n]*\|\s*\**(\d{4}\.\d\d\.\d\d\.)")
    mismatches = []
    for path in sorted((ROOT / "docs").rglob("*.md")):
        if path.name == "06-utemterv.md":
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            for key, day in pattern.findall(line):
                expected = milestones.get(key)
                if expected and dt.date(*map(int, day.strip(".").split("."))) != expected["date"]:
                    mismatches.append(f"{path.name}: {key} {day}")
    assert mismatches == []


def test_bid_deadline_is_the_same_everywhere_and_a_workday():
    schedule_end = next(t["end"] for t in _tasks() if t["id"].startswith("Ajánlati szakasz"))
    assert _workday(schedule_end)
    rfp = read_doc("docs/3-execution/02-ajanlatkeresi-dokumentacio.md")
    assert f"**{YEAR}.{schedule_end:%m.%d}., 12:00**" in rfp
    plan = read_doc("docs/2-planning/12-beszerzesi-terv.md")
    assert f"{YEAR}.{schedule_end:%m.%d}.  Ajánlati határidő lejár" in plan
    report = read_doc("docs/4-monitoring/08-merfoldko-riport.md")
    assert f"| Ajánlati határidő | {schedule_end:%m.%d}. | {schedule_end:%m.%d}. |" in report


def test_bids_arrived_before_the_deadline():
    text = read_doc("docs/3-execution/03-ajanlat-osszehasonlitas.md")
    deadline = dt.datetime(YEAR, 4, 2, 12, 0)
    for r in tables(section(text, "2. Beérkezett ajánlatok"))[0]:
        day, time = r[2].split()
        hour, minute = map(int, time.split(":"))
        arrived = dt.datetime.combine(_date(day), dt.time(hour, minute))
        assert arrived <= deadline, r[1]


@pytest.mark.parametrize("path", [
    "docs/4-monitoring/01-statuszriport.md",
])
def test_weekly_reports_fall_on_the_first_workday_of_the_week(path):
    for r in tables(section(read_doc(path), "Riportnapló"))[0]:
        if not r[0].replace("*", "").startswith("SR-"):
            continue
        last = _date(r[1].replace("*", "").split("–")[-1].strip())
        monday = last - dt.timedelta(days=last.weekday())
        first_workday = next(monday + dt.timedelta(i) for i in range(5) if _workday(monday + dt.timedelta(i)))
        assert last == first_workday, (r[0], last)
