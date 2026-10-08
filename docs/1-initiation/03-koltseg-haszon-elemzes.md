# Költség-haszon elemzés (Cost-Benefit Analysis)

**Dokumentum azonosítója:** XYO-CP-003\
**Projekt:** Xyo Cloud Pilot\
**Készült:** 2025. december 12.\
**Készítette:** Tóth Gergő, projektmenedzser\
**Pénzügyi ellenőrzés:** Balogh Tamás, kontroller\
**Verzió:** 1.1

> Ez a dokumentum az *Üzleti indoklás* pénzügyi részének kibontása. Azért készült
> külön, mert a keretösszeg meghaladja a 25 M Ft-ot, amelynél a gazdasági
> igazgatóság háromévi kitekintésű számítást kér.

---

## 1. Számítási alapfeltevések

| Feltevés | Érték | Forrás |
|---|---|---|
| Vizsgált időtáv | 3 év (2026–2028) | Kontrolling előírás |
| Vizsgált létszám | 50 fő (a pilot köre) | Projekt ötlet |
| Laptop élettartam | 4 év | IT eszközpolitika |
| Asztali gép élettartam | 5 év | IT eszközpolitika |
| Diszkontálás | nem alkalmazunk (3 éves táv, kontrolling döntés) | Balogh Tamás, 2025.12.10. |
| Licencár-emelkedés | évi 5% | CSP partner tájékoztatása |
| Belső munkaóra elszámolási ára | 6 500 Ft / óra | Kontrolling |

> **Fontos:** a belső munkaidőt nem szerepeltetjük költségként, mert a kontrolling
> nem terheli a projektre. A megtakarított munkaóra viszont hasznként megjelenik,
> **jelzett módon**, hogy a két oldal ne keveredjen.

## 2. Költségek — a javasolt megoldás (3. lehetőség)

### 2.1 Egyszeri (CAPEX jellegű) költségek — 2026

| Tétel | Összeg |
|---|---:|
| Laptop, 50 db | 21 000 000 Ft |
| Dokkoló, 50 db | 2 250 000 Ft |
| Otthoni monitor, 50 db | 3 250 000 Ft |
| Headset, 50 db | 1 250 000 Ft |
| Bevezetési szolgáltatás (CSP partner) | 6 500 000 Ft |
| Oktatás és változáskezelés | 1 200 000 Ft |
| **Összesen** | **35 450 000 Ft** |

### 2.2 Folyó (OPEX) költségek

| Tétel | 2026 | 2027 | 2028 |
|---|---:|---:|---:|
| M365 Business Premium (50 fő) | 5 280 000 Ft | 5 544 000 Ft | 5 821 000 Ft |
| Azure infrastruktúra és VPN Gateway | 3 000 000 Ft | 3 150 000 Ft | 3 308 000 Ft |
| Mobilinternet-hozzájárulás | 2 400 000 Ft | 2 400 000 Ft | 2 400 000 Ft |
| **Összesen** | **10 680 000 Ft** | **11 094 000 Ft** | **11 529 000 Ft** |

### 2.3 Tartalékkeret

| | |
|---|---:|
| Tartalék (a részösszeg 10%-a) | 4 613 000 Ft |
| Felhasználási szabály | 1 000 000 Ft-ig a projektmenedzser dönt; e felett a szponzor |

### 2.4 Teljes költség 3 évre

| | 2026 | 2027 | 2028 | Összesen |
|---|---:|---:|---:|---:|
| Egyszeri | 35 450 000 Ft | — | — | 35 450 000 Ft |
| Folyó | 10 680 000 Ft | 11 094 000 Ft | 11 529 000 Ft | 33 303 000 Ft |
| Tartalék | 4 613 000 Ft | — | — | 4 613 000 Ft |
| **Összesen** | **50 743 000 Ft** | **11 094 000 Ft** | **11 529 000 Ft** | **73 366 000 Ft** |

## 3. Költségek — a viszonyítási alap (2. lehetőség: hagyományos gépcsere)

| | 2026 | 2027 | 2028 | Összesen |
|---|---:|---:|---:|---:|
| Egyszeri (gép, monitor, szerver, bevezetés) | 27 550 000 Ft | — | — | 27 550 000 Ft |
| Üzemeltetés (fájlszerver, mentés, energia, támogatás) | 7 600 000 Ft | 7 828 000 Ft | 8 063 000 Ft | 23 491 000 Ft |
| **Összesen** | **35 150 000 Ft** | **7 828 000 Ft** | **8 063 000 Ft** | **51 041 000 Ft** |

## 4. Összevetés

