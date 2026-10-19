"""A WBS-nézet: a WBS, a WBS-szótár és az ütemterv dokumentumaiból rajzol, és semmit nem told
hozzá vagy hagy el; a három dokumentum nem mondhat ellent egymásnak."""

from __future__ import annotations

import re

import pytest
from conftest import read_doc, section, tables
from test_schedule import _tasks

from pm_app import gantt, wbs
from pm_app.dependencies import parse_dependencies

# Az ütemterv nem tartalmaz sort ezekhez: a hardverszállítás ott WBS-azonosító nélküli
# várakozás-sor, a T0 mérés (8.2) a baseline előtt kész volt.
UNSCHEDULED = {"2.3.1", "2.3.2", "8.2"}


@pytest.fixture(scope="module")
def data():
    return wbs.load()


def _wbs_doc() -> str:
    return read_doc(wbs.WBS_FILE)


def _table_rows() -> dict[str, list[str]]:
    rows = tables(section(_wbs_doc(), "2. Munkacsomagok"))[0]
    return {r[0]: r for r in rows if re.match(r"^\d+(\.\d+)*$", r[0])}


# ------------------------------------------------------------------ fa és táblázat

def test_every_leaf_of_the_tree_is_a_package_and_vice_versa(data):
    leaves = {p["id"] for p in data["packages"]}
    assert leaves == set(_table_rows())
    assert len(leaves) == 37


def test_tree_numbering_is_consistent(data):
    nodes = data["nodes"]
    ids = [n["id"] for n in nodes]
    assert len(ids) == len(set(ids))
    for n in nodes:
        if n["parent"]:
            assert n["id"].startswith(n["parent"] + ".") and n["parent"] in ids, n["id"]
        assert n["level"] == n["id"].count(".") + 1
    assert [b["id"] for b in data["branches"]] == [str(i) for i in range(1, 9)]
    assert all(b["name"] == b["name"].capitalize() for b in data["branches"])


def test_package_names_follow_the_tree_and_owners_the_table(data):
    rows = _table_rows()
    for p in data["packages"]:
        assert p["owner"] == rows[p["id"]][2].replace("**", "").strip(), p["id"]
        assert p["hours"] == int(re.sub(r"\D", "", rows[p["id"]][3])), p["id"]


# ------------------------------------------------------------------ ráfordítás

def test_hours_add_up_to_the_documented_totals(data):
    doc = _wbs_doc()
    total = int(re.sub(r"\D", "", re.search(r"\*\*Összesen\*\* \| \| \*\*([\d\s]+) óra\*\*", doc)[1]))
    assert sum(p["hours"] for p in data["packages"]) == total == 1260
    summary = {r[0]: int(re.sub(r"\D", "", r[1])) for r in tables(section(doc, "2. Munkacsomagok"))[1]}
    assert sum(p["internal"] for p in data["packages"]) == summary["Belső ráfordítás"] == 948
    assert sum(p["external"] for p in data["packages"]) == summary["Külső (Cloudia Solutions)"] == 312


def test_every_package_splits_into_internal_and_external_hours(data):
    for p in data["packages"]:
        assert p["internal"] + p["external"] == p["hours"], p["id"]
        if p["kind"] == "belső":
            assert p["external"] == 0, p["id"]
        if p["kind"] == "külső":
            assert p["internal"] == 0, p["id"]
    mixed = {p["id"] for p in data["packages"] if p["kind"] == "vegyes"}
    assert mixed == {"3.3.1", "3.4.2", "3.5", "5.2"}
    assert all(p["internal"] and p["external"] for p in data["packages"] if p["id"] in mixed)


def test_branch_totals_are_the_sum_of_their_packages(data):
    for b in data["branches"]:
        own = [p for p in data["packages"] if p["branch"] == b["id"]]
        assert b["count"] == len(own) > 0
        assert b["hours"] == sum(p["hours"] for p in own) == b["internal"] + b["external"]
    assert sum(b["hours"] for b in data["branches"]) == 1260


