# Üzleti indoklás (Business Case)

**Dokumentum azonosítója:** XYO-CP-002\
**Projekt munkaneve:** Xyo Cloud Pilot\
**Készült:** 2025. december 5.\
**Készítette:** Tóth Gergő, projektmenedzser\
**Jóváhagyó:** Kovács Anita, gazdasági igazgató (szponzor)\
**Verzió:** 1.2 — jóváhagyva 2025.12.18.

---

## 1. Vezetői összefoglaló

A Xyo Kft. 50 asztali gépe elavult, a garancia a többségnél lejárt, és a csere a
következő két évben mindenképp esedékes. A cseréhez két út vezet: a jelenlegi modell
megismétlése (asztali gép + fájlszerver), vagy a váltás felhőalapú munkakörnyezetre.

Javasoljuk a **3. lehetőséget: 50 fős felhőalapú pilot Microsoft 365 alapokon**,
50 743 000 Ft tervezett költséggel, 2026. február – június között, majd egy
3 hónapos mérési szakasszal.

A megoldás **az első évben nem olcsóbb** a jelenlegi modellnél — a haszon a
rugalmasságban, a támogatási terhelés csökkenésében és a 3. évtől jelentkező
költségelőnyben van. A pilot valódi hozadéka azonban a **döntési alap**: tényadat
arról, hogy a modell kiterjeszthető-e a teljes, 240 fős szervezetre.

## 2. A jelenlegi helyzet számokban

### 2.1 Éves üzemeltetési költség (a pilot körre vetítve)

| Tétel | Éves költség |
|---|---:|
| Fájlszerver amortizáció és karbantartás | 3 200 000 Ft |
| Mentési rendszer és médiaköltség | 900 000 Ft |
| Szerverterem energia és hűtés (arányos rész) | 1 100 000 Ft |
| Külső támogatási szerződés | 2 400 000 Ft |
| **Összesen** | **7 600 000 Ft / év** |

### 2.2 Működési mutatók (2025. teljes év, a pilot köre)

| Mutató | Érték |
|---|---:|
| Helpdesk ticketek száma | 1 240 db / év (kb. 103 db / hó) |
| Ebből hozzáférés / jelszó | 41% |
| Ebből fájlszerver-elérési probléma | 22% |
| Ebből hardverhiba | 18% |
| Átlagos megoldási idő (MTTR) | 11,4 óra |
| Egy gép beüzemelésének ideje | 6,5 óra |
| Új belépő munkába állásáig eltelt idő | 3,5 munkanap |
| Home office napok aránya | 0% (nincs technikai lehetőség) |
| Adatvesztéssel járó eset 2025-ben | 3 db |

### 2.3 Elkerülhetetlen kiadás

A géppark cseréje **a döntéstől függetlenül** esedékes: 50 gép, 2 éven belül.
Ez a beruházás minden vizsgált lehetőségben szerepel — a különbség az, hogy
asztali gépet vagy laptopot veszünk.

## 3. Vizsgált lehetőségek

### 1. lehetőség — Ne csináljunk semmit

A gépeket addig használjuk, amíg működnek, hibánként cserélve.

| | |
|---|---|
| Egyszeri költség | 0 Ft |
| Éves költség | 7 600 000 Ft üzemeltetés + növekvő hibaköltség |
| Előny | Nincs beruházás, nincs változás |
| Hátrány | A hibák és a leállások száma nő; a garancia nélküli gépek javítása drága; a home office igény kezeletlen marad; 2 éven belül kényszerhelyzetben, rosszabb feltételekkel kell dönteni |
| **Értékelés** | **Nem javasolt** — csak a döntés elhalasztása, magasabb áron |

### 2. lehetőség — Hagyományos gépcsere, a jelenlegi modell megtartásával

50 új asztali gép, a fájlszerver megtartásával és a szerver cseréjével.

| | |
|---|---:|
| Asztali gépek (50 × 340 000 Ft) | 17 000 000 Ft |
| Monitor csere (50 × 65 000 Ft) | 3 250 000 Ft |
| Fájlszerver csere és mentési rendszer | 5 800 000 Ft |
| Bevezetés, munkadíj | 1 500 000 Ft |
| **Egyszeri összesen** | **27 550 000 Ft** |
| Éves üzemeltetés (változatlan) | 7 600 000 Ft |

| | |
|---|---|
| Előny | Ismert modell, alacsonyabb egyszeri költség, nincs tanulási görbe |
| Hátrány | A home office igény továbbra sem megoldott; a támogatási terhelés nem csökken; a modell további 5-6 évre rögzül; a kiterjesztés kérdése megválaszolatlan marad |
| **Értékelés** | **Nem javasolt** — nem old meg egyetlen üzleti problémát sem |

### 3. lehetőség — Felhőalapú pilot 50 főre *(javasolt)*

Laptop + Microsoft 365 Business Premium + Entra ID + Intune + SharePoint/OneDrive
+ Azure VPN, home office lehetőséggel.

| | |
|---|---:|
| Egyszeri és első éves költség | 50 743 000 Ft (részletezés a 4. pontban) |
| Ebből tartalék | 4 613 000 Ft |
| 2. évtől folyó költség | 10 680 000 Ft / év |

| | |
|---|---|
| Előny | Home office mindenkinek; a fájlszerver-függőség megszűnik; automatizált gépbeüzemelés; egységes azonosítás és MFA; mérhető döntési alap a kiterjesztéshez |
| Hátrány | Magasabb egyszeri költség; új kompetencia szükséges; a folyó előfizetési költség a projekt után is fut |
| **Értékelés** | **Javasolt** |

