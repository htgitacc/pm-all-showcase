# Biztonsági alapkonfiguráció (Security Baseline)

**Dokumentum azonosítója:** XYO-CP-119\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Szabó Márk, rendszergazda\
**Szakmailag jóváhagyta:** Nagy Péter, IT osztályvezető\
**Adatvédelmi szempontból véleményezte:** dr. Fekete Zsolt, DPO\
**Verzió:** 1.1

> **Verziójegyzet:** a nyertes szállító neve (Cloudia Solutions Kft.) a szerződéskötés után, 2026.04.20-án került a dokumentumba. A korábbi változatban a beszerzési tételek (B1–B4) szerepeltek; a baseline tartalma — hatókör, ütem, költség — ezzel nem változott.

> Új környezetnél a biztonságot **induláskor** kell rendbe tenni. Utólag
> sokkal drágább — és a rossz szokások addigra rögzülnek.

---

## 1. Azonosítás és hitelesítés

| # | Beállítás | Érték | Indok |
|---|---|---|---|
| B-01 | Többtényezős hitelesítés (MFA) | **kötelező minden pilot fiókra** | K02 követelmény; a ticketek 41%-a hozzáférés-jellegű |
| B-02 | MFA módszer | Microsoft Authenticator alkalmazás; SMS csak kivételesen | Az SMS-alapú MFA gyengébb |
| B-03 | Jelszóházirend | Min. 12 karakter, tiltott gyakori jelszavak; **nincs kényszerített lejárat** | A NIST és a Microsoft ajánlása szerint a rendszeres csere rontja a jelszóerősséget |
| B-04 | Önkiszolgáló jelszó-visszaállítás | bekapcsolva, MFA-val | K27 követelmény; a helpdesk terhelését ez csökkenti leginkább |
| B-05 | Vészhozzáférési (break-glass) fiók | **2 db**, MFA-kizárással, széfben tárolt jelszóval, riasztással a használatra | Ha a feltételes hozzáférés kizárja az adminokat, ez az egyetlen belépés |

## 2. Feltételes hozzáférés

| # | Szabály | Beállítás | Indok |
|---|---|---|---|
| B-06 | Belépés csak megfelelő (compliant) eszközről | bekapcsolva | Nem céges gépről ne legyen hozzáférés a céges adathoz |
| B-07 | Országkorlátozás | Csak Magyarországról; kivételkérés a DPO-nál | K05 követelmény |
| B-08 | Örökölt (legacy) hitelesítési protokollok | **tiltva** | Ezek megkerülik az MFA-t |
| B-09 | Kockázatalapú belépés | Magas kockázatnál MFA újrakérése | Entra ID P1 funkció, a licenc része |
| B-10 | **Bevezetés jelentés-módban** | **Legalább 5 munkanap, éles blokkolás nélkül** | R11 kockázat: rosszul beállított szabály kizárhatja a felhasználókat |

> **B-10 nem opcionális.** A feltételes hozzáférés a leggyakoribb oka annak,
> hogy egy bevezetés első napján 50 ember nem tud belépni. A jelentés-mód
> megmutatja, kit zárna ki a szabály — mielőtt tényleg kizárná.

## 3. Eszközfelügyelet (Intune)

| # | Beállítás | Érték | Indok |
|---|---|---|---|
| B-11 | Lemeztitkosítás (BitLocker) | **kötelező**, helyreállítási kulcs Entra ID-ban | K08; az otthoni munkavégzés miatt nő az eszközvesztés kockázata |
| B-12 | Képernyőzár | 10 perc tétlenség után, jelszóval | Alapvető védelem |
| B-13 | Biztonsági frissítések | automatikus, legfeljebb 7 nap halasztással | K11 |
| B-14 | Vírusvédelem | Microsoft Defender, valós idejű védelem, kikapcsolása tiltva | A licenc része |
| B-15 | Távoli hozzáférés-visszavonás | Elveszett eszköznél a céges adat 15 percen belül törölhető | AK-04 |
| B-16 | **Magánhasználat figyelése** | **NEM engedélyezett** — nincs böngészési előzmény-, billentyűleütés- vagy képernyőfigyelés | **L7 korlát, üzemi tanácsi kikötés; a DPIA feltétele** |
| B-17 | Alkalmazástelepítés | Céges alkalmazásportálon keresztül; szabad telepítés korlátozott | Támogathatóság |

> **B-16 a legfontosabb sor a dokumentumban.** Ez az, amit a munkavállalók
> félnek, és ez az, amit az üzemi tanács kikötött. Az Intune profil beállításait
> **dr. Fekete Zsolt tételesen ellenőrzi** az élesítés előtt (AK-10), és arról
> írásos nyilatkozatot ad.

## 4. Adatvédelem és megőrzés

