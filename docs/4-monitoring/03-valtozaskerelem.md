# Változáskérelem (Change Request)

**Dokumentum azonosítója:** XYO-CP-303\
**Projekt:** Xyo Cloud Pilot\
**Verzió:** 1.0

> **A kérelem formálissá teszi a módosítást, és kikényszeríti a
> hatásvizsgálatot.** Enélkül a módosítás hatókör-elszivárgás, aminek a
> következményét rajtad kérik számon.

---

# VK-01 — A pilot bővítése 50 → 65 főre

| | |
|---|---|
| **Sorszám** | VK-01 |
| **Benyújtó** | Papp Zsófia, területvezető (Logisztika) |
| **Benyújtás dátuma** | 2026.05.19. |
| **Nyilvántartásba véve** | 2026.05.20. |
| **Státusz** | **ELUTASÍTVA** — 2026.06.03. |

## 1. Mit kérsz?

A pilot körének bővítése a jelenlegi 50 főről 65 főre, a logisztikai
szervezeti egység további 15 munkatársával.

## 2. Miért?

*(a benyújtó szövege)*

> „Az első hullám tapasztalatai a csapatban gyorsan terjedtek, és további
> 15 kolléga jelezte, hogy szeretne bekapcsolódni. A logisztikai csapat
> munkája erősen terepi jellegű, számukra a home office és a bárhonnan
> elérhető dokumentumok kiemelten hasznosak lennének. Ha most maradnak ki,
> a következő lehetőségre akár egy évet is várniuk kell."

## 3. Mi történik, ha nem valósul meg?

*(a benyújtó szövege)*

> „A 15 kolléga a régi asztali gépeken dolgozik tovább, home office lehetőség
> nélkül. Ez a csapaton belül két különböző működési módot jelent, ami
> a napi együttműködést nehezíti."

> **Ez a mező szűri ki a „jó lenne, ha" típusú kéréseket.** Papp Zsófia
> konkrét működési problémát írt le — a kérés szakmailag megalapozott volt.

---

## 4. Hatásvizsgálat

*(a projektmenedzser tölti ki)*

### 4.1 Költséghatás

| Tétel | Menny. | Egységár | Összesen |
|---|---:|---:|---:|
| Laptop | 15 | 420 000 Ft | 6 300 000 Ft |
| Dokkoló | 15 | 45 000 Ft | 675 000 Ft |
| Monitor | 15 | 65 000 Ft | 975 000 Ft |
| Headset | 15 | 25 000 Ft | 375 000 Ft |
| **Egyszeri összesen** | | | **8 325 000 Ft** |
| M365 licenc (12 hó) | 15 | 105 600 Ft | 1 584 000 Ft |
| Mobilinternet (12 hó) | 15 | 48 000 Ft | 720 000 Ft |
| **Folyó, évente** | | | **2 304 000 Ft** |

### 4.2 Rendelkezésre álló fedezet

| Forrás | Összeg |
|---|---:|
| Tartalékkeret szabad része | 4 431 000 Ft |
| Keretmozgástér (52 M − 50 743 e) | 1 257 000 Ft |
| Beszerzési megtakarítás | 1 490 000 Ft |
| **Összesen elérhető** | **7 178 000 Ft** |
| **Szükséges** | **8 325 000 Ft** |
| **Hiány** | **−1 147 000 Ft** |

**A fedezet nem elegendő** — és ez még csak az egyszeri költség; a folyó
2 304 000 Ft/év a következő évek IT-keretét terhelné.

### 4.3 Ütemhatás

| Tevékenység | Időigény |
|---|---:|
| Új beszerzési eljárás (15 készlet, 8 325 000 Ft → 3 ajánlat kell) | 3 hét |
| Szállítási idő | 6 hét (párhuzamosan futtatható) |
| 2 további oktatási csoport | 1 hét |
| +1 élesítési hullám | 1 hét |
| **Nettó eltolódás a kritikus úton** | **+3 hét** |

