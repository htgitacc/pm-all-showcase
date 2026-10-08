# Hatalom-érdek mátrix (Power-Interest Grid)

**Dokumentum azonosítója:** XYO-CP-007\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Készült:** 2026. február 6.\
**Verzió:** 1.0

> **Verziójegyzet:** a nyertes szállító neve (TechLine Zrt.) a szerződéskötés után, 2026.04.20-án került a dokumentumba. A korábbi változatban a beszerzési tételek (B1–B4) szerepeltek; a baseline tartalma — hatókör, ütem, költség — ezzel nem változott. 2026.03.06-án az E17 (Fodor Gábor, felhasználói képviselő) a Szorosan kezelendő negyedbe került.

> ⚠️ **Bizalmas — korlátozott terjesztés.** Ezt a dokumentumot csak a
> projektmenedzser és a szponzor látja. Senki nem szereti magáról olvasni, hogy
> „alacsony érdekeltségű, elég tájékoztatni".

---

## 1. Mire jó ez a dokumentum?

Véges az időd. Ez a mátrix segít eldönteni, **kire mennyit fordíts belőle**.
Négy negyedbe soroljuk az érintetteket befolyás (hatalom) és érdekeltség szerint,
és mind a négyhez más stratégia tartozik.

```
     magas  ┌─────────────────────────┬─────────────────────────┐
            │  ELÉGEDETTEN TARTANDÓ   │   SZOROSAN KEZELENDŐ    │
            │  (Keep Satisfied)       │   (Manage Closely)      │
            │                         │                         │
  B         │  E1  Horváth Júlia      │  E2  Kovács Anita       │
  E         │  E9  dr. Fekete Zsolt   │  E3  Nagy Péter         │
  F         │  E13 Üzemi tanács       │  E17 Fodor Gábor        │
  O         ├─────────────────────────┼─────────────────────────┤
  L         │      FIGYELENDŐ         │     TÁJÉKOZTATANDÓ      │
  Y         │      (Monitor)          │     (Keep Informed)     │
  Á         │                         │                         │
  S         │  E15 TechLine Zrt.      │  E4  Szabó Márk         │
            │  E16 Mobilszolgáltatók  │  E5  Kiss Réka          │
            │  E12 Kimaradó kollégák  │  E8  Varga Eszter       │
            │                         │  E10 Pilot résztvevők   │
            │                         │  E6, E7, E11, E14       │
     alacsony└────────────────────────┴─────────────────────────┘
             alacsony            ÉRDEKELTSÉG            magas
```

## 2. Negyedenkénti stratégia

### Szorosan kezelendő (magas befolyás, magas érdekeltség)

| Érintett | Stratégia | Konkrét lépés |
|---|---|---|
| E2 Kovács Anita (szponzor) | Folyamatos, kétirányú kapcsolat | Heti státusz + havi személyes egyeztetés. **A rossz hírt tőlem hallja először.** |
| E3 Nagy Péter (szakmai vezető) | Társdöntéshozóként kezelni | Heti szakmai egyeztetés; minden technikai döntésbe bevonva |
| E17 Fodor Gábor (felhasználói képviselő) | Az átvételt vele együtt készíteni elő, ne a végén szembesüljön vele | A tesztterv társszerzője; az UAT alatt heti egyeztetés; az aláírása nélkül nincs átvétel |

> Ez a két ember a projekt sorsa — az átvételnél pedig a felhasználói képviselő. Ide megy az időd nagy része, és ez így helyes.

### Elégedetten tartandó (magas befolyás, alacsonyabb érdekeltség)

| Érintett | Stratégia | Konkrét lépés |
|---|---|---|
| E1 Horváth Júlia (ügyvezető) | Ne terheld részletekkel, de soha ne érje meglepetés | Havi **egyoldalas** Steering riport; nagy eltérésnél előzetes jelzés |
| E9 dr. Fekete Zsolt (DPO) | Formális, írásos bevonás, korán | Írásos megkeresés február első hetében; ne az utolsó pillanatban |
| E13 Üzemi tanács | Formális egyeztetés a tervezési fázisban | Megkeresés 2026.03.06-ig, dokumentált véleményezés |

