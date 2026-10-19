# Szolgáltatásleírás és katalógus-bejegyzés — „Felhőalapú munkahely”

**Dokumentum azonosítója:** XYO-ITIL-001\
**Szolgáltatás:** Felhőalapú munkahely (pilot, 50 fő)\
**Szolgáltatásgazda:** Nagy Péter, IT osztályvezető\
**Készítette:** Tóth Gergő, Kiss Rékával és Szabó Márkkal közösen\
**Jóváhagyta:** Horváth Júlia, ügyvezető (megrendelő)\
**Dátum:** **2026. június 26.** — az üzemeltetésbe adás napja\
**Verzió:** 1.0

> ⚠ **ITIL 4-kiegészítés.** A Xyo-projekt ezt a dokumentumot nem készítette el. A Run-book
> (XYO-CP-402) leírja, **mit kell üzemeltetni**; a szolgáltatásleírás azt, **mit kap a
> felhasználó és a cég** — és mit nem. Az előbbi az IT-nak szól, az utóbbi a megrendelőnek és a
> felhasználóknak.
>
> **A lényege:** a projekt végén a *termékből* (beállított Microsoft 365, 50 laptop)
> **szolgáltatás** lesz. A projektalapító okirat a projektet indította el; ez a dokumentum azt
> rögzíti, ami a projekt után megmarad.

---

## 1. A szolgáltatás egy mondatban

**Biztonságos, bárhonnan elérhető munkakörnyezet a pilot kör 50 munkatársának: céges laptop,
fájlok a felhőben, belépés kétlépcsős azonosítással, és egy Service Desk, amely munkaidőben
segít.**

| | |
|---|---|
| **Kinek szól (felhasználók)** | A pilot kör 50 munkatársa: Pénzügy, Értékesítés, Logisztika |
| **Ki rendeli meg (megrendelő)** | Horváth Júlia, ügyvezető |
| **Ki fizeti (szponzor)** | Kovács Anita, gazdasági igazgató — IT-2026-UZ költséghely |
| **Ki nyújtja (szolgáltató)** | Az IT osztály, Nagy Péter vezetésével |
| **Milyen eredményt támogat** | Rugalmas, helyszíntől független munkavégzés a home office szabályzat keretei között; gyorsabb munkába állás; kevesebb elveszett munkaidő az IT-hibák miatt |

> **Mire jó a négy külön sor?** Az ITIL 4 megkülönbözteti a **felhasználót** (aki használja), a
> **megrendelőt** (aki az elvárásokat meghatározza) és a **szponzort** (aki a költségét
> jóváhagyja). A Xyo-nál ez három különböző ember vagy csoport — és a szolgáltatás
> felülvizsgálatánál mindhárom szempontja más.

## 2. Haszon és garancia — mit ad, és mennyire megbízhatóan

Az ITIL 4 a szolgáltatás értékét két részre bontja: a **haszon** (*utility*) az, **amit** a
szolgáltatás tud („alkalmas a célra”); a **garancia** (*warranty*) az, **ahogyan** tudja
(„alkalmas a használatra”). Egyik sem elég a másik nélkül: a legjobb funkció is értéktelen, ha
reggel nem lehet belépni.

### 2.1 Haszon — amit a felhasználó kap

| # | Képesség | Amit ez a munkatársnak jelent |
|---|---|---|
| U1 | Céges laptop dokkolóval, előre beállítva | A gépet bekapcsolja, belép, és dolgozik — nem kell telepítenie semmit |
| U2 | Fájlok a SharePointon (csapatoldalak) és a OneDrive-on | A munkafájljai otthonról és az irodából ugyanúgy elérhetők |
| U3 | Közös csapatoldal (`CP-Kozos`) | Csapatok közötti anyagok egy helyen |
| U4 | Biztonságos belépés jelszóval és Authenticator-értesítéssel | Bárhonnan beléphet, a cég adatai mégis védettek |
| U5 | VPN a bérszámfejtő és az ügyviteli rendszerhez | Az otthoni munka a belső rendszereket is lefedi |
| U6 | Önkiszolgáló jelszó-visszaállítás | Elfelejtett jelszónál nem kell a Service Deskre várnia |
| U7 | Külső megosztás nevesített partnernek, 30 napos lejárattal | Ügyféllel, szállítóval biztonságosan megoszthat fájlt |

### 2.2 Garancia — amire a felhasználó és a cég számíthat

