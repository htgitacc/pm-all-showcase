# Havi mérési riportok (T+1, T+2, T+3)

**Dokumentum azonosítója:** XYO-CP-BEN-004\
**Projekt:** Xyo Cloud Pilot\
**Összeállította:** Tóth Gergő, mérési koordinátor\
**A hasznok gazdája:** Nagy Péter, IT osztályvezető\
**Verzió:** 1.2 (a T+3 mérés után)

> **A trend a lényeg. Egyetlen mérés félrevezető** — az élesítés utáni hetek
> mindig rosszabbak a betanulás miatt. A három hónap együtt ad értelmezhető
> képet.

---

## 1. Teljes adatsor, T0-tól T+3-ig

| # | Mérőszám | T0 | T+1 (júl) | T+2 (aug) | **T+3 (szept)** | Cél | Elérve? |
|---|---|---:|---:|---:|---:|---:|:-:|
| M1 | Ticket / hó | 103 | **118** | 71 | **74** | ≤ 72 | **✖** |
| M2 | MTTR (óra) | 11,4 | 8,2 | 6,4 | **5,1** | ≤ 6,0 | ✔ |
| M3 | Hozzáférési ticketek (%) | 41 | 34 | 22 | **17** | ≤ 20 | ✔ |
| M4 | Gépbeüzemelés (óra) | 6,5 | 1,5 | 1,4 | **1,4** | ≤ 1,5 | ✔ |
| M5 | Új belépő (munkanap) | 3,5 | 0,9 | — | **0,8** | ≤ 1,0 | ✔ |
| M6 | Home office (%) | 0 | 34 | 38 | **37** | ≥ 40 | **✖** |
| M7 | Adaptáció (%) | 0 | 86 | 91 | **94** | ≥ 90 | ✔ |
| M8 | MFA-lefedettség (%) | 0 | 100 | 100 | **100** | 100 | ✔ |
| M9 | Rendelkezésre állás (%) | 97,8 | 99,7 | 99,9 | **99,6** | ≥ 99,5 | ✔ |
| M10 | Adatvesztés (db/negyedév) | 0,75 | — | — | **0** | 0 | ✔ |
| M11 | Elégedettség (1–5) | 3,1 | — | — | **4,2** | ≥ 4,0 | ✔ |
| M12 | Fajlagos költség (Ft/fő/hó) | 12 667 | 17 633 | 17 633 | **17 633** | ≤ 20 000 | ✔ |

**Célérték elérve: 10 / 12. Kudarcküszöb alatt: 0.**

---

# T+1 riport — 2026. július 31.

## Összkép: 🟡 vegyes, a betanulási hatás dominál

| Mutató | Érték | Értékelés |
|---|---:|---|
| **M1 Ticket/hó** | **118** | **A T0 (103) FÖLÖTT!** |
| M2 MTTR | 8,2 óra | javul, de a cél még távol |
| M7 Adaptáció | 86% | a jelzésküszöb (70%) felett |

### Az M1 magyarázata — miért 118?

| Ok | Becsült hatás |
|---|---:|
| **Betanulási időszak** — a 2. és 3. hullám 40 fője július elején legfeljebb 4 hete dolgozik élesben | +25 ticket |
| **Hypercare 07.03-ig** — a kiemelt támogatás aktívan ösztönzi a bejelentést | +12 ticket |
| Szabadságolás (csökkentő hatás) | −22 ticket |

> **A T+1 értéket nem hasonlítjuk a célértékhez** — a KPI-adatlap ezt előre
> rögzítette. A 118-as szám nem riasztás, hanem várt jelenség.
>
> **Beavatkozás nem szükséges.** Ha viszont a T+2 is 100 felett marad, az már
> az R5 kockázat bekövetkezését jelezné.

### Amit a T+1 megmutatott

**Az M4 (gépbeüzemelés) azonnal célértéken van: 1,5 óra.** Ez volt az egyetlen
mutató, ami az élesítéstől kezdve teljesült — a technikai hasznok azonnal
jelentkeznek, a szervezetiek hónapokat igényelnek.

---

# T+2 riport — 2026. augusztus 31.

## Összkép: 🟢 a trend jó irányba mutat

