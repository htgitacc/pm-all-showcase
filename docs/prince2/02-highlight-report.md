# Highlight Report — kiemelt állapotjelentés

**Dokumentum azonosítója:** XYO-P2-002\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, Project Manager\
**Címzett:** **Project Board** (Kovács Anita, Nagy Péter, Cloudia Solutions)\
**Jelentési időszak:** 2026. május 11 – 22.\
**Szakasz:** 3. — Kialakítás és teszt\
**Kiadás dátuma:** 2026. május 26.

> ⚠ **PRINCE2-kiegészítés.** A PMI Status Report megfelelője — de nem
> azonos vele.
>
> **A különbség:** a Highlight Report **a toleranciákhoz méri az állapotot**,
> nem általában a tervhez. A Board azt akarja tudni, hogy a PM **a kapott
> sávon belül van-e még.**

---

## 1. Az időszak összefoglalása

A 3. szakasz a felénél tart. Az M5 (környezet kész) és az M6 (első hullám,
UAT indul) mérföldkő **határidőre teljesült**. Az UAT első köre lezárult,
**81,5%-os megfelelési aránnyal** — a kilépési feltétel 95%.

Az élesítés első napján **két kritikus (S1) hiba** merült fel; mindkettő
javítva. A hibajavítási ablak (05.25 – 06.02., 9 naptári nap — Pünkösdhétfő miatt 6 munkanap) most indul, és
**puffer nélküli**.

---

## 2. Tolerancia-állapot

| Terület | Szakasz-tolerancia | Jelenlegi állás | Előrejelzés | Állapot |
|---|---|---|---|:-:|
| **Idő** | ± 5 munkanap | 0 nap eltérés | **0 – 8 nap** csúszás | 🟡 **veszélyben** |
| **Költség** | ± 5% | −3,2% (szerződött a költségbázishoz) | −2,8% (a tartalékfelhasználással) | 🟢 |
| **Hatókör** | nulla | változatlan | változatlan | 🟢 |
| **Minőség** | S1 hibából nulla | **0 nyitott S1** | 0 | 🟢 |
| **Kockázat** | 6-tól jelenteni | 4 db 6-os (R1, R4, R5, R6) — mind lent | R1 a pótlás után zárul | 🟢 |
| **Haszon** | a kudarcküszöbök | nem mérhető még | — | — |

> **Az idő-tolerancia a kritikus.** Ha a hibajavítás 06.02-ig nem zárul le,
> az M7 mérföldkő csúszik, és ezzel a szakasz **túllépi az ± 5 munkanapos
> toleranciát**. Ebben az esetben **Exception Reportot** készítek.
>
> **Visszajelzési időpontot vállalok: 2026. május 29.**

---

## 3. Ebben az időszakban elkészült termékek

| Termék | Állapot | Megjegyzés |
|---|---|---|
| Konfigurált felhőkörnyezet (M5) | ✔ elfogadva | 2026.05.08., határidőre |
| Mentési és visszaállítási képesség | ✔ elfogadva | Teljes könyvtár visszaállítva, **42 perc** |
| Első élesítési hullám — 10 fő | ✔ elfogadva | 2026.05.11–13. |
| UAT 1. kör | ⚠ **részben** | 22/27 teszteset megfelelt (81,5%) |

## 4. A következő időszakban várható termékek

| Termék | Tervezett |
|---|---|
| Javított hibák és újratesztelés | 2026.06.02. |
| 2. és 3. oktatási csoport (a 40 gép érkezése után) | 2026.06.01–02. |
| As-built dokumentáció (folyamatban) | 2026.06.19. |
| Második élesítési hullám — 20 fő | 2026.06.03–05. |

---

## 5. Nyitott problémák *(issues)*

| # | Probléma | Súlyosság | Hatás a toleranciára | Felelős | Határidő |
|---|---|:-:|---|---|---|
| P-07 | SharePoint keresés lassú | S2 | nincs | Cloudia | 05.27. |
| P-09 | Első OneDrive szinkronizálás 40+ perc | S3 | nincs | Szabó Márk | 05.26. |
| P-11 | Videóhívás megszakadása mobilneten (2 fő) | S2 | nincs — szolgáltatói ok | Nagy Péter | 07.31. |
| P-12 | Alkalmazásportál hiányos magyar felirata | S3 | nincs | Cloudia | 09.30. |

