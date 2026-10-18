"""A Kőris-minta (irodaköltözés) belső következetessége: a számok, a dátumok és a hivatkozások.

A Xyo-mintát külön tesztfájlok őrzik; ez a második példa saját, független számokkal él, ezért
külön ellenőrizzük — a számok forrása a `koris_szamok.py`.
"""

from __future__ import annotations

import datetime as dt
import re

import koris_szamok as k
import pytest
from conftest import example_docs, read_doc, section, tables

from pm_app import content

BASE = "docs/peldak/koris/1-initiation/"
IDEA, CASE, CBA, FEAS, CHARTER, REGISTER, GRID, LOG, BENEFITS, KICKOFF, GLOSSARY = (
    BASE + name
    for name in (
        "01-projekt-otlet.md", "02-uzleti-indoklas.md", "03-koltseg-haszon-elemzes.md",
        "04-megvalosithatosagi-tanulmany.md", "05-projektalapito-okirat.md",
        "06-erintettek-nyilvantartasa.md", "07-hatalom-erdek-matrix.md",
        "08-feltevesek-korlatok-naploja.md", "09-haszonrealizalasi-terv.md",
        "10-kick-off-jegyzokonyv.md", "11-projektszotar.md",
    )
)
ALL = [IDEA, CASE, CBA, FEAS, CHARTER, REGISTER, GRID, LOG, BENEFITS, KICKOFF, GLOSSARY]
WEEKDAYS = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
# 2027. március 15. (hétfő) munkaszüneti nap; az évszám a mintában csak ezen az egy napon számít.
HOLIDAYS = {dt.date(2027, 3, 15)}


def _day(text: str) -> dt.date:
    year, month, day = (int(x) for x in re.search(r"(\d{4})\.(\d\d)\.(\d\d)", text).groups())
    return dt.date(year, month, day)


def _ft(n: int) -> str:
    return k.ft(n)


# ------------------------------------------------------------------ azonosítók, nevek


def test_document_ids_are_sequential_and_match_the_yaml():
    for number, path in enumerate(ALL, start=1):
        assert f"**Dokumentum azonosítója:** KTK-IK-{number:03d}" in read_doc(path), path
    assert len(example_docs("koris")) == len(ALL)  # nincs gazdátlan fájl a mappában


def test_every_document_is_declared_as_a_koris_example():
    phase = next(p for p in content.load_phases() if p["id"] == "initiation")
    declared = [d["examples"]["koris"] for d in phase["documents"]]
    assert declared == [path for path in ALL]


def test_named_people_are_in_the_project_roster():
    roster = {r["name"] for r in next(p for p in content.sample_projects() if p["id"] == "koris")["roles"]}
    groups = {"Tervezők (36 fő)", "Adminisztratív munkatársak (6 fő)", "Kulcsügyfelek"}
    listed = {r[1] for r in tables(read_doc(REGISTER))[0]}
    assert groups <= listed                      # a csoportok a nyilvántartásban vannak, a névsorban nem
    people = listed - groups
    assert people and people <= roster, people - roster
    assert {"Kertész Ágnes", "Szűcs Dóra", "Lakatos Péter", "Sipos Márk", "Fehér Lilla"} <= roster


# ------------------------------------------------------------------ pénz


def test_one_off_items_sum_to_the_budget_everywhere():
    cba = read_doc(CBA)
    for name, value in k.ONE_OFF.items():
        assert _ft(value) in cba, name
    assert _ft(sum(k.ONE_OFF.values())) in cba                      # részösszeg
    assert _ft(k.reserve) in cba and _ft(k.one_off_total) in cba
    assert k.reserve == round(sum(k.ONE_OFF.values()) * 0.10)
    assert _ft(k.one_off_total) in section(read_doc(CHARTER), "5. Költségkeret")
    assert _ft(k.one_off_total) in section(read_doc(CHARTER), "2. Mérhető célok")
    for path in (CASE, KICKOFF):
        assert _ft(k.one_off_total) in read_doc(path), path


def test_monthly_costs_and_saving_are_consistent():
    assert k.renew_month - k.new_month == k.saving_month
    for path in (IDEA, CASE, CBA):
        assert _ft(k.renew_month) in read_doc(path), path
    for path in (CASE, CBA):
        assert _ft(k.saving_month) in read_doc(path), path
    assert _ft(12 * k.saving_month) in read_doc(CBA)


