# Ajánlatkérési dokumentáció (RFP / RFQ)

**Dokumentum azonosítója:** XYO-CP-202\
**Projekt:** Xyo Cloud Pilot\
**Kiadta:** Molnár Katalin, beszerzési vezető\
**Műszaki tartalom:** Nagy Péter, Szabó Márk\
**Kiadás dátuma:** 2026. március 20.\
**Ajánlati határidő:** **2026. április 2., 12:00**

> **Amit ide nem írsz bele, azt nem is fogod megkapni** — és utólag már csak
> felárral. Ez a dokumentum két külön eljárást indít: **B1** (hardver) és
> **B2+B3** (licenc és bevezetés).

---

## 1. Az ajánlatkérés tárgya

| Eljárás | Tárgy | Becsült érték | Eljárásrend |
|---|---|---:|---|
| **B1** | 50 munkaállomás-készlet (laptop, dokkoló, monitor, headset) | 27 750 000 Ft | 3 ajánlat + értékelő bizottság |
| **B2+B3** | Microsoft 365 licenc (12 hó) + felhőkörnyezet bevezetése | 14 780 000 Ft | 3 ajánlat |

**Megszólított ajánlattevők** (az előzetes piaci tájékozódás alapján, 2026.02.24–26.):

| B1 — hardver | B2+B3 — licenc és bevezetés |
|---|---|
| TechLine Zrt. | Cloudia Solutions Kft. |
| NovaComp Kft. | Azurion Consulting Kft. |
| BitPartner Zrt. | DataBridge Kft. |

## 2. B1 — Műszaki követelmények (hardver)

| # | Tétel | Mennyiség | Elvárás |
|---|---|---:|---|
| 1 | Laptop | 50 db | 14", Intel i5 (vagy azzal egyenértékű), 16 GB RAM, 512 GB SSD, Windows 11 Pro |
| 2 | Dokkoló | 50 db | USB-C, tápellátással, min. 2 külső kijelző támogatása |
| 3 | Monitor | 50 db | 24", Full HD, **HDMI vagy DisplayPort csatlakozóval** |
| 4 | Headset | 50 db | USB vagy USB-C, mikrofonnal, zajszűréssel |

> **A 3. tétel csatlakozó-kikötése tanulság.** A tervezéskor derült ki, hogy a
> meglévő irodai monitorok 14 darabja csak VGA-csatlakozós — ezért az új
> monitoroknál ezt tételesen kikötöttük.

## 3. Kötelező vállalások — enélkül az ajánlat érvénytelen

| # | Vállalás | Miért kizáró feltétel |
|---|---|---|
| **V1** | **Windows Autopilot regisztráció** gyári szinten, a Xyo Kft. bérlőjéhez rendelve | Enélkül 50 gép × 6,5 óra = 325 óra kézi beüzemelés, és a beüzemelési célérték (≤1,5 óra/gép) teljesíthetetlen |
| **V2** | **Részszállítás:** 10 db 2026.05.06-ig, 40 db 2026.05.29-ig | A tesztelés 05.11-én indul; a kritikus úton nincs puffer |
| **V3** | Készlethelyzet igazolása az ajánlatban | Korai jelzés a szállítási kockázatra |
| **V4** | Kötbér: napi 0,5%, legfeljebb 10% | A határidő betartásának egyetlen valódi eszköze |
| **V5** | **Adatfeldolgozói megállapodás** aláírása (B2+B3) | GDPR-kötelezettség |
| **V6** | **EU-s adattárolás** (EU Data Boundary) (B2+B3) | Az adatvédelmi hatásvizsgálat feltétele |
| **V7** | **Tudásátadás és Run-book** átadása teljesítési feltételként (B3) | Enélkül nincs önálló üzemeltetés a projekt után |
| **V8** | Helyettesítési kötelezettség a nevesített konzultánsokra (B3) | A kulcsember kiesésének kockázata |

## 4. B2+B3 — Elvárt szolgáltatási tartalom

| # | Terület | Elvárás |
|---|---|---|
| 1 | Licenc | Microsoft 365 Business Premium, 50 felhasználó, 12 hónap |
| 2 | Entra ID | Bérlő kiterjesztése, 50 fiók, MFA, feltételes hozzáférés |
| 3 | Intune | Eszközprofilok, megfelelőségi szabályok, Autopilot folyamat, alkalmazáscsomagok |
| 4 | SharePoint / OneDrive | 6 csapatoldal, jogosultsági modell, megőrzési szabályok |
| 5 | Azure VPN | VPN Gateway, kliensprofil, 2 belső rendszer elérése |
| 6 | Dokumentáció | As-built konfigurációs dokumentáció + üzemeltetési Run-book |
| 7 | Oktatás | Oktatási anyag, 5 csoport oktatása, magyar nyelvű gyorssegédlet |
| 8 | Tudásátadás | A rendszergazda felkészítése önálló üzemeltetésre |

**Ütemezési elvárás:** a környezet 2026.05.08-ra tesztelésre alkalmas állapotban.

## 5. Szerződéses alapfeltételek