**Lezárva az időszakban:** P-04 (bérszámfejtés VPN-en), P-05 (feltételes
hozzáférés kizárta 3 felhasználót), P-06 (Autopilot — 5 gépen újramérve, 05.21.),
P-10 (közös csapatoldal, 05.20.).

---

## 6. Kockázatok

| # | Kockázat | Besorolás | Trend | Kockázatgazda |
|---|---|:-:|:-:|---|
| R5 | Felhasználói ellenállás, alacsony adaptáció | **6** | → | Varga Eszter |
| R6 | Az UAT több kritikus hibát talál a tervezettnél | 4 → **6** | ↑ | Nagy Péter |
| R1 | Laptopszállítás csúszik | **6** | → | Molnár Katalin |
| R4 | Belső kapacitáshiány | **6** | → | Nagy Péter |
| R12 | Service Desk kapacitás a hypercare alatt | 4 | → | Kiss Réka |
| **R11** | Feltételes hozzáférés kizárja a felhasználókat | **lezárva** | ↓ | — |

### R11 — bekövetkezett és lezárva

A kockázatot 2026.02.19-én azonosítottuk, a válaszlépés (5 napos jelentés-mód)
végre is hajtottuk — **mégis bekövetkezett**, mert a jelentés-mód irodai
hálózaton futott, a hiba pedig mobilneten jelentkezett. Javítva 05.12-én.

> Ez a **Tanulságok naplójába** került. A tanulság nem az, hogy legyen több
> kockázat a listán, hanem hogy **a válaszlépéseket ugyanolyan gondosan kell
> megtervezni, mint az azonosítást.**

---

## 7. Tanulságok az időszakból

| # | Tanulság |
|---|---|
| 1 | A próbaüzem jellegű ellenőrzést **a valós használati környezetben** kell futtatni, nem irodából |
| 2 | A **szabad tesztelés** (2 nap valós munka) két olyan hiányt talált, amit egyik teszteset sem fedett le |
| 3 | A szállítás közbeni minőségellenőrzés az Autopilot-hibát **26 nappal a 2–3. hullám 40 gépe előtt** találta meg |

---

## 8. Amit a Boardtól kérek

**Jelenleg semmit.** A helyzet a toleranciákon belül kezelhető.

**2026. május 29-én visszajelzek** arról, hogy a hibajavítási ablak elegendő-e.
Ha nem, **Exception Reportot** nyújtok be, döntési javaslattal.

---

| | |
|---|---|
| Készítette | Tóth Gergő, Project Manager |
| Dátum | 2026.05.26. |
| Következő Highlight Report | 2026.06.08. |

---

## Mi a különbség a PMI Status Reporthoz képest?

| | PMI Status Report | **PRINCE2 Highlight Report** |
|---|---|---|
| Kihez megy | Projektcsapat, szponzor, kontroller | **Kizárólag a Project Boardhoz** |
| Mihez méri az állapotot | A tervhez | **A toleranciákhoz** |
| Gyakoriság | Rögzített (hetente) | **A Board határozza meg a PID-ben** (itt kéthetente) |
| Mit vár el az olvasótól | Tájékozódás | **Semmit — amíg a tolerancián belül vagyunk.** Ez a lényeg. |
| Ha baj van | A státusz sárga/piros lesz | **Külön dokumentum készül: Exception Report** |

> **A legfontosabb különbség filozófiai.** A PMI státuszriport azt mondja:
> „így állunk". A Highlight Report azt: **„a rám bízott sávon belül vagyok,
> nem kell beavatkoznod."** Ha kiderül, hogy nem, akkor az már nem Highlight
> Report, hanem Exception Report — és az más műfaj.
>
> A Xyo projekt SR-10 státuszriportja (2026.05.18.) ugyanezt az időszakot
> fedte le, **piros státusszal**. PRINCE2-ben ez nem piros lett volna, hanem
> „sárga, tolerancián belül, visszajelzés 05.29-én" — mert a tolerancia
> túllépése akkor még csak lehetőség volt, nem tény.
