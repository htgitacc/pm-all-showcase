"""A mintaprojekt kulcsszámainak keresztellenőrzése a dokumentumok között.

Egy PM-portfólióban a számok hitelessége a legfontosabb: ezek a tesztek
elkapják, ha egy dokumentum módosítása után a többi nem követi.
"""

from __future__ import annotations

from conftest import ft, num, read_doc, section, tables

BUDGET = "docs/2-planning/07-koltsegvetes.md"
EVM = "docs/4-monitoring/06-evm-elemzes.md"
FIN_CLOSE = "docs/5-closure/04-penzugyi-zaras.md"

BAC = 46_130_000
RESERVE = 4_613_000
TOTAL = 50_743_000
ACTUAL = 44_822_000


def test_budget_items_add_up():
    rows = tables(section(read_doc(BUDGET), "1. Költségtételek"))[0]
    items = [r for r in rows if r[0]]  # a WBS-kóddal rendelkező sorok
    assert sum(ft(r[4]) for r in items) == BAC
    for r in items:
        qty, unit, total = int(r[2]), ft(r[3]), ft(r[4])
        assert qty * unit == total, r[1]
    assert round(BAC * 0.10) == RESERVE
    assert BAC + RESERVE == TOTAL


def test_cost_baseline_phasing_matches_payment_schedule():
    text = section(read_doc(BUDGET), "3. Időbeli elosztás")
    phasing, payments = tables(text)[:2]
    monthly = [ft(r[1]) for r in phasing if ft(r[1]) is not None]
    cumulative = [ft(r[2]) for r in phasing if ft(r[1]) is not None]
    running = 0
    for amount, cum in zip(monthly, cumulative):
        running += amount
        assert running == cum
    assert running == BAC

    # A fizetési ütemezés tételei az arányokból jönnek, és lefedik a szerződéses tételeket.
    lot_totals = {}
    for r in payments:
        lot = r[0].split("—")[0].strip()
        share = int(r[2].rstrip("%")) / 100
        lot_totals.setdefault(lot, []).append((share, ft(r[3])))
    for lot, parts in lot_totals.items():
        assert abs(sum(s for s, _ in parts) - 1.0) < 1e-9, lot
        whole = sum(a for _, a in parts)
        for share, amount in parts:
            assert amount == round(whole * share), lot


def test_financial_closure_payments_add_up():
    text = read_doc(FIN_CLOSE)
    rows = tables(section(text, "4. Kifizetések"))[0]
    paid = [ft(r[3]) for r in rows if r[0].isdigit()]
    total_row = next(r for r in rows if "Kifizetve a zárásig" in r[1])
    assert sum(paid) == ft(total_row[3])
    open_commitment = tables(section(text, "4. Kifizetések"))[1][0]
    assert sum(paid) + ft(open_commitment[1]) == ACTUAL
    # 10 hónap mobilnet a 2 kifizetett (május–június) után: 2026.07 – 2027.04.
    assert "2026.07 – 2027.04." in open_commitment[2]


def test_evm_indices_match_their_inputs():
    text = read_doc(EVM)
    for heading in ("2. Az első próbálkozás", "4. A javított számok"):
        for r in tables(section(text, heading))[0]:
            pv, ev, ac = ft(r[1]), ft(r[2]), ft(r[3])
            assert round(ev / pv, 2) == num(r[4]), (heading, r[0], "SPI")
            assert round(ev / ac, 2) == num(r[5]), (heading, r[0], "CPI")


def test_evm_first_attempt_uses_the_real_baseline_and_payments():
    """Az „első próbálkozás" PV-je a költségbázisból, AC-je a tényleges kifizetésekből jön."""
    first = {r[0]: r for r in tables(section(read_doc(EVM), "2. Az első próbálkozás"))[0]}
    phasing = tables(section(read_doc(BUDGET), "3. Időbeli elosztás"))[0]
    cum_by_month = {r[0]: ft(r[2]) for r in phasing}
    assert ft(first["2026.04.30."][1]) == cum_by_month["2026. április"]
    assert ft(first["2026.05.31."][1]) == cum_by_month["2026. május"]

    payments = tables(section(read_doc(FIN_CLOSE), "4. Kifizetések"))[0]

    def paid_until(month_day: str) -> int:
        total = 0
        for r in payments:
            if not r[0].isdigit() or r[5] == "folyamatos":
                continue
            day = r[5].replace("*", "").strip(".")[5:]  # "2026.04.20." → "04.20"
            if day <= month_day:
                total += ft(r[3])
        return total

    mobile_may = 200_000
    assert ft(first["2026.04.30."][3]) == paid_until("04.30")
    assert ft(first["2026.05.31."][3]) == paid_until("05.31") + mobile_may
    assert ft(first["2026.06.19."][3]) == paid_until("06.19") + mobile_may


def test_closure_report_counts_goals_correctly():
    text = read_doc("docs/5-closure/03-projektzaro-jelentes.md")
    goals = tables(section(text, "2. A célok teljesülése"))[0]
    met = [g for g in goals if "teljesült" in g[-1]]
    assert len(goals) == 8 and len(met) == 3
    assert "nyolc vállalt céljából **három" in text


def test_status_report_count():
    text = read_doc("docs/4-monitoring/01-statuszriport.md")
    log = tables(section(text, "Riportnapló"))[0]
    count = 0
    for r in log:
        ids = r[0].replace("*", "")
        if not ids.startswith("SR-"):
            continue
        parts = [int(p.strip().removeprefix("SR-")) for p in ids.split("–")]
        count += parts[-1] - parts[0] + 1
    total = next(r for r in log if "Összesen" in r[0])
    assert f"{count} riport" in total[1]
