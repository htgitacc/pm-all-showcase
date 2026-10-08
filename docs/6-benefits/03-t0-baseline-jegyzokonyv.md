# Kiindulási (T0) mérési jegyzőkönyv

**Dokumentum azonosítója:** XYO-CP-BEN-003\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**A mérés dátuma:** **2026. január 30.**\
**Verzió:** 1.0

> **Ez a legfontosabb és a leggyakrabban kihagyott dokumentum az egész
> módszertanban.** Rögzíti, honnan indultunk.
>
> A mérés a **Charter aláírása (2026.02.02.) előtt** történt. Ez az egyetlen
> alkalom, amikor a „projekt előtti" állapot mérhető — utólag legfeljebb
> közelíteni lehet.

---

## 1. A mérés köre

| | |
|---|---|
| Mért kör | A pilotra kijelölt 50 munkatárs és a hozzájuk tartozó IT-szolgáltatás |
| Visszatekintési időszak | 2025.01.01 – 2025.12.31. (teljes naptári év) |
| Mérési időpont | 2026.01.30. |
| Adatszolgáltatók | Kiss Réka (Service Desk), Szabó Márk (IT), Varga Eszter (HR), Balogh Tamás (kontrolling) |

> **A kijelölés 2026.02.26-án zárult**, a mérés viszont 01.30-án történt.
> Ezért a T0 a **leendő pilot körre** vonatkozik, a szervezeti egységek
> alapján lehatárolva (Pénzügy, Értékesítés, Logisztika). A végleges névsor
> ezt a kört 96%-ban lefedte — a 2 fő eltérés a mérést nem torzítja érdemben.

## 2. A kiindulási értékek

| # | Mérőszám | Mértékegység | **T0 érték** | Adatforrás | Mérte |
|---|---|---|---:|---|---|
| M1 | Helpdesk ticketek száma | db / hó | **103** | Service Desk ticketrendszer | Kiss Réka |
| M2 | Átlagos megoldási idő (MTTR) | óra | **11,4** | Service Desk ticketrendszer | Kiss Réka |
| M3 | Hozzáférési / jelszó ticketek aránya | % | **41** | Service Desk ticketrendszer | Kiss Réka |
| M4 | Gépbeüzemelési idő | óra / gép | **6,5** | IT munkanapló, 9 gép átlaga | Szabó Márk |
| M5 | Új belépő munkába állásáig eltelt idő | munkanap | **3,5** | HR + IT folyamatmérés, 8 belépő | Varga Eszter |
| M6 | Home office napok aránya | % | **0** | — (nincs technikai lehetőség) | Varga Eszter |
| M7 | SharePoint / OneDrive aktív felhasználók | % | **0** | — (nincs bevezetve) | Szabó Márk |
| M8 | MFA-lefedettség | % | **0** | — (nincs bevezetve) | Szabó Márk |
| M9 | Szolgáltatás-rendelkezésre állás | % | **97,8** | Fájlszerver üzemeltetési napló | Szabó Márk |
| M10 | Adatvesztéssel járó esetek | db / negyedév | **0,75** (3 db / év) | Service Desk + mentési napló | Kiss Réka |
| M11 | Felhasználói elégedettség | 1–5 skála | **3,1** | Kérdőív, 2026.01.26–29. | Varga Eszter |
| M12 | Fajlagos IT-költség | Ft / fő / hó | **12 667** | Kontrolling | Balogh Tamás |

## 3. Az egyes értékek levezetése

### M1–M3 — Service Desk adatok

| | |
|---|---|
| Lekérdezés | A ticketrendszerből, a három érintett szervezeti egység bejelentőire szűrve |
| Időszak | 2025.01.01 – 2025.12.31. |
| Összes ticket | **1 240 db** → 1 240 / 12 = **103,3 db/hó** |
| Kategóriabontás | hozzáférés/jelszó **41%** (508 db) · fájlszerver-elérés 22% (273) · hardver 18% (223) · egyéb 19% (236) |
| MTTR számítása | A lezárt ticketek `bejelentés → lezárás` idejének átlaga, munkaidőben számolva: **11,4 óra** |

**A pontos szűrőfeltétel:** `szervezeti_egyseg IN (Penzugy, Ertekesites,
Logisztika) AND statusz = lezart AND datum BETWEEN 2025-01-01 AND 2025-12-31`

> A szűrőt szó szerint rögzítettük, mert a havi mérésnél **ugyanezzel** kell
> lekérdezni. Ha egyetlen hónapban másképp kérdezzük le, az egész idősor
> használhatatlan lesz.

### M4 — Gépbeüzemelési idő