def test_only_documented_packages_break_the_8_to_80_hour_rule(data):
    off = {p["id"] for p in data["packages"] if not 8 <= p["hours"] <= 80}
    assert off == wbs.OVERSIZED == {"1.2"}
    doc = section(_wbs_doc(), "2. Munkacsomagok")
    assert "8–80 órás elvtől egy munkacsomag tér el: az **1.2** (120 óra)" in doc


# ------------------------------------------------------------------ ütemterv

def test_dates_and_critical_flags_come_from_the_schedule(data):
    schedule = {t["id"]: t for t in _tasks()}
    scheduled = {p["id"]: p for p in data["packages"] if p["scheduled"]}
    assert set(scheduled) == {t for t in schedule if re.match(r"^\d+(\.\d+)*$", t)}
    for pid, p in scheduled.items():
        assert (p["start"], p["end"], p["critical"], p["deps"]) == (
            schedule[pid]["start"], schedule[pid]["end"], schedule[pid]["ku"], schedule[pid]["deps"]
        ), pid


def test_the_unscheduled_packages_are_exactly_the_documented_ones(data):
    assert {p["id"] for p in data["packages"] if not p["scheduled"]} == UNSCHEDULED
    for p in data["packages"]:
        if not p["scheduled"]:
            assert p["start"] is None and p["deps"] == "" and not p["critical"]


# ------------------------------------------------------------------ szótár

def test_dictionary_entries_belong_to_packages_and_agree_with_the_table(data):
    ids = {p["id"] for p in data["packages"]}
    by_id = {p["id"]: p for p in data["packages"]}
    entries = {p["id"]: p["dictionary"] for p in data["packages"] if p["dictionary"]}
    assert set(entries) == {"2.3.1", "3.1.2", "3.3.2", "5.3", "6.3", "7.4", "8.3"}
    assert set(entries) <= ids
    for pid, entry in entries.items():
        assert int(re.sub(r"\D", "", entry["Becsült ráfordítás"].split("óra")[0])) == by_id[pid]["hours"], pid
        first_owner = by_id[pid]["owner"].split(" + ")[0].split(",")[0]
        assert first_owner in entry["Felelős"], (pid, entry["Felelős"])
        assert entry["Kész-definíció"], pid


def test_dictionary_dependencies_cover_the_schedule_ones(data):
    """A szótár „Függőség" sora legalább azokat a csomagokat említi, amelyekre az ütemterv épít."""
    for p in data["packages"]:
        if not (p["dictionary"] and p["scheduled"]):
            continue
        listed = set(re.findall(r"\d+(?:\.\d+)+|\d+", p["dictionary"]["Függőség"]))
        for dep in parse_dependencies(p["deps"]):
            for pid in wbs.resolve(dep.target, data)["ids"]:
                assert pid in listed, (p["id"], pid, p["dictionary"]["Függőség"])


# ------------------------------------------------------------------ függőségek

def test_every_schedule_dependency_resolves_to_something_known(data):
    for p in data["packages"]:
        for dep in parse_dependencies(p["deps"]):
            r = wbs.resolve(dep.target, data)
            assert r["type"] in {"package", "group", "milestone", "row", "external"}
            assert r["label"]
            if r["type"] == "external":
                assert re.search(r"\(\d\d\.\d\d\.", dep.target), (p["id"], dep.target, "feloldatlan függőség")


def test_predecessors_and_successors_are_each_others_inverse(data):
    for p in data["packages"]:
        for item in wbs.predecessors(p, data):
            for pid in item["ids"]:
                assert any(s["package"]["id"] == p["id"] for s in wbs.successors(pid, data)), (pid, p["id"])
    for p in data["packages"]:
        for s in wbs.successors(p["id"], data):
            assert any(p["id"] in x["ids"] for x in wbs.predecessors(s["package"], data)), (p["id"], s["package"]["id"])


def test_group_dependency_expands_to_its_packages(data):
    r = wbs.resolve("2.1.x", data)
    assert r["type"] == "group" and r["ids"] == ["2.1.1", "2.1.2"]