### 4. lehetőség — Azonnali, teljes körű bevezetés 240 főre

| | |
|---|---|
| Előny | Egy lépésben megtörténik az átállás |
| Hátrány | Kb. 230 M Ft egyszeri költség; nincs tapasztalat; a hibák a teljes szervezetet érintik; a szervezeti kapacitás nem elegendő |
| **Értékelés** | **Nem javasolt** — kockázata aránytalanul nagy tapasztalat nélkül |

## 4. A javasolt megoldás költsége

| Tétel | Menny. | Egységár | Összesen |
|---|---:|---:|---:|
| Laptop (üzleti kategória, i5 / 16 GB / 512 GB) | 50 | 420 000 Ft | 21 000 000 Ft |
| Dokkoló és tápegység | 50 | 45 000 Ft | 2 250 000 Ft |
| Monitor otthoni munkavégzéshez (24" FHD) | 50 | 65 000 Ft | 3 250 000 Ft |
| Headset | 50 | 25 000 Ft | 1 250 000 Ft |
| Microsoft 365 Business Premium (12 hónap) | 50 | 105 600 Ft | 5 280 000 Ft |
| Azure infrastruktúra és VPN Gateway (12 hónap) | 1 | 3 000 000 Ft | 3 000 000 Ft |
| Mobilinternet-hozzájárulás (12 hónap) | 50 | 48 000 Ft | 2 400 000 Ft |
| Bevezetési szolgáltatás (CSP partner) | 1 | 6 500 000 Ft | 6 500 000 Ft |
| Oktatás és változáskezelés | 1 | 1 200 000 Ft | 1 200 000 Ft |
| **Részösszeg** | | | **46 130 000 Ft** |
| Tartalékkeret (10%) | | | 4 613 000 Ft |
| **Mindösszesen** | | | **50 743 000 Ft** |

**Rendelkezésre álló keret:** 52 000 000 Ft — a mozgástér 1 257 000 Ft.

**A 2. évtől jelentkező folyó költség:** M365 licenc 5 280 000 Ft + Azure/VPN
3 000 000 Ft + mobilinternet 2 400 000 Ft = **10 680 000 Ft / év.**
Ezzel szemben megszűnik a jelenlegi 7 600 000 Ft/év üzemeltetési költség.
A különbözet **+3 080 000 Ft / év** — ez a rugalmasság és a támogatáscsökkenés ára.

> **Megjegyzés a monitorokról:** az irodai monitorok a cégnél rendelkezésre állnak,
> ezért csak az **otthoni** második monitorral számolunk. A mobilinternet a dolgozói
> csomagokban korlátlan; a cég a havi hozzájárulást vállalja át.

## 5. Várt hasznok

| Haszon | Mérőszám | Jelenlegi (T0) | Célérték (T+3 hó) |
|---|---|---:|---:|
| Csökkenő támogatási terhelés | Ticket / hó | 103 | ≤ 72 (−30%) |
| Gyorsabb hibaelhárítás | MTTR (óra) | 11,4 | ≤ 6,0 |
| Gyors gépbeüzemelés | óra / gép | 6,5 | ≤ 1,5 |
| Rugalmas munkavégzés | Home office napok aránya | 0% | ≥ 40% |
| Gyorsabb belépő-folyamat | munkanap | 3,5 | ≤ 1,0 |
| Biztonságosabb azonosítás | MFA-lefedettség | n. a. | 100% |
| Adatvesztés megszűnése | eset / év | 3 | 0 |
| Felhasználói elégedettség | 1–5 skála | 3,1 | ≥ 4,0 |

A mérés részletes módszertana a **Haszonrealizálási tervben** szerepel.

## 6. Fő kockázatok

| Kockázat | Hatás | Kezelés |
|---|---|---|
| A laptopszállítás csúszik | Az élesítés eltolódik | Korai beszerzésindítás; kötbér a szerződésben |
| A mobilinternet nem elegendő a napi munkához | A home office nem működik | Megvalósíthatósági tanulmányban mérés; szükség esetén fix internet-hozzájárulás |
| Adatvédelmi hatásvizsgálat szükséges | Csúszás a tervezésben | Korai DPO-egyeztetés, még a tervezési fázisban |
| Felhasználói ellenállás | Alacsony adaptáció | Oktatás, hypercare időszak, folyamatos kommunikáció |
| Belső kapacitáshiány (2 fő IT) | Csúszás | A bevezetést CSP partner végzi; írásos kapacitás-jóváhagyás |

## 7. Javaslat

Javasoljuk a **3. lehetőség** elfogadását: 50 fős felhőalapú pilot,
50 743 000 Ft tervezett költséggel, 2026.02.02 – 2026.06.30 között, majd
2026.07.01 – 2026.09.30 közötti mérési szakasszal, amelynek végén a Projekt
Irányító Bizottság dönt a kiterjesztésről.

---

## Jóváhagyás

| Szerep | Név | Dátum | Aláírás |
|---|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2025.12.05. | |
| Szakmai véleményező | Nagy Péter, IT osztályvezető | 2025.12.11. | |
| Pénzügyi ellenőrzés | Balogh Tamás, kontroller | 2025.12.15. | |
| Jóváhagyta | Kovács Anita, gazdasági igazgató | 2025.12.18. | |

> **Kapcsolódó dokumentumok:** bemenete a *Projekt ötlet*; kimenete a
> *Projektalapító okirat*, a *Költség-haszon elemzés* és a *Haszonrealizálási terv*.