| Mutató | T+1 → T+2 | Értékelés |
|---|---|---|
| M1 Ticket | 118 → **71** | Erős csökkenés — **de torzított** |
| M2 MTTR | 8,2 → **6,4** | Közel a célhoz |
| M3 Hozzáférési | 34% → **22%** | Az önkiszolgáló jelszó-visszaállítás hatása |
| M7 Adaptáció | 86% → **91%** | Célérték elérve |

### ⚠ Az M1 = 71 nem ünneplendő

| | |
|---|---|
| **Miért torzított** | Augusztusban a pilot körben **18%-kal kevesebb ledolgozott munkanap** volt (szabadságolás) |
| **Torzítás nélkül becsülve** | 71 / 0,82 ≈ **87 ticket/hó** |
| **Következtetés** | A valós szint augusztusban kb. 87 — a cél (72) még nincs meg |

> **Ez a riport legfontosabb mondata.** A 71-es szám a célérték alatt van, és
> könnyű lett volna sikerként jelenteni. **A KPI-adatlap előre rögzítette,
> hogy a T+3 a mérvadó** — pontosan azért, hogy ez a kísértés ne merüljön fel.

### Beavatkozás

Az M6 (home office, 38%) a cél alatt maradt. Varga Eszter jelezte, hogy
**két területvezető heti maximum 2 napban korlátozza** a home office-t,
miközben a szabályzat heti 3 napot enged.

| | |
|---|---|
| Beavatkozás | Nagy Péter és Varga Eszter egyeztetést kezdeményez a két vezetővel |
| Dátum | 2026.09.08. |
| Eredmény | A vezetők a saját mérlegelési jogukra hivatkozva fenntartották a korlátozást |

---

# T+3 riport — 2026. szeptember 30. (**mérvadó mérés**)

## Összkép: 🟢 10 / 12 mérőszám elérte a célértéket

### Elért célértékek

| # | Mérőszám | T0 | T+3 | Cél | Változás |
|---|---|---:|---:|---:|---|
| M2 | MTTR (óra) | 11,4 | **5,1** | ≤ 6,0 | **−55%** |
| M3 | Hozzáférési ticketek | 41% | **17%** | ≤ 20% | **−59%** |
| M4 | Gépbeüzemelés | 6,5 óra | **1,4 óra** | ≤ 1,5 | **−78%** |
| M5 | Új belépő | 3,5 nap | **0,8 nap** | ≤ 1,0 | **−77%** |
| M7 | Adaptáció | 0% | **94%** | ≥ 90% | — |
| M8 | MFA | 0% | **100%** | 100% | — |
| M9 | Rendelkezésre állás | 97,8% | **99,6%** | ≥ 99,5% | **+1,8 pp** |
| M10 | Adatvesztés | 0,75/né | **0** | 0 | **−100%** |
| M11 | Elégedettség | 3,1 | **4,2** | ≥ 4,0 | **+1,1** |
| M12 | Fajlagos költség | 12 667 Ft | **17 633 Ft** | ≤ 20 000 | +39% *(tervezett)* |

### Nem elért célértékek

#### M1 — Ticket/hó: 74 (cél ≤ 72)

| | |
|---|---:|
| T0 | 103 db/hó |
| T+3 | **74 db/hó** |
| Csökkenés | **−28%** |
| Célérték | ≤ 72 db/hó (−30%) |
| **Eltérés** | **2 ticket, azaz 2,8%** |
| Kudarcküszöb | > 95 — **jóval felette vagyunk** |

> **A cél −30% volt, a tény −28%.** Két tickettel maradtunk le havonta.
> A mutató **egyértelműen a kívánt irányba mozdult**, és a kudarcküszöbtől
> messze van. A PIR-ben ezt „lényegében teljesült, de formálisan nem"
> minősítéssel kezeljük — **nem írjuk át a célértéket utólag.**

#### M6 — Home office arány: 37% (cél ≥ 40%)

| | |
|---|---:|
| T0 | 0% |
| T+3 | **37%** |
| Célérték | ≥ 40% |
| Kudarcküszöb | < 20% — jóval felette |

