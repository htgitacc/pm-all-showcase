"""A nyilvántartások számai: változásnapló és tartalék, döntés-, probléma- és
eszkalációs napló, hibalista, átvételi kritériumok, szerződések és kötbér.

Minden összesítő sornak abból kell kijönnie, amit a napló tételesen tartalmaz —
és ugyanannak a számnak minden dokumentumban ugyanannak kell lennie.
"""

from __future__ import annotations

import datetime as dt
import re

from conftest import ft, read_doc, section, tables
from test_schedule import _workday

CR = "docs/4-monitoring/03-valtozaskerelem.md"
CHANGE_LOG = "docs/4-monitoring/04-valtozasnaplo.md"
DECISIONS = "docs/3-execution/11-dontesnaplo.md"
ISSUES = "docs/3-execution/10-problemanaplo.md"
ESCALATIONS = "docs/4-monitoring/09-eszkalacios-naplo.md"
TESTS = "docs/3-execution/07-tesztjegyzokonyv.md"
UAT = "docs/3-execution/08-uat-elfogadas.md"
MINUTES = "docs/3-execution/12-meeting-jegyzokonyvek.md"
CONTRACT = "docs/3-execution/04-szerzodes.md"
HANDOVER = "docs/5-closure/01-atadas-atveteli-jegyzokonyv.md"
CLOSURE = "docs/5-closure/03-projektzaro-jelentes.md"
FIN_CLOSE = "docs/5-closure/04-penzugyi-zaras.md"
CONTRACT_CLOSE = "docs/5-closure/06-szerzodeszaras.md"

RESERVE = 4_613_000


def _plain(cell: str) -> str:
    return cell.replace("*", "").strip()


def _count(cell: str) -> int:
    return int(re.match(r"\d+", _plain(cell)).group(0))


def _ids(cell: str, prefix: str) -> list[str]:
    return re.findall(rf"{prefix}-\d+", cell)


def _kv(text: str) -> dict[str, str]:
    """Kétoszlopos (`| kulcs | érték |`) táblák egyetlen szótárban."""
    return {_plain(r[0]): r[1] for t in tables(text) for r in t if len(r) == 2}


def _date(text: str) -> dt.date:
    year, month, day = re.search(r"(\d{4})\.(\d\d)\.(\d\d)\.", text).groups()
    return dt.date(int(year), int(month), int(day))


def _pct(part: int, whole: int) -> str:
    return f"{part / whole * 100:.1f}".replace(".", ",") + "%"


# ---------------------------------------------------------------- változások és tartalék


def _change_requests() -> list[list[str]]:
    return tables(section(read_doc(CHANGE_LOG), "1. Benyújtott"))[0]


def test_change_log_summary_matches_its_rows():
    rows = _change_requests()
    approved = [r for r in rows if "jóváhagyva" in r[5]]
    rejected = [r for r in rows if "elutasítva" in r[5]]
    summary = {_plain(r[0]): r for r in tables(section(read_doc(CHANGE_LOG), "2. Összesítés"))[0]}

    assert _count(summary["Jóváhagyva"][1]) == len(approved)
    assert _count(summary["Elutasítva"][1]) == len(rejected)
    assert _count(summary["Összesen benyújtva"][1]) == len(rows)
    approved_cost = sum(ft(r[8]) or 0 for r in approved)
    assert ft(summary["Jóváhagyva"][2]) == approved_cost == ft(summary["Összesen benyújtva"][2])


def test_reserve_balance_runs_in_date_order_and_adds_up():
    text = section(read_doc(CHANGE_LOG), "3. A tartalékkeret")
    rows = tables(text)[0]
    dates = [_date(r[0]) for r in rows]
    assert dates == sorted(dates), "a tartalék alakulása időrendben haladjon"

    balance = ft(rows[0][3])
    assert balance == RESERVE
    for r in rows[1:]:
        balance += ft(r[2]) or 0
        assert ft(r[3]) == balance, r[1]

    used = RESERVE - balance
    assert f"{_pct(used, RESERVE)}-a" in text.replace("**", "")