| Szempont | Vállalás | Honnan jön |
|---|---|---|
| **Szolgáltatási idő** | Munkanapokon 7:30 – 17:00 | A KPI-adatlap munkaidő-definíciója és a gyorssegédlet |
| **Rendelkezésre állás** | Legalább 99,5% a szolgáltatási időben | M9 célértéke; részletesen az SLA-ban (XYO-ITIL-002) |
| **Megoldási idő** | A lezárt ticketek átlaga legfeljebb 6,0 munkaóra | M2 célértéke |
| **Biztonság** | 100% MFA-lefedettség; BitLocker-titkosítás minden gépen; elveszett gépnél távoli hozzáférés-visszavonás 8 percen belül | M8; Run-book 4. pont, 10. eset |
| **Adatbiztonság** | Törölt fájl 30 + 30 napig visszaállítható; teljes könyvtár visszaállítása kb. 42 perc | As-built 4.3 |
| **Kapacitás** | 50 felhasználói licenc; csapatoldalanként 50–150 GB, a közös oldalon 200 GB tárhely | Run-book 3. pont, As-built 4.1 |
| **Folytonosság** | Hardverhibánál következő munkanapi helyszíni szerviz; kizárt adminisztrátoroknál break-glass fiók | Run-book 2. és 6. pont |

> **Tipikus hiba:** a szolgáltatásleírás csak a haszon-oldalt sorolja fel („van SharePoint,
> van VPN”), a garancia-oldal kimarad. Ilyenkor az első kiesésnél derül ki, hogy senki nem
> ígért semmit — vagy mindenki mást hitt.

## 3. A szolgáltatásajánlat — mi van a csomagban

A **szolgáltatásajánlat** (*service offering*) az, amit a felhasználó ténylegesen megkap. Az
ITIL 4 szerint háromféle elemből áll:

| Elem | ITIL-név | A Xyo-nál |
|---|---|---|
| **Áru** — tulajdonba vagy használatba kerül | *Goods* | Laptop, dokkoló (adapteres munkahelyen HDMI–VGA adapter) — leltárszámmal, a munkaviszony végéig |
| **Hozzáférés erőforráshoz** — használhatja, de nem az övé | *Access to resources* | Microsoft 365 licenc, csapatoldalak, OneDrive, VPN a három belső célhoz |
| **Szolgáltatási tevékenység** — amit érte elvégeznek | *Service actions* | Service Desk-támogatás, új gép beüzemelése, fájl-visszaállítás, jogosultságkezelés |

## 4. Kéréskatalógus — mit lehet kérni, és mennyi idő alatt

A **szolgáltatáskérés** nem hiba: előre ismert, szabványos lépésekből álló igény. A
Run-book 4. pontjának „15 leggyakoribb esete” vegyesen tartalmaz hibákat és kéréseket — az ITIL
ezeket szétválasztja, mert másképp kell kezelni és mérni őket.

| # (Run-book) | Tünet a Run-bookban | ITIL-besorolás | Hogyan teljesül |
|---|---|---|---|
| 1 | „Nem jön az MFA-értesítés” | Incidens | Ismert ok (H-09), kerülőmegoldással |
| 2 | „Hova mentsem a fájlt?” | **Szolgáltatáskérés — információkérés** | Gyorssegédlet 3. pont |
| 3 | „Nem találom a fájlomat” | **Szolgáltatáskérés — visszaállítás** | Lomtár vagy verziótörténet |
| 4 | „Nem tudok belépni” | Incidens | Háromlépcsős ellenőrzés |
| 5 | „A VPN nem indul el” | Incidens | Kliens és profil |
| 6 | „A bérszámfejtés nem érhető el” | Incidens | VPN-kapcsolat ellenőrzése |
| 7 | „A monitor nem működik” | Incidens | Tápkábel, adapter |
| 8 | „Lassú a gép” | Incidens | Szinkronizálás, frissítés |
| 9 | „Nem tudok megosztani külső partnerrel” | **Szolgáltatáskérés — információkérés** | A korlátozás szándékos; a helyes beállítás elmagyarázása |
| 10 | „Elveszett / ellopták a gépet” | Incidens — **biztonsági, kiemelt** | Azonnali távoli hozzáférés-visszavonás |
| 11 | „Nem települ egy alkalmazás” | Incidens | Alkalmazásportál, telepítési napló |
| 12 | „Új munkatárs gépe kell” | **Szolgáltatáskérés — szabványos változással** | Autopilot, ≈1,5 óra |
| 13 | „Kilépő munkatárs” | **Szolgáltatáskérés — szabványos változással** | Fiók letiltása, 30 napos megőrzés |
| 14 | „Nem működik a videóhívás otthonról” | Incidens | Ismert ok (H-06) |
| 15 | „Angol feliratok az alkalmazásportálon” | Incidens | Ismert hiba (H-08) |

**A 15 esetből 10 incidens és 5 szolgáltatáskérés.** A kérések közül kettő puszta
információkérés (2., 9.), három valódi teljesítés (3., 12., 13.).