| # | Beállítás | Érték | Indok |
|---|---|---|---|
| B-18 | Adattárolás helye | **Kizárólag EU Data Boundary** | L6 korlát, DPIA |
| B-19 | OneDrive lomtár | 30 nap, majd további 30 nap a másodlagos lomtárban | K15, AK-14 |
| B-20 | SharePoint verziókövetés | Legalább 50 verzió megtartása | Véletlen felülírás elleni védelem |
| B-21 | Megőrzési szabály | A munkaviszony megszűnése után 30 nap, majd törlés | DPIA 2. pont |
| B-22 | **Visszaállítási teszt** | **Kötelező**: 1 fájl + 1 teljes könyvtár, jegyzőkönyvvel | R7 kockázat, AK-15 |
| B-23 | Külső megosztás | Csak nevesített külső címzettnek, lejárati idővel | K19 |

> ⚠️ **A felhő nem mentés.** A Microsoft a szolgáltatás rendelkezésre állásáért
> felel, nem azért, hogy visszaállítsa, amit a felhasználó töröl vagy felülír.
> A megőrzési idő beállítása és a **tesztelt** visszaállíthatóság külön feladat.

## 5. Hálózat és VPN

| # | Beállítás | Érték | Indok |
|---|---|---|---|
| B-24 | VPN azonosítás | Entra ID azonosítóval, MFA-val | K22 |
| B-25 | VPN hatóköre | **Csak a 2 belső rendszer és a régi fájlszerver olvasása** — nem teljes hálózati hozzáférés | A legkisebb jogosultság elve |
| B-26 | VPN-naplózás | Kapcsolódási időpont és forrás-IP, 90 napig | Incidenskezelés |

## 6. Jogosultsági szintek

| Szint | Ki | Mit tehet | Hány fő |
|---|---|---|---:|
| Globális adminisztrátor | Szabó Márk + 2 break-glass fiók | Minden | 1 + 2 |
| Felhasználó-adminisztrátor | Service Desk (Kiss Réka) | Jelszó-visszaállítás, fiókzárolás feloldása | 1 |
| Intune-adminisztrátor | Cloudia Solutions (a projekt idejére) | Eszközprofilok kezelése | 2 |
| SharePoint csapatoldal-gazda | csapatonként 1 fő | A saját oldal tagjainak kezelése | 6 |
| Felhasználó | pilot résztvevők | Saját adat és a csapatoldal | 50 |

**Kikötések:**

- A Cloudia Solutions adminisztrátori hozzáférése **2026.06.19-én, az
  UAT-elfogadással megszűnik** — ezt az üzemeltetésbe adáskor ellenőrizni kell.
- A globális adminisztrátori jogot **nem kapja meg a projektmenedzser**.
  Nincs rá szüksége, és az összeférhetetlenség elkerülése is indokolja.

## 7. Amit tudatosan NEM vezetünk be most

| Mit | Miért nem |
|---|---|
| Hardveres biztonsági kulcs (FIDO2) | E05 követelmény, elhalasztva; a kiterjesztésnél újra vizsgálandó |
| Adatvesztés-megelőzés (DLP) szabályok | 50 fős pilotnál aránytalan; a kiterjesztésnél kötelező lesz |
| Behatolásteszt | A pilot mérete nem indokolja; a kiterjesztés előtt javasolt |
| Külső mentési szolgáltatás | Nincs a hatókörben; a megőrzési szabályok elegendők a pilothoz |

> **A „mit nem vezetünk be" lista ugyanolyan fontos, mint a másik.** Így
> látszik, hogy a döntés tudatos volt, nem feledékenység — és a kiterjesztésnél
> kész lista áll rendelkezésre arról, mit kell pótolni.

## 8. Ellenőrzés az átvételkor

| Kritérium | Kapcsolódó átvételi kritérium |
|---|---|
| MFA-lefedettség 100% | AK-02 |
| Break-glass fiók tesztelve | AK-03 |
| Hozzáférés-visszavonás 15 percen belül | AK-04 |
| Lemeztitkosítás 50/50 gépen | AK-08 |
| Az Intune profil nem tartalmaz magánhasználati figyelést | AK-10 |
| 30 napos visszaállíthatóság | AK-14 |
| Teljes könyvtár visszaállítása tesztelve | AK-15 |

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Szabó Márk, rendszergazda | 2026.03.09. |
| Jóváhagyta | Nagy Péter, IT osztályvezető | 2026.03.11. |
| Véleményezte | dr. Fekete Zsolt, DPO | 2026.03.12. |

> **Kapcsolódó dokumentumok:** bemenete az *Adatvédelmi hatásvizsgálat*;
> kimenete a *Konfigurációs (as-built) dokumentáció*, a *Tesztterv* és az
> *Üzemeltetésbe adás*.
