"""A Kőris-minta (irodaköltözés) adatlapjának számai — minden szám innen kerül a mintákba.

A tesztek (test_koris.py) ebből ellenőrzik a dokumentumokat. Kiírás: .venv/bin/python tests/koris_szamok.py
"""

OLD_M2, OLD_RENT, OLD_SVC = 620, 4900, 1400      # Ft/m²/hó: bérleti díj, üzemeltetési díj
INCREASE = 0.18                                   # a régi bérbeadó jelzett emelése hosszabbításkor
NEW_M2, NEW_RENT, NEW_SVC = 430, 5600, 1500
STAFF, AVG_USE, PEAK_USE = 42, 0.55, 0.72         # létszám, átlagos és csúcs-irodahasználat

current_month = OLD_M2 * (OLD_RENT + OLD_SVC)
renew_month = round(OLD_M2 * (OLD_RENT * (1 + INCREASE) + OLD_SVC))
new_month = NEW_M2 * (NEW_RENT + NEW_SVC)
saving_month = renew_month - new_month

ONE_OFF = {
    "belsőépítészeti kialakítás (a bérbeadói hozzájárulás után)": 16_500_000,
    "bútorzat (részben átvitt)": 7_800_000,
    "IT: hálózat, wifi, tárgyalótechnika": 4_600_000,
    "költöztetés (cég + csomagolás)": 2_100_000,
    "párhuzamos bérlet (1 hónap, régi iroda)": current_month,
    "a régi iroda helyreállítása": 1_900_000,
    "ügynöki díj, jogi átvilágítás": 1_450_000,
}
base = sum(ONE_OFF.values())
reserve = round(base * 0.10)
one_off_total = base + reserve


# Változatok az üzleti indokláshoz: név → (havi díj, egyszeri költség); 5 éves összevetés.
OPTIONS = {
    "0 — hosszabbítás változatlanul (620 m²)": (renew_month, 0),
    "1 — hosszabbítás kisebb területtel (520 m², ugyanott)": (
        round(520 * (OLD_RENT * (1 + INCREASE) + OLD_SVC)), 9_200_000),
    "2 — költözés: Duna Irodaház (430 m²)": (new_month, one_off_total),
    "3 — költözés: Budaörsi út (410 m²)": (410 * (5100 + 1450), 39_500_000),
}


def ft(n: int) -> str:
    return f"{n:,}".replace(",", " ") + " Ft"


if __name__ == "__main__":
    print("jelenlegi havi:", ft(current_month))
    print("hosszabbítva havi:", ft(renew_month))
    print("új iroda havi:", ft(new_month))
    print("havi megtakarítás:", ft(saving_month), "| éves:", ft(12 * saving_month))
    for name, value in ONE_OFF.items():
        print(f"  {name}: {ft(value)}")
    print("  tartalék (10%):", ft(reserve))
    print("egyszeri összesen:", ft(one_off_total))
    print("megtérülés:", round(one_off_total / saving_month, 1), "hónap")
    print("5 éves nettó haszon:", ft(60 * saving_month - one_off_total))
    print("csúcsban egyszerre bent:", round(STAFF * PEAK_USE), "fő; átlagosan:", round(STAFF * AVG_USE), "fő")
    print()
    for name, (month, once) in OPTIONS.items():
        print(f"{name}: havi {ft(month)}, egyszeri {ft(once)}, 5 év összesen {ft(60 * month + once)}")
    print("érzékenység: +20% egyszeri →", ft(round(one_off_total * 1.2)), "| megtérülés:",
          round(one_off_total * 1.2 / saving_month, 1), "hónap")
