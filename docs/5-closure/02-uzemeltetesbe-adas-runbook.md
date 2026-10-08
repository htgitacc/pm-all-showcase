# Üzemeltetésbe adás (Run-book)

**Dokumentum azonosítója:** XYO-CP-402\
**Projekt:** Xyo Cloud Pilot\
**Átadó:** Tóth Gergő (PM) és Cloudia Solutions Kft.\
**Átvevő:** Nagy Péter, IT osztályvezető\
**Átadás dátuma:** **2026. június 26.**\
**Verzió:** 1.0

> **Ez a dokumentum szabadít fel téged.** Amíg nincs formális üzemeltetésbe
> adás, minden hiba a projekt — vagyis a te — problémád marad.
>
> A hibakezelési részt **Kiss Rékával közösen** írtuk. Amit a projekt
> logikusnak talál, az a Service Desknek gyakran használhatatlan — ők a valós
> hívásokat ismerik.

---

## 1. Mit üzemeltetünk?

| Elem | Hol | Részletes leírás |
|---|---|---|
| Microsoft 365 bérlő | `xyokft.onmicrosoft.com`, tartomány: `xyo.hu` | As-built 1. pont |
| Entra ID | 50 felhasználó, 7 csoport, 5 feltételes hozzáférési szabály | As-built 2. pont |
| Intune | 4 eszközprofil, 5 alkalmazáscsomag, 50 Autopilot-eszköz | As-built 3. pont |
| SharePoint / OneDrive | 6 csapatoldal + CP-Kozos, 50 OneDrive | As-built 4. pont |
| Azure VPN | VpnGw1 (West Europe), 3 elérhető belső erőforrás | As-built 5. pont |

**A teljes konfiguráció:** *Konfigurációs (as-built) dokumentáció, XYO-CP-206 v1.4.*

## 2. Hozzáférések átadása

| Hozzáférés | Kinek | Átadva | Ellenőrizve |
|---|---|---|---|
| Globális adminisztrátor (Entra ID, M365) | Szabó Márk | 2026.04.22. | ✔ |
| Azure előfizetés tulajdonos | Nagy Péter | 2026.06.26. | ✔ |
| Felhasználó-adminisztrátor (jelszó-visszaállítás) | Kiss Réka + 2 Service Desk munkatárs | 2026.04.27. | ✔ |
| **Break-glass fiókok jelszava** | Lezárt boríték a pénzügyi széfben | 2026.05.06. | ✔ |
| **A Cloudia Solutions Intune-adminisztrátori joga** | **MEGSZŰNT** | 2026.06.19. | **✔ ellenőrizve 06.26-án** |
| Microsoft partnerportál | Nagy Péter | 2026.06.26. | ✔ |

> **A szállítói hozzáférés megszűnését külön ellenőriztük.** A szerződés
> szerint az UAT-elfogadással (06.19.) automatikusan megszűnik — de az
> „automatikusan" szót üzemeltetési kérdésekben soha ne vedd készpénznek.

### Break-glass fiókok — használati rend

| | |
|---|---|
| Mikor használható | Csak akkor, ha a feltételes hozzáférés kizárja az adminisztrátorokat |
| Ki férhet hozzá a jelszóhoz | Nagy Péter, Kovács Anita |
| Hol | Lezárt boríték, pénzügyi széf |
| Riasztás | Bejelentkezéskor azonnali e-mail Nagy Péternek és Szabó Márknak |
| Használat után | **Kötelező jelszócsere**, új boríték, jegyzőkönyv |
| Rendszeres teszt | Félévente (következő: 2026.12.18.) |

## 3. Rendszeres üzemeltetési feladatok

| Feladat | Gyakoriság | Felelős | Mit kell tenni |
|---|---|---|---|
| Mentés-ellenőrzés | havonta | Szabó Márk | 1 véletlenszerű fájl visszaállítása a lomtárból |
| **Visszaállítási teszt (teljes könyvtár)** | **félévente** | Szabó Márk | Teljes könyvtár visszaállítása, időmérés, jegyzőkönyv |
| Megfelelőségi állapot ellenőrzése | havonta | Szabó Márk | Intune riport: 50/50 gép megfelelő? |
| MFA-lefedettség ellenőrzése | havonta | Szabó Márk | Entra ID riport: 100%? |
| Licencfelhasználás | havonta | Szabó Márk | 50 licenc, nincs kiosztatlan vagy hiányzó |
| Break-glass fiók teszt | félévente | Szabó Márk | Bejelentkezés, jelszócsere, jegyzőkönyv |
| Feltételes hozzáférési szabályok átnézése | negyedévente | Szabó Márk, Nagy Péter | Van-e felesleges vagy hiányzó szabály |
| **Licenc-megújítás előkészítése** | **2027.02.28-ig** | Nagy Péter | A 12 hónapos előfizetés 2027.04.30-án jár le |