**Érintett mérföldkövek:** M7 (06.12. → 07.03.) és M10 (06.30. → 07.21.).

### 4.4 Kockázathatás

| # | Kockázat | Hatás |
|---|---|---|
| R1 | Laptopszállítás csúszik | **súlyosbodik** — új eljárás, új szállítási határidő, ezúttal puffer nélkül |
| R4 | Belső kapacitáshiány | **súlyosbodik** — Szabó Márk terhelése júliusban is megmarad |
| R12 | Service Desk kapacitás | **súlyosbodik** — 15 további felhasználó a hypercare alatt |

### 4.5 Minőséghatás

Nincs. Az átvételi kritériumok változatlanok maradnának, csak nagyobb körre.

### 4.6 Hatókörhatás

**Három korlátot sértene:**

| # | Korlát | Sértés |
|---|---|---|
| L1 | A projektnek 2026.06.30-ig le kell zárulnia | +3 hét eltolódás |
| L2 | A költségkeret 52 000 000 Ft, nem növelhető | −1 147 000 Ft hiány |
| L4 | A pilot köre 50 fő, Steering-döntés nélkül nem bővíthető | a kérés maga |

### 4.7 Közvetett hatások

| Mit | Hatás |
|---|---|
| Újratesztelés | Nem szükséges (azonos konfiguráció) |
| Oktatás | +2 csoport, +8 óra oktatói idő |
| Dokumentáció | Az as-built és a Run-book frissítése |
| Kommunikáció | +1 kommunikációs kör; a kimaradók köre újra változik |
| **Mérés** | **A T0 baseline 50 főre készült.** 65 fővel az összehasonlítás torzul, vagy a baseline-t újra kellene mérni — ami már nem lehetséges |

> **A 4.7 utolsó sora volt a döntő szakmai érv.** A haszonrealizálási mérés
> teljes rendszere az 50 fős körre és annak T0 adataira épül. A kör
> megváltoztatása menet közben **a mérést tenné értelmezhetetlenné** — vagyis
> pont azt a döntési alapot rombolná le, amiért a pilot egyáltalán elindult.

## 5. Alternatívák

| # | Alternatíva | Értékelés |
|---|---|---|
| A1 | A 15 fő bevonása a pilotba | A fenti hatásokkal — nem javasolt |
| A2 | **A 15 fő a kiterjesztési szakasz első hulláma** | **Javasolt.** A PIR (2026.10.09.) után, a pilot tapasztalataival, olcsóbban és biztonságosabban |
| A3 | 15 fő helyett 5 fő bevonása | A fedezet elég lenne (2 775 000 Ft), de az ütemhatás (+2 hét) és a mérés torzulása marad |

## 6. A projektmenedzser javaslata

**ELUTASÍTÁS**, az A2 alternatíva felajánlásával.

**Indoklás:** a kérés szakmailag megalapozott, de három jóváhagyott korlátot
sértene, a fedezet 1 147 000 Ft-tal hiányzik, és — a legfontosabb — a
haszonrealizálási mérés alapját tenné tönkre. A 15 fő igénye a kiterjesztési
szakaszban, jobb feltételekkel kielégíthető.

## 7. Döntés

| | |
|---|---|
| **Döntéshozó** | Projekt Irányító Bizottság |
| **Dátum** | 2026.06.03. |
| **Döntés** | **ELUTASÍTVA** |
| **Indoklás** | A Bizottság a projektmenedzser javaslatát elfogadta. A 15 fő a kiterjesztési szakasz első hulláma lesz, a PIR eredményének függvényében. |
| **Kiegészítés** | Horváth Júlia kérésére Papp Zsófia személyes tájékoztatást kap az indokokról (megtörtént 2026.06.05-én). |
| **Baseline frissítve** | **Nem szükséges** — a kérelem elutasításra került |
| **Döntésnapló** | D-19 |

---

# VK-02 — Hypercare támogatás bővítése *(rövidített)*