def test_option_table_matches_the_calculator():
    rows = tables(section(read_doc(CASE), "2. A vizsgált változatok"))[0]
    assert len(rows) == len(k.OPTIONS)
    for row, (month, once) in zip(rows, k.OPTIONS.values(), strict=True):
        text = " ".join(row)
        assert _ft(month) in text and _ft(60 * month + once) in text, row[0]
        if once:
            assert _ft(once) in text, row[0]


def test_recommendation_discloses_that_it_is_not_the_cheapest():
    # A keret „ne csináljunk semmit" és „puha haszon" szabálya itt azt kényszerítette ki, hogy a
    # nem legolcsóbb ajánlást nyíltan indokoljuk — ezt a teszt rögzíti.
    options = list(k.OPTIONS.values())
    totals = [60 * month + once for month, once in options]
    recommended = totals[2]
    assert min(totals) != recommended
    gap = recommended - min(totals)
    assert _ft(gap) in read_doc(CASE)


def test_payback_roi_and_sensitivity():
    cba = read_doc(CBA)
    assert f"≈ **{round(k.one_off_total / k.saving_month)} hónap**" in cba
    net3 = 36 * k.saving_month - k.one_off_total
    net5 = 60 * k.saving_month - k.one_off_total
    assert _ft(net3) in cba and _ft(net5) in cba
    assert f"**{round(net5 / k.one_off_total * 100)}%**" in cba
    stressed = round(k.one_off_total * 1.2)
    stressed_net3 = 36 * k.saving_month - stressed
    assert _ft(stressed) in cba
    assert f"**−{_ft(abs(stressed_net3))}**" in cba                  # a dokumentum valódi mínuszjelet használ
    assert _ft(60 * k.saving_month - stressed) in cba
    # a +20%-os eset 3 év alatt veszteséges, 5 év alatt nyereséges: ezért kell legalább 5 éves bérlet
    assert stressed_net3 < 0 < 60 * k.saving_month - stressed
    assert "legalább 5 éves" in cba and "legalább 5 éves" in read_doc(CHARTER)


# ------------------------------------------------------------------ dátumok


@pytest.mark.parametrize(
    "path, text, weekday",
    [
        (KICKOFF, "2026.11.04. (szerda)", "szerda"),
        (CHARTER, "2027.03.15. (hétfő)", "hétfő"),
    ],
)
def test_weekday_labels_are_right(path, text, weekday):
    assert text in read_doc(path)
    assert WEEKDAYS[_day(text).weekday()] == weekday


def test_charter_milestones_are_ordered_and_land_on_workdays():
    rows = tables(section(read_doc(CHARTER), "4. Mérföldkövek"))[0]
    days = {r[0]: _day(r[2].replace("–", " ").split()[0]) for r in rows}
    assert list(days) == [f"M{i}" for i in range(1, 9)]
    ordered = list(days.values())
    assert ordered == sorted(ordered)
    # M5 (költözés) hétvégi; a többi hétköznap, és egyik sem esik munkaszüneti napra
    for key, day in days.items():
        assert day not in HOLIDAYS, key
        if key != "M5":
            assert day.weekday() < 5, (key, day)
    assert days["M5"].weekday() == 4                                 # péntek: a költözés itt indul
    assert days["M6"] - days["M5"] == dt.timedelta(days=3)           # hétfő: az első munkanap


def test_decision_deadline_is_before_the_old_lease_notice():
    # A szerződést (M3) a hosszabbítási szándék határideje (2026.12.31.) előtt alá kell írni.
    rows = tables(section(read_doc(CHARTER), "4. Mérföldkövek"))[0]
    m3 = _day(next(r for r in rows if r[0] == "M3")[2])
    notice = dt.date(2026, 12, 31)
    assert m3 < notice
    assert "2026. december 31-ig" in read_doc(IDEA) and "2026.12.31-ig" in read_doc(CASE)


def test_internet_order_deadline_is_the_same_everywhere():
    # A kick-off döntése (D2) és a feltevésnapló F2-je az előrehozott határidőt mondja, a
    # megvalósíthatósági tanulmány eredeti dátumát (2027.01.11.) pedig a napló kifejezetten
    # jelzi, hogy felülírta.
    assert "2026.12.11" in read_doc(KICKOFF)
    f2 = next(r for r in tables(section(read_doc(LOG), "1. Feltevések"))[0] if r[0] == "F2")
    assert "2026.12.11" in " ".join(f2)
    assert "2026.12.11." in read_doc(LOG).split("**F2 előrehozva:**")[1]
    assert dt.date(2026, 12, 11).weekday() == 4


