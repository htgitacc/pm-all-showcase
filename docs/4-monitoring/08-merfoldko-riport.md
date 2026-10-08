# Mérföldkő-riport (Milestone Report)

**Dokumentum azonosítója:** XYO-CP-308\
**Projekt:** Xyo Cloud Pilot\
**Készíti:** Tóth Gergő, projektmenedzser\
**Ez a kiadás:** 2026. június 19. (M8 után)

> **A csúszás okát mindig írd le.** Fél év múlva a záró jelentésben pontosan
> ezekre lesz szükséged, és akkor már nem fogsz emlékezni rájuk.

---

## 1. Mérföldkövek — terv és tény

| # | Mérföldkő | Terv | Tény | Eltérés | Kritikus úton |
|---|---|---|---|---:|:-:|
| M1 | Projektalapító okirat aláírva | 2026.02.02. | 2026.02.02. | 0 | ✔ |
| M2 | Kick-off megtartva | 2026.02.09. | 2026.02.09. | 0 | ✔ |
| M3 | Baseline jóváhagyva (Planning-kapu) | 2026.03.13. | 2026.03.13. | 0 | ✔ |
| M4 | Szerződések aláírva | 2026.04.17. | 2026.04.17. | 0 | ✔ |
| M5 | Felhőkörnyezet tesztelésre kész | 2026.05.08. | 2026.05.08. | 0 | ✔ |
| M6 | 1. hullám élesben, UAT indul | 2026.05.11. | 2026.05.11. | 0 | ✔ |
| M7 | Teljes 50 fő élesben | 2026.06.12. | 2026.06.12. | 0 | ✔ |
| M8 | UAT lezárva, átvétel aláírva | 2026.06.19. | 2026.06.19. | 0 | ✔ |
| M9 | Üzemeltetésbe adás | 2026.06.26. | *tervezett* | — | ✔ |
| M10 | Projekt lezárva | 2026.06.30. | *tervezett* | — | ✔ |
| M11 | Utólagos értékelés (PIR) | 2026.10.09. | *tervezett* | — | |

**Nyolc teljesült mérföldkőből nyolc határidőre.**

## 2. Ez nem azt jelenti, hogy minden simán ment

A nulla eltérés **nem a szerencse eredménye**, és nem is azt jelenti, hogy
nem volt feszültség. Négy ponton került veszélybe a mérföldkő:

### M4 — Szerződéskötés (2026.04.17.)

| | |
|---|---|
| **Mi veszélyeztette** | A belső jóváhagyási kör a 3. munkanapján járt, és a gazdasági igazgatói jóváhagyás nem érkezett meg (R8 kockázat) |
| **Mikor derült ki** | 2026.04.13., a heti státusz készítésekor |
| **Mit tettünk** | Az SR-05 státuszriport **sárgára** állítva; eszkaláció Kovács Anitához (E-02) |
| **Eredmény** | A jóváhagyás 04.16-án megérkezett; a szerződés 04.17-én aláírva |
| **Elfogyott puffer** | A 6 munkanapból mind a 6 |

### M5 — Felhőkörnyezet kész (2026.05.08.)

| | |
|---|---|
| **Mi veszélyeztette** | A CSP partner egyik nevesített konzultánsa 04.24-én kiesett (R14 bekövetkezett, P-02) |
| **Mit tettünk** | A szerződés helyettesítési kötelezettségére hivatkozva 2 munkanapon belül helyettest kértünk |
| **Eredmény** | Csúszás nem történt |

### M7 — Teljes 50 fő élesben (2026.06.12.)

| | |
|---|---|
| **Mi veszélyeztette** | 1) 2 kritikus (S1) hiba az élesítés első napján (05.11.). 2) 12 hiányzó dokkoló tápkábel a 2. részszállításnál (05.28.) |
| **Mit tettünk** | 1) Mindkét S1 hiba 1–2 napon belül javítva. 2) Fenntartással történő átvétel, visszatartott fizetéssel; a pótlás 06.02-án megérkezett |
| **Eredmény** | A 3. hullám 06.10–12. között lement, határidőre |
| **Elfogyott puffer** | A 9 napos hibajavítási ablakból **mind a 9 nap** |