> Ezek az érintettek **napi szinten nem érdeklődnek**, de ha valami rosszul megy,
> a befolyásuk azonnal aktiválódik. A DPO és az üzemi tanács gyakorlatilag vétójogú.

### Tájékoztatandó (alacsonyabb befolyás, magas érdekeltség)

| Érintett | Stratégia | Konkrét lépés |
|---|---|---|
| E4 Szabó Márk | Rendszeres, szakmai bevonás | Napi kapcsolat; a tudásátadás írásos garanciája megnyugtatja |
| E5 Kiss Réka | **Bevonás, nem tájékoztatás** | Részvétel a tervezésben; élesítés előtt 2 héttel felkészítés |
| E8 Varga Eszter | Együttműködés a kijelölésben és a kommunikációban | Kétheti egyeztetés |
| E10 Pilot résztvevők | Rendszeres, közérthető tájékoztatás | Kéthetente rövid hírlevél; oktatás; gyorssegédlet |
| E6, E7, E11, E14 | Ütemezett, célzott tájékoztatás | A saját területüket érintő információ, a saját formátumukban |

> **Figyelem:** ez a negyed a legveszélyesebb. Sokan érdekeltek, de egyenként
> kevés befolyásuk van — **együtt viszont eldönthetik a projekt sorsát**.
> Az 50 pilot résztvevő elégedettsége az egyik sikerkritérium (C7).

### Figyelendő (alacsony befolyás, alacsony érdekeltség)

| Érintett | Stratégia | Konkrét lépés |
|---|---|---|
| E15 TechLine Zrt. | Minimális, tranzakciós kapcsolat | Szállítási státusz e-mailben |
| E16 Mobilszolgáltatók | Csak igény esetén | Nincs rendszeres kommunikáció |
| E12 Kimaradó kollégák | **Egyszeri, világos kommunikáció** | A kijelölés szempontjai a névsor előtt |

> E12 azért kerül ide és nem feljebb, mert egyénileg alacsony a befolyásuk.
> **De ha méltányossági vita indul, az érdekeltségük hirtelen magasra ugrik** —
> ezért kell a szempontrendszert előre kommunikálni.

## 3. Ellenállók kezelési terve

| Érintett | Az ellenállás oka | Konkrét lépés | Határidő | Státusz |
|---|---|---|---|---|
| E5 Kiss Réka | Korábbi bevezetéseknél felkészítés nélkül kapta a terhelést | Bevonás a WBS-workshoptól; 2 hetes előzetes felkészítés; hypercare tervezése; nevesített szerep a mérésben | 2026.02.10-től folyamatos | **rendezve** — 2026.02.09-től óvatosan támogató |
| E11 Két területvezető | Attól tart, hogy home office-ban nem látja a munkatársai teljesítményét | Egyéni beszélgetés; a mérés csoportszintű, nem egyéni; a home office szabályzat rendezi a kereteket | 2026.02.20. | nyitva |
| E12 Kimaradó kollégák | „Miért nem én?" | A kijelölési szempontok kommunikációja a névsor előtt; a kiterjesztés perspektívájának kimondása | 2026.02.27. | nyitva |

## 4. Amire figyelj junior PM-ként

1. **A besorolás változik.** Kiss Réka egy hét alatt átkerült egy másik
   hozzáállási kategóriába. Nézd át a mátrixot havonta.
2. **A vétójogú, alacsony érdekeltségű érintett a legveszélyesebb.** A DPO és az
   üzemi tanács napokig nem gondol a projektedre — de egyetlen megkeresésre adott
   nemleges válaszuk megállíthatja.
3. **Az ellenállás mindig okkal van.** Kiss Réka nem a felhő ellen volt, hanem
   egy korábbi rossz tapasztalat ellen. Az ok megértése nélkül nem lehet kezelni.
4. **Ezt a dokumentumot ne oszd meg.** Az őszinteséggel jár, hogy nem publikus.

---

> **Kapcsolódó dokumentumok:** bemenete az *Érintettek nyilvántartása*;
> kimenete a *Kommunikációs terv*.