def test_the_dependency_graph_has_no_cycle(data):
    graph: dict[str, set[str]] = {}
    for pred, succ, _ in wbs.edges(data):
        graph.setdefault(pred, set()).add(succ)
    state: dict[str, int] = {}

    def visit(node: str) -> None:
        assert state.get(node) != 1, f"kör a függőségekben: {node}"
        if state.get(node) == 2:
            return
        state[node] = 1
        for nxt in graph.get(node, ()):
            visit(nxt)
        state[node] = 2

    for node in list(graph):
        visit(node)


def test_known_typed_dependencies_are_shown(data):
    by_id = {p["id"]: p for p in data["packages"]}
    pred = {i["dependency"].target: i["dependency"].describe() for i in wbs.predecessors(by_id["8.3"], data)}
    assert pred == {"8.1": "BK", "1.3": "KK +2 mn"}
    assert {i["dependency"].describe() for i in wbs.predecessors(by_id["3.5"], data)} == {"BK", "BB"}
    assert {s["package"]["id"] for s in wbs.successors("6.4", data)} == {"3.5"}


def test_dot_contains_every_edge_and_marks_the_critical_path(data):
    dot = wbs.build_dot(data)
    for pred, succ, note in wbs.edges(data):
        assert f'"{pred}" -> "{succ}"' in dot
    assert '"8.3"' in dot and 'label="KK +2 mn"' in dot
    in_graph = {pid for a, b, _ in wbs.edges(data) for pid in (a, b)}
    critical = next(p for p in data["packages"] if p["critical"] and p["id"] in in_graph)
    assert re.search(rf'"{re.escape(critical["id"])}" \[[^\]]*color="{gantt.CATEGORIES[gantt.CRITICAL]}"', dot)
    assert dot.count("subgraph cluster_") >= 5


# ------------------------------------------------------------------ oldal

def _page(script: str):
    from streamlit.testing.v1 import AppTest

    return AppTest.from_string(script, default_timeout=60).run()


def test_page_renders_with_all_four_tabs(tmp_progress):
    at = _page("from pm_app import wbs\nwbs.view()\n")
    assert not at.exception, at.exception
    assert [t.label for t in at.tabs] == ["Fa", "Táblázat", "Függőségek", "Ráfordítás"]
    assert any("kiegészítő nézet" in t.value for t in at.title)


def test_tree_has_one_expander_per_branch_with_every_package(data, tmp_progress):
    at = _page("from pm_app import wbs\nwbs.view()\n")
    assert len(at.expander) >= len(data["branches"])
    body = " ".join(m.value for m in at.markdown)
    for p in data["packages"]:
        assert f"**{p['id']}** {p['name']}" in body, p["id"]


def test_every_package_can_be_chosen_on_the_dependency_tab(data, tmp_progress):
    at = _page("from pm_app import wbs\nwbs.view()\n")
    box = next(s for s in at.selectbox if s.key == "wbs-csomag")
    for p in data["packages"]:
        at = box.select(p["id"]).run()
        assert not at.exception, (p["id"], at.exception)
        assert any(m.value == f"#### {wbs._package_label(p)}" for m in at.markdown), p["id"]
        assert any(p["owner"] in c.value for c in at.caption), p["id"]
        box = next(s for s in at.selectbox if s.key == "wbs-csomag")
    assert any("Mitől függ" in m.value for m in at.markdown)


def test_dependency_tab_opens_with_a_package_that_shows_several_types(data, tmp_progress):
    at = _page("from pm_app import wbs\nwbs.view()\n")
    box = next(s for s in at.selectbox if s.key == "wbs-csomag")
    assert box.value == wbs.DEFAULT_PACKAGE == "3.5"
    package = next(p for p in data["packages"] if p["id"] == "3.5")
    kinds = {i["dependency"].kind for i in wbs.predecessors(package, data)}
    assert kinds == {"BK", "BB"} and wbs.successors("3.5", data)


