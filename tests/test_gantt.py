"""A Gantt-nézet: az ütemterv-dokumentumból rajzol, és semmit nem told hozzá vagy hagy el."""

from __future__ import annotations

import datetime as dt
import itertools

import pytest
from streamlit.testing.v1 import AppTest

from conftest import read_doc, section, tables
from pm_app import gantt
from test_schedule import HOLIDAYS, _milestones, _tasks


@pytest.fixture(scope="module")
def data():
    return gantt.load_schedule()


def _real(tasks):
    """A dokumentum soraiból készült feladatok (a szintetikus tartaléksáv nélkül)."""
    return [t for t in tasks if isinstance(t["order"], int)]


def test_every_schedule_row_becomes_a_bar_with_the_same_dates(data):
    expected = _tasks()
    real = _real(data["tasks"])
    assert len(real) == len(expected)
    for got, want in zip(real, expected):
        assert (got["start"], got["end"], got["days"], got["critical"]) == (
            want["start"], want["end"], want["days"], want["ku"]
        ), want["id"]


def test_milestones_carry_plan_and_actual(data):
    plan = _milestones()
    assert [m["key"] for m in data["milestones"]] == list(plan)
    report = tables(section(read_doc(gantt.MILESTONE_REPORT_FILE), "1. Mérföldkövek"))[0]
    for m, row in zip(data["milestones"], report):
        assert m["date"] == plan[m["key"]]["date"]
        assert m["critical"] == plan[m["key"]]["ku"]
        assert (m["actual"] is None) == ("tervezett" in row[3]), m["key"]


def test_holidays_are_the_weekday_holidays_of_the_project(data):
    parsed = {h["date"] for h in data["holidays"]}
    first = min(t["start"] for t in data["tasks"])
    last = max(t["end"] for t in data["tasks"])
    expected = {d for d in HOLIDAYS if first <= d <= last and d.weekday() < 5}
    assert parsed == expected


def test_waiting_and_buffer_rows_are_classified(data):
    rows = {t["name"].split(" (")[0]: gantt.category(t) for t in data["tasks"] if not t["wbs"]}
    assert rows["Ajánlati szakasz"] == gantt.CRITICAL_WAIT
    assert rows["Belső jóváhagyási kör"] == gantt.CRITICAL_WAIT
    assert rows["Hardver szállítási idő"] == gantt.NORMAL_WAIT
    assert rows["Hibajavítás és újratesztelés"] == gantt.BUFFER
    assert all(gantt.category(t) in {gantt.CRITICAL, gantt.NORMAL} for t in data["tasks"] if t["wbs"])


def test_buffer_bars_match_the_documented_buffers(data):
    bars = [t for t in data["tasks"] if t["buffer"]]
    assert len(bars) == len(data["buffers"])
    for bar, buffer in zip(sorted(bars, key=lambda t: t["start"]), data["buffers"]):
        assert bar["days"] == (bar["end"] - bar["start"]).days + 1 == buffer["planned"], buffer["name"]
    gap = next(t for t in bars if t["name"].startswith("Tartalék"))
    waves = {t["wbs"]: t for t in data["tasks"] if t["wbs"] in {"7.2", "7.3"}}
    assert gap["start"] == waves["7.2"]["end"] + dt.timedelta(days=1)
    assert gap["end"] == waves["7.3"]["start"] - dt.timedelta(days=1)
    assert sum(b["used"] for b in data["buffers"]) == 9  # a Mérföldkő-riport 3. pontja


@pytest.mark.parametrize("critical_only,include_measurement,by_wbs", list(itertools.product([False, True], repeat=3)))
def test_chart_rows_are_exactly_the_shown_items(data, critical_only, include_measurement, by_wbs):
    spec = gantt.build_chart(data, critical_only, include_measurement, by_wbs).to_dict()
    bars = next(layer for layer in spec["layer"] if layer["mark"]["type"] == "bar")
    shown = [t for t in data["tasks"] if t["critical"] or not critical_only]
    order = bars["encoding"]["y"]["sort"]
    assert len(order) == len(set(order))
    assert {t["label"] for t in shown} <= set(order)
    # Egy sáv a befejezés napját is lefedi: hossza = a dokumentum naptári napjai.
    for row in spec["datasets"][bars["data"]["name"]]:
        start, end = (dt.datetime.fromisoformat(row[k]) for k in ("Kezdés", "Vége"))
        assert (end - start).days == row["Naptári nap"], row["Sor"]
    holidays = next(layer for layer in spec["layer"] if layer["mark"]["type"] == "rect")
    assert len(spec["datasets"][holidays["data"]["name"]]) == len(data["holidays"])
    has_pir = any(label.startswith("M11 ") for label in order)
    assert has_pir == (include_measurement and not critical_only)
    if by_wbs:
        assert order[0].startswith("M1 ")


def test_gantt_page_renders_and_reacts(tmp_progress):
    at = AppTest.from_string("from pm_app import gantt\ngantt.view()\n", default_timeout=60).run()
    assert not at.exception, at.exception
    assert any("Gantt-nézet" in t.value for t in at.title)
    at.toggle[0].set_value(True).run()
    assert not at.exception, at.exception
