# Minőségellenőrzési jegyzőkönyv (Quality Control Report)

**Dokumentum azonosítója:** XYO-CP-307\
**Projekt:** Xyo Cloud Pilot\
**Készíti:** Nagy Péter, IT osztályvezető (szakmai vezető)\
**Nyilvántartja:** Tóth Gergő, projektmenedzser\
**Verzió:** 1.3

> **Nem csak az átvételkor ellenőrzünk** — az akkor talált hiba a legdrágább,
> és a határidőt is veszélyezteti. Ez a dokumentum a **szállítás közbeni**
> ellenőrzéseket rögzíti.
>
> **Az eredményt akkor is leírjuk, ha rendben volt.** A „nem találtunk hibát"
> is bizonyíték arra, hogy megnézted.

---

## 1. Ellenőrzési terv és teljesülés

| # | Mit ellenőrzünk | Tervezett | Tényleges | Eredmény |
|---|---|---|---|:-:|
| E-01 | SharePoint jogosultsági modell | 05.04. | 05.04. | ✔ megfelelt |
| E-02 | Entra ID és MFA konfiguráció | 05.06. | 05.06. | **⚠ eltéréssel** |
| E-03 | Intune profilok és Autopilot | 05.08. | 05.08. | **⚠ eltéréssel** |
| E-04 | Mentés, megőrzés, visszaállítás | 05.08. | 05.08. | ✔ megfelelt |
| E-05 | Hardver — 1. részszállítás | 05.05. | 05.05. | ✔ megfelelt |
| E-06 | Hardver — 2. részszállítás | 05.28. | 05.28. | **✖ hiánnyal** |
| E-07 | Hardver — hiánypótlás | — | 06.02. | ✔ megfelelt |
| E-08 | As-built dokumentáció készültsége | kéthetente | 05.11., 05.26., 06.08., 06.19. | ✔ megfelelt |

---

## 2. E-01 — SharePoint jogosultsági modell

| | |
|---|---|
| **Dátum** | 2026.05.04. |
| **Ellenőrizte** | Nagy Péter |
| **Módszer** | Jogosultsági teszt: 6 csapatoldal × 2 ellenőrzés (van-e hozzáférése a sajátjához; nincs-e a másikéhoz) |
| **Kapcsolódó kritérium** | AK-13 |

| Csapatoldal | Saját hozzáférés | Idegen hozzáférés tiltva | Eredmény |
|---|:-:|:-:|:-:|
| CP-Penzugy | ✔ | ✔ | megfelelt |
| CP-Ertekesites | ✔ | ✔ | megfelelt |
| CP-Logisztika | ✔ | ✔ | megfelelt |
| CP-Vezetoseg | ✔ | ✔ | megfelelt |
| CP-IT | ✔ | ✔ | megfelelt |
| CP-Kozos | ✔ | n. a. (mindenki) | megfelelt |

**Megállapítás: 12/12 ellenőrzés rendben. Eltérés nincs.**

---

## 3. E-02 — Entra ID és MFA konfiguráció

| | |
|---|---|
| **Dátum** | 2026.05.06. |
| **Ellenőrizte** | Szabó Márk, Nagy Péter jóváhagyásával |
| **Kapcsolódó kritériumok** | AK-02, AK-03, AK-05 |

| Ellenőrzési pont | Elvárás | Tapasztalat | Eredmény |
|---|---|---|:-:|
| MFA-lefedettség | 100% a regisztrált körben | 10/10 (az 1. hullám) | ✔ |
| Break-glass fiók | dokumentált és tesztelt | 2 fiók, tesztelve | ✔ |
| Feltételes hozzáférés jelentés-módban | 5 munkanap hiba nélkül | 5 nap, 0 kizárás | ✔ |
| **Önkiszolgáló jelszó-visszaállítás** | működik | **csak regisztrált MFA-módszerrel** | **⚠ eltérés** |

### Feltárt eltérés — QC-01

| | |
|---|---|
| **Leírás** | Az önkiszolgáló jelszó-visszaállítás nem használható az első belépés előtt, amíg az MFA nincs regisztrálva |
| **Súlyosság** | S3 (zavaró) |
| **Hatás** | A K27 követelmény részben nem teljesül |
| **Kezelés** | Elfogadott működés: az MFA regisztrációja **az oktatáson megtörténik**, tehát az első belépés előtti helyzet nem áll elő. Az oktatási tematika 2. blokkja 25-ről 30 percre bővült. |
| **Nyilvántartás** | Problémanapló P-03 |
| **Lezárva** | 2026.05.07. |

