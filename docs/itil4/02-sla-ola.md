# SLA, OLA és alátámasztó szerződések — „Felhőalapú munkahely”

**Dokumentum azonosítója:** XYO-ITIL-002\
**Szolgáltatás:** Felhőalapú munkahely (XYO-ITIL-001)\
**Szolgáltató:** IT osztály — Nagy Péter, szolgáltatásgazda\
**Megrendelő:** Horváth Júlia, ügyvezető\
**Készítette:** Kiss Réka, szolgáltatásszint-felelős, Tóth Gergővel\
**Dátum:** **2026. október 14.**\
**Verzió:** 1.1 — a PIR mért adataival véglegesítve

> ⚠ **ITIL 4-kiegészítés.** A Xyo-projektben „SLA” csak a Microsoft-szerződésnél szerepel.
> Célértékek viszont vannak — a haszonmérés KPI-jai (M2, M9, M11) —, csak a mérési szakasz
> végén, 2026.09.30-án lejárnak. **Ez a dokumentum a haszonmérés céljait tartós
> szolgáltatási vállalássá alakítja.**
>
> **A lényege:** a célszint **adatból jön, nem hasból.** A Xyo-nak szerencséje van: négy
> mérési pontja van (T0, T+1, T+2, T+3), előre rögzített definíciókkal. A legtöbb szervezet
> ehhez képest hasra ütött számokkal ír SLA-t.

---

## Verziók

| Verzió | Dátum | Mi változott |
|---|---|---|
| 1.0 | 2026.06.26. | Az üzemeltetésbe adáskor, **ideiglenes** célokkal a Haszonrealizálási terv célértékeiből |
| **1.1** | **2026.10.14.** | A T+1 – T+3 mérések és a PIR (2026.10.09.) alapján véglegesítve; prioritási célidők próbaidőszakra |

> **Miért két lépésben?** Az átadás napján még nem lehetett tudni, hogy a célok
> teljesíthetők-e. Az SLA-t mégis akkor kell aláírni — különben a projekt után három hónapig
> senki nem felel a szolgáltatási szintért. Az ITIL 4 irányelve: **haladj iteratívan,
> visszajelzéssel** (*progress iteratively with feedback*).

## 1. Három megállapodás, egy lánc

| Megállapodás | Kik között | Mit rögzít | Ebben a dokumentumban |
|---|---|---|---|
| **SLA** — szolgáltatási szintű megállapodás | IT osztály ↔ megrendelő | Mit kap a felhasználó, milyen szinten | 2–5. pont |
| **OLA** — működési szintű megállapodás | Service Desk ↔ rendszergazda ↔ HR | Ki mit ad a másiknak, mennyi idő alatt, hogy az SLA teljesíthető legyen | 5. pont |
| **Alátámasztó szerződés** (*underpinning contract*) | Xyo ↔ beszállítók | Mit vállal a Microsoft, a Cloudia és a TechLine | 6. pont |

> **A lánc szabálya:** az SLA nem ígérhet többet, mint amit az OLA és az alátámasztó
> szerződések együtt lehetővé tesznek. Ha a beszállító 24/7-ben 99,9%-ot vállal, a belső SLA nem
> lehet 99,99%. A 6.2 pont kiszámolja, hol van a Xyo határa.

## 2. Hatály és szolgáltatási idő

| | |
|---|---|
| **Szolgáltatás** | Felhőalapú munkahely — 50 felhasználó (Pénzügy, Értékesítés, Logisztika) |
| **Hatály** | 2026.10.15-től a licenc lejáratáig (**2027.04.30.**), illetve a kiterjesztés indulásáig |
| **Szolgáltatási idő** | Munkanapokon **7:30 – 17:00**; hétvége és ünnepnap nem számít bele |
| **Mérés és jelentés** | Havonta, a hónapot követő 2. munkanapon (Kiss Réka) — a KPI-adatlap szűrőivel |
| **Szolgáltatás-felülvizsgálat** | Negyedévente: Nagy Péter és Horváth Júlia; először 2027 januárjában |

> **A szolgáltatási idő a KPI-adatlap munkaidő-definíciója.** Ugyanaz az idősáv, amelyben az
> M2 és az M9 mérése történt — így az SLA-célok és a mért adatok összevethetők.

## 3. Szolgáltatási célszintek — az adatokból

### 3.1 A mért sorozat