| **Ok** | **Nem technikai.** Két területvezető heti max. 2 napban korlátozza a home office-t, miközben a szabályzat heti 3-at enged. Az érintett 22 fő aránya emiatt 29%, a többieké 43%. |
| **Bontás** | Korlátozás nélküli körben (28 fő): **43%** ✔ · Korlátozott körben (22 fő): **29%** ✖ |

> **A projekt a technikai lehetőséget megteremtette; a kihasználás vezetői
> döntés kérdése.** Ez nem a megoldás hibája — de a kiterjesztés
> szempontjából kezelendő, mert a haszon jelentős része (M2, M11) éppen a
> rugalmas munkavégzésből fakad.

## Az M2 értelmezése — figyelem a torzításra

Az MTTR 11,4 → 5,1 óra, ami látszólag hatalmas javulás. **A KPI-adatlap
előre jelezte a torzítást:** az önkiszolgáló jelszó-visszaállítás miatt a
gyors, egyszerű ticketek eltűntek a mintából, ami a maradék átlagát
**felfelé** tolná.

Mégis csökkent — vagyis a javulás **valós, sőt alulbecsült**.

## Kapacitás-haszon számítása

A Költség-haszon elemzés (XYO-CP-003) módszertanával, a tényadatokkal:

| Haszon | Számítás | Éves érték |
|---|---|---:|
| Kevesebb ticket | 348 ticket/év × 1,2 óra × 6 500 Ft | 2 714 400 Ft |
| Rövidebb megoldási idő a maradékon | 892 ticket × 0,8 óra × 6 500 Ft | 4 638 400 Ft |
| Gyorsabb gépbeüzemelés | 15 gép/év × 5,1 óra × 6 500 Ft | 497 250 Ft |
| Gyorsabb belépő-folyamat | 8 belépő × 2,7 nap × 8 óra × 6 500 Ft | 1 123 200 Ft |
| Elmaradó adatvesztés-helyreállítás | 3 eset × 12 óra × 6 500 Ft | 234 000 Ft |
| **Összesen** | | **9 207 250 Ft / év** |

*Ugyanaz a módszer, mint a Költség-haszon elemzésben: a megtakarított
ticket = (103 − 74) × 12 = 348, a maradék = a T0 éves 1 240 tickete − 348 = 892.*

| | |
|---|---:|
| A tervezett kapacitás-haszon (CBA) | 9 176 700 Ft/év |
| **A tényleges** | **9 207 250 Ft/év** |
| **Eltérés** | **+0,3%** |

> ⚠ **Ezek kapacitás-felszabadulások, nem pénzbeli megtakarítások.** A
> felszabaduló idő csak akkor válik valódi haszonná, ha más értékteremtő
> feladatra fordítjuk. A kontrolling ezért nem számolja el megtakarításként —
> ahogy azt a Költség-haszon elemzés is jelezte.

## Adathiány

**Nincs.** Mind a 12 mérőszámhoz teljes adatsor áll rendelkezésre a
mérési időszakra. Az M5, M10, M11 mutatóknál a kiolvasás a KPI-adatlap
szerinti gyakoriságban történt (eseményenként, illetve negyedév végén).

---

## Trend

```
M1 — Ticket/hó
118 │       ●118
103 │ ●103
 74 │                   ●74
 72 │┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ cél (≤ 72)
 71 │             ●71
    └───────────────────────
      T0    T+1   T+2   T+3

M7 — Adaptáció (%)  — T0: 0%
 94 │                   ●94
 91 │             ●91
 90 │┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ cél (≥ 90)
 86 │       ●86
 70 │┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ kudarcküszöb
    └───────────────────────
            T+1   T+2   T+3
```

---

| Szerep | Név | Dátum |
|---|---|---|
| Összeállította | Tóth Gergő, mérési koordinátor | 2026.10.02. |
| Adatot szolgáltatott | Kiss Réka, Szabó Márk, Varga Eszter, Balogh Tamás | havonta |
| Elfogadta | Nagy Péter, a hasznok gazdája | 2026.10.02. |

> **Kapcsolódó dokumentumok:** bemenete a *KPI-adatlap*, a *T0 baseline
> jegyzőkönyv* és a *Haszonrealizálási terv*; kimenete a *PIR*.