def test_reserve_figures_agree_across_closure_documents():
    final_free = ft(tables(section(read_doc(CHANGE_LOG), "3. A tartalékkeret"))[0][-1][3])
    fin = {_plain(r[0]): r[1] for r in tables(section(read_doc(FIN_CLOSE), "3. A tartalékkeret"))[0]}
    adapters = -ft(fin["Felhasznált: 14 db HDMI–VGA adapter (D-07, 2026.03.03.)"])
    unspent = ft(fin["Fel nem használt (nem elköltött)"])
    earmarked = ft(next(v for k, v in fin.items() if "elkülönítve" in k))

    assert ft(fin["Jóváhagyott tartalékkeret"]) - adapters == unspent
    assert unspent - earmarked == ft(fin["— ebből szabad"]) == final_free

    closure = read_doc(CLOSURE)
    sources = {_plain(r[0]): r[1] for r in tables(section(closure, "4. Költség"))[1]}
    assert ft(sources["Fel nem használt tartalék"]) == unspent

    # A le nem hívott keret = keretmozgástér + beszerzési megtakarítás + el nem költött tartalék.
    summary = {_plain(r[0]): r[1] for r in tables(section(read_doc(FIN_CLOSE), "1. Összefoglaló"))[0]}
    headroom = ft(summary["Jóváhagyott költségkeret"]) - ft(summary["Tervezett költség (költségbázis + tartalék)"])
    savings = -ft(tables(section(read_doc(FIN_CLOSE), "2. Tételes"))[0][-3][4])
    assert headroom + savings + unspent == ft(summary["Le nem hívott keret"])
    assert f"{_pct(adapters, RESERVE)}" == _plain(fin["A tartalék tényleges felhasználása"])


def test_vk01_impact_assessment_adds_up():
    vk01 = section(read_doc(CR), "VK-01")
    cost = tables(section(vk01, "4.1"))[0]
    for r in cost:
        if r[1]:
            assert int(r[1]) * ft(r[2]) == ft(r[3]), r[0]
    one_off = sum(ft(r[3]) for r in cost[:4])
    assert ft(cost[4][3]) == one_off
    assert ft(cost[7][3]) == ft(cost[5][3]) + ft(cost[6][3])

    cover = {_plain(r[0]): ft(r[1]) for r in tables(section(vk01, "4.2"))[0]}
    available = cover["Tartalékkeret szabad része"] + cover["Keretmozgástér (52 M − 50 743 e)"] + cover["Beszerzési megtakarítás"]
    assert cover["Összesen elérhető"] == available
    assert cover["Szükséges"] == one_off
    assert cover["Hiány"] == available - one_off

    # A megtakarítás ugyanaz, mint a pénzügyi zárásban (B1 + B2/B3 + B4), és a
    # Steering-ülés is ugyanazokkal a számokkal döntött.
    fin_savings = -ft(tables(section(read_doc(FIN_CLOSE), "2. Tételes"))[0][-3][4])
    assert cover["Beszerzési megtakarítás"] == fin_savings
    minutes = _kv(section(read_doc(MINUTES), "VK-01"))["Fedezet"]
    for figure in (cover["Beszerzési megtakarítás"], available, -cover["Hiány"]):
        assert f"{figure:,}".replace(",", " ") in minutes


def test_every_change_request_has_a_decision_entry():
    decisions = {r[0].strip("*"): r for r in tables(read_doc(DECISIONS))[0]}
    cr_text = read_doc(CR)
    for r in _change_requests():
        vk = r[0]
        entry = [d for d, row in decisions.items() if f"({vk})" in row[1]]
        assert len(entry) == 1, f"{vk}: hiányzik vagy kétszer szerepel a Döntésnaplóban"
        block = cr_text.split(f"# {vk}")[1].split("\n# ")[0]
        assert re.search(rf"Döntésnapló\**\s*\|\s*\**{entry[0]}\b", block), vk