| Mutató | KPI | T0 | T+1 | T+2 | T+3 | Haszonmérési cél |
|---|---|---:|---:|---:|---:|---:|
| Rendelkezésre állás (%) | M9 | 97,8 | 99,7 | 99,9 | 99,6 | ≥ 99,5 |
| Átlagos megoldási idő (óra) | M2 | 11,4 | 8,2 | 6,4 | 5,1 | ≤ 6,0 |
| Adatvesztés (db/negyedév) | M10 | 0,75 | — | — | 0 | 0 |
| Felhasználói elégedettség (1–5) | M11 | 3,1 | — | — | 4,2 | ≥ 4,0 |

### 3.2 A vállalt célszintek

| Célszint | Cél | Elfogadhatatlan szint | Indoklás az adatokból |
|---|---:|---:|---|
| **Rendelkezésre állás** a szolgáltatási időben | **≥ 99,5%** | < 99,0% | **Mindhárom mért hónapban teljesült** (99,7 / 99,9 / 99,6). Szigorítani nem lehet: a beszállítói lánc ennél többet nem fedez (6.2 pont). |
| **Átlagos megoldási idő** | **≤ 6,0 munkaóra** | > 10,0 munkaóra | **Csak a T+3-ban teljesült** (5,1), a T+2-ben még nem (6,4). Egy jó hónapra nem szigorítunk; két negyedév után újra megnézzük. |
| **Adatvesztés** | **0** | ≥ 1 eset | A visszaállítási teszt (42 perc a teljes könyvtárra) és a 30 + 30 napos lomtár alapján tartható |
| **Felhasználói elégedettség** | **≥ 4,0** | < 3,5 | 4,2 a T+3-ban. Évente egyszer, **ugyanazzal a hat kérdéssel**, mint a T0-nál |

*Az „elfogadhatatlan szint” a KPI-adatlap kudarcküszöbe. Ha ezt eléri a mutató, nem a
következő negyedévben beszélünk róla, hanem azonnal: Nagy Péter tájékoztatja Horváth Júliát.*

### 3.3 Amit szándékosan nem vállalunk célszintként

| Mutató | Miért nem SLA-cél |
|---|---|
| **M1 — ticket/hó** | **A ticketek száma a keresletet méri, nem a szolgáltatás szintjét.** Egy új belépő vagy egy oktatás után nő, és ettől a szolgáltatás nem lesz rosszabb. Jelentjük, de nem vállaljuk. |
| **M3 — hozzáférési ticketek aránya** | Belső hatékonysági mutató — a Service Desk teljesítményéről szól, nem a felhasználónak tett ígéretről |
| **M6 — home office arány** | A PIR kimutatta: vezetői gyakorlaton múlik, nem a szolgáltatáson |

> **Tipikus hiba:** minden mérőszámot SLA-célnak tenni, ami a projektben volt. Az SLA az, amit
> **a felhasználónak ígérünk**, és amiért az IT felelősséget vállal. A ticketszám nem ilyen: azt
> a felhasználók viselkedése alakítja.

### 3.4 A „dinnye-effektus” ellen

Az **átlag** elrejti a kiugró eseteket: zöld SLA mellett is lehet elégedetlen felhasználó
(kívül zöld, belül piros — innen a „dinnye” név). A Xyo saját mérése is mutatta, hogy a szám
nem mindig azt méri, amit gondolunk: a **T-22 tanulság** szerint az önkiszolgáló
jelszó-visszaállítás kivitte a gyors ticketeket a mintából, és ez az MTTR-t felfelé tolta.

**Ezért a havi jelentés három dolgot közöl együtt:**

1. az átlagos megoldási időt (a vállalt célszint),
2. **prioritásonként** a célidőn belül megoldott ticketek arányát (4. pont),
3. a legrosszabb három ticket rövid leírását — mi tartott sokáig, és miért.

Az elégedettséget pedig nem csak évente mérjük: a lezárt ticketek után egy egykérdéses
visszajelzés („megoldódott a problémád?”) havonta mutatja, amit az éves kérdőív csak egyszer.

## 4. Prioritás és célidők — próbaidőszakra

A projekt a **hibák súlyosságát** mérte (S1–S4, Minőségterv 2. pont). Az üzemeltetésben a
**prioritás** számít: a súlyosság mellett az is, **hány embert érint** és **mennyire sürgős**.

