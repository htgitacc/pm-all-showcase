# Folyamatos fejlesztési nyilvántartás (CIR) — „Felhőalapú munkahely”

**Dokumentum azonosítója:** XYO-ITIL-006\
**Szolgáltatás:** Felhőalapú munkahely (XYO-ITIL-001)\
**Gazdája:** Nagy Péter, szolgáltatásgazda — átvette Tóth Gergőtől\
**Dátum:** **2026. október 14.**\
**Verzió:** 1.1 — a PIR és a kiterjesztési döntés után

> ⚠ **ITIL 4-kiegészítés.** A Xyo-projektnek kiváló **Tanulságok naplója** van: 23 tanulság, a
> nagy részük menet közben rögzítve. A tanulságok azonban a **következő projektnek** szólnak.
> A szolgáltatás fejlesztési ötleteinek — „így jobb lenne az, ami most fut” — a projekt
> zárása után nincs gazdája. Ez a nyilvántartás ad nekik.
>
> **A lényege:** a folyamatos fejlesztés nem egy projekt a projekt után, hanem **egy lista,
> egy gazda és egy rendszeres időpont**, amikor valaki ránéz. Az ITIL 4 szerint ez mindenkinek
> a dolga — de a listát valakinek vezetnie kell.

---

## Verziók

| Verzió | Dátum | Mi változott |
|---|---|---|
| 1.0 | 2026.06.30. | Megnyitva, amikor Tóth Gergő átadta a Tanulságok naplóját Nagy Péternek; a Run-book és az átadás nyitott pontjaival |
| **1.1** | **2026.10.14.** | A PIR (2026.10.09.), a kiterjesztési döntés és az ITIL-minták (XYO-ITIL-001 – 005) tételeivel |

## 1. Tanulság vagy fejlesztés?

| | Tanulságok naplója | **Folyamatos fejlesztési nyilvántartás** |
|---|---|---|
| Kinek szól | A következő projektnek | **A futó szolgáltatásnak** |
| Mi egy tétel | „Ezt legközelebb másképp csinálnám” | **„Ezt most jobban lehetne csinálni”** |
| Mikor zárul | Amikor átadták | **Amikor megvalósult és mérték a hatását** |
| Ki a gazdája | A projektmenedzser, a zárásig | **A szolgáltatásgazda, folyamatosan** |

**A 23 tanulságból 6 érinti a futó szolgáltatást** — ezek a nyilvántartásba is bekerültek vagy
már beépültek. A többi 17 a projektvezetésről szól (beszerzés, tervezés, riportálás), és a
kiterjesztési projektnek szól.

| Tanulság | Mit jelent a szolgáltatásnak | Hová került |
|---|---|---|
| T-01 — A jelentés-módot a valós használati környezetben kell futtatni | A feltételes hozzáférés minden módosításánál | Változásengedélyezési modell, 4.1 pont 3. kérdés (XYO-ITIL-003) |
| T-16 — Az MFA-t az oktatáson kell beállítani, nem otthon | Az új belépőnél az MFA-regisztráció az átadás része | Szabványos változás SV-1 (XYO-ITIL-003) |
| T-20 — A T+1 mérés önmagában félrevezető | Az SLA-mérés az ELS után kezdődik | XYO-ITIL-005, 4.3 pont |
| T-21 — A torzító tényezőket előre kell leírni | A havi SLA-riport a KPI-adatlap definícióival készül | SLA 2. pont (XYO-ITIL-002) |
| T-22 — A mérőszám nem mindig azt méri, amit hiszel | Az átlag mellett prioritásonként és a legrosszabb esetekkel jelentünk | SLA 3.4 (XYO-ITIL-002), CI-08 |
| T-23 — A technikai lehetőség nem egyenlő a kihasználással | A szolgáltatás haszna szervezeti feltételeken is múlik | CI-09 |

## 2. A nyilvántartás

**Prioritás:** az érték és a ráfordítás aránya. *Magas* = kicsi ráfordítás, legalább közepes
értékkel — ezzel kezdünk. *Közepes* = nagy érték nagy ráfordítással. *Alacsony* = minden más:
kicsi érték, vagy nagy ráfordítás nem nagy értékért.