# ---------------------------------------------------------------- döntésnapló


def test_decision_log_statistics_partition_the_log():
    rows = tables(read_doc(DECISIONS))[0]
    ids = [r[0].strip("*") for r in rows]
    assert ids == [f"D-{i:02d}" for i in range(1, len(ids) + 1)], "folyamatos sorszámozás"
    makers = {r[0].strip("*"): _plain(r[3]) for r in rows}

    stats = {_plain(r[0]): r[1] for r in tables(section(read_doc(DECISIONS), "Statisztika"))[0]}
    assert _count(stats["Összes döntés"]) == len(ids)

    by_maker = {k: v for k, v in stats.items() if k not in
                {"Összes döntés", "Elutasított változáskérelem", "Feltételesen jóváhagyott változáskérelem"}}
    listed = [d for v in by_maker.values() for d in _ids(v, "D")]
    assert sorted(listed) == ids, "a döntéshozói sorok együtt pontosan a naplót fedik le"
    for key, value in stats.items():
        if key != "Összes döntés":
            assert _count(value) == len(_ids(value, "D")), key

    pm = _ids(by_maker["Projektmenedzser, saját hatáskörben"], "D")
    assert all(makers[d].startswith("Tóth Gergő") for d in pm)
    assert all(makers[d] == "Projekt Irányító Bizottság" for d in _ids(by_maker["Projekt Irányító Bizottság"], "D"))
    assert all("Nagy Péter" in makers[d] for d in _ids(by_maker[next(k for k in by_maker if k.startswith("Szakmai"))], "D"))


# ---------------------------------------------------------------- problémák és eszkalációk


def test_issue_log_summary_matches_entries():
    text = read_doc(ISSUES)
    closed = re.findall(r"^### (P-\d+)", section(text, "1. Lezárt"), re.M)
    open_ = re.findall(r"^### (P-\d+)", section(text, "2. Nyitott"), re.M)
    summary = {_plain(r[0]): r[1] for r in tables(section(text, "3. Összesítés"))[0]}
    assert _count(summary["Összes problémabejegyzés"]) == len(closed) + len(open_)
    assert _count(summary["Lezárva"]) == len(closed)
    assert _count(summary["Nyitva, elfogadott kezeléssel"]) == len(open_)

    from_risk = sorted(re.findall(r"### (P-\d+)[^#]*?Kapcsolódó kockázat", text, re.S))
    assert sorted(_ids(summary["Ebből korábban azonosított kockázatból lett"], "P")) == from_risk

    closure = {_plain(r[0]): r[1] for r in tables(section(read_doc(CLOSURE), "7. Kockázatok"))[0]}
    assert _count(closure["Problémabejegyzés"]) == len(closed) + len(open_)
    assert _count(closure["Ebből lezárva"]) == len(closed)


def _escalations() -> dict[str, dict[str, str]]:
    text = section(read_doc(ESCALATIONS), "1. Eszkalációk")
    blocks = re.split(r"^### (E-\d+)", text, flags=re.M)[1:]
    return {blocks[i]: _kv(blocks[i + 1]) for i in range(0, len(blocks), 2)}


def _response_workdays(entry: dict[str, str]) -> int:
    asked, answered = _date(entry["Mikor"]), _date(entry["Válasz"])
    return sum(_workday(asked + dt.timedelta(i)) for i in range(1, (answered - asked).days + 1))


def test_escalation_response_times_and_summary():
    esc = _escalations()
    deciding = {k: v for k, v in esc.items() if "Válaszidő" in v}
    days = {}
    for key, entry in deciding.items():
        days[key] = _response_workdays(entry)
        stated = _plain(entry["Válaszidő"])
        if days[key] == 0:
            assert stated.startswith(("aznap", "4 óra")), key
        else:
            assert stated.startswith(f"{days[key]} munkanap"), key

    summary = {_plain(r[0]): r[1] for r in tables(section(read_doc(ESCALATIONS), "2. Összesítés"))[0]}
    assert _count(summary["Eszkaláció összesen"]) == len(esc)
    assert sorted(_ids(summary["Ebből döntést kért"], "E")) == sorted(deciding)
    average = f"{sum(days.values()) / len(days):.1f}".replace(".", ",")
    assert _plain(summary[f"Átlagos válaszidő a {len(deciding)} döntéskérésre"]).startswith(average)

    levels = tables(section(read_doc(ESCALATIONS), "2. Összesítés"))[1]
    assert sum(_count(r[1]) for r in levels) == len(esc)


