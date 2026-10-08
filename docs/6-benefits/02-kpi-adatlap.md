# KPI-adatlap és mérési terv

**Dokumentum azonosítója:** XYO-CP-BEN-002\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő a mérési felelősökkel közösen\
**Dátum:** 2026. július 2.\
**Verzió:** 1.0

> **Minden mérőszámhoz egy adatlap: pontosan hogyan áll elő a szám.**
> Enélkül három hónap múlva senki nem tudja reprodukálni, és a mérés
> vitathatóvá válik.

---

## Áttekintő

| # | Mérőszám | Forrás | Kiolvasás napja | Felelős |
|---|---|---|---|---|
| M1 | Helpdesk ticketek | Service Desk ticketrendszer | hó 2. munkanap | Kiss Réka |
| M2 | MTTR | Service Desk ticketrendszer | hó 2. munkanap | Kiss Réka |
| M3 | Hozzáférési ticketek aránya | Service Desk ticketrendszer | hó 2. munkanap | Kiss Réka |
| M4 | Gépbeüzemelési idő | Intune Autopilot napló | eseményenként | Szabó Márk |
| M5 | Új belépő munkába állása | HR + IT folyamatmérés | eseményenként | Varga Eszter |
| M6 | Home office napok aránya | HR jelenléti rendszer | hó 3. munkanap | Varga Eszter |
| M7 | SharePoint/OneDrive adaptáció | M365 Usage Report | hó 2. munkanap | Szabó Márk |
| M8 | MFA-lefedettség | Entra ID hitelesítési riport | hó 2. munkanap | Szabó Márk |
| M9 | Rendelkezésre állás | M365 Service Health + Azure | hó 2. munkanap | Szabó Márk |
| M10 | Adatvesztési esetek | Service Desk + mentési napló | negyedév végén | Kiss Réka |
| M11 | Felhasználói elégedettség | Kérdőív (HR) | csak T+3 | Varga Eszter |
| M12 | Fajlagos IT-költség | Kontrolling | hó 3. munkanap | Balogh Tamás |

---

## M1 — Helpdesk ticketek száma

| | |
|---|---|
| **Definíció** | A pilot körből egy naptári hónapban bejelentett és lezárt helpdesk ticketek száma |
| **Képlet** | `db / hó` — egész szám |
| **Adatforrás** | Service Desk ticketrendszer |
| **Szűrő** | `szervezeti_egyseg IN (Penzugy, Ertekesites, Logisztika) AND bejelento IN (pilot_50) AND statusz = lezart AND datum BETWEEN honap_elso_nap AND honap_utolso_nap` |
| **Kiolvasás** | A hónapot követő **2. munkanapon**, hogy a hónap végi ticketek lezáródjanak |
| **T0** | 103 db/hó · **Cél** ≤ 72 · **Kudarcküszöb** > 95 |
| **Felelős** | Kiss Réka |
| **Torzító tényezők** | 1) A **júliusi-augusztusi szabadság** kb. 18%-kal csökkenti a munkanapokat. 2) A **betanulás** a T+1 hónapban növeli. 3) A **hypercare 07.03-ig** tart, a kiemelt támogatás több bejelentést generál. |
| **Ezért** | **A T+3 (szeptemberi) érték a mérvadó.** |

## M2 — Átlagos megoldási idő (MTTR)

| | |
|---|---|
| **Definíció** | A lezárt ticketek `bejelentés → lezárás` idejének átlaga, **munkaidőben** számolva |
| **Képlet** | `SUM(lezaras - bejelentes, munkaido) / lezart_ticketek_szama` |
| **Adatforrás** | Service Desk ticketrendszer, ugyanaz a szűrő, mint M1 |
| **Munkaidő definíciója** | H–P 7:30 – 17:00; hétvége és ünnepnap nem számít bele |
| **T0** | 11,4 óra · **Cél** ≤ 6,0 · **Kudarcküszöb** > 10,0 |
| **Felelős** | Kiss Réka |
| **Torzító tényező** | Az önkiszolgáló jelszó-visszaállítás miatt a **gyors, egyszerű ticketek eltűnnek** a mintából — ez a maradék átlagot **felfelé** tolhatja |

> **Az utolsó sor fontos.** Ha a legkönnyebb ticketeket megszünteti egy
> funkció, a maradék átlagos megoldási ideje nőhet, miközben a szolgáltatás
> javult. Ezt előre le kell írni, különben a T+3-nál vitatható lesz.