> **Miért számít ez?** A PIR szerint az M1 mutató (ticket/hó) azért maradt el a céltól (74 a
> 72 helyett), mert a fájlszerver-hibák helyett **„hova mentsem?” jellegű használati
> kérdések** jelentek meg. Ezek ITIL-szemmel **nem hibák, hanem információkérések** — ha a
> ticketrendszer külön számolná őket, látszana, hogy a hibák száma jobban csökkent, mint az
> összes ticketé, a kérdések pedig oktatással és tudáscikkel csökkenthetők.

### 4.1 Katalógus-bejegyzések — a kérhető tételek

| Kérés | Ki kérheti | Jóváhagyás | Célidő | Mérés |
|---|---|---|---|---|
| **Új belépő munkába állítása** (gép, fiók, MFA, jogosultságok) | HR (Varga Eszter) | nem kell — szabványos | ≤ 1,0 munkanap a HR-igénytől; a gépbeüzemelés ≤ 1,5 óra | M5, M4 |
| **Kilépő munkatárs** (fiók letiltása, adatmegőrzés) | HR, a közvetlen vezető | **Nagy Péter** — az adatok törléséhez | Letiltás a munkaviszony utolsó napján; törlés 30 nap után | — |
| **Fájl visszaállítása** | bármely felhasználó | nem kell | 1 fájl: kb. 2 perc; teljes könyvtár: kb. 42 perc (a visszaállítási teszt szerint) | — |
| **Külső megosztás beállítása** | bármely felhasználó (önkiszolgáló) | nem kell — a 30 napos lejárat kötelező | azonnal | — |
| **Jelszó-visszaállítás** | bármely felhasználó (önkiszolgáló) | nem kell | azonnal | M3 |

*A csapatoldal-tagságot nem az IT adja: az oldalgazda maga kezeli (As-built 4.2). Ez is
katalógus-döntés — a kérés oda kerül, ahol a döntéshez szükséges tudás van.*

> **Tipikus hiba:** a kérések célidejét a kérés beérkezésétől mérni, holott a felhasználó a
> **teljes utat** érzékeli. Az M5 ezért a HR-igénytől méri a munkába állást, nem attól, hogy
> az IT megkapta a ticketet — így a HR és az IT közötti átadás is benne van.

## 5. Mi nem része a szolgáltatásnak

A kizárások ugyanolyan fontosak, mint a vállalások: ezekről később nem lehet vita.

| Kizárás | Miért | Honnan |
|---|---|---|
| Céges mobiltelefon | A projekt hatókörén kívül esett (K9) | Változásnapló 5. pont |
| Otthoni irodabútor | Hatókörön kívül (K10) | Változásnapló 5. pont |
| Otthoni nyomtatás | Hatókörön kívül (K11) | Változásnapló 5. pont |
| Az otthoni internetkapcsolat minősége | A mobilszolgáltató felelőssége; a Xyo csak hozzájárulást fizet | Run-book 4. pont, 14. eset (H-06) |
| Adatvesztés-megelőzés (DLP), hardveres biztonsági kulcs | Az 50 fős pilotnál tudatosan elfogadott korlát | Run-book 7. pont |
| Támogatás munkaidőn kívül | A szolgáltatási idő munkanapokon 7:30 – 17:00 | 2.2 pont |

> **Mire jó ez a táblázat?** A Xyo projektje a hatókörön kívüli kéréseket gondosan
> nyilvántartotta (K8–K11). Ha a szolgáltatásleírás nem veszi át őket, a projekt után
> ugyanezek a kérések **szolgáltatási panaszként** térnek vissza: „miért nem kaptunk céges
> telefont?”

## 6. A szolgáltatás mögötti technika — a Run-bookból

A felhasználó a 2–4. pontot látja; az IT ezt is. A **konfigurációs tételek** részletes leírása
az As-built dokumentációban (XYO-CP-206) van; a változásaikat a változásengedélyezési modell
(XYO-ITIL-003) szabályozza.

| Konfigurációs tétel | Hol | Gazdája |
|---|---|---|
| Microsoft 365 bérlő | `xyokft.onmicrosoft.com`, tartomány: `xyo.hu` | Szabó Márk |
| Entra ID | 50 felhasználó, 7 csoport, 5 feltételes hozzáférési szabály | Szabó Márk |
| Intune | 4 eszközprofil, 5 alkalmazáscsomag, 50 Autopilot-eszköz | Szabó Márk |
| SharePoint / OneDrive | 6 csapatoldal + CP-Kozos, 50 OneDrive | Szabó Márk; csapatoldalanként az oldalgazda |
| Azure VPN | VpnGw1 (West Europe), 3 elérhető belső erőforrás | Szabó Márk |

**Függőségek — amitől a szolgáltatás garanciája függ:**

