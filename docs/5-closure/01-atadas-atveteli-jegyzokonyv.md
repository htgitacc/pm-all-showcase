# Átadás-átvételi jegyzőkönyv (Final Acceptance Certificate)

**Dokumentum azonosítója:** XYO-CP-401\
**Projekt:** Xyo Cloud Pilot\
**Dátum:** **2026. június 26.** (M9 mérföldkő)\
**Helyszín:** Xyo Kft. központi iroda, kistárgyaló\
**Átadó:** Tóth Gergő, projektmenedzser\
**Átvevő:** Nagy Péter, IT osztályvezető

> **Ez az egyetlen bizonyíték arra, hogy teljesítettél.** Az átvételi
> kritériumokat **egyesével** vezetjük végig — a „minden rendben" típusú
> átvétel vita esetén semmit nem bizonyít.

---

## 1. A szállított eredmények

| # | Szállítandó eredmény | Mennyiség / állapot | Átvéve |
|---|---|---|:-:|
| D1 | Beüzemelt, Autopilot-regisztrált munkaállomás-készlet | 50 db (laptop, dokkoló, monitor, headset) | ✔ |
| D2 | Konfigurált Entra ID környezet MFA-val és feltételes hozzáféréssel | 50 fiók, 5 CA-szabály | ✔ |
| D3 | Intune eszközfelügyelet, eszközprofilok és alkalmazáscsomagok | 4 profil, 5 alkalmazáscsomag | ✔ |
| D4 | SharePoint csapatoldalak és OneDrive tárhely | 6 csapatoldal + CP-Kozos, 50 OneDrive | ✔ |
| D5 | Azure VPN Gateway működő klienskapcsolattal | VpnGw1, 3 elérhető erőforrás | ✔ |
| D6 | As-built konfigurációs dokumentáció | XYO-CP-206 v1.4, 100% | ✔ |
| D7 | Oktatási anyag, gyorssegédlet, megtartott oktatások | 50/50 fő, 6 alkalom | ✔ |
| D8 | Lezárt UAT, aláírt átvételi elfogadás | XYO-CP-208, 2026.06.19. | ✔ |
| D9 | Üzemeltetésbe adási dokumentáció (Run-book) | XYO-CP-402 | ✔ |
| D10 | KPI-adatlapok és a mérési felelősségek átadása | 12 mérőszám, nevesített felelősökkel | ✔ |

**Mind a 10 szállítandó eredmény átadásra került.**

## 2. Az átvételi kritériumok tételes végigvezetése

| # | Kritérium | Elvárás | Tény | Eredmény |
|---|---|---|---|:-:|
| AK-01 | Mind az 50 felhasználó belép Entra ID-val | 50/50 | 50/50 | **megfelelt** |
| AK-02 | MFA-lefedettség | 100% | 100% | **megfelelt** |
| AK-03 | Break-glass fiók dokumentált és tesztelt | igen | 2 fiók, tesztelve 05.06. és 06.18. | **megfelelt** |
| AK-04 | Hozzáférés-visszavonás | ≤ 15 perc | 8 perc | **megfelelt** |
| AK-05 | Önkiszolgáló jelszó-visszaállítás | 5 fő sikeresen | 5/5 | **megfelelt** |
| AK-06 | Autopilot beüzemelés | ≤ 1,5 óra | 1 óra 22 perc | **megfelelt** |
| AK-07 | Bekapcsolástól bejelentkezésig | ≤ 90 mp | 71 mp | **megfelelt** |
| AK-08 | Lemeztitkosítás | 50/50 | 50/50 | **megfelelt** |
| AK-09 | Alapszoftverek és biztonsági frissítések automatikus telepítése | 50/50 | 50/50 | **megfelelt** |
| AK-10 | Nincs magánhasználati adatgyűjtés | DPO igazolás | dr. Fekete Zsolt, 2026.05.07. | **megfelelt** |
| AK-11 | Monitor csatlakoztatható | 50/50 | 50/50 (36 közvetlen, 14 adapterrel) | **megfelelt** |
| AK-12 | OneDrive elérése | 50/50 | 50/50 | **megfelelt** |
| AK-13 | SharePoint jogosultsági teszt | 6 csapat × 2 | 12/12 | **megfelelt** |
| AK-14 | 30 napos visszaállíthatóság | igen | 30 + 30 nap | **megfelelt** |
| AK-15 | Teljes könyvtár visszaállítása | tesztelt | sikeres, 42 perc | **megfelelt** |
| AK-16 | Régi fájlszerver olvasása VPN-en | 3 csapat | 14/14 fő | **megfelelt** |
| AK-17 | VPN otthoni mobilnetről | 10/10 | 10/10 | **megfelelt** |
| AK-18 | 2 belső rendszer elérése VPN-en | igen | igen | **megfelelt** |
| **AK-19** | **30 perces videóhívás mobilneten** | **5/5** | **3/5** | **NEM FELELT MEG** |
| AK-20 | Oktatáson részt vettek | 50/50 | 50/50 | **megfelelt** |
| AK-21 | Gyorssegédlet elkészült | igen | 4 oldal, magyar, képernyőképes | **megfelelt** |
| AK-22 | Service Desk útmutató ≥ 2 héttel az élesítés előtt | ≤ 04.27. | 04.27. | **megfelelt** |
| AK-23 | Az as-built alapján az üzemeltetés átveheti | igen | lásd 5. pont | **megfelelt** |
| AK-24 | UAT tesztesetek megfelelése | ≥ 95% | 96,3% | **megfelelt** |
| AK-25 | Nincs nyitott S1 hiba | 0 | 0 | **megfelelt** |
| AK-26 | Nyitott S2 hibákhoz elfogadott határidő | igen | igen | **megfelelt** |