## M3 — Hozzáférési / jelszó ticketek aránya

| | |
|---|---|
| **Definíció** | A `hozzáférés` és `jelszó` kategóriájú ticketek aránya az összes tickethez |
| **Képlet** | `hozzaferesi_ticketek / osszes_ticket × 100` |
| **Szűrő** | M1 szűrője + `kategoria IN (hozzaferes, jelszo)` |
| **T0** | 41% · **Cél** ≤ 20 · **Kudarcküszöb** > 35 |
| **Felelős** | Kiss Réka |
| **Miért fontos** | A T0 méréskor ez volt a **legnagyobb ticketkategória**. Az önkiszolgáló jelszó-visszaállítás (K27 követelmény) elsősorban ezt célozza. |

## M4 — Gépbeüzemelési idő

| | |
|---|---|
| **Definíció** | Egy új gép beüzemelése az Autopilot folyamat indításától a felhasználónak való átadhatóságig |
| **Képlet** | Átlag, a mérési időszakban beüzemelt gépekre |
| **Adatforrás** | Intune Autopilot naplók, `deployment_start` – `deployment_complete` |
| **Kiolvasás** | Eseményenként, gépenként rögzítve |
| **T0** | 6,5 óra (9 gép átlaga) · **Cél** ≤ 1,5 · **Kudarcküszöb** > 3,0 |
| **Felelős** | Szabó Márk |
| **Torzító tényező** | **Kis elemszám** — a mérési időszakban várhatóan 6-8 gép. Az átlag mellé a **tartományt** is közöljük. |

## M5 — Új belépő munkába állásáig eltelt idő

| | |
|---|---|
| **Definíció** | A HR-igény beérkezésétől a munkára kész gép átadásáig eltelt munkanapok száma |
| **Adatforrás** | HR belépési nyilvántartás + IT átadási jegyzőkönyv |
| **T0** | 3,5 munkanap (8 belépő) · **Cél** ≤ 1,0 · **Kudarcküszöb** > 2,0 |
| **Felelős** | Varga Eszter |
| **Torzító tényező** | Kis elemszám (várhatóan 2-4 belépő); a tartományt is közöljük |

## M6 — Home office napok aránya

| | |
|---|---|
| **Definíció** | A pilot körben otthonról ledolgozott munkanapok aránya az összes ledolgozott munkanaphoz |
| **Képlet** | `home_office_napok / osszes_ledolgozott_munkanap × 100` |
| **Adatforrás** | HR jelenléti rendszer |
| **Fontos** | **Arányszám, nem abszolút napszám** — nyáron kevesebb a munkanap |
| **T0** | 0% · **Cél** ≥ 40 · **Kudarcküszöb** < 20 |
| **Felelős** | Varga Eszter |
| **⚠ Adatvédelem** | **Kizárólag csoportszintű összesítés.** Egyéni bontású home office statisztika nem készíthető és nem adható ki a vezetőknek. |

## M7 — SharePoint / OneDrive adaptáció

| | |
|---|---|
| **Definíció** | Az adott hónapban legalább egyszer aktív felhasználók aránya a pilot körben |
| **Képlet** | `aktiv_felhasznalok / 50 × 100` |
| **Adatforrás** | Microsoft 365 Usage Report → *SharePoint activity* és *OneDrive activity*, 30 napos időszak |
| **Aktivitás definíciója** | Fájl megnyitása, létrehozása, szerkesztése vagy megosztása |
| **T0** | 0% · **Cél** ≥ 90 · **Kudarcküszöb** < 70 |
| **Felelős** | Szabó Márk |
| **⚠ Adatvédelem** | A riportot **anonimizált módban** kell lekérni (M365 admin beállítás). Egyéni felhasználói aktivitás nem kerül ki a mérésbe. |
| **Kapcsolódó kockázat** | **R5** — a 70% alatti érték a kockázat bekövetkezési jelzése |

## M8 — MFA-lefedettség

| | |
|---|---|
| **Definíció** | A regisztrált MFA-módszerrel rendelkező pilot felhasználók aránya |
| **Adatforrás** | Entra ID → *Authentication methods activity* |
| **T0** | 0% · **Cél** 100 · **Kudarcküszöb** < 100 |
| **Felelős** | Szabó Márk |
| **Megjegyzés** | Bináris mutató: bármely érték 100% alatt kudarc. Belépőnél a regisztráció az átadás része. |