def test_e02_approval_round_workdays():
    problem = _plain(_escalations()["E-02"]["A probléma"])
    m1, d1, m2, d2, stated = re.search(r"\((\d\d)\.(\d\d)\.? – (\d\d)\.(\d\d)\., (\d+) munkanap\)", problem).groups()
    start, end = dt.date(2026, int(m1), int(d1)), dt.date(2026, int(m2), int(d2))
    workdays = [start + dt.timedelta(i) for i in range((end - start).days + 1) if _workday(start + dt.timedelta(i))]
    assert len(workdays) == int(stated)
    noticed = _date(_escalations()["E-02"]["Mikor vettem észre"])
    phrase = f"a {workdays.index(noticed) + 1}. munkanapján"
    assert phrase in problem
    # Ugyanezt a pillanatot írja le a státuszriport (SR-05) és a mérföldkő-riport is.
    for path in ("docs/4-monitoring/01-statuszriport.md", "docs/4-monitoring/08-merfoldko-riport.md"):
        text = read_doc(path)
        assert "jóváhagyási kör" in text and phrase in text, path


# ---------------------------------------------------------------- hibák és átvétel


def _defects() -> dict[str, str]:
    text = section(read_doc(TESTS), "4. Feltárt hibák")
    status = {}
    for key, body in re.findall(r"^#### (H-\d+).*?\n(.*?)(?=^####|^###|\Z)", text, re.S | re.M):
        status[key] = "javítva" if "Javítva" in body else "nyitva"
    for t in tables(text):
        for r in t:
            if r[0].startswith("H-"):
                status[r[0]] = "nyitva" if "nyitva" in r[-1] else "javítva"
    return status


def test_defect_counts_agree_everywhere():
    status = _defects()
    fixed = sorted(k for k, v in status.items() if v == "javítva")
    open_ = sorted(k for k, v in status.items() if v == "nyitva")
    text = read_doc(TESTS)

    stats = {_plain(r[0]): r[1] for r in tables(section(text, "7. Statisztika"))[0]}
    assert _count(stats["Feltárt hibák összesen"]) == len(status)
    assert _count(stats["Ebből javítva"]) == len(fixed)
    assert _count(stats["Ebből nyitva, elfogadott kezeléssel"]) == len(open_)
    assert sorted(_ids(stats["Ebből nyitva, elfogadott kezeléssel"], "H")) == open_

    listed = [r[0] for r in tables(section(text, "5. Nyitva maradt"))[0]]
    assert sorted(listed) == open_
    levels = {r[0]: r[2] for r in tables(section(text, "5. Nyitva maradt"))[0]}
    result = {_plain(r[0]): r[1] for r in tables(section(text, "2. Végeredmény"))[0]}
    assert _count(result["Nyitott S2 hiba elfogadott határidővel"]) == sum(v == "S2" for v in levels.values())
    assert _count(result["Nyitott S3–S4 hiba"]) == sum(v in {"S3", "S4"} for v in levels.values())

    closure = {_plain(r[0]): r[1] for r in tables(section(read_doc(CLOSURE), "6. Minőség"))[0]}
    assert _count(closure["Ebből javítva a zárásig"]) == len(fixed)
    assert _count(closure["Nyitva, elfogadott kezeléssel"]) == len(open_)
    handover = [r[0] for r in tables(section(read_doc(HANDOVER), "3. Nyitva maradt"))[0]]
    assert sorted(handover) == open_

    # A javítási ablakban javított hibák száma a mérföldkő-riportban is ugyanaz.
    window = next(r for r in tables(section(text, "1. A teszt szakaszai"))[0] if r[0] == "Hibajavítás")
    in_window = _ids(window[3].split(";")[0], "H")
    assert all(status[h] == "javítva" for h in in_window)
    assert _count(window[3]) == len(in_window)
    m8 = _kv(section(read_doc("docs/4-monitoring/08-merfoldko-riport.md"), "M8"))["Mit tettünk"]
    assert f"({len(in_window)} hiba;" in m8


