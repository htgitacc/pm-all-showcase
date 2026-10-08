# Haszonrealizálási terv (Benefits Management Plan)

**Dokumentum azonosítója:** XYO-CP-009\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**A hasznok gazdája:** Nagy Péter, IT osztályvezető\
**Jóváhagyta:** Kovács Anita, szponzor — 2026.02.05.\
**Verzió:** 1.0

> **Ez a hatodik, mérési fázis alapdokumentuma.** Itt fogalmazzuk meg **előre**,
> mit várunk a projekttől és hogyan fogjuk mérni. Ha ez most nem készül el, a
> projekt végén nem tudjuk bizonyítani, hogy sikeres volt — csak állítani.

---

## 1. Mit várunk a projekttől?

A Xyo Cloud Pilot **nem költségmegtakarítási projekt** (lásd Költség-haszon
elemzés). Öt haszon megjelenését várjuk:

| # | Haszon | Kinek jó? | Mikor jelentkezik? |
|---|---|---|---|
| H1 | Csökkenő IT-támogatási terhelés | IT részleg, Service Desk | a bevezetés után 2-3 hónappal |
| H2 | Rugalmas, helyfüggetlen munkavégzés | Munkatársak, HR | azonnal az élesítéstől |
| H3 | Gyorsabb IT-folyamatok (gépbeüzemelés, belépés) | IT, HR | azonnal |
| H4 | Magasabb biztonsági szint | Egész vállalat | azonnal az élesítéstől |
| H5 | Megalapozott döntési alap a kiterjesztéshez | Vezetés | 2026.10.09. |

## 2. Mérőszámok, kiindulási értékek és célértékek

| # | Mérőszám | Mértékegység | **T0 (baseline)** | Célérték T+3 | Kudarcküszöb | Adatforrás | Felelős |
|---|---|---|---:|---:|---:|---|---|
| M1 | Helpdesk ticketek száma a pilot körben | db / hó | **103** | ≤ 72 | > 95 | Service Desk ticketrendszer | Kiss Réka |
| M2 | Átlagos megoldási idő (MTTR) | óra | **11,4** | ≤ 6,0 | > 10,0 | Service Desk ticketrendszer | Kiss Réka |
| M3 | Hozzáférési/jelszó ticketek aránya | % | **41** | ≤ 20 | > 35 | Service Desk ticketrendszer | Kiss Réka |
| M4 | Gépbeüzemelési idő | óra / gép | **6,5** | ≤ 1,5 | > 3,0 | Intune Autopilot naplók | Szabó Márk |
| M5 | Új belépő munkába állásáig eltelt idő | munkanap | **3,5** | ≤ 1,0 | > 2,0 | HR + IT folyamatmérés | Varga Eszter |
| M6 | Home office napok aránya a pilot körben | % | **0** | ≥ 40 | < 20 | HR jelenléti rendszer | Varga Eszter |
| M7 | SharePoint/OneDrive aktív felhasználók aránya | % | **0** | ≥ 90 | < 70 | M365 Usage Report | Szabó Márk |
| M8 | MFA-lefedettség | % | **0** | 100 | < 100 | Entra ID riport | Szabó Márk |
| M9 | Szolgáltatás-rendelkezésre állás | % | **97,8** (fájlszerver, 2025) | ≥ 99,5 | < 99,0 | M365 Service Health | Szabó Márk |
| M10 | Adatvesztéssel járó esetek | db / negyedév | **0,75** (3 db/év) | 0 | ≥ 1 | Service Desk + mentési naplók | Kiss Réka |
| M11 | Felhasználói elégedettség | 1–5 skála | **3,1** | ≥ 4,0 | < 3,5 | Kérdőív (HR bonyolítja) | Varga Eszter |
| M12 | Fajlagos IT-költség a pilot körben | Ft / fő / hó | **12 667** | ≤ 20 000 | > 24 000 | Kontrolling | Balogh Tamás |

> **M12 magyarázata:** a jelenlegi 7 600 000 Ft/év üzemeltetés 50 főre és 12
> hónapra vetítve 12 667 Ft/fő/hó. A felhős folyó költség 10 680 000 Ft/év =
> 17 800 Ft/fő/hó. **A fajlagos költség tehát nőni fog** — a célérték ezt
> tudatosan tükrözi. Kudarc az, ha 24 000 Ft fölé megy.

## 3. Mérési ütemterv

| Mérés | Dátum | Mit mérünk | Felelős |
|---|---|---|---|
| **T0 — baseline** | **2026.01.30.** | Mind a 12 mérőszám a projekt előtti állapotban | Tóth Gergő (koordinál) |
| T+0 — átadás | 2026.06.30. | M8, M9 (technikai állapot az átadáskor) | Szabó Márk |
| T+1 | 2026.07.31. | Mind a 12, a betanulási hatás jelzésével | Tóth Gergő |
| T+2 | 2026.08.31. | Mind a 12 | Tóth Gergő |
| T+3 | 2026.09.30. | Mind a 12 + elégedettségi kérdőív | Tóth Gergő |
| PIR | 2026.10.09. | Értékelés, kiterjesztési javaslat | Tóth Gergő |