## M9 — Szolgáltatás-rendelkezésre állás

| | |
|---|---|
| **Definíció** | A tervezetten kívüli szolgáltatáskiesés nélküli üzemidő aránya |
| **Képlet** | `(elvart_uzemido - kieses) / elvart_uzemido × 100` |
| **Elvárt üzemidő** | H–P 7:30 – 17:00 |
| **Adatforrás** | M365 Service Health + Azure Service Health + Service Desk incidensek |
| **Mibe számít bele** | M365, SharePoint, OneDrive, Entra ID, Azure VPN kiesése |
| **T0** | 97,8% (fájlszerver) · **Cél** ≥ 99,5 · **Kudarcküszöb** < 99,0 |
| **Felelős** | Szabó Márk |
| **Torzító tényező** | A T0 a **fájlszerverre** vonatkozott; a felhős szolgáltatás más profilú. Az összehasonlítás **irányadó, nem szigorúan azonos alapú**. |

## M10 — Adatvesztéssel járó esetek

| | |
|---|---|
| **Definíció** | Olyan eset, ahol munkafájl véglegesen, visszaállíthatatlanul elveszett |
| **Adatforrás** | Service Desk ticketek (`adatvesztes` kategória) + mentési/visszaállítási napló |
| **Kiolvasás** | Negyedév végén |
| **T0** | 0,75 db/negyedév (3 db/év) · **Cél** 0 · **Kudarcküszöb** ≥ 1 |
| **Felelős** | Kiss Réka |
| **Megjegyzés** | A sikeres visszaállítás **nem** adatvesztés. Csak a véglegesen elveszett fájl számít. |

## M11 — Felhasználói elégedettség

| | |
|---|---|
| **Definíció** | 6 kérdéses kérdőív átlaga, 1–5 skálán |
| **Adatforrás** | Kérdőív, HR bonyolítja, **névtelenül** |
| **Kiolvasás** | **Csak T+3-kor** (2026.09.30.) |
| **Kritikus szabály** | **Ugyanazok a kérdések, mint a T0-nál.** Ha a kérdések változnak, az eredmény nem összehasonlítható. |
| **T0** | 3,1 (38 válasz, 73%) · **Cél** ≥ 4,0 · **Kudarcküszöb** < 3,5 |
| **Felelős** | Varga Eszter |
| **⚠ Adatvédelem** | Névtelen; csak összesített eredmény közölhető |

## M12 — Fajlagos IT-költség

| | |
|---|---|
| **Definíció** | A pilot kör IT-szolgáltatásának **folyó (OPEX)** költsége főre és hónapra vetítve |
| **Képlet** | `eves_folyo_koltseg / 50 / 12` |
| **Mit tartalmaz** | M365 licenc + Azure/VPN + mobilinternet-hozzájárulás |
| **Mit NEM tartalmaz** | Az egyszeri beruházást (hardver, bevezetés) — **jelzett módon** |
| **Adatforrás** | Kontrolling, IT-2026-UZ költséghely |
| **T0** | 12 667 Ft/fő/hó · **Cél** ≤ 20 000 · **Kudarcküszöb** > 24 000 |
| **Felelős** | Balogh Tamás |
| **Megjegyzés** | **A célérték tudatosan magasabb a T0-nál.** A projekt nem költségmegtakarítási projekt — ezt az Üzleti indoklás nyíltan kimondta. |

---

## Ellenőrzőlista minden havi méréshez

| # | Mielőtt a riportot elküldöd |
|---|---|
| 1 | Ugyanazt a szűrőt használtad, mint a T0-nál? |
| 2 | A kiolvasás a megadott napon történt? |
| 3 | Az anonimizált riportmódot használtad az M6 és M7 esetében? |
| 4 | A kis elemszámú mutatóknál (M4, M5) közölted a tartományt is? |
| 5 | Jeleztél minden adathiányt — nem pótoltad becsléssel jelölés nélkül? |
| 6 | A torzító tényezőket megjegyzésben feltüntetted? |

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő a mérési felelősökkel | 2026.07.02. |
| Jóváhagyta | Nagy Péter, a hasznok gazdája | 2026.07.02. |

> **Kapcsolódó dokumentumok:** bemenete a *Haszonrealizálási terv*; kimenete a
> *T0 baseline jegyzőkönyv* és a *Havi mérési riportok*.