| Prioritás | Mikor | Reakcióidő | Helyreállítási cél | Példák a Run-bookból |
|---|---|---:|---:|---|
| **P1 — kritikus** | A szolgáltatás vagy egy teljes csapat nem működik, **vagy** biztonsági esemény | 15 perc | 4 munkaóra | 10. eset (elveszett gép), Microsoft 365-kiesés |
| **P2 — magas** | Egy felhasználó nem tud dolgozni, nincs kerülőmegoldás | 1 munkaóra | 1 munkanap | 4. eset (nem tud belépni), 6. eset (bérszámfejtés nem érhető el) |
| **P3 — közepes** | A munka akadályozott, de van kerülőmegoldás | 4 munkaóra | 3 munkanap | 1. eset (késő MFA-értesítés), 8. eset (lassú gép), 11. eset (nem települ alkalmazás) |
| **P4 — alacsony** | Kényelmi vagy kozmetikai hiba | következő munkanap | 10 munkanap, vagy ismert hibaként | 15. eset (angol feliratok) |

**Adatvédelmi incidensnél** a prioritástól függetlenül azonnal dr. Fekete Zsoltot kell
értesíteni, a szinteket átugorva (Run-book 5. pont, 4. szint).

> **Súlyosság ≠ prioritás.** A projektben „a felhasználó nem tud belépni MFA-val” **S1** volt,
> mert blokkolta az átvételt. Az üzemeltetésben ugyanez egy felhasználónál **P2**, húsz
> felhasználónál **P1**. A prioritás a szolgáltatásra gyakorolt hatást méri, nem a hiba
> természetét.

**Miért „próbaidőszakra”?** A prioritásonkénti célidőkre még nincs mért adat: a
ticketrendszer eddig nem rögzített prioritást. Az első negyedévben ezek **mérési célok**, nem
vállalások. A 2027. januári szolgáltatás-felülvizsgálaton a mért adatok alapján rögzítjük
őket (1.2 verzió) — ugyanúgy, ahogy a 3. pont céljai is mérésből születtek.

### 4.1 Szolgáltatáskérések célideje

| Kérés | Célidő | Mért érték (T+3) | Forrás |
|---|---:|---:|---|
| Új belépő munkába állása | ≤ 1,0 munkanap a HR-igénytől | 0,8 munkanap | M5 |
| Gépbeüzemelés (Autopilot) | ≤ 1,5 óra | 1,4 óra | M4 |
| Kilépő fiók letiltása | a munkaviszony utolsó napján | — | Run-book 4. pont, 13. eset |
| Fájl visszaállítása lomtárból | 1 munkaóra | — | Run-book 4. pont, 3. eset |

## 5. OLA — belső vállalások, hogy az SLA teljesíthető legyen

Az SLA-t az IT osztály egésze vállalja, de **három belső átadáson** múlik. Mindegyikhez egy sor
OLA tartozik.

### 5.1 Service Desk → rendszergazda (1. → 2. szint)

| Vállalás | P1 | P2 | P3 | P4 |
|---|---:|---:|---:|---:|
| A Service Desk eszkalál, ha nem tudja megoldani | 10 percen belül | 30 percen belül | 2 munkaórán belül | következő munkanap |
| Szabó Márk átveszi az eszkalált ticketet | 15 percen belül | 1 munkaórán belül | 4 munkaórán belül | 2 munkanapon belül |

**Az eszkaláció feltétele:** a Run-book 4. pontjának első szintű lépései elvégezve és a
ticketben rögzítve. Például „nem tudok belépni” (4. eset) csak akkor kerül tovább, ha az
önkiszolgáló jelszó-visszaállítás és az MFA-újraregisztrálás nem segített. **A ticketet a
Service Desk zárja**, a felhasználó megerősítése után — nem a 2. szint.

> **A helyettesítés nyitott pont.** Ha Szabó Márk szabadságon van, a 2. szint ma nem létezik.
> Ideiglenesen Nagy Péter veszi át, a szavatossági időben (2026.12.19-ig) a konfigurációs
> hibáknál a Cloudia Solutions. A tartós megoldás a kiterjesztés kapacitásbővítésénél (F4)
> dől el. **Ezt az OLA nem oldja meg, csak láthatóvá teszi** — és ez éppen a dolga.

### 5.2 HR → IT (új belépő, kilépő)

