# Adatvédelmi hatásvizsgálat (DPIA)

**Dokumentum azonosítója:** XYO-CP-118\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** dr. Fekete Zsolt, adatvédelmi tisztviselő (DPO)\
**Adatot szolgáltatott:** Tóth Gergő (PM), Szabó Márk (rendszergazda)\
**Kelt:** 2026. március 6.\
**Verzió:** 1.0

> **Verziójegyzet:** a nyertes szállító neve (Cloudia Solutions Kft.) a szerződéskötés után, 2026.04.20-án került a dokumentumba. A korábbi változatban a beszerzési tételek (B1–B4) szerepeltek; a baseline tartalma — hatókör, ütem, költség — ezzel nem változott.

> **Jogalap:** GDPR 35. cikk. A vizsgálatot az **eszközfelügyelet (Intune)**
> és a **felhőalapú adattárolás** kombinációja indokolja.

---

## 1. Előzetes állásfoglalás

A projektmenedzser 2026.02.12-én írásban megkereste az adatvédelmi tisztviselőt
azzal a kérdéssel, hogy szükséges-e adatvédelmi hatásvizsgálat.

**Az állásfoglalás (2026.02.20.):** igen, hatásvizsgálat szükséges, mert a
tervezett adatkezelés **munkavállalói eszközök központi felügyeletét** foglalja
magában, ami a NAIH ajánlása szerint magas kockázatú adatkezelésnek minősülhet.

> **Tanulság junior PM-nek:** az állásfoglalást akkor is írásban kell kérni, ha
> a válasz „nem kell hatásvizsgálat". A „nem kell" is dokumentálandó döntés —
> és téged véd, ha később valaki megkérdőjelezi.

## 2. Az adatkezelés leírása

| | |
|---|---|
| **Az adatkezelés célja** | Munkavégzéshez szükséges IT-környezet biztosítása és a céges eszközök biztonságos üzemeltetése |
| **Érintettek köre** | 50 munkavállaló (a pilot résztvevői) |
| **Jogalap** | GDPR 6. cikk (1) b) — a munkaszerződés teljesítése; és f) — a munkáltató jogos érdeke az eszközök védelmében |
| **Adatkezelő** | Xyo Kft. |
| **Adatfeldolgozók** | Microsoft Ireland Operations Ltd.; Cloudia Solutions Kft. |
| **Adattárolás helye** | Microsoft EU Data Boundary — kizárólag EU-s adatközpontok |
| **Megőrzési idő** | A munkaviszony megszűnését követő 30 nap (fiók és tartalom), majd törlés |

## 3. Kezelt személyes adatok

| Adatkör | Mit tartalmaz | Miért szükséges | Kockázat |
|---|---|---|---|
| Azonosító adatok | Név, céges e-mail, munkakör, szervezeti egység | Fiók létrehozása, jogosultságkezelés | alacsony |
| Hitelesítési adatok | Jelszó (hash), MFA telefonszám vagy alkalmazás | Biztonságos belépés | alacsony |
| Bejelentkezési naplók | Időpont, eszköz, IP-cím, ország | Biztonsági incidensek felderítése | **közepes** |
| Eszközadatok | Eszközazonosító, operációs rendszer, titkosítási állapot, telepített céges alkalmazások | Megfelelőség ellenőrzése | **közepes** |
| Felhasználói tartalom | Az OneDrive-on és SharePointon tárolt dokumentumok | A munkavégzés tárgya | **közepes** |
| Használati statisztika | Aktív felhasználók száma, szolgáltatásonként, **összesítve** | A projekt haszonrealizálási mérése | **magas, ha egyéni** |

## 4. Kockázatok és a csökkentésükre tett intézkedések

### K1 — Munkavállalói megfigyelés kockázata

| | |
|---|---|
| **Leírás** | Az Intune eszközfelügyelet és az M365 használati riportok elvileg alkalmasak lennének a munkavállalók egyéni tevékenységének nyomon követésére |
| **Súlyosság** | **Magas** — munkajogi és adatvédelmi következménnyel járhat |
| **Intézkedés 1** | Az Intune profil **nem tartalmaz** böngészési előzmény-, billentyűleütés- vagy képernyőfigyelést. A profil beállításait tételesen ellenőrzöm (AK-10 átvételi kritérium). |
| **Intézkedés 2** | A haszonrealizálási mérés **kizárólag csoportszintű összesítést** használhat. Egyéni bontású használati riport **nem készíthető és nem adható ki** a vezetőknek. |
| **Intézkedés 3** | Az üzemi tanács kikötése a Biztonsági alapkonfigurációba és az L7 korlátba bekerült: **az eszközfelügyelet nem terjedhet ki a magánhasználatra**. |
| **Intézkedés 4** | A munkavállalók az oktatáson és írásbeli tájékoztatóban megkapják, pontosan mit lát és mit nem lát a rendszer. |
| **Maradékkockázat** | **alacsony** |

### K2 — Adattovábbítás harmadik országba

