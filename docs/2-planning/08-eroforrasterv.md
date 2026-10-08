# Erőforrásterv (Resource Plan)

**Dokumentum azonosítója:** XYO-CP-108\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Verzió:** 1.1 — **baseline, befagyasztva 2026.03.13-án**

> **Verziójegyzet:** a nyertes szállítók neve (Cloudia Solutions Kft., TechLine Zrt.) a szerződéskötés után, 2026.04.20-án került a dokumentumba. A korábbi változatban a beszerzési tételek (B1–B4) szerepeltek; a baseline tartalma — hatókör, ütem, költség — ezzel nem változott.

> **A projekten mindenki a napi munkája mellett dolgozik.** Ezért nem elég
> megtervezni a ráfordítást — **írásos kapacitás-jóváhagyás kell a szervezeti
> vezetőtől.** A szóbeli ígéret az első üzemi tűzoltásnál elpárolog.

---

## 1. Belső erőforrások

| Név | Szerep a projektben | Ráfordítás | Időszak | Kapacitás jóváhagyva |
|---|---|---:|---|---|
| Tóth Gergő | projektmenedzser | 240 óra (~30%) | 02.02 – 06.30 | ✔ Kovács Anita, 2026.02.02. |
| Nagy Péter | szakmai vezető, a hasznok gazdája | 180 óra (~20%) | 02.09 – 09.30 | ✔ Horváth Júlia, 2026.02.13. |
| Szabó Márk | rendszergazda | 220 óra (~25% a teljes időszakra; keret: heti 12 óra) | 03.16 – 06.30 | ✔ Nagy Péter, 2026.02.13. |
| Molnár Katalin | beszerzés | 96 óra | 02.10 – 04.17 | ✔ Kovács Anita, 2026.02.20. |
| Kiss Réka | Service Desk, hypercare | 84 óra | 03.16 – 07.03 | ✔ Nagy Péter, 2026.02.24. |
| Varga Eszter | HR, oktatás, kommunikáció | 72 óra | 02.16 – 06.30 | ✔ Horváth Júlia, 2026.02.20. |
| Balogh Tamás | kontrolling | 24 óra | 03.16 – 06.30 | ✔ Kovács Anita, 2026.02.20. |
| dr. Fekete Zsolt | DPO | 24 óra | 02.12 – 03.20 | ✔ Horváth Júlia, 2026.02.13. |
| UAT tesztcsoport (10 fő) | felhasználói tesztelés | 80 óra összesen | 05.11 – 05.22 | ✔ területvezetők, 2026.03.09. |
| Service Desk munkatársak (2 fő) | hypercare támogatás | 40 óra | 06.15 – 07.03 | ✔ Kiss Réka, 2026.02.24. |
| | **Belső összesen** | **1 060 óra** | | |

> **A WBS 948 belső órájához képest 112 óra a többlet.** Az erőforrásterv a
> teljes *személyes* ráfordítást tartalmazza: a Service Desk két munkatársának
> hypercare-óráit (40 óra) és a vezetői, kontrolling- és jóváhagyási részvételt
> (Steering, státusz, kapuk), amely a WBS-ben nem önálló munkacsomag. A WBS az
> *eredmények* ráfordítását méri, az erőforrásterv az *emberekét* — a kettő
> ezért nem egyezik, és nem is kell egyeznie, de az eltérést meg kell tudni
> magyarázni.

## 2. Külső erőforrás

| Szállító | Szerep | Ráfordítás | Időszak | Alapja |
|---|---|---:|---|---|
| Cloudia Solutions Kft. | bevezetési konzultáns (2 fő) | 312 óra | 04.20 – 06.19 | 6 500 000 Ft átalánydíj |
| TechLine Zrt. | hardverszállítás és Autopilot-regisztráció | — | 04.20 – 05.29 | szállítási szerződés |

**A szerződés kötelező eleme:** helyettesítési kötelezettség, ha a nevesített
konzultáns kiesik (R14 kockázat válaszlépése), és **tudásátadás + Run-book
átadása teljesítési feltételként** (F-4 feltétel).

## 3. Terhelés hónapokra bontva

| Fő | 02 | 03 | 04 | 05 | 06 | 07 |
|---|---:|---:|---:|---:|---:|---:|
| Tóth Gergő | 60 | 50 | 40 | 45 | 45 | — |
| Nagy Péter | 20 | 25 | 35 | 50 | 40 | 10 |
| Szabó Márk | — | 8 | 60 | 90 | 62 | — |
| Molnár Katalin | 4 | 40 | 52 | — | — | — |
| Kiss Réka | — | 4 | 16 | 24 | 30 | 10 |
| Varga Eszter | 12 | 16 | 12 | 20 | 12 | — |
| Balogh Tamás | — | 6 | 6 | 6 | 6 | — |
| dr. Fekete Zsolt | 12 | 12 | — | — | — | — |
| UAT csoport (10 fő) | — | — | — | 80 | — | — |
| Service Desk (2 fő) | — | — | — | — | 28 | 12 |
| **Havi összesen** | **108** | **161** | **221** | **315** | **223** | **32** |