| Beszállító | Mit ad | Meddig | Részletesen |
|---|---|---|---|
| Microsoft (CSP-n keresztül) | Microsoft 365 licenc és platform | 2027.04.30. | SLA, XYO-ITIL-002, 6. pont |
| Microsoft (Azure) | VPN Gateway | folyamatos | SLA, XYO-ITIL-002, 6. pont |
| Cloudia Solutions Kft. | A bevezetés szavatossága | 2026.12.19. | Szerződés 3.6 |
| TechLine Zrt. | Hardvergarancia, helyszíni szerviz | 2029.05.29. | Run-book 6. pont |

> **A 4. és a 6. pont között van a Xyo egyik rejtett kockázata:** mind az öt konfigurációs
> tétel gazdája Szabó Márk. Ez nem hiba, egy 50 fős pilotnál ésszerű — de a szolgáltatásleírás
> **láthatóvá teszi**, és így a helyettesítés kérdése a szolgáltatás-felülvizsgálat napirendjére
> kerül (lásd: Szerepek és igazodás, a koncentráció).

## 7. Költség

| | |
|---|---:|
| Tervezett folyó költség a 2. évtől | 10 680 000 Ft/év |
| **Egy felhasználóra vetítve** | **17 800 Ft/fő/hó** |
| Mit tartalmaz | M365 licenc, Azure/VPN, mobilinternet-hozzájárulás |
| Mit nem tartalmaz | Az egyszeri beruházást (hardver, bevezetés) |

> **Miért kell a költség a szolgáltatásleírásba?** Mert a megrendelő ezt a számot veti össze a
> haszonnal, és a kiterjesztésről is ebből dönt. A fajlagos költség az M12 mutatóval
> azonos módon számol (éves folyó költség / 50 fő / 12 hónap), így a mérés és a vállalás
> ugyanazt jelenti.

## 8. Katalógus-bejegyzés — így látja a felhasználó

*(A szolgáltatáskatalógus a szolgáltatások listája, ahogy a felhasználó és a megrendelő látja:
röviden, technikai szakszavak nélkül. Ez a bejegyzés kerül a belső portálra.)*

| | |
|---|---|
| **Szolgáltatás** | Felhőalapú munkahely |
| **Röviden** | Céges laptop, fájlok a felhőben, biztonságos belépés bárhonnan |
| **Kinek** | A pilot kör munkatársainak (Pénzügy, Értékesítés, Logisztika) |
| **Mit kérhetsz** | Új belépő munkába állítása · kilépő kezelése · fájl visszaállítása |
| **Önkiszolgáló** | Jelszó-visszaállítás · külső megosztás 30 napos lejárattal · csapatoldal-tagság az oldalgazdánál |
| **Ha baj van** | Service Desk: belső 4200, `servicedesk@xyo.hu` — munkanapokon 7:30 – 17:00 |
| **Elveszett vagy ellopott gép** | **Azonnal** hívd a 4200-at — távolról letiltjuk |
| **Szolgáltatásgazda** | Nagy Péter |
| **Állapot** | Pilot — a kiterjesztésről a PIR után dönt a Projekt Irányító Bizottság |

---

## Mi a különbség a projekt dokumentumaihoz képest?

| | Projektalapító okirat | Run-book | **Szolgáltatásleírás** |
|---|---|---|---|
| Kinek szól | Szponzor, Steering | Üzemeltetés (IT) | **Megrendelő és felhasználók** |
| Mit rögzít | Mit hoz létre a projekt | Hogyan kell üzemeltetni | **Mit kap a felhasználó, és mit nem** |
| Meddig él | A projekt zárásáig | A rendszer élettartamáig | **A szolgáltatás élettartamáig** |
| Ki tartja karban | A projektmenedzser | A rendszergazda | **A szolgáltatásgazda** |
| Mi a mérce | Határidő, keret, hatókör | Működik-e | **Az ígért haszon és garancia** |

> **A tanulság egy PM-nek:** a szolgáltatásleírás az átadás-átvétel hiányzó harmadik lába. A
> Xyo átadta a terméket (átadás-átvételi jegyzőkönyv) és az üzemeltetést (Run-book), de azt
> nem, hogy **mit ígér a szolgáltatás a felhasználóknak**. Egy 50 fős pilotnál ez még pótolható
> menet közben; a 190 fős kiterjesztésnél már az átadás feltétele.

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, Kiss Réka, Szabó Márk | 2026.06.26. |
| Szolgáltatásgazda | Nagy Péter | 2026.06.26. |
| **Jóváhagyta (megrendelő)** | **Horváth Júlia** | 2026.06.26. |

---

> **Kapcsolódó dokumentumok:** bemenete a *Run-book* (XYO-CP-402), az *As-built
> dokumentáció*, a *Felhasználói gyorssegédlet*, a *Változásnapló* és a *KPI-adatlap*;
> kimenete az *SLA, OLA és alátámasztó szerződések* (XYO-ITIL-002) és a
> *Változásengedélyezési modell* (XYO-ITIL-003).