| Vállalás | Ki | Határidő |
|---|---|---|
| Az új belépő igénye hiánytalan adatokkal (név, csapat, belépés napja) | Varga Eszter, HR | legalább 2 munkanappal a belépés előtt |
| A kilépő bejelentése | HR | legkésőbb a munkaviszony utolsó napja előtti munkanapon |
| Az IT visszaigazolja, hogy a gép és a fiók kész | Kiss Réka | a belépés előtti munkanapon |

> **Miért kell OLA a HR-rel?** Az M5 a HR-igénytől méri a munkába állást. Ha az igény a belépés
> reggelén érkezik, az 1 munkanapos cél nem az IT-n múlik — és ezt csak egy előre rögzített
> belső vállalás teszi láthatóvá.

### 5.3 Rendszergazda → IT osztályvezető (3. szint)

Szolgáltatáskiesésnél, biztonsági eseménynél és szállítói kérdésnél Szabó Márk **azonnal**
értesíti Nagy Pétert (Run-book 5. pont, 3. szint). Nagy Péter dönt a szállítói bejelentésről
és a felhasználók tájékoztatásáról.

## 6. Alátámasztó szerződések

### 6.1 A beszállítói vállalások

| Beszállító | Szolgáltatás | Vállalás | Mérés módja | Meddig |
|---|---|---|---|---|
| Microsoft (CSP-n keresztül) | Microsoft 365 (SharePoint Online, OneDrive, Teams) | **99,9%** havi rendelkezésre állás, szolgáltatásonként | a hónap teljes ideje, 24/7 | 2027.04.30. |
| Microsoft | Microsoft Entra ID | **99,99%** havi rendelkezésre állás | 24/7 | folyamatos |
| Microsoft (Azure) | VPN Gateway (VpnGw1) | **99,95%** havi rendelkezésre állás | 24/7 | folyamatos |
| Cloudia Solutions Kft. | A bevezetés szavatossága | konfigurációs hibák díjmentes javítása | — | 2026.12.19. |
| TechLine Zrt. | Hardvergarancia (50 munkaállomás-készlet) | helyszíni szerviz, következő munkanapi kiszállás | — | 2029.05.29. |

**Három dolog, amit a szerződések nem fednek:**

1. **A Microsoft vállalása jóváírás, nem kártérítés.** Ha a Microsoft nem teljesít, a
   szolgáltatási díj egy részét írja jóvá — a Xyo kiesett munkaidejét nem téríti meg.
2. **A Cloudia szavatosságához nincs rögzített válaszidő.** A szerződés 3.6 pontja a
   szavatosság tartalmát rögzíti, a reakcióidőt nem; az ajánlat-értékelésben a támogatási
   konstrukció 85 pontot kapott. **Ellenőrizendő**, hogy az ajánlatban vállalt válaszidő része-e
   a szerződésnek — ha nem, a P1-célidő nem építhet a Cloudiára.
3. **A mobilszolgáltatónak nincs vállalása a Xyo felé** az otthoni lefedettségre — ezért
   került a H-06 a kizárások közé (XYO-ITIL-001, 5. pont).

### 6.2 Hol van a Xyo határa? — a lánc kiszámolva

A belső célszint a **szolgáltatási időre** szól (munkanapokon 7:30 – 17:00), a Microsoft
vállalása a **hónap teljes idejére** (24/7). Egy 2026. szeptemberi példán:

| | Számítás | Eredmény |
|---|---|---:|
| Szolgáltatási idő szeptemberben | 22 munkanap × 9,5 óra | 209 óra |
| **A belső SLA megengedett kiesése (0,5%)** | 209 óra × 0,005 | **62,7 perc** |
| A T+3-ban mért kiesés (99,6%) | 209 óra × 0,004 | kb. 50 perc |
| Microsoft 365 megengedett kiesése (0,1%) | 30 nap × 24 óra × 0,001 | 43,2 perc |
| Entra ID megengedett kiesése (0,01%) | 30 nap × 24 óra × 0,0001 | 4,3 perc |
| VPN Gateway megengedett kiesése (0,05%) | 30 nap × 24 óra × 0,0005 | 21,6 perc |
| **A három beszállító együtt, legrosszabb esetben** | 43,2 + 4,3 + 21,6 | **69,1 perc** |

**Mit mutat ez?** Ha mindhárom beszállító pontosan teljesíti a saját vállalását, de a
kiesések munkaidőre esnek, a Xyo belső 99,5%-os célja **sérülhet** (69,1 > 62,7 perc) —
anélkül, hogy bárki szerződést szegett volna. A 99,5% tehát **a lánc határán van**:
szigorúbbat (például 99,9%-ot) a beszállítók nem fedeznek.

