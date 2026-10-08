# Érintetti elégedettségi felmérés (Stakeholder Satisfaction Survey)

**Dokumentum azonosítója:** XYO-CP-409\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Lebonyolította:** Varga Eszter, HR vezető (névtelenül)\
**Kitöltési időszak:** 2026. június 22–26.\
**Dátum:** 2026. június 29.

> Megmutatja, **hogyan élték meg** az érintettek a projektet — ami nem
> ugyanaz, mint hogy teljesültek-e a mérőszámok.
> **Rövid és névtelen.** A 20 kérdéses, azonosítható kérdőívet vagy nem
> töltik ki, vagy nem őszintén.

---

## 1. A felmérés módszere

| | |
|---|---|
| Kérdőív terjedelme | 6 zárt kérdés (1–5 skála) + 2 nyitott |
| Kitöltés | Névtelen, HR-en keresztül |
| Célcsoport | 50 pilot résztvevő + 12 projektcsapat-tag és érintett |
| **Kitöltési arány** | **50 résztvevőből 41 (82%)**, 12 érintettből 11 (92%) |
| Emlékeztető | 1 db, 2026.06.24-én |

> Ez **nem azonos** a mérési szakasz felhasználói kérdőívével
> (XYO-CP-BEN-005). Az a **megoldást** méri, T0-hoz hasonlítva; ez itt
> **a projekt lebonyolítását**.

## 2. Eredmények — a pilot résztvevők (41 válasz)

| # | Kérdés | Átlag | Szórás |
|---|---|---:|---:|
| K1 | Időben és érthetően kaptam tájékoztatást arról, mi fog történni velem | **4,3** | 0,7 |
| K2 | Az oktatás felkészített az új környezet használatára | **4,5** | 0,6 |
| K3 | Amikor problémám volt, kaptam segítséget | **4,1** | 0,9 |
| K4 | Az átállás nem akadályozta érdemben a napi munkámat | **3,7** | 1,1 |
| K5 | A visszajelzéseimet figyelembe vették | **4,2** | 0,8 |
| K6 | Összességében elégedett vagyok a projekt lebonyolításával | **4,3** | 0,7 |
| | **Átlag** | **4,18** | |

### A leggyengébb eredmény: K4 (3,7) — „az átállás nem akadályozta a munkámat"

**Ez a legmagasabb szórású kérdés is (1,1)** — vagyis a válaszok erősen
megoszlanak. A bontás megmagyarázza:

| Csoport | K4 átlag |
|---|---:|
| 1. hullám (10 fő, az UAT tesztcsoport) | **2,9** |
| 2. hullám (20 fő) | 3,8 |
| 3. hullám (20 fő) | **4,3** |

> **Az első hullám élte meg a legnehezebben az átállást** — és joggal: ők
> találkoztak a két kritikus hibával (05.11.), ők tesztelték a lassú első
> szinkronizálást, és nekik még nem volt döntési ábra a gyorssegédletben.
>
> **A 3. hullám 4,3-as értéke azt mutatja, hogy a menet közbeni javítások
> működtek.** Ugyanez látszik a ticketszámokban is: 3,4 → 2,1 → 1,5 ticket/fő.
>
> Ez a projekt egyik legfontosabb megállapítása: **az első hullám ára**, hogy
> ők a tesztelők. Ezt előre kommunikálni kell — és a következő bevezetésnél
> érdemes elismerni is.

## 3. Eredmények — projektcsapat és érintettek (11 válasz)

| # | Kérdés | Átlag |
|---|---|---:|
| K1 | Világos volt, mi a feladatom és mikorra | **4,5** |
| K2 | A projektmenedzser időben jelezte a problémákat | **4,7** |
| K3 | A megbeszélések hasznosak és nem túl hosszúak voltak | **4,4** |
| K4 | A döntések követhetőek voltak | **4,6** |
| K5 | A ráfordításom nagyjából annyi volt, amennyire számítottam | **3,6** |
| K6 | Összességében elégedett vagyok az együttműködéssel | **4,5** |
| | **Átlag** | **4,38** |

### A leggyengébb eredmény: K5 (3,6) — a ráfordítás

A tényadat ezt alátámasztja: a belső ráfordítás 1 082 óra lett a tervezett
1 060 helyett (+2,1%) — de **nem egyenletesen oszlott el**. Szabó Márk
májusban 62 órát dolgozott a projekten, ami heti ~15 óra a jóváhagyott 12
helyett.