**Eredmény: 25 kritérium megfelelt, 1 nem felelt meg.**

### Az AK-19 kezelése

| | |
|---|---|
| **Mi nem teljesült** | 2 tesztelőnél a 30 perces videóhívás mobilneten megszakadt |
| **Ok** | A lakóhelyükön gyenge a mobilszolgáltatói lefedettség — **nem a megoldás hibája** |
| **Kapcsolódó követelmény** | K23, **F prioritású** (fontos, de nem kötelező) |
| **Elfogadott kezelés** | Egyeztetés a mobilszolgáltatóval; ha nem javul, fix internet-hozzájárulás 2 főnek 12 hónapra |
| **Elkülönített fedezet** | **240 000 Ft** a tartalékkeretből (VK-04, feltételes jóváhagyás) |
| **Határidő** | 2026.07.31. |
| **Felelős** | Nagy Péter, IT osztályvezető |
| **Az átvevő döntése** | **Az átvételt nem akadályozza.** A kezelésre elfogadott terv, fedezet, határidő és felelős van. |

## 3. Nyitva maradt hibák — az átvevő által elfogadva

| # | Hiba | Szint | Kezelés | Határidő | Felelős |
|---|---|:-:|---|---|---|
| H-06 | Videóhívás megszakadása mobilneten (2 fő) | S2 | Szolgáltatói egyeztetés, majd fix internet | 2026.07.31. | Nagy Péter |
| H-08 | Alkalmazásportál hiányos magyar felirata | S3 | Szállítói szolgáltatásfrissítés (szavatosság alatt) | 2026.09.30. | Cloudia Solutions |
| H-09 | Authenticator értesítés késése | S3 | Szolgáltatói jelenség, figyelés alatt | folyamatos | Szabó Márk |
| H-13 | Alkalmazásportál ikon nem céges | S4 | Üzemeltetési feladat | — | Szabó Márk |

**Nyitott S1 (kritikus) hiba nincs.**

## 4. Egyéb nyitott pontok az átvételkor

| # | Nyitott pont | Határidő | Felelős |
|---|---|---|---|
| NY-1 | A hypercare időszak lezárása (kilépési feltétel teljesülése) | 2026.07.03. | Kiss Réka |
| NY-2 | A régi asztali gépek selejtezése (a 3 feltétel teljesülése után) | várhatóan 2026.07.10. | Nagy Péter |
| NY-3 | A Cloudia Solutions adminisztrátori hozzáférésének megszűnése | **ellenőrizve: 2026.06.19-én megszűnt** | Szabó Márk |
| NY-4 | A 2. évtől jelentkező folyó költség gazdája | 2026.06.30. | Balogh Tamás |
| NY-5 | A mérési szakasz lebonyolítása | 2026.09.30. | Nagy Péter |

## 5. Az átvevő nyilatkozata

> Alulírott Nagy Péter, a Xyo Kft. IT osztályvezetője nyilatkozom, hogy a
> Xyo Cloud Pilot projekt eredményeit **átvettem**.
>
> Nyilatkozom, hogy az **as-built konfigurációs dokumentációt (XYO-CP-206) és
> az üzemeltetésbe adási dokumentációt (Run-book, XYO-CP-402) átolvastam**, és
> azok alapján az üzemeltetés a megoldást önállóan üzemeltetni tudja.
>
> A 3. pontban felsorolt nyitott hibákat és a 4. pontban felsorolt nyitott
> pontokat ismerem és elfogadom, a megjelölt határidőkkel és felelősökkel.

> **Ez a mondat nem formalitás.** Az „aláírom, majd megnézem" átadás semmit
> nem ér — két hét múlva visszahívják a projektcsapatot. Nagy Péter az
> átadás-átvételi egyeztetés előtt 3 nappal megkapta a dokumentációt, és az
> egyeztetésen tételesen végigmentünk rajta.

## 6. Aláírások

| Szerep | Név | Mit igazol | Aláírás | Dátum |
|---|---|---|---|---|
| **Átvevő** | **Nagy Péter**, IT osztályvezető | A megoldás üzemeltethető, a dokumentáció elegendő | | 2026.06.26. |
| **Felhasználói képviselő** | **Fodor Gábor**, területvezető | A megoldás a valós napi munkára alkalmas (UAT, 06.19.) | | 2026.06.26. |
| **Átadó** | **Tóth Gergő**, projektmenedzser | A vállalt hatókör teljesült | | 2026.06.26. |
| Jelen volt | Szabó Márk, rendszergazda | | | 2026.06.26. |
| Jelen volt | Kiss Réka, Service Desk vezető | | | 2026.06.26. |

---

## 7. Az átadással átkerülő felelősség

**2026.06.26-tól** a megoldás üzemeltetése, a hibakezelés és a felhasználói
támogatás az IT osztály felelőssége. A projektszervezet ettől a naptól nem
felel a működésért.

**Kivételek — ami a projektnél marad 2026.06.30-ig:**

- A projektzáró jelentés és a pénzügyi zárás elkészítése
- A mérési felelősségek formális átadása (NY-5)
- A tanulságok rögzítése

---

> **Kapcsolódó dokumentumok:** bemenete a *Minőségterv*, az *UAT-elfogadás*,
> a *Teljesítésigazolás* és a *Minőségellenőrzési jegyzőkönyv*; kimenete a
> *Projektzáró jelentés* és az *Üzemeltetésbe adás (Run-book)*.