def test_dependency_tab_shows_type_and_lag(tmp_progress):
    at = _page("from pm_app import wbs\nwbs.view()\n")
    at = next(s for s in at.selectbox if s.key == "wbs-csomag").select("8.3").run()
    shown = " ".join(str(cell) for t in at.table for cell in t.value.to_numpy().ravel())
    assert "kezdés–kezdés (KK +2 mn)" in shown and "befejezés–kezdés (BK)" in shown
    at = next(s for s in at.selectbox if s.key == "wbs-csomag").select("6.4").run()
    shown = " ".join(str(cell) for t in at.table for cell in t.value.to_numpy().ravel())
    assert "3.5  As-built konfigurációs dokumentáció" in shown
    assert "befejezés–befejezés (BB)" in shown


def test_table_filters_narrow_the_packages(data, tmp_progress):
    at = _page("from pm_app import wbs\nwbs.view()\n")
    next(s for s in at.selectbox if s.key == "wbs-kind").select("vegyes")
    at = at.run()
    assert not at.exception
    captions = " ".join(c.value for c in at.caption)
    assert "4 munkacsomag, összesen 152 óra" in captions
    assert wbs._hu(1260) == "1\u00a0260"
    at.toggle(key="wbs-ku").set_value(True)
    at = at.run()
    assert not at.exception
    assert "munkacsomag, összesen" in " ".join(c.value for c in at.caption)


def test_dependency_graph_toggle_draws_the_graph(tmp_progress):
    at = _page("from pm_app import wbs\nwbs.view()\n")
    at.toggle(key="wbs-halo").set_value(True)
    at = at.run()
    assert not at.exception
    assert len(at.get("graphviz_chart")) == 1


def test_wbs_page_is_in_the_menu_under_segedletek():
    from pathlib import Path

    app = (Path(__file__).resolve().parent.parent / "app.py").read_text(encoding="utf-8")
    segedletek = app.split('"Segédletek": [', 1)[1].split("],", 1)[0]
    assert 'url_path="wbs"' in segedletek and "wbs.view" in segedletek
    assert segedletek.index("wbs.view") < segedletek.index("gantt.view")


def test_branch_expander_labels_summarise_the_branch(data, tmp_progress):
    at = _page("from pm_app import wbs\nwbs.view()\n")
    labels = [e.label for e in at.expander]
    for b in data["branches"]:
        assert wbs._branch_summary(b) in labels, b["id"]
        assert f"{b['count']} munkacsomag, {b['hours']} óra" in wbs._branch_summary(b)


# ------------------------------------------------------------------ jelmagyarázatok

def test_every_open_branch_explains_the_red_dot_next_to_it(data, tmp_progress):
    """A piros pont jelentése a kinyitott ágban látszik, nem csak a lap tetején."""
    at = _page("from pm_app import wbs\nwbs.view()\n")
    branches = [e for e in at.expander if e.label[:2].strip(". ").isdigit()]
    assert len(branches) == len(data["branches"])
    for expander in branches:
        assert next(m.value for m in expander.markdown) == wbs.TREE_LEGEND, expander.label
    assert "●" in wbs.TREE_LEGEND and "kritikus úton" in wbs.TREE_LEGEND
    assert "●" in wbs._tree_markdown(data["branches"][0], data) or "●" in wbs._tree_markdown(data["branches"][2], data)


def test_table_tab_explains_the_ku_column(data, tmp_progress):
    at = _page("from pm_app import wbs\nwbs.view()\n")
    captions = [c.value for c in at.caption]
    assert any(wbs.TABLE_LEGEND in c for c in captions)
    assert "KU = kritikus úton van" in wbs.TABLE_LEGEND


def test_dependency_tab_explains_every_code_it_uses(data, tmp_progress):
    from pm_app.dependencies import KIND_NAMES

    at = _page("from pm_app import wbs\nwbs.view()\n")
    assert any(c.value == wbs.DEPENDENCY_LEGEND for c in at.caption)
    for code, name in KIND_NAMES.items():
        assert f"{code} = {name}" in wbs.DEPENDENCY_LEGEND, code
    assert "mn = munkanap" in wbs.DEPENDENCY_LEGEND
    # az oldalon használt minden jelölés (típus, mn) a jelmagyarázatban szerepel
    used = {d.kind for p in data["packages"] for d in parse_dependencies(p["deps"])}
    assert used <= set(KIND_NAMES)