> **A licenc-megújítás dátumát külön kiemeltük.** Ez a leggyakoribb elfelejtett
> üzemeltetési feladat egy pilot után — és a lejárat napján 50 ember nem tud
> belépni.

## 4. Hibakezelés — a 15 leggyakoribb eset

*(A Service Desk hibakezelési útmutatójából, Kiss Rékával közösen összeállítva.
Az élesítés utáni 6 hét tapasztalata alapján rendezve gyakoriság szerint.)*

| # | Tünet | Valószínű ok | Teendő | Eszkaláció |
|---|---|---|---|---|
| 1 | „Nem jön az MFA-értesítés" | Telefon offline, vagy szolgáltatói késés (H-09) | Authenticator kézi megnyitása; ha 1 percen túl sem jön, jelszó + kódos belépés | Szabó Márk, ha rendszeres |
| 2 | „Hova mentsem a fájlt?" | Nem hiba — felhasználói kérdés | Gyorssegédlet 3. pont, döntési ábra | — |
| 3 | „Nem találom a fájlomat" | Törölve vagy másik helyre mentve | OneDrive lomtár (30+30 nap); SharePoint verziótörténet | Szabó Márk, ha nincs a lomtárban |
| 4 | „Nem tudok belépni" | Jelszó, MFA, vagy feltételes hozzáférés | 1) Önkiszolgáló jelszó-visszaállítás. 2) MFA újraregisztrálás. 3) Entra ID bejelentkezési napló ellenőrzése | Szabó Márk, ha CA-szabály zárja ki |
| 5 | „A VPN nem indul el" | Kliensprofil vagy hálózat | VPN-kliens újraindítása; profil újratöltése | Szabó Márk |
| 6 | „A bérszámfejtés nem érhető el" | VPN nincs csatlakoztatva | VPN-kapcsolat ellenőrzése | Szabó Márk, ha a VPN fut |
| 7 | „A monitor nem működik" | Dokkoló tápkábel, vagy adapter | Tápkábel ellenőrzése; adapteres gépeknél az adapter csatlakozása | helyszíni segítség |
| 8 | „Lassú a gép" | Első szinkronizálás, vagy frissítés fut | 1 óra türelem; OneDrive szinkron-állapot ellenőrzése | Szabó Márk 24 óra után |
| 9 | „Nem tudok megosztani külső partnerrel" | Külső megosztás korlátozott | Nevesített külső címzett + 30 napos lejárat beállítása | — |
| 10 | „Elveszett / ellopták a gépet" | — | **AZONNAL:** Intune → távoli hozzáférés-visszavonás (8 perc); jegyzőkönyv | **Nagy Péter + dr. Fekete Zsolt azonnal** |
| 11 | „Nem települ egy alkalmazás" | Céges alkalmazásportál | Portál újraindítása; Intune telepítési napló | Szabó Márk |
| 12 | „Új munkatárs gépe kell" | — | Autopilot-folyamat: gép regisztrálása, csoportba sorolás (≈1,5 óra) | — |
| 13 | „Kilépő munkatárs" | — | Fiók letiltása; adatok megőrzése 30 napig, majd törlés | Nagy Péter jóváhagyása |
| 14 | „Nem működik a videóhívás otthonról" | Mobilnetes lefedettség (H-06) | Sávszélesség-mérés; ha tartósan gyenge, jelentés Nagy Péternek | Nagy Péter |
| 15 | „Angol feliratok az alkalmazásportálon" | Ismert hiba (H-08) | Nem hiba, javítás folyamatban a szállítónál | — |

## 5. Eszkalációs út az üzemeltetésben

| Szint | Kihez | Mikor | Elérhetőség |
|---|---|---|---|
| 1 | Service Desk | Minden felhasználói bejelentés | belső 4200, `servicedesk@xyo.hu` |
| 2 | Szabó Márk, rendszergazda | Konfigurációs kérdés, több felhasználót érintő hiba | belső 4215 |
| 3 | Nagy Péter, IT osztályvezető | Szolgáltatáskiesés, biztonsági esemény, szállítói kérdés | belső 4210 |
| 4 | **dr. Fekete Zsolt, DPO** | **Adatvédelmi incidens — AZONNAL, a szinteket átugorva** | belső 4180 |
| — | Cloudia Solutions támogatás | Szavatossági időn belüli konfigurációs hiba | a szerződés szerinti csatorna |
| — | TechLine Zrt. szerviz | Hardverhiba, garanciális | helyszíni, következő munkanap |