> **A jelentés-mód „5 nap, 0 kizárás" eredménye megtévesztő volt.**
> Az ellenőrzés formálisan megfelelt — a hiba (P-05) mégis bekövetkezett
> 5 nappal később, mert **a jelentés-mód irodai hálózaton futott**.
> Ez az ellenőrzés módszertani hibája volt, nem a konfigurációé.
> → Tanulságok naplója.

---

## 4. E-03 — Intune profilok és Autopilot

| | |
|---|---|
| **Dátum** | 2026.05.08. |
| **Ellenőrizte** | Szabó Márk |
| **Kapcsolódó kritériumok** | AK-06, AK-08, AK-09, AK-10 |

| Ellenőrzési pont | Elvárás | Mért érték | Eredmény |
|---|---|---|:-:|
| Lemeztitkosítás | 100% | 10/10 | ✔ |
| Alapszoftverek telepítése | 100% | 10/10 | ✔ |
| **Autopilot beüzemelési idő** | **≤ 1,5 óra** | **2 óra 06 perc / 2 óra 11 perc** | **⚠ eltérés** |
| Magánhasználati adatgyűjtés | nincs | dr. Fekete Zsolt tételes átnézése 05.07-én: nincs | ✔ |

### Feltárt eltérés — QC-02

| | |
|---|---|
| **Leírás** | Az Autopilot beüzemelés 2,1 óra a célzott 1,5 óra helyett |
| **Súlyosság** | S2 (súlyos) — átvételi kritériumot érint (AK-06) |
| **Ok** | Az összes alkalmazáscsomag kötelező, **telepítés-blokkoló** módban volt beállítva; a beüzemelés megvárta az ügyviteli rendszer kliensét is |
| **Kezelés** | Az ügyviteli kliens (14 főnek szükséges) átállítva opcionálisra, a portálról telepíthetőre (D-15) |
| **Újramérés** | 2026.05.20–21., 5 gépen (a Minőségterv szerint): 1:22, 1:18, 1:25, 1:20, 1:25 → **átlag 1 óra 22 perc** ✔ |
| **Nyilvántartás** | Problémanapló P-06, hibalista H-05 |
| **Lezárva** | 2026.05.21. (az újramérés után, nem a javítás napján) |

> **Ez az ellenőrzés térült meg a legjobban.** A hiba még a 10 tesztgépen
> derült ki (05.08.), **26 nappal a 2–3. hullám 40 gépe (06.03.) előtt**. A
> javítás 05.19-re elkészült, 05.21-én újramérve — a 40 gép már a javított
> folyamattal települt. Ha csak az átvételkor (06.19.) mérjük, az AK-06
> kritérium megbukik, és 50 gépet kellett volna újra beüzemelni.

---

## 5. E-04 — Mentés, megőrzés, visszaállítás

| | |
|---|---|
| **Dátum** | 2026.05.08. |
| **Ellenőrizte** | Szabó Márk |
| **Kapcsolódó kritériumok** | AK-14, AK-15 |
| **Kapcsolódó kockázat** | R7 |

| Teszt | Elvárás | Eredmény | Időigény |
|---|---|:-:|---:|
| Megőrzési szabály beállítva | ≥ 30 nap | 30 nap + 30 nap másodlagos lomtár | — |
| SharePoint verziókövetés | ≥ 50 verzió | 50 verzió | — |
| 1 törölt fájl visszaállítása | sikeres | ✔ sikeres | **2 perc** |
| **Teljes könyvtár visszaállítása** | sikeres | ✔ sikeres (1 240 fájl, 4,2 GB) | **42 perc** |

**Megállapítás: eltérés nincs.** A 42 perces visszaállítási időt
dokumentáltuk, mert üzemeltetési szempontból ez a lényeges információ:
incidens esetén ennyivel kell számolni. Átvezetve a Run-bookba.