| | |
|---|---|
| Módszer | Az IT munkanapló alapján, 2025-ben beüzemelt 9 gép ráfordítása |
| Mérési tartomány | 5,5 – 8,0 óra |
| **Átlag** | **6,5 óra** |
| Mi tartozik bele | OS-telepítés, alapszoftverek, felhasználói profil, hálózati beállítás, átadás |

### M5 — Új belépő munkába állása

| | |
|---|---|
| Módszer | 8 belépő 2025-ben; a HR-igény beérkezésétől a munkára kész gép átadásáig |
| Mérési tartomány | 2 – 6 munkanap |
| **Átlag** | **3,5 munkanap** |

### M9 — Rendelkezésre állás

| | |
|---|---|
| Módszer | A fájlszerver tervezetten kívüli kiesései 2025-ben |
| Kiesés | 4 esemény, összesen 44 óra (munkaidőben) |
| Elvárt üzemidő | 250 munkanap (2025-ös munkanaptár) × 8 óra = 2 000 óra |
| **Rendelkezésre állás** | (2 000 − 44) / 2 000 = **97,8%** |

### M11 — Elégedettség (T0 kérdőív)

| | |
|---|---|
| Kitöltés | 2026.01.26–29., névtelenül, HR-en keresztül |
| Kiküldve | 52 fő (a leendő pilot kör) |
| Beérkezett | **38 válasz (73%)** |
| Kérdések | 6 kérdés, 1–5 skála |
| **Átlag** | **3,1** |

| Kérdés | T0 átlag |
|---|---:|
| Elégedett vagyok a munkaeszközeimmel | 3,0 |
| A fájljaimhoz akkor férek hozzá, amikor kell | 3,6 |
| Amikor IT-problémám van, időben kapok segítséget | 3,1 |
| A rendszerek elég gyorsak a munkámhoz | 3,3 |
| Rugalmasan tudok dolgozni (idő, helyszín) | **2,2** |
| Összességében elégedett vagyok az IT-szolgáltatással | 3,4 |
| **Átlag (= M11)** | **3,1** |

> A leggyengébb érték a **rugalmasság (2,2)** — pontosan az, amire a projekt
> válaszol. Ez a szám adta a projekt legerősebb üzleti indokát.

### M12 — Fajlagos IT-költség

| | |
|---|---:|
| Éves üzemeltetési költség a pilot körre | 7 600 000 Ft |
| Fő | 50 |
| Hónap | 12 |
| **Fajlagos költség** | 7 600 000 / 50 / 12 = **12 667 Ft / fő / hó** |

**Bontás:** fájlszerver amortizáció és karbantartás 3 200 000 · mentés
900 000 · szerverterem energia 1 100 000 · külső támogatás 2 400 000 Ft.

## 4. Ismert torzítások és hiányzó adatok

| # | Mit | Hatás | Hogyan kezeljük |
|---|---|---|---|
| 1 | **Az M6, M7, M8 értéke nulla**, mert a szolgáltatás nem létezett | Nincs valódi „előtte" állapot | A T+3 érték önmagában értelmezendő, nem növekményként |
| 2 | A T0 a leendő kört szervezeti egység szerint közelíti, nem a végleges névsor szerint | 2 fő eltérés | A mérést nem torzítja érdemben (96%-os fedés) |
| 3 | Az M4 csak 9 gép átlaga | Nagy szórás (5,5–8,0 óra) | A T+3-nál is átlagot mérünk, hasonló elemszámmal |
| 4 | Az M11 kitöltési aránya 73% | Önszelekciós torzítás lehetséges | A T+3 kérdőív **ugyanazokkal a kérdésekkel** megy ki |
| 5 | Az M9 csak a fájlszerverre vonatkozik | A felhős szolgáltatás más profilú | Az összehasonlítás irányadó, nem szigorúan azonos alapú |

## 5. Amit ebből tanulni kell

> **Ha ez a dokumentum nem készül el 2026.01.30-án, a teljes mérési szakasz
> értelmét veszti.**
>
> Nem lenne mihez hasonlítani a szeptemberi adatokat, és a kiterjesztésről
> szóló, több mint 100 millió forintos döntés **benyomásokon alapulna**.
>
> A mérést a Kezdeményezés fázis checklistje írja elő (`init-12`), és nem
> véletlenül: ez az a lépés, amit a legkönnyebb elhalasztani, és amit utólag
> lehetetlen pótolni.

---

| Szerep | Név | Aláírás | Dátum |
|---|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | | 2026.01.30. |
| Adatot szolgáltatott | Kiss Réka, Szabó Márk, Varga Eszter, Balogh Tamás | | 2026.01.28–30. |
| Tudomásul vette | Kovács Anita, szponzor | | 2026.02.02. |

> **Kapcsolódó dokumentumok:** bemenete a *Haszonrealizálási terv* és a
> *KPI-adatlap*; kimenete a *Havi mérési riportok* és a *PIR*.