## 6. Szerződések és garanciák

| Szállító | Mire | Meddig | Mit fed |
|---|---|---|---|
| TechLine Zrt. | 50 munkaállomás-készlet | **2029.05.29.** (3 év) | Helyszíni szerviz, következő munkanapi kiszállás |
| Cloudia Solutions Kft. | Bevezetés (konfiguráció) | **2026.12.19.** (6 hó szavatosság) | Konfigurációs hibák díjmentes javítása |
| Microsoft (CSP-n keresztül) | M365 licenc | **2027.04.30.** | Szolgáltatási SLA |
| Microsoft (Azure) | VPN Gateway, infrastruktúra | folyamatos | Szolgáltatási SLA |

## 7. Ismert korlátok és nyitott hibák

| # | Mi | Hatás | Állapot |
|---|---|---|---|
| H-06 | 2 felhasználónál a videóhívás megszakad mobilneten | Korlátozott otthoni videóhívás | Nyitva, 2026.07.31., Nagy Péter, 240 000 Ft elkülönítve |
| H-08 | Alkalmazásportál hiányos magyar felirata | Kozmetikai | Nyitva, szállítói javítás 2026.09.30-ig |
| H-09 | Authenticator értesítés késése | Kényelmi | Figyelés alatt |
| H-13 | Alkalmazásportál ikon nem céges | Kozmetikai | Üzemeltetési feladat |
| — | Nincs adatvesztés-megelőzés (DLP) | 50 fős pilotnál elfogadott | **A kiterjesztésnél kötelező lesz** |
| — | Nincs hardveres biztonsági kulcs (FIDO2) | Elfogadott | A kiterjesztésnél újra vizsgálandó |
| — | Nem történt behatolásteszt | Elfogadott | **A kiterjesztés előtt javasolt** |

> Az utolsó három sor a *Biztonsági alapkonfiguráció* 7. pontjából származik:
> tudatosan nem vezettük be őket. Így látszik, hogy a döntés szándékos volt,
> és kész lista áll rendelkezésre arról, mit kell pótolni a kiterjesztésnél.

## 8. Visszaállási lehetőség

**2026.07.10-ig** a régi asztali gépek megmaradnak, bekapcsolható állapotban
(*Visszaállási terv*, V1–V3 előfeltételek).

**A selejtezés három feltétele:**

| # | Feltétel | Állapot |
|---|---|---|
| S1 | Az utolsó élesítési hullám után eltelt 4 hét | 2026.07.10. |
| S2 | A hypercare lezárult a kilépési feltétel teljesülésével | 2026.07.03. |
| S3 | Nagy Péter írásban nyilatkozik: nincs visszaállást indokoló nyitott hiba | — |

**Felelős:** Nagy Péter. Ez a projekt egyik nyitott pontja (NY-2).

## 9. Az átvevő nyilatkozata

> A Run-bookot átolvastam. Az abban foglaltak alapján az IT osztály a
> megoldást önállóan üzemeltetni tudja. A 7. pontban felsorolt korlátokat és
> nyitott hibákat ismerem és elfogadom.
>
> **Nagy Péter**, IT osztályvezető — 2026.06.26.

| Szerep | Név | Aláírás | Dátum |
|---|---|---|---|
| Átadó (projekt) | Tóth Gergő | | 2026.06.26. |
| Átadó (szállító) | Cloudia Solutions Kft. | | 2026.06.26. |
| **Átvevő** | **Nagy Péter**, IT osztályvezető | | 2026.06.26. |
| Átvevő (üzemeltetés) | Szabó Márk, rendszergazda | | 2026.06.26. |
| Átvevő (támogatás) | Kiss Réka, Service Desk vezető | | 2026.06.26. |

---

> **Kapcsolódó dokumentumok:** bemenete az *As-built dokumentáció*, a
> *Biztonsági alapkonfiguráció*, a *Visszaállási terv*, a *Felhasználói
> gyorssegédlet*, az *Oktatási anyag* és az *Átadás-átvételi jegyzőkönyv*;
> kimenete az *Archiválási jegyzék*.