| | |
|---|---|
| Benyújtó | Kiss Réka, Service Desk vezető, 2026.05.28. |
| Kérés | +1 Service Desk munkatárs a hypercare 3 hetére |
| Indok | A kapacitásbecslés szerint a 2 fő nem elég a 3. hullám utáni terhelésre (R12 kockázat) |
| **Költséghatás** | **0 Ft** — belső átcsoportosítás, nem új felvétel |
| Ütemhatás | 0 nap |
| Kockázathatás | R12 besorolása 4 → 2 |
| Hatókörhatás | Nincs |
| Közvetett hatás | Az érintett munkatárs 3 hétig nem végzi a szokásos feladatait — a Service Desk belső ügye |
| PM javaslata | **Jóváhagyás** |
| **Döntés** | **JÓVÁHAGYVA** — Nagy Péter, 2026.06.01. (erőforrás-hatáskör) |
| Baseline frissítve | Nem szükséges (nincs költség- és ütemhatás) |
| Döntésnapló | D-20 |

---

# VK-03 — Monitorcsere az adapteres felhasználóknál *(rövidített)*

| | |
|---|---|
| Benyújtó | Fodor Gábor, területvezető, 2026.06.01. |
| Kérés | A 14 adapteres felhasználónál az irodai monitor cseréje új, HDMI-s példányra |
| Indok | „Az adapter esztétikailag zavaró és kilazulhat" |
| **Mi történik, ha nem valósul meg?** | *(a benyújtó nem töltötte ki)* |
| Költséghatás | +910 000 Ft (14 × 65 000 Ft) |
| Ütemhatás | +2 hét (új beszerzés) |
| PM javaslata | **Elutasítás.** Az adapterek működnek (AK-11 megfelelt, 50/50); a 182 000 Ft-os megoldás már megvalósult. A csere 910 000 Ft-ot és 2 hetet igényelne funkcionális nyereség nélkül. |
| **Döntés** | **ELUTASÍTVA** — Tóth Gergő, PM-hatáskörben, 2026.06.03. |
| Döntésnapló | D-21 |

> **Figyeld meg a 3. mezőt:** a benyújtó nem tudta megmondani, mi történik a
> kérés nélkül. Ez a leggyakoribb jele annak, hogy „jó lenne, ha" típusú
> kérésről van szó — és pont ezekből áll össze a hatókör-elszivárgás.

---

# VK-04 — Feltételes keret a H-06 hiba kezelésére *(rövidített)*

| | |
|---|---|
| Benyújtó | Nagy Péter, IT osztályvezető, 2026.06.17. |
| Kérés | 240 000 Ft elkülönítése a tartalékból: ha a mobilszolgáltatói egyeztetés nem hoz eredményt, 2 fő fix internet-hozzájárulást kap 12 hónapra |
| Indok | A H-06 hiba (videóhívás megszakadása) és az AK-19 nem teljesülése; az UAT-elfogadásban rögzített kezelési terv |
| Költséghatás | 240 000 Ft, **feltételesen**, a tartalékból |
| Ütemhatás | 0 nap (a projekt utáni időszakot érinti) |
| PM javaslata | **Feltételes jóváhagyás.** A keret elkülönítve, felhasználás csak akkor, ha a szolgáltatói egyeztetés 2026.07.31-ig nem hoz eredményt. |
| **Döntés** | **JÓVÁHAGYVA feltételesen** — Tóth Gergő, PM-hatáskörben (≤1 M Ft), 2026.06.17. |
| Tartalék hatása | Szabad tartalék: 4 431 000 → **4 191 000 Ft** |
| Baseline frissítve | Költségvetés v1.1, 2026.06.18. |
| Döntésnapló | D-22 |

---

> **Kapcsolódó dokumentumok:** bemenete a *Változáskezelési eljárás*;
> kimenete a *Változásnapló*, az *Ütemterv*, a *Költségvetés* és a
> *Hatókör-nyilatkozat*.