> **A T0 mérés a legfontosabb lépés az egész tervben.** 2026.01.30-án, még a
> Charter aláírása előtt elvégezve — ez az egyetlen alkalom, amikor a
> „projekt előtti" állapot mérhető. A T0 jegyzőkönyv: *XYO-CP-BEN-003*.

## 4. Mi számít sikernek?

Ezt **most** kell rögzíteni, nem a mérés után.

| Minősítés | Feltétel |
|---|---|
| **Sikeres** | A 12 mérőszámból legalább **9 eléri a célértéket**, és egyik sem esik a kudarcküszöb alá. Az M11 (elégedettség) mindenképp eléri a 4,0-t. |
| **Nem sikeres** | 6-nál kevesebb mérőszám éri el a célértéket, **vagy** 2-nél több esik a kudarcküszöb alá, **vagy** az M11 elégedettség 3,5 alatt marad. |
| **Részben sikeres** | **Minden más eset** — például 6–8 célérték, vagy legalább 9 célérték mellett is, ha 1-2 mutató a kudarcküszöb alá esik, vagy ha az M11 3,5 és 4,0 közé kerül. |

> **A szabály hézagmentes:** előbb a *Sikeres*, aztán a *Nem sikeres*
> feltételét vizsgáljuk; ami egyikbe sem esik, az *Részben sikeres*. Így
> nincs olyan mérési eredmény, amelyre utólag kellene szabályt kitalálni.

**Kiterjesztési javaslat a minősítés alapján:**

- Sikeres → javaslat a szakaszos kiterjesztésre a teljes szervezetre.
- Részben sikeres → feltételes kiterjesztés: előbb a gyenge mutatók okának
  kezelése, majd újramérés 3 hónap múlva.
- Nem sikeres → a kiterjesztés elvetése; a pilot kör üzemeltetése folytatódik,
  a tanulságok írásba foglalásával.

## 5. Ismert torzító tényezők

Ezeket előre le kell írni, különben a mérés után válnak vitatottá.

| Mérőszám | Torzító tényező | Kezelés |
|---|---|---|
| M1, M2 | **Júliusi-augusztusi szabadságolás** csökkenti a ticketszámot | A T+3 (szeptemberi) érték a mérvadó; a T+1 és T+2 trendjelző |
| M1 | A **betanulási időszak** átmenetileg növeli a ticketszámot | A T+1 hónap külön értelmezendő, nem összehasonlítható a célértékkel |
| M6 | A nyári időszakban több a szabadság, kevesebb a munkanap | Arányszámot használunk, nem abszolút napszámot |
| M11 | Az újdonság okozta lelkesedés felfelé torzíthat | A T0 kérdőívvel azonos kérdéseket használunk |
| M12 | Az egyszeri beruházás nem szerepel a folyó költségben | Kizárólag a folyó (OPEX) költséget mérjük, jelzett módon |

## 6. A hasznok gazdája és a felelősségek

| Szerep | Név | Felelősség |
|---|---|---|
| **A hasznok gazdája** | Nagy Péter, IT osztályvezető | Azért felel, hogy a hasznok **ténylegesen megjelenjenek**; beavatkozik, ha egy mutató rossz irányba megy |
| Mérési koordinátor | Tóth Gergő, projektmenedzser | A mérések begyűjtése, riportálás, PIR elkészítése |
| Adatszolgáltatók | Kiss Réka, Szabó Márk, Varga Eszter, Balogh Tamás | A saját mérőszámaik pontos, azonos módszertanú kiolvasása |
| Döntéshozó | Projekt Irányító Bizottság | A kiterjesztésről szóló döntés a PIR alapján |

> **Fontos:** a projekt 2026.06.30-án lezárul, de a mérés még 3 hónapig tart.
> A mérési feladat átadása a projektzárás **feltétele** — írásban, nevesített
> gazdával.

## 7. Adatvédelmi kikötés

Az M6 (home office arány) és az M7 (adaptáció) mérése személyes adatot érinthet.

- **Csak csoportszintű összesítés** publikálható; egyéni bontás nem.
- Az elégedettségi kérdőív **névtelen**.
- A mérési adatgyűjtésre dr. Fekete Zsolt (DPO) írásos állásfoglalását be kell
  szerezni a mérési szakasz indulásáig.

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.02.04. |
| A hasznok gazdájaként elfogadta | Nagy Péter, IT osztályvezető | 2026.02.05. |
| Jóváhagyta | Kovács Anita, szponzor | 2026.02.05. |

> **Kapcsolódó dokumentumok:** bemenete az *Üzleti indoklás* és a
> *Projektalapító okirat*; kimenete a *Haszonrealizálási terv (végleges)*, a
> *KPI-adatlap* és a *Kiindulási (T0) mérési jegyzőkönyv*.