| | Felhő (3. lehetőség) | Hagyományos (2. lehetőség) | Különbözet |
|---|---:|---:|---:|
| 2026 | 50 743 000 Ft | 35 150 000 Ft | +15 593 000 Ft |
| 2027 | 11 094 000 Ft | 7 828 000 Ft | +3 266 000 Ft |
| 2028 | 11 529 000 Ft | 8 063 000 Ft | +3 466 000 Ft |
| **3 év összesen** | **73 366 000 Ft** | **51 041 000 Ft** | **+22 325 000 Ft** |

**A felhős megoldás három év alatt 22,3 M Ft-tal drágább.** Ezt nyíltan ki kell
mondani: a projekt **nem költségmegtakarítási projekt**.

## 5. A hasznok pénzben kifejezve

Az alábbi hasznok abból származnak, hogy a támogatási terhelés csökken és a
folyamatok gyorsulnak. Belső munkaidő-megtakarításról van szó, ezért **elkülönítve**
szerepeltetjük.

| Haszon | Számítás | Éves érték |
|---|---|---:|
| Kevesebb helpdesk ticket | 372 ticket/év × 1,2 óra × 6 500 Ft | 2 901 600 Ft |
| Rövidebb megoldási idő a maradék ticketeknél | 868 ticket × 0,8 óra megtakarítás × 6 500 Ft | 4 513 600 Ft |
| Gyorsabb gépbeüzemelés | 15 gép/év × 5 óra × 6 500 Ft | 487 500 Ft |
| Gyorsabb belépő-folyamat | 8 belépő/év × 2,5 nap × 8 óra × 6 500 Ft | 1 040 000 Ft |
| Elmaradó adatvesztési helyreállítás | 3 eset/év × 12 óra × 6 500 Ft | 234 000 Ft |
| **Összesen** | | **9 176 700 Ft / év** |

> **Óvatosság:** ezek **kapacitás-felszabadulások**, nem pénzbeli megtakarítások.
> A felszabaduló idő csak akkor válik valódi haszonná, ha azt más értékteremtő
> feladatra fordítjuk. A kontrolling ezért nem számolja el megtakarításként —
> jelen elemzésben tájékoztató jellegű.

## 6. Megtérülés

| | Érték |
|---|---:|
| 3 éves többletköltség a hagyományoshoz képest | 22 325 000 Ft |
| 3 éves kapacitás-haszon (2027-től teljes évben, 2026-ban fél évre) | 22 941 750 Ft |
| **Egyenleg 3 év alatt** | **+616 750 Ft** |

**Egyszerű megtérülési idő:** kb. **2 év 11 hónap** — vagyis a projekt a harmadik
év végére fordul pozitívba, *ha* a felszabaduló kapacitást hasznosítjuk.

**Ezt tehát nem lehet megtérülési projektként eladni.** Az érv a rugalmasság,
a home office lehetőség, a biztonsági szint emelkedése és a jövőbeli kiterjeszthetőség.

## 7. Érzékenységvizsgálat

| Forgatókönyv | Változás | 3 éves egyenleg |
|---|---|---:|
| Alapeset | — | +617 000 Ft |
| Hardver 20%-kal drágább | +5 550 000 Ft | −4 933 000 Ft |
| Licencár 10%/év emelkedéssel | +1 108 000 Ft | −491 000 Ft |
| A ticketcsökkenés csak 15% (nem 30%) | −4 800 000 Ft haszon | −4 183 000 Ft |
| Kedvező: a kiterjesztés 2028-ban megtörténik | a fajlagos költség csökken | jelentősen pozitív |

**Következtetés:** a számítás **érzékeny a hardverárra és a ticketcsökkenés
mértékére**. Mindkettőt kötelező mérni a hatodik fázisban — a hardverárat a
beszerzési eljárás, a ticketcsökkenést a Service Desk adatai igazolják.

## 8. Következtetés és javaslat

A projekt pénzügyileg **nagyjából nullszaldós** hároméves távon. A döntést nem a
megtérülés, hanem három tényező indokolja:

1. A gépcsere elkerülhetetlen — a kérdés csak az, milyen modellre költünk.
2. A home office lehetőség munkaerő-megtartási értéke a számításban nem szerepel.
3. A pilot **döntési opciót vásárol**: 50 M Ft-ért megtudjuk, érdemes-e 230 M Ft-ot
   költeni a teljes szervezetre.

Javasoljuk a 3. lehetőség elfogadását, azzal a feltétellel, hogy a hatodik fázis
mérései tényadatot szolgáltatnak a kiterjesztési döntéshez.

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2025.12.12. |
| Pénzügyileg ellenőrizte | Balogh Tamás, kontroller | 2025.12.16. |

> **Kapcsolódó dokumentumok:** bemenete az *Üzleti indoklás*; kimenete a
> *Projektalapító okirat* és a *Költségvetés*.