| # | Fejlesztés | Forrás | Érték | Ráfordítás | Prioritás | Gazda | Határidő | Mérés | Állapot |
|---|---|---|---|---|---|---|---|---|---|
| CI-01 | Kérések és incidensek külön számolása a ticketrendszerben | PIR 4. pont (M1); XYO-ITIL-001, 4. pont | nagy | kicsi | **magas** | Kiss Réka | 2026.11.30. | Kérések aránya; incidens/hó | folyamatban |
| CI-02 | Tudáscikk és rövid emlékeztető a „hova mentsem?” kérdésre | PIR 4. pont; Run-book 4. pont, 2. eset | közepes | kicsi | **magas** | Kiss Réka | 2026.11.30. | Az ilyen kérések száma havonta | tervezett |
| CI-03 | A késő MFA-értesítés: szállítói ügy és kiváltó feltétel (PR-01) | XYO-ITIL-004, 4. pont | nagy | kicsi | **magas** | Szabó Márk | 2026.10.30. | PR-01-hez kötött bejelentések | folyamatban |
| CI-04 | Helyettes a 2. támogatási szinten | XYO-ITIL-002, 5.1; XYO-ITIL-005, SZE-10 | nagy | nagy | közepes | Nagy Péter | 2026.12.15. | Van-e kijelölt, betanított helyettes | nyitott |
| CI-05 | Ki mit figyel: riasztás a szolgáltatás állapotára | XYO-ITIL-005, SZE-09 | közepes | kicsi | **magas** | Szabó Márk | 2026.12.31. | Riasztási szabályok listája | nyitott |
| CI-06 | A Cloudia válaszidejének ellenőrzése; a kiterjesztés szerződésébe válaszidő | XYO-ITIL-002, 6.1 | közepes | kicsi | **magas** | Molnár Katalin | 2026.11.30. | A szerződésben rögzített válaszidő | nyitott |
| CI-07 | Prioritás rögzítése minden ticketnél, a P1–P4 célidők mérése | XYO-ITIL-002, 4. pont | nagy | kicsi | **magas** | Kiss Réka | 2026.11.30. | Célidőn belüli arány prioritásonként | folyamatban |
| CI-08 | A megoldási idő jelentése az átlag mellett prioritásonként és a legrosszabb esetekkel | T-22; XYO-ITIL-002, 3.4 | közepes | kicsi | **magas** | Kiss Réka | 2026.11.30. | — (jelentési forma) | tervezett |
| CI-09 | A home office szabályzat egységes vezetői alkalmazása | T-23; PIR 4. pont (M6); Kiterjesztési javaslat F1 | nagy | nagy | közepes | Varga Eszter, Horváth Júlia | 2026.12.15. | M6 a két csoportban | folyamatban |
| CI-10 | A „mindig elérhető” elvárás: a home office szabályzat pontosítása | PIR 5. pont, 5. megfigyelés | közepes | kicsi | **magas** | Varga Eszter | 2026.12.15. | Kérdőív-megjegyzések | nyitott |
| CI-11 | Service Desk kapacitás a kiterjesztésre | Kiterjesztési javaslat F4 | nagy | nagy | közepes | Kiss Réka, Nagy Péter | 2026.12.15. | Ticket/fő hullámonként | folyamatban |

**11 tétel: 8 magas, 3 közepes prioritású.** Alacsony prioritású tétel most nincs — ha lesz,
az is a listán marad, indoklással: a nyilvántartás arra is jó, hogy látsszon, **mit döntöttünk
el, hogy nem csinálunk meg.**

> **Tipikus hiba:** a nyilvántartás ötletgyűjteménnyé válik, gazda és határidő nélkül. Itt
> minden sornak van gazdája, határideje és — ahol lehet — **mérőszáma**. Az utolsó oszlop nélkül
> nem lehet megmondani, hogy a fejlesztés hozott-e valamit.

### 2.1 Ami nem ide tartozik — a kiterjesztési projekt

A kiterjesztési javaslat öt előfeltétele közül kettő a futó szolgáltatás fejlesztése (F1 → CI-09,
F4 → CI-11). A másik három **új képességet** hoz, ezért a kiterjesztési projekt hatókörébe
tartozik — nem itt kell kezelni:

| Előfeltétel | Miért projekt, és nem folyamatos fejlesztés | Felelős |
|---|---|---|
| F2 — adatvesztés-megelőzés (DLP) | Új biztonsági képesség, tervezéssel és teszteléssel | Szabó Márk, dr. Fekete Zsolt |
| F3 — behatolásteszt | Egyszeri, külső szakértői munka, beszerzéssel | Nagy Péter |
| F5 — csapat-szintű haladás | A kiterjesztés hullámainak összetétele | Tóth Gergő |

> **A határ:** ha a fejlesztéshez beszerzés, külön költségkeret vagy több hónapos terv kell,
> akkor projekt. Ha a meglévő szolgáltatáson belül, a meglévő emberekkel megoldható, akkor a
> CIR-ben a helye. Az ITIL 4 mindkettőt folyamatos fejlesztésnek tekinti — a különbség a
> kezelés módjában van.

## 3. A fejlesztési modell egy tételen végigvezetve: CI-01

Az ITIL 4 folyamatosfejlesztési modellje hét kérdés. Egy tételen így néz ki:

| # | Kérdés | Angolul | CI-01: kérések és incidensek külön |
|---|---|---|---|
| 1 | Mi a vízió? | *What is the vision?* | A H1 haszon: csökkenő IT-támogatási terhelés — és hogy ez **látszódjon is** |
| 2 | Hol tartunk most? | *Where are we now?* | M1 = 74 ticket/hó (T+3), a kérések és a hibák együtt; a Run-book 15 leggyakoribb esetéből 5 kérés |
| 3 | Hová akarunk eljutni? | *Where do we want to be?* | Külön számolt incidensek és kérések; az incidensek száma csökkenő trendet mutat. **A célszámot az első két hónap adatából rögzítjük, nem előre** |
| 4 | Hogyan jutunk oda? | *How do we get there?* | „Típus” mező a ticketrendszerben (incidens / kérés); a Service Desk besorolja a bejelentést; a CI-02 tudáscikke a kérések egy részét kiváltja |
| 5 | Cselekedj! | *Take action* | 2026. november: a mező bevezetése, a Service Desk eligazítása |
| 6 | Elértük? | *Did we get there?* | A 2027. januári szolgáltatás-felülvizsgálaton: két hónap adata |
| 7 | Hogyan tartjuk a lendületet? | *How do we keep the momentum going?* | Az arány a havi SLA-riport állandó sora; a kiterjesztés hullámainál a hullámonkénti ticket/fő mellett a kérés/fő is |

> **Miért pont ez a tétel?** Mert a Xyo saját mérése mutatta meg, hogy kell: a PIR szerint az M1
> elmaradását részben a „hova mentsem?” kérdések okozták. A fejlesztés **adatból indul, és
> adattal zárul** — ez a 3. kérdés lényege: a célt nem előre találjuk ki, hanem az első mérés
> után rögzítjük.

## 4. A ritmus — ki, mikor néz rá

| Mikor | Mi | Ki |
|---|---|---|
| Havonta, a szolgáltatásszint-riporttal | A „folyamatban” tételek állása; új tételek felvétele | Kiss Réka, Nagy Péter |
| Negyedévente, a szolgáltatás-felülvizsgálaton | A prioritások újragondolása; a lezárt tételek hatásának bemutatása | Nagy Péter, Horváth Júlia |
| Kiemelt incidens vagy probléma után | Új tétel, ha az értékelés javaslatot hozott | Szabó Márk |
| A kiterjesztés minden hulláma után | A hullám tapasztalatai: CIR-tétel vagy tanulság? | Tóth Gergő, Nagy Péter |

## 5. Bárki javasolhat

Az ITIL 4 szerint a folyamatos fejlesztés **mindenki feladata**. A Xyo-nál ez így működik:

| Honnan jöhet javaslat | Hogyan kerül a listára |
|---|---|
| Felhasználó | Ticketként, „javaslat” típussal — a Service Desk továbbítja |
| Service Desk | Közvetlenül Kiss Rékánál; a havi riportban |
| Kérdőív | A nyitott kérdések válaszaiból, évente |
| Vezető | A szolgáltatás-felülvizsgálaton |

> **A PIR nyitott kérdéseiből két tétel már bekerült** (CI-09, CI-10): mindkettő HR-hatáskör,
> nem IT-feladat. A CIR azért szolgáltatási és nem IT-nyilvántartás, mert **a szolgáltatás
> értéke szervezeti feltételeken is múlik** — ezt mondja ki a T-23 tanulság is.

---

## Mi a különbség a projekt tanulságaihoz és a PIR-hez képest?

| | Tanulságok naplója | PIR | **Folyamatos fejlesztési nyilvántartás** |
|---|---|---|---|
| Időpont | A projekt alatt és a zárásakor | Egyszer, a mérési szakasz végén | **Folyamatosan** |
| Kérdés | Mit tanultunk? | Megérte-e? | **Mit javítunk most, és sikerült-e?** |
| Kimenet | Javaslat a következő projektnek | Minősítés, döntési alap | **Megvalósított és mért fejlesztés** |
| Ki zárja le | A projektmenedzser | A Projekt Irányító Bizottság | **Senki — a lista él** |

> **A tanulság egy PM-nek:** a PIR a projekt utolsó szava a haszonról — a CIR az első lépés
> utána. A Xyo PIR-je becsületesen megnevezte, mi nem sikerült (M1, M6) és miért. Ha ezek a
> megállapítások nem kerülnek egy gazdás listára, a következő PIR ugyanezt fogja leírni.

| Szerep | Név | Dátum |
|---|---|---|
| Átadta | Tóth Gergő, projektmenedzser | 2026.06.30. |
| **Gazdája** | **Nagy Péter**, szolgáltatásgazda | 2026.10.14. |
| Közreműködött | Kiss Réka, Szabó Márk, Varga Eszter | 2026.10.14. |

---

> **Kapcsolódó dokumentumok:** bemenete a *Tanulságok naplója*, a *PIR*, a *Kiterjesztési
> javaslat*, a *Havi mérési riportok* és az ITIL-minták (XYO-ITIL-001 – 005); kimenete a
> negyedéves szolgáltatás-felülvizsgálat napirendje.