> Az R7 kockázat („a felhő magától ment" tévhit) **nem következett be** —
> pontosan azért, mert a visszaállítási tesztet kötelezővé tettük a
> WBS-szótár kész-definíciójában.

---

## 6. E-06 — Hardver, 2. részszállítás

| | |
|---|---|
| **Dátum** | 2026.05.28. |
| **Ellenőrizte** | Szabó Márk |
| **Kapcsolódó kritériumok** | Sz-1 – Sz-5 (szerződéses) |

| Ellenőrzési pont | Elvárás | Tapasztalat | Eredmény |
|---|---|---|:-:|
| Mennyiség | 40 db teljes készlet | 40 laptop, 40 dokkoló, 40 monitor, 40 headset | ✔ |
| **Dokkoló tápkábel** | 40 db | **28 db** | **✖ 12 db hiány** |
| Autopilot-lista | 40/40 | 40/40 | ✔ |
| Monitor csatlakozó | HDMI/DP | 40/40 | ✔ |
| Gyári specifikáció | megfelelő | 5 db mintavételes | ✔ |

### Feltárt hiány — QC-03

| | |
|---|---|
| **Leírás** | 12 dokkoló dobozából hiányzott a tápkábel |
| **Súlyosság** | S2 |
| **Hatás** | 12 munkatárs dokkolója nem használható; a 3. élesítési hullám (06.10.) veszélyben |
| **Kezelés** | Átvétel **fenntartással**, tételes hiánylistával; a 80%-os fizetési részlet a pótlásig visszatartva (D-18) |
| **Pótlás** | 2026.06.02., 1 nappal a vállalt határidő előtt |
| **Újraellenőrzés** | E-07, 2026.06.02.: 12/12 megérkezett, 3 db mintavételesen tesztelve ✔ |
| **Nyilvántartás** | Problémanapló P-08, hibalista H-04 |
| **Lezárva** | 2026.06.02. |

---

## 7. E-08 — As-built dokumentáció készültsége

| Ellenőrzés | Készültség | Megállapítás |
|---|---:|---|
| 2026.05.11. | 25% | Entra ID és SharePoint rész elkészült |
| 2026.05.26. | 55% | Intune és VPN rész; **a CA-05 módosítás indoklása bekerült** |
| 2026.06.08. | 80% | Mentés, jogosultságok, naplózás |
| 2026.06.19. | 100% | Az „Eltérések a tervezett konfigurációtól" fejezet elkészült |

> **A kétheti ellenőrzés célja nem a tartalom minősítése volt, hanem hogy
> egyáltalán íródjon.** Ha csak a végén kérjük, a projekt utolsó hetében
> senki nem emlékszik, miért állítottak be valamit úgy, ahogy — és pont az
> az indoklás lesz később fontos.

---

## 8. Összesítés

| | Darab |
|---|---:|
| Elvégzett ellenőrzés | 8 |
| Eltérés nélkül megfelelt | 5 |
| Eltéréssel (kezelve és lezárva) | 3 |
| **Az átvételig lezáratlan eltérés** | **0** |

| Feltárt eltérés | Súlyosság | Ha csak az átvételkor derül ki |
|---|:-:|---|
| QC-01 — jelszó-visszaállítás MFA nélkül | S3 | Oktatási hiányosság, kezelhető |
| **QC-02 — Autopilot beüzemelési idő** | **S2** | **Az AK-06 kritérium megbukik; 50 gép újra-beüzemelése** |
| QC-03 — 12 hiányzó tápkábel | S2 | A 3. élesítési hullám csúszik, az M7 mérföldkő veszélybe kerül |

> **A szállítás közbeni ellenőrzés két olyan hibát talált (QC-02, QC-03),
> amelyek az átvételkor a mérföldkövet veszélyeztették volna.** Ez a
> dokumentum legfontosabb üzenete: az ellenőrzés nem adminisztráció, hanem
> a legolcsóbb hibajavítási időpont megtalálása.

---

| Szerep | Név | Dátum |
|---|---|---|
| Ellenőrzéseket végezte | Szabó Márk, Nagy Péter | 2026.05.04 – 06.19. |
| Szakmai felelős | Nagy Péter, IT osztályvezető | 2026.06.19. |
| Nyilvántartja | Tóth Gergő, projektmenedzser | 2026.06.19. |

> **Kapcsolódó dokumentumok:** bemenete a *Minőségterv* és a
> *Tesztjegyzőkönyv*; kimenete az *Átadás-átvételi jegyzőkönyv* és a
> *Projektzáró jelentés*.