| | |
|---|---|
| **Leírás** | A Microsoft globális szolgáltató; elvi lehetőség van EU-n kívüli adattovábbításra |
| **Súlyosság** | Közepes |
| **Intézkedés** | Az **EU Data Boundary** konfiguráció kötelező kikötése a szerződésben (L6 korlát, P6 ajánlatkérési elem). A szolgáltatási beállítás ellenőrzése az átvételkor. |
| **Maradékkockázat** | alacsony |

### K3 — Jogosulatlan hozzáférés a dokumentumokhoz

| | |
|---|---|
| **Leírás** | Hibás SharePoint jogosultsági beállítás miatt egy csapat láthatná egy másik adatait |
| **Súlyosság** | Közepes |
| **Intézkedés 1** | Dokumentált jogosultsági modell (WBS 3.3.1) |
| **Intézkedés 2** | Jogosultsági teszt az átvételkor: 6 csapat × 2 ellenőrzés (AK-13) |
| **Intézkedés 3** | Külső megosztás alapértelmezetten korlátozott, lejárati idővel (K19) |
| **Maradékkockázat** | alacsony |

### K4 — Elveszett vagy ellopott eszköz

| | |
|---|---|
| **Leírás** | Az otthoni munkavégzés miatt az eszközök gyakrabban hagyják el a telephelyet |
| **Súlyosság** | Közepes |
| **Intézkedés 1** | Kötelező lemeztitkosítás (BitLocker), központilag mentett kulccsal (K08, AK-08) |
| **Intézkedés 2** | Távoli hozzáférés-visszavonás 15 percen belül, tesztelt módon (AK-04) |
| **Intézkedés 3** | Az eszközök bejelentési kötelezettsége a Service Desk felé |
| **Maradékkockázat** | alacsony |

### K5 — Adatvesztés

| | |
|---|---|
| **Leírás** | Törölt vagy sérült dokumentumok nem állíthatók vissza — a „felhő magától ment" tévhit miatt nincs beállított megőrzés |
| **Súlyosság** | Közepes |
| **Intézkedés 1** | Megőrzési szabályok beállítása, legalább 30 nap (K15, AK-14) |
| **Intézkedés 2** | **Kötelező visszaállítási teszt** fájlra és teljes könyvtárra, jegyzőkönyvvel (K16, AK-15) |
| **Maradékkockázat** | alacsony |

## 5. Az érintettek jogainak biztosítása

| Jog | Hogyan biztosított |
|---|---|
| Tájékoztatáshoz való jog | Írásbeli munkavállalói tájékoztató az élesítés előtt; az oktatás 5. blokkja |
| Hozzáféréshez való jog | A saját OneDrive tartalmához közvetlen hozzáférés; naplóadat kérésre, 30 napon belül |
| Helyesbítéshez való jog | HR-en keresztül, a törzsadatokra |
| Törléshez való jog | A munkaviszony megszűnését követő 30 nap után automatikus törlés |
| Tiltakozáshoz való jog | A jogos érdeken alapuló naplózás ellen, a DPO-n keresztül |

## 6. Az adatvédelmi tisztviselő álláspontja

> A tervezett adatkezelés a fenti intézkedések maradéktalan végrehajtása esetén
> **megfelel a GDPR követelményeinek**, és a maradékkockázat elfogadható szintű.
>
> A hozzájárulásomat **három feltételhez** kötöm:
>
> 1. Az **Intune eszközprofil beállításait az élesítés előtt tételesen
>    ellenőrzöm**, és arról írásos nyilatkozatot adok (AK-10).
> 2. A haszonrealizálási mérésben **egyéni bontású használati adat nem
>    gyűjthető és nem adható ki**. A mérési adatgyűjtésre a mérési szakasz
>    indulása előtt külön állásfoglalást kérek.
> 3. Az **adatfeldolgozói megállapodásokat** a Microsofttal (licencfeltételek
>    részeként) és a Cloudia Solutions Kft.-vel a szerződéskötéssel egyidejűleg
>    alá kell írni.
>
> dr. Fekete Zsolt, adatvédelmi tisztviselő — 2026.03.06.

## 7. Ami ebből a projektre következik

| # | Következmény | Hova került át | Felelős |
|---|---|---|---|
| 1 | L6 korlát: EU-s adattárolás | Feltevés- és korlátnapló; ajánlatkérés (P6) | Molnár Katalin |
| 2 | L7 korlát: nincs magánhasználati megfigyelés | Feltevés- és korlátnapló; Biztonsági alapkonfiguráció | Szabó Márk |
| 3 | AK-10 átvételi kritérium: profil tételes átnézése | Minőségterv | dr. Fekete Zsolt |
| 4 | K09 követelmény | Követelménymátrix | Nagy Péter |
| 5 | Adatfeldolgozói megállapodás a szerződésben | Beszerzési terv (P5) | Molnár Katalin |
| 6 | Csoportszintű mérés kikötése | Haszonrealizálási terv 7. pont | Tóth Gergő |
| 7 | Munkavállalói tájékoztató az élesítés előtt | Oktatási terv | Varga Eszter |

---

> **Kapcsolódó dokumentumok:** bemenete a *Megvalósíthatósági tanulmány* és a
> *Hatókör-nyilatkozat*; kimenete a *Biztonsági alapkonfiguráció* és a
> *Szerződés*.
