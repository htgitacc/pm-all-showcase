"""A függőségjelölés értelmezője (`pm_app/dependencies.py`): típus, késleltetés, előrehozás."""

from __future__ import annotations

import pytest

from pm_app.dependencies import (
    KIND_NAMES,
    Dependency,
    parse_dependencies,
    parse_dependency,
)


@pytest.mark.parametrize(
    ("raw", "target", "kind", "lag"),
    [
        ("3.2.1", "3.2.1", "BK", 0),
        ("M5", "M5", "BK", 0),
        ("2.1.x", "2.1.x", "BK", 0),
        ("4.3 (KK)", "4.3", "KK", 0),
        ("6.4 (BB)", "6.4", "BB", 0),
        ("1.3 (KK +2 mn)", "1.3", "KK", 2),
        ("5.1 (−14 mn)", "5.1", "BK", -14),
        ("7.2 (+1 mn)", "7.2", "BK", 1),
        ("6.1 (KB −1 mn)", "6.1", "KB", -1),
        # dátumos zárójel nem jelölés: a szöveg egészében marad, befejezés–kezdés
        ("ajánlati határidő (04.02. 12:00)", "ajánlati határidő (04.02. 12:00)", "BK", 0),
        ("10 gép (05.06.)", "10 gép (05.06.)", "BK", 0),
    ],
)
def test_single_dependency(raw, target, kind, lag):
    dep = parse_dependency(raw)
    assert (dep.target, dep.kind, dep.lag) == (target, kind, lag)
    assert dep.raw == raw


def test_cell_with_several_dependencies():
    deps = parse_dependencies("M5; 6.4 (BB), 1.3 (KK +2 mn)")
    assert [(d.target, d.kind, d.lag) for d in deps] == [("M5", "BK", 0), ("6.4", "BB", 0), ("1.3", "KK", 2)]
    assert parse_dependencies("") == []
    assert parse_dependencies(" ; ") == []


def test_misspelled_marking_is_not_silently_a_known_kind():
    """Az elírt jelölés (FF, KK+2) nem ismert típus: a szöveg egészében célként marad."""
    for raw in ("6.4 (FF)", "1.3 (KK+2)", "6.4 ()"):
        dep = parse_dependency(raw)
        assert (dep.kind, dep.lag) == ("BK", 0) and dep.target == raw


def test_describe_is_short_and_readable():
    assert Dependency("x", "x").describe() == "BK"
    assert parse_dependency("4.3 (KK)").describe() == "KK"
    assert parse_dependency("1.3 (KK +2 mn)").describe() == "KK +2 mn"
    assert parse_dependency("5.1 (−14 mn)").describe() == "−14 mn"
    assert parse_dependency("6.1 (KB −1 mn)").describe() == "KB −1 mn"


def test_every_kind_has_a_hungarian_name():
    assert set(KIND_NAMES) == {"BK", "KK", "BB", "KB"}
    assert parse_dependency("6.4 (BB)").kind_name == "befejezés–befejezés"
