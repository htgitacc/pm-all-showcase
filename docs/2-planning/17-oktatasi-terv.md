# Oktatási és adaptációs terv (Training and Adoption Plan)

**Dokumentum azonosítója:** XYO-CP-117\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Varga Eszter (HR) és Tóth Gergő (PM), Kiss Rékával egyeztetve\
**Verzió:** 1.1

> **Verziójegyzet:** a nyertes szállító neve (Cloudia Solutions Kft.) a szerződéskötés után, 2026.04.20-án került a dokumentumba. A korábbi változatban a beszerzési tételek (B1–B4) szerepeltek; a baseline tartalma — hatókör, ütem, költség — ezzel nem változott.

> **A technológia működni fog; az emberek elfogadása a valódi kockázat.**
> Egy IT bevezetés sikere nem a rendszeren, hanem azon múlik, hogy a
> felhasználók tudják és **akarják** is használni.

---

## 1. Célcsoportok és tudásigény

| Célcsoport | Létszám | Mit kell tudnia | Formátum | Időtartam |
|---|---:|---|---|---|
| **Pilot felhasználók** | 50 fő | Belépés, MFA, OneDrive, SharePoint, VPN, hibabejelentés | Csoportos, 5 × 10 fő | 3 óra / csoport |
| **UAT tesztcsoport** | 10 fő | Ugyanez + hibabejelentés módja, tesztesetek | Külön, korábbi alkalom | 3 + 1 óra |
| **Service Desk** | 3 fő | Hibatípusok, megoldások, eszkaláció, admin felület alapjai | Műhelymunka | 4 óra |
| **Területvezetők** | 3 fő | Mi változik a csapatuknál, mit várhatnak | Rövid tájékoztató | 1 óra |
| **Rendszergazda** | 1 fő | Entra ID, Intune, SharePoint jogosultság, Azure VPN üzemeltetés | Szállítói oktatás + közös munka | 3 nap |

## 2. Ütemezés

| Mit | Kinek | Dátum |
|---|---|---|
| Területvezetői tájékoztató | 3 fő | 2026.04.28. |
| Service Desk műhelymunka | 3 fő | 2026.04.27. |
| Rendszergazdai oktatás (szállítói) | Szabó Márk | 2026.04.27–05.06. |
| **UAT csoport oktatása** | 10 fő — élesítés 05.11. | **2026.05.07.** |
| 2. csoport oktatása | 10 fő — élesítés 06.03. | 2026.06.01. |
| 3. csoport oktatása | 10 fő — élesítés 06.04–05. | 2026.06.02. |
| 4. csoport oktatása | 10 fő — élesítés 06.10. | 2026.06.08. |
| 5. csoport oktatása | 10 fő — élesítés 06.11–12. | 2026.06.09. |
| **Pótló alkalom a hiányzóknak** | max. 10 fő | **2026.06.10.** |

> **Az oktatás mindig a csoport élesítése ELŐTT van**, 2–4 nappal.
> Ha túl korán van, elfelejtik; ha utána, akkor az első napokat
> segítség nélkül szenvedik végig. **És csak akkor, ha a csoport gépei már
> megérkeztek** — mindenki a saját gépén tanul, a 2–5. csoport 40 gépe pedig
> 05.29-re érkezik.

## 3. Oktatási tematika (3 óra)

| Blokk | Idő | Tartalom |
|---|---:|---|
| 1. Miért csináljuk? | 15 perc | Mit nyersz vele: home office, gyorsabb támogatás, bárhonnan elérhető fájlok |
| 2. Első belépés | 25 perc | Entra ID azonosító, MFA beállítása telefonon — **mindenki a saját gépén** |
| 3. Fájlok az új világban | 45 perc | OneDrive vs. SharePoint: mit hova; megosztás; egyidejű szerkesztés |
| — | 15 perc | szünet |
| 4. Otthoni munkavégzés | 30 perc | Dokkoló, monitor, VPN indítása, videóhívás |
| 5. Ha valami nem megy | 20 perc | Gyorssegédlet, önkiszolgáló jelszó-visszaállítás, Service Desk elérése |
| 6. Kérdések és szabad gyakorlás | 30 perc | |

**Alapelvek:**

- **Mindenki a saját gépén dolgozik** az oktatás alatt, nem vetítést néz.
- Az MFA beállítása az oktatáson történik meg, nem otthon.
- A magyar nyelvű gyorssegédletet mindenki megkapja kinyomtatva is.
- Az oktató a Cloudia Solutions konzultánsa, de **Kiss Réka végig jelen van** —
  így hallja, hol akadnak el az emberek, még az élesítés előtt.

## 4. Segédanyagok