> **A csúcsterhelést az Erőforrásterv előre jelezte** (3. pont, „Terhelési
> csúcs: 2026. május"), és három intézkedéssel enyhítettük. A visszajelzés
> szerint ez **nem volt elég** — a következő projektnél a csúcshónapra
> érdemes külső kapacitást tervezni, nem csak átcsoportosítani.

## 4. Nyitott kérdések — a leggyakoribb válaszok

### „Mi volt a leghasznosabb a projektben?"

| Válasz | Hányan említették |
|---|---:|
| A home office lehetőség | 28 |
| Az oktatás, ahol a saját gépen dolgoztunk | 19 |
| A gyorssegédlet (kinyomtatva is) | 14 |
| Hogy bárhonnan elérem a fájljaimat | 12 |
| A Service Desk gyors reagálása a bevezetés után | 9 |

### „Mit csináltunk volna másképp?"

| Válasz | Hányan említették | Mit kezdtünk vele |
|---|---:|---|
| „Több idő kellett volna az első héten" | 11 | → Tanulság: az első hullámnál tervezni kell csökkentett munkaterhelést |
| „Előbb kellett volna tudni, hogy én is bekerülök" | 7 | A kijelölés 02.26-án zárult, az első hullám 05.11-én indult — a köztes kommunikáció (hírlevél) ezt nem pótolta teljesen |
| „A régi gépen még mindig van pár dolgom" | 5 | → A régi gépek 07.10-ig megmaradnak (NY-2); ezt jobban kellett volna kommunikálni |
| „Az MFA elsőre bonyolult volt" | 4 | Az oktatáson beállítottuk — enélkül több lett volna |
| „Nem tudtam, kihez forduljak" | 3 | A gyorssegédlet 5. pontja tartalmazza; a 3. hullámnál már nem merült fel |

## 5. Amit a felmérésből tanultunk

| # | Megállapítás | Következmény |
|---|---|---|
| 1 | **Az első hullám érezhetően rosszabbul élte meg az átállást** (K4: 2,9 vs. 4,3) | A kiterjesztésnél az első hullám résztvevőinek csökkentett munkaterhelést kell tervezni, és ezt előre kommunikálni |
| 2 | **A hullámról hullámra javuló élmény** igazolja a menet közbeni javításokat | A szakaszos bevezetés (nem „big bang") bevált — a kiterjesztésnél is így |
| 3 | A **kijelölés és az élesítés között 10 hét telt el** | A köztes kommunikáció (kéthetenkénti hírlevél) hasznos volt, de a várakozás így is hosszú |
| 4 | A **csapat ráfordítás-érzete a leggyengébb** (3,6) | A csúcshónapra külső kapacitást kell tervezni, nem csak belső átcsoportosítást |
| 5 | A **legerősebb pozitívum a home office** (28 említés) | A kiterjesztés kommunikációjának ezt kell a középpontjába tennie, nem a technológiát |

**Az 1., 4. és 5. megállapítás átvezetve a Tanulságok naplójába.**

## 6. Visszacsatolás a kitöltőknek

Az eredmények összefoglalóját **2026.06.30-án minden kitöltő megkapta**, a
projektzáró levéllel együtt, kiemelve, hogy mit változtattunk a
visszajelzéseik alapján:

- a gyorssegédlet „hova mentsem?" döntési ábrája,
- a `CP-Kozos` közös csapatoldal,
- az automatikusan induló VPN,
- az OneDrive előszinkronizálás a kiosztás előtt.

> **Ha kérdőívet töltetsz ki valakivel, de nem mondod el az eredményét,
> legközelebb nem fogja kitölteni.** A mérési szakasz kérdőíve (T+3) ugyanezt
> a kört fogja igényelni — és ott már a kiterjesztési döntés múlik a
> kitöltési arányon.

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.06.29. |
| Lebonyolította | Varga Eszter, HR vezető | 2026.06.22–26. |

> **Kapcsolódó dokumentumok:** bemenete az *Érintettek nyilvántartása* és a
> *Kommunikációs terv*; kimenete a *Tanulságok naplója* és a
> *Felhasználói elégedettségi kérdőív* (mérési szakasz).