*A táblázat a kezelés **előtti** tervet mutatja; a májusi csúcs kezelését lásd lent.*

### Terhelési csúcs: 2026. május

**Szabó Márk áprilistól júniusig végig a heti 12 órás keret fölött van**
(április ~15, június ~14 óra/hét), a csúcs pedig május: **90 óra, heti ~24 óra**
(19 munkanap) — a keret duplája.

| | |
|---|---|
| **Miért** | A környezet kialakítása, a technikai teszt és az első két élesítési hullám egy hónapra esik |
| **Hatás** | R4 kockázat (belső kapacitáshiány) bekövetkezik |
| **Kezelés** | 1) A 3.1.x, 3.2.x és 3.4.x munkacsomagok **végrehajtója a Cloudia Solutions**, Szabó Márk csak átvevő és véleményező (lásd RACI). 2) A 3.3.2 (mentés, visszaállítási teszt) átütemezve 05.05–05.08-ra, amikor a szállítói munka fut. 3) Nagy Péter írásban vállalta, hogy májusban Szabó Márkot mentesíti a napi ügyeleti beosztás alól. |
| **Maradék terhelés** | A kezelés után kb. 62 óra májusban (heti ~16 óra) — a keret fölött, de az ügyeleti mentesítés ezt fedezi; figyelendő |
| **Figyelés** | A heti státuszon Szabó Márk külön kérdést kap: „belefért a heti keretbe?" |

## 4. Kompetenciahiányok és pótlásuk

| Terület | Ki | Hiány | Pótlás | Mikor |
|---|---|---|---|---|
| Entra ID, feltételes hozzáférés | Szabó Márk | alapszintű tudás | CSP partner oktatása (a bevezetési díj része) | 04.27 – 05.06. |
| Intune, Autopilot | Szabó Márk | nincs tapasztalat | Közös munkavégzés a szállítóval + Run-book | 04.27 – 06.19. |
| SharePoint jogosultságkezelés | Nagy Péter, Szabó Márk | alapszintű | Dokumentált jogosultsági modell + oktatás | 04.20 – 05.04. |
| Azure hálózat, VPN | Szabó Márk | nincs tapasztalat | A szállító alakítja ki; Run-book átadás | 04.22 – 06.19. |

> **Ezért kötöttük ki a tudásátadást teljesítési feltételként.** Ha a szállító
> kialakítja a környezetet, de a belső csapat nem érti, akkor az üzemeltetésbe
> adás formálisan megtörténik, a gyakorlatban viszont minden hibánál a szállítót
> kell hívni — pénzért.

## 5. Az UAT tesztcsoport

| | |
|---|---|
| **Létszám** | 10 fő, az első élesítési hullám résztvevői |
| **Kiválasztás szempontjai** | Területenként legalább 1 fő; legyen köztük 2 kevésbé IT-affin munkatárs; legyen köztük legalább 3, aki rendszeresen otthonról dolgozna |
| **Ráfordítás** | fejenként 8 óra tesztelési többletmunka 2 hét alatt |
| **Jóváhagyás** | A területvezetők (Szilágyi Anna, Fodor Gábor, Papp Zsófia) írásban, 2026.03.09. |

> **A 2 kevésbé IT-affin munkatárs bevonása szándékos.** Ha csak a lelkes,
> technikailag magabiztos kollégák tesztelnek, a teszt nem mutatja meg, hol fog
> elakadni a többség — és pont ők adják majd a helpdesk ticketek nagy részét.

## 6. Erőforrás-elengedés

| Ki | Mikortól szabadul fel |
|---|---|
| Molnár Katalin | 2026.04.20. (a szerződéskötés után) |
| dr. Fekete Zsolt | 2026.03.20. (a DPIA lezárása után) |
| UAT tesztcsoport | 2026.05.22. |
| Cloudia Solutions | 2026.06.19. (az UAT-elfogadás után) |
| Szabó Márk, Tóth Gergő, Varga Eszter, Balogh Tamás | 2026.06.30. |
| Kiss Réka | 2026.07.03. (a hypercare után) |
| Nagy Péter | **2026.09.30.** — a mérési szakasz végéig marad, a hasznok gazdájaként |

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.03.06. |
| Kapacitást jóváhagyta | a szervezeti vezetők (lásd 1. táblázat) | 2026.02.13 – 03.09. |
| Jóváhagyta | Projekt Irányító Bizottság | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete a *WBS* és az *Ütemterv*; kimenete a
> *RACI mátrix*, az *Erőforrás-elengedés* és a *Kockázatnyilvántartás*.