| | B1 | B2+B3 |
|---|---|---|
| Szerződéstípus | Adásvételi, fix áras | **Átalánydíjas (fix price)** |
| Fizetés | 20% részszállításkor, 80% teljes átvételkor | 30% szerződéskötés, 40% M5, 30% M8 |
| Garancia | Min. 2 év, helyszíni szerviz megajánlható | Bevezetésre 6 hónap szavatosság |
| Teljesítés igazolása | Mennyiségi és minőségi átvétel után | Az átvételi kritériumok teljesülése után |

> **Miért átalánydíjas a bevezetés?** Óradíjas szerződésnél a szállító a
> ráfordított órát számlázza — minél tovább tart, annál többet keres. Fix áras
> szerződésnél a késés az ő kockázata.

## 6. Az értékelés szempontjai

Az értékelés a **2026.03.13-án, az ajánlatok beérkezése előtt** jóváhagyott
szempontrendszer szerint történik (XYO-CP-113).

**B1 — hardver:**

| Szempont | Súly |
|---|---:|
| Ajánlati ár | 45% |
| Szállítási határidő a teljes tételre | 20% |
| Garancia és helyszíni szerviz | 15% |
| Referencia hasonló Autopilot-szállításra | 12% |
| Vállalt kötbérmérték | 8% |

**B2+B3 — licenc és bevezetés:**

| Szempont | Súly |
|---|---:|
| Ajánlati ár (12 hónapos teljes költség) | 35% |
| Bevezetési módszertan és ütemterv részletessége | 20% |
| Referencia magyar vállalati M365 + Intune bevezetésre | 15% |
| Tudásátadás tartalma és a Run-book minősége | 15% |
| Támogatási konstrukció a bevezetés után | 10% |
| A nevesített konzultánsok tapasztalata | 5% |

## 7. Az ajánlat kötelező mellékletei

| # | Melléklet | Mindkét eljárás |
|---|---|:-:|
| M1 | Cégkivonat, 30 napnál nem régebbi | ✔ |
| M2 | Nemleges köztartozás-igazolás | ✔ |
| M3 | Tételes árajánlat, nettó és bruttó bontásban | ✔ |
| M4 | Nyilatkozat a V1–V8 vállalásokról | ✔ |
| M5 | Referencialista, kapcsolattartóval | ✔ |
| M6 | Készletigazolás vagy gyártói visszaigazolás | csak B1 |
| M7 | Bevezetési módszertan és ütemterv-javaslat | csak B2+B3 |
| M8 | **Run-book mintadokumentum** | csak B2+B3 |
| M9 | A nevesített konzultánsok önéletrajza, tanúsítványai | csak B2+B3 |

> **Az M8 (Run-book minta) bekérése tudatos.** A „vállaljuk a tudásátadást"
> mondat semmit nem jelent. Egy korábbi projektjéből származó minta viszont
> megmutatja, mit ért alatta a szállító — és ez lett az egyik legerősebben
> megkülönböztető szempont az értékelésnél.

## 8. Az eljárás menete

| Lépés | Dátum |
|---|---|
| Ajánlatkérés kiadása | 2026.03.20. |
| Kérdésfeltevési határidő | 2026.03.27. |
| Válaszok kiküldése minden ajánlattevőnek | 2026.03.30. |
| **Ajánlati határidő** | **2026.04.02., 12:00** |
| Bontás | 2026.04.02., 14:00 |
| Értékelés | 2026.04.07–04.08. (04.03. Nagypéntek, 04.06. Húsvéthétfő) |
| Eredményhirdetés | 2026.04.09. |
| Szerződéskötés | 2026.04.17. |

**A kérdésekre adott válaszokat minden ajánlattevő megkapja**, a kérdező
megnevezése nélkül — így az eljárás mindenki számára azonos feltételekkel folyik.

**Közzététel:** a Cloudia Solutions Kft. 2026 januárjában előzetes felmérést
végzett a Xyo Kft.-nél, és a 2026.02.10-11-i WBS-workshopon tanácsadóként részt
vett. Az ajánlatkérés mellékleteként **minden ajánlattevő megkapja** a felmérés
összefoglalóját és a WBS-t — így az előzetes részvétel nem jelent információs
előnyt. A Cloudia Solutions ajánlata ugyanazon szempontok szerint értékelődik.

## 9. Amit az ajánlatkérés NEM tartalmaz

| Mit | Miért |
|---|---|
| A jóváhagyott keretösszeg | Az ajánlatok pontosan ahhoz igazodnának |
| A belső költségbecslés | Ugyanez; a beszerzési szabályzat is tiltja |
| A többi megszólított ajánlattevő neve | Nem segíti a versenyt |
| A projekt belső kockázatnyilvántartása | Szállítóra vonatkozó, névvel ellátott kockázatokat tartalmaz |

---

| Szerep | Név | Dátum |
|---|---|---|
| Műszaki tartalom | Nagy Péter, Szabó Márk | 2026.03.19. |
| Kiadta | Molnár Katalin, beszerzési vezető | 2026.03.20. |

> **Kapcsolódó dokumentumok:** bemenete a *Beszerzési terv* és a
> *Szállítóértékelési szempontrendszer*; kimenete az
> *Ajánlat-összehasonlítás* és a *Szerződés*.