def test_every_date_in_the_documents_is_a_real_date():
    for path in ALL:
        for match in re.finditer(r"(\d{4})\.(\d\d)\.(\d\d)\.", read_doc(path)):
            year, month, day = (int(x) for x in match.groups())
            dt.date(year, month, day)  # ValueError, ha nincs ilyen nap
            assert 2025 <= year <= 2027, (path, match.group(0))


# ------------------------------------------------------------------ láncok


def test_baseline_values_agree_between_case_and_benefits_plan():
    plan = read_doc(BENEFITS)
    assert _ft(k.current_month) in plan and _ft(k.new_month) in plan
    assert f"{round(k.AVG_USE * 100)}%" in plan and f"{round(k.AVG_USE * k.STAFF)} fő" in plan
    assert f"{round(k.PEAK_USE * 100)}%" in plan and f"{round(k.PEAK_USE * k.STAFF)} fő" in plan
    case = read_doc(CASE)
    rows = {r[0]: r for r in tables(section(plan, "1. A várt hasznok"))[0]}
    assert "3,1" in rows["H3"][3] and "3,1" in case          # elégedettség
    assert "9 / hét" in rows["H2"][3] and "heti 9" in case   # tárgyalóütközés


def test_every_benefit_has_baseline_target_source_and_owner():
    rows = tables(section(read_doc(BENEFITS), "1. A várt hasznok"))[0]
    assert [r[0] for r in rows] == [f"H{i}" for i in range(1, 6)]
    for row in rows:
        assert all(cell.strip() for cell in row), row
    sources = tables(section(read_doc(BENEFITS), "2. Adatforrás"))[0]
    assert [r[0] for r in sources] == [r[0] for r in rows]


def test_stakeholder_ids_are_the_same_in_register_and_grid():
    register = {r[0] for r in tables(read_doc(REGISTER))[0]}
    assert register == {f"E{i}" for i in range(1, 12)}
    grid = read_doc(GRID)
    assert set(re.findall(r"\bE\d+\b", grid)) <= register
    # minden szorosan kezelendő és ellenálló szerepel a stratégiatáblában
    strategy = tables(section(grid, "2. Stratégia"))[0]
    assert {"E1", "E3", "E10"} <= {r[0] for r in strategy}


def test_resistant_stakeholders_have_a_plan():
    rows = tables(read_doc(REGISTER))[0]
    resistant = {r[0] for r in rows if "ellenálló" in r[-1]}
    assert resistant == {"E3", "E10"}
    plan = section(read_doc(GRID), "3. Az ellenállók kezelése")
    for key in resistant:
        assert f"{key})" in plan or f"{key}," in plan, key


def test_feasibility_conditions_are_carried_into_the_log():
    # „A feltételeket emeld át a feltevésnaplóba": a négy feltétel mindegyike megvan a naplóban.
    feas = section(read_doc(FEAS), "6. Következtetés")
    assert len(re.findall(r"^\d\. ", feas, re.MULTILINE)) == 4
    rows = {r[0]: " ".join(r).lower() for t in tables(read_doc(LOG)) for r in t}
    # feltétel → a naplósor azonosítója (F: feltevés, K: korlát)
    for needle, key in {"tervtár": "F6", "internet": "F2", "foglalási": "F3", "munkavédelmi": "K6"}.items():
        assert needle in feas.lower(), needle
        assert key in rows and needle in rows[key], (needle, key)


def test_glossary_terms_are_used_in_the_documents():
    terms = [r[0] for r in tables(read_doc(GLOSSARY))[0]]
    assert len(terms) == 6
    corpus = " ".join(read_doc(p) for p in ALL if p != GLOSSARY).lower()
    for term in terms:
        assert term.lower() in corpus, term     # csak valódi félreértésből született fogalom kerül be


def test_charter_has_scope_exclusions_and_pm_authority():
    # A két rész, amit a keret a legfontosabbnak tart (és amit a legtöbbször kihagynak).
    charter = read_doc(CHARTER)
    assert "NEM része" in charter and "parkolóhelyek" in charter.lower()
    assert "tételenként 1 000 000 Ft-ig" in charter
    assert "parkolás" in read_doc(KICKOFF).lower()      # a kizárás a kick-offon meg is védett egy vitát


def test_meta_facts_match_the_documents():
    koris = next(p for p in content.sample_projects() if p["id"] == "koris")
    assert _ft(k.one_off_total).split(" Ft")[0] in koris["facts"]["Jóváhagyott költségkeret"]
    assert _ft(k.saving_month).split(" Ft")[0] in koris["facts"]["Havi megtakarítás"]
    assert str(k.STAFF) in koris["facts"]["Érintett létszám"]