A három szolgáltatás együttes, 24/7-es rendelkezésre állása 99,9% × 99,99% × 99,95% ≈
**99,84%**. Ez jóval a 99,5% fölött van — a gond nem az átlag, hanem az, hogy **a kiesés
mikor következik be**.

> **Ezért szerepel az M9 definíciójában, hogy a Microsoft-kiesés is beleszámít.** A
> felhasználót nem érdekli, kinek a hibája: ha nem tud dolgozni, a szolgáltatás nem elérhető.
> Az SLA ezt vállalja; a beszállítói kockázatot az IT viseli, és ezért kell ismernie.
>
> *A valóságban a kockázat kicsit nagyobb is lehet, mert a 99,9% Microsoft 365-szolgáltatásonként
> értendő: a SharePoint és a Teams kiesése külön is bekövetkezhet.*

## 7. Ha a célszint nem teljesül

| Helyzet | Mi történik | Ki |
|---|---|---|
| Egy hónapban a cél alatt, de az elfogadhatatlan szint fölött | A havi jelentésben ok és intézkedés | Kiss Réka |
| Két egymást követő hónapban a cél alatt | Fejlesztési javaslat a folyamatos fejlesztési nyilvántartásba | Nagy Péter |
| Az elfogadhatatlan szint elérése | Azonnali tájékoztatás a megrendelőnek, rendkívüli felülvizsgálat | Nagy Péter |
| Beszállítói ok | Bejelentés a beszállítónak; a jóváírás érvényesítése | Nagy Péter, Molnár Katalin |

> **Belső SLA-nál nincs kötbér** — az IT és a megrendelő ugyanannak a cégnek dolgozik. A
> következmény itt **átláthatóság és döntés**: a megrendelő látja, mi nem működik, és dönthet
> arról, hogy pénzt vagy embert ad-e rá.

---

## Mi a különbség a haszonmérés céljaihoz képest?

| | Haszonmérési cél (KPI-adatlap) | **SLA-célszint** |
|---|---|---|
| Kérdés | Megérte-e a projekt? | **Mit kap a felhasználó minden hónapban?** |
| Meddig él | A mérési szakasz végéig (2026.09.30.) | **A szolgáltatás élettartamáig** |
| Ki felel érte | A hasznok gazdája (Nagy Péter) | **A szolgáltatásgazda (Nagy Péter) — a Service Desk és a rendszergazda OLA-ival** |
| Mi történik, ha nem teljesül | A PIR rögzíti | **Intézkedés, a következő hónapban** |
| Mi számít bele | Minden, ami a hasznot mutatja (12 mutató) | **Csak amit a felhasználónak ígérünk (4 célszint)** |

> **A tanulság egy PM-nek:** a projekt legjobb öröksége itt nem a rendszer, hanem a **mérési
> fegyelem**. A KPI-adatlap pontos definíciói (szűrő, munkaidő, kiolvasási nap) nélkül ez az
> SLA nem lenne megírható. Egy PM, aki a haszonmérést így építi fel, az SLA alapját is leteszi.

| Szerep | Név | Aláírás | Dátum |
|---|---|---|---|
| Készítette | Kiss Réka, szolgáltatásszint-felelős | | 2026.10.14. |
| **Szolgáltató** | **Nagy Péter**, IT osztályvezető, szolgáltatásgazda | | 2026.10.14. |
| **Megrendelő** | **Horváth Júlia**, ügyvezető | | 2026.10.14. |
| OLA — 2. szint | Szabó Márk, rendszergazda | | 2026.10.14. |
| OLA — HR | Varga Eszter, HR vezető | | 2026.10.14. |

---

> **Kapcsolódó dokumentumok:** bemenete a *Szolgáltatásleírás* (XYO-ITIL-001), a
> *KPI-adatlap*, a *Havi mérési riportok*, a *PIR*, a *Run-book* és a *Szerződés*; kimenete a
> havi szolgáltatásszint-jelentés és a negyedéves szolgáltatás-felülvizsgálat.
>
> **Források a beszállítói vállalásokhoz:** Microsoft — *Service Level Agreements (SLA) for
> Online Services* (microsoft.com/licensing/docs); Azure VPN Gateway SLA (99,95% a Basic
> kivételével minden VPN Gateway típusra).