| Anyag | Kinek | Formátum | Ki készíti | Határidő |
|---|---|---|---|---|
| Felhasználói gyorssegédlet | 50 fő | 4 oldal, magyar, képernyőképes, PDF + nyomtatott | Cloudia Solutions, Kiss Réka lektorálja | 2026.05.15. |
| Oktatási diasor | oktatók | PPTX | Cloudia Solutions | 2026.05.06. |
| Service Desk hibakezelési útmutató | 3 fő | 15 leggyakoribb hibatípus, tünet-ok-teendő | Kiss Réka, Szabó Márkkal | **2026.04.27.** |
| „Első heted az új gépen" e-mail | 50 fő | rövid e-mail az élesítés napján | Tóth Gergő | hullámonként |
| Videós mini-útmutatók (3 db, 2-3 perc) | 50 fő | SharePointon | Cloudia Solutions | 2026.05.15. |

> A gyorssegédletet **oda kell tenni, ahol keresni fogják**, és el is kell
> mondani, hol van. A SharePointon eldugott PDF-et senki nem találja meg —
> ezért kap mindenki nyomtatott példányt is a géppel együtt.

## 5. Hypercare — a bevezetés utáni fokozott támogatás

| | |
|---|---|
| **Időszak** | 2026.06.15 – 2026.07.03. (3 hét, az utolsó hullám után) |
| **Mit jelent** | Kiemelt válaszidő a „CP" címkés ticketekre: 2 óra; napi hibaáttekintés; helyszíni segítség igény szerint |
| **Kapacitás** | Kiss Réka + 2 Service Desk munkatárs, összesen 68 óra |
| **Kilépési feltétel** | A napi új hibabejelentések száma **két egymást követő héten a normál szint 150%-a alá** csökken |
| **Ha nem teljesül** | A hypercare meghosszabbítása a projektzáráson túl, Nagy Péter felelősségével |

> **A hypercare a legtöbb IT projektből hiányzik.** Nélküle az élesítés utáni
> hetekben a Service Deskre zúdul minden, a felhasználók magukra maradnak, és a
> technikailag hibátlan bevezetés is kudarcként rögzül a szervezet emlékezetében.

## 6. Változáskezelés — miért jó ez nekik?

Nem elég megtanítani a rendszert; el kell fogadtatni a változást.

| Ellenérzés | Amit hallani fogsz | Válasz |
|---|---|---|
| Félelem a megfigyeléstől | „Most majd látják, mikor kapcsolom be a gépet" | Az eszközfelügyelet **nem terjed ki a magánhasználatra** (L7, üzemi tanácsi kikötés). A mérés csoportszintű, nem egyéni. |
| Félelem a tudáshiánytól | „Én ehhez nem értek" | Oktatás mindenkinek, gyorssegédlet, 3 hét hypercare, pótló alkalom |
| A régi megszokás | „Eddig is jó volt a fájlszerver" | Otthonról nem érhető el. A home office lehetőség csak így működik. |
| Bizalmatlanság a felhővel | „Hol vannak az adataim?" | EU-s adatközpontban, a DPO által jóváhagyott feltételekkel (L6) |
| Méltányossági kérdés | „Miért ő és nem én?" | A kijelölési szempontok előre kommunikálva; sikeres pilot esetén mindenkire kiterjed |

**A legerősebb érv a home office.** Ezt kell a kommunikáció középpontjába
tenni — nem a technológiát.

## 7. Adaptáció mérése

| Mit mérünk | Cél | Mikor | Ki |
|---|---|---:|---|
| Oktatáson részt vettek aránya | 100% | hullámonként | Varga Eszter |
| SharePoint/OneDrive aktív felhasználók | ≥ 90% | havonta | Szabó Márk |
| „CP" címkés ticketek száma | csökkenő trend | hetente | Kiss Réka |
| Gyorssegédlet letöltések / megnyitások | — (tájékoztató) | havonta | Szabó Márk |
| Elégedettség (1–5) | ≥ 4,0 | T+3 | Varga Eszter |

> Ha az adaptációs mutató 4 héttel az élesítés után **70% alatt van**, az az
> R5 kockázat bekövetkezési jelzése — beavatkozás kell (pótoktatás, célzott
> segítség), nem türelem.

## 8. Kockázatok

| Kockázat | Kezelés |
|---|---|
| A hiányzók lemaradnak, és ők adják a legtöbb ticketet | Kötelező pótló alkalom 06.10-én, dokumentált jelenléttel |
| Az oktatás túl korán van, elfelejtik | Az élesítés előtt 2–4 nappal |
| A Service Desk nem tud segíteni, mert ő sem ismeri | Felkészítés **2 héttel** az első élesítés előtt (AK-22) |
| A vezetők nem támogatják a home office-t | Külön területvezetői tájékoztató 04.28-án |

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Varga Eszter, HR vezető | 2026.03.09. |
| Készítette | Tóth Gergő, projektmenedzser | 2026.03.09. |
| Egyeztette | Kiss Réka, Service Desk vezető | 2026.03.10. |
| Jóváhagyta | Projekt Irányító Bizottság | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete a *Kommunikációs terv* és a
> *Hatókör-nyilatkozat*; kimenete az *Oktatási anyag*, a *Felhasználói
> gyorssegédlet* és a *Felhasználói elégedettségi kérdőív*.