### M8 — UAT lezárva (2026.06.19.)

| | |
|---|---|
| **Mi veszélyeztette** | Az UAT első köre 22/27 teszteseten felelt meg (81,5%) — a kilépési feltétel 95% |
| **Mit tettünk** | A nyitott hibák javítása a 9 napos ablakban (4 hiba; további 5 már az UAT első köre alatt javult), majd újratesztelés 06.03–06.16. között |
| **Eredmény** | 26/27 (96,3%), nincs nyitott S1 hiba |
| **Elfogyott puffer** | A teljes javítási ablak |

## 3. Ahol tartalékidőt használtunk fel

| Tartalék | Tervezett | Felhasznált | Maradék |
|---|---:|---:|---:|
| Hibajavítás és újratesztelés az UAT után | 9 nap | **9 nap** | **0 nap** |
| A 7.2 és 7.3 hullám között | 4 nap | 0 nap | 4 nap |
| **Összesen** | **13 nap** | **9 nap** | **4 nap** |

> **A 9 napos javítási ablak teljes egészében elfogyott.** Ha az UAT egyetlen
> további kritikus hibát talál, az M7 mérföldkő csúszott volna — és mivel a
> kritikus úton nulla puffer van, az M10 (2026.06.30., L1 korlát) is.
>
> **Ez a projekt legszűkösebb pontja volt**, és a Steering riportokban is így
> jelentettem: „ha a javítási ablak nem lesz elég, 05.29-én jelzem."

## 4. Részteljesítések (a mérföldkövek között)

| Esemény | Terv | Tény | Eltérés |
|---|---|---|---:|
| Ajánlatkérés kiadva | 03.20. | 03.20. | 0 |
| Ajánlati határidő | 04.02. | 04.02. | 0 |
| Értékelés lezárva | 04.08. | 04.08. | 0 |
| 1. részszállítás (10 gép) | 05.06. | **05.05.** | **−1 nap** |
| 2. részszállítás (40 gép) | 05.29. | **05.28.** | **−1 nap** |
| Hiánypótlás (12 kábel) | 06.03. | **06.02.** | **−1 nap** |
| 1. élesítési hullám (10 fő) | 05.11–13. | 05.11–13. | 0 |
| 2. élesítési hullám (20 fő) | 06.03–05. | 06.03–05. | 0 |
| 3. élesítési hullám (20 fő) | 06.10–12. | 06.10–12. | 0 |
| Oktatás — 5 csoport + pótló | 06.10-ig | 06.10. | 0 |

**A hardverszállító mindhárom határidőt 1 nappal korábban teljesítette.**
Ez az egyetlen hely, ahol pozitív eltérés keletkezett.

## 5. Miért teljesült minden mérföldkő?

Három tényező, amit érdemes megjegyezni:

| # | Tényező | Hol dőlt el |
|---|---|---|
| 1 | **A részszállítás kikötése a szerződésben** | A 10 tesztgép 05.06-i határideje nélkül a tesztelés csak 05.29. után indulhatott volna — az M6, M7, M8 mind csúszott volna. Ez a *Beszerzési terv* P2 eleme, az R1 kockázat válaszlépése. |
| 2 | **A szállítás közbeni minőségellenőrzés** | A QC-02 (Autopilot beüzemelési idő) 26 nappal a 2–3. hullám 40 gépe (06.03.) előtt derült ki. Az átvételkor ez az AK-06 kritérium bukását és 50 gép újra-beüzemelését jelentette volna. |
| 3 | **A fenntartással történő átvétel** | Ha a 12 hiányzó kábel miatt megtagadjuk az átvételt, a 28 használható készlet is a raktárban marad, és a 3. hullám biztosan csúszik (D-18). |

> **Egyik sem az Execution fázisban dőlt el, hanem a Tervezésben.**
> A részszállítás, az ellenőrzési terv és az átvételi eljárás mind a
> tervezési fázis dokumentumaiban készült el — a Megvalósításban már csak
> alkalmazni kellett őket.

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.06.19. |

> **Kapcsolódó dokumentumok:** bemenete az *Ütemterv*; kimenete a
> *Státuszriport* és a *Projektzáró jelentés*.