def _acceptance(path: str) -> dict[str, bool]:
    result = {}
    for t in tables(read_doc(path)):
        for r in t:
            m = re.match(r"\**(AK-\d+)", r[0])
            if m:
                result[m.group(1)] = "nem felelt meg" not in r[-1].lower()
    return result


def test_acceptance_criteria_counts():
    handover, uat = _acceptance(HANDOVER), _acceptance(UAT)
    assert handover == uat
    passed, total = sum(handover.values()), len(handover)
    sentence = f"{passed} kritérium megfelelt, {total - passed} nem felelt meg"
    assert sentence in read_doc(HANDOVER) and sentence in read_doc(UAT)
    assert read_doc(CLOSURE).count(f"{passed}/{total} megfelelt") == 2

    # A Cloudia-szerződés Sz-6 feltétele csak az AK-01 – AK-23 kört köti.
    in_contract = {k: v for k, v in handover.items() if int(k[3:]) <= 23}
    sz6 = next(r for t in tables(read_doc(CONTRACT_CLOSE)) for r in t if r[0].startswith("Sz-6"))
    assert sz6[2].startswith(f"{sum(in_contract.values())}/{len(in_contract)} megfelelt")


# ---------------------------------------------------------------- szerződések és kötbér


def test_contract_payment_schedules_and_penalty():
    text = read_doc(CONTRACT)
    summary = {_plain(r[0]): r for r in tables(section(text, "1. Szerződés-összefoglaló"))[0]}
    value1, value2 = ft(summary["Nettó érték"][1]), ft(summary["Nettó érték"][2])

    for heading, value in (("2.4 Fizetési", value1), ("3.3 Fizetési", value2)):
        rows = tables(section(text, heading))[0]
        assert sum(int(r[1].rstrip("%")) for r in rows) == 100
        for r in rows:
            assert ft(r[2]) == value * int(r[1].rstrip("%")) // 100, r[0]

    penalty = _kv(section(text, "2.3 Kötbér"))
    daily = float(re.search(r"(\d+,\d+)%", penalty["Késedelmi kötbér"]).group(1).replace(",", "."))
    cap_pct = int(re.search(r"(\d+)%", penalty["Maximum"]).group(1))
    cap = ft(penalty["Maximum"])
    assert cap == value1 * cap_pct // 100

    # A szerződészárás viszonyítási számítása ugyanebből a szerződésből jön.
    closing = _kv(section(read_doc(CONTRACT_CLOSE), "Hibás teljesítés és kötbér"))["Kötbér"]
    second = ft(tables(section(text, "2.4 Fizetési"))[0][1][2])
    def huf(n: int) -> str:
        return f"{n:,}".replace(",", " ") + " Ft"

    assert f"napi {huf(round(second * daily / 100))}" in closing
    assert f"{huf(second)} × {daily:.1f}%".replace(".", ",") in closing
    assert f"legfeljebb {huf(cap)}" in closing


def test_cloudia_final_payment_follows_the_acceptance_it_depends_on():
    sz7 = next(r for t in tables(read_doc(CONTRACT_CLOSE)) for r in t if "Sz-7" in r[0])
    accepted = _date(sz7[2])
    payments = tables(section(read_doc(FIN_CLOSE), "4. Kifizetések"))[0]
    m8 = next(r for r in payments if "M8" in r[2])
    assert accepted <= _date(m8[5]), "a záró 30% nem fizethető ki a Run-book elfogadása előtt"
