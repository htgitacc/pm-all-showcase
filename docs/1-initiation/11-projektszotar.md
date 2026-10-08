# Projektszótár (Project Glossary)

**Dokumentum azonosítója:** XYO-CP-011\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Létrehozva:** 2026. február 13.\
**Utolsó frissítés:** 2026. március 13.\
**Verzió:** 1.3 — **élő dokumentum**

> **Csak azok a fogalmak szerepelnek benne, amelyek körül ténylegesen volt
> félreértés.** A 200 elemes, senki által nem olvasott szótár rosszabb, mint a
> semmi. Minden bejegyzésnél szerepel, hogy **hol derült ki** a félreértés.

---

## 1. Fogalmak

### Felhasználó

| | |
|---|---|
| **Angolul** | user |
| **Mit jelent ebben a projektben** | **Egy természetes személy**, aki a pilot körbe tartozik és névre szóló Entra ID fiókkal rendelkezik. |
| **Mit NEM jelent** | Nem azonos a „licenc" vagy a „fiók" fogalmával: egy személyhez tartozhat szolgáltatásfiók is, ami nem felhasználó. |
| **Gazda** | Nagy Péter |
| **Honnan a félreértés** | A WBS-workshopon a HR „50 felhasználót" 50 munkavállalóként értette, az IT pedig 50 fiókként. A szolgáltatásfiókokkal együtt 54 fiók van — de **50 felhasználó**. |

### Élesítés

| | |
|---|---|
| **Angolul** | go-live |
| **Mit jelent ebben a projektben** | Az a nap, amikor egy felhasználó **átáll** az új környezetre, és a napi munkáját ott végzi. Nem egyetlen dátum: szakaszos, 2026.05.11-től 2026.06.12-ig. |
| **Mit NEM jelent** | Nem a rendszer kialakításának befejezését (az az M5 mérföldkő). |
| **Gazda** | Tóth Gergő |
| **Honnan a félreértés** | A Service Desk az M5-öt (2026.05.08.) tekintette élesítésnek, és arra tervezte a kapacitást. Valójában a terhelés 2026.06.12-ig elhúzódik. |

### Kész

| | |
|---|---|
| **Angolul** | done |
| **Mit jelent ebben a projektben** | Egy munkacsomag akkor kész, ha teljesíti a **WBS-szótárban rögzített kész-definícióját**, és a munkacsomag-felelős ezt írásban visszaigazolta. |
| **Mit NEM jelent** | Nem azt, hogy „a munka nagy része megvan". |
| **Gazda** | Tóth Gergő |
| **Honnan a félreértés** | Az első heti státuszon három munkacsomag is „90%-on" állt, ami a gyakorlatban bármit jelenthetett. |

### Pilot

| | |
|---|---|
| **Angolul** | pilot |
| **Mit jelent ebben a projektben** | **Éles, valós munkavégzés** korlátozott körben (50 fő), a kiterjeszthetőség eldöntése céljából. |
| **Mit NEM jelent** | Nem teszt és nem próbaüzem: a résztvevők a valódi munkájukat végzik, valódi adatokkal. |
| **Gazda** | Kovács Anita |
| **Honnan a félreértés** | Több területvezető „kipróbálásként" értelmezte, és azt hitte, a résztvevők a régi gépet is megtarthatják. |

### Migráció

| | |
|---|---|
| **Angolul** | migration |
| **Mit jelent ebben a projektben** | **Nem történik migráció.** A régi fájlszerver adatai a helyükön maradnak; az új munka SharePointon indul. |
| **Mit NEM jelent** | Nem jelenti azt, hogy a régi adatok elérhetetlenné válnak: 3 csapat olvasási hozzáférést kap VPN-en keresztül (N1 nyitott kérdés nyomán). |
| **Gazda** | Nagy Péter |
| **Honnan a félreértés** | A kick-offon (Q1 kérdés) derült ki, hogy többen adatvesztésre gondoltak. |

### Home office

| | |
|---|---|
| **Angolul** | remote work / home office |
| **Mit jelent ebben a projektben** | A HR home office szabályzata szerinti, **bejelentett és engedélyezett** otthoni munkavégzés. |
| **Mit NEM jelent** | Nem korlátlan és nem automatikus: a szabályzat kereteit a vezető engedélyezi. A projekt a **technikai lehetőséget** biztosítja, nem a jogosultságot. |
| **Gazda** | Varga Eszter |
| **Honnan a félreértés** | A pilot résztvevői között elterjedt, hogy a projekt „megadja" a home office-t. A projekt az eszközt adja; a jogosultságot a szabályzat és a vezető. |

### Támogatás

| | |
|---|---|
| **Angolul** | support |
| **Mit jelent ebben a projektben** | Két külön dolog, amit nem szabad összekeverni: **(1) hypercare** — a projekt által biztosított, 3 hetes fokozott támogatás az élesítés után; **(2) üzemeltetési támogatás** — a Service Desk normál működése, az átadás után. |
| **Gazda** | Kiss Réka |
| **Honnan a félreértés** | A tervezési szakaszban a „támogatás" szó mindkettőre használatban volt, ami a kapacitástervezést zavarta. |

### Baseline

| | |
|---|---|
| **Angolul** | baseline |
| **Mit jelent ebben a projektben** | **Két, eltérő jelentése van, és mindkettőt használjuk:** (1) **projekt-baseline** — a 2026.03.13-án befagyasztott hatókör, ütemterv és költségvetés; (2) **mérési baseline (T0)** — a 2026.01.30-i kiindulási mérési értékek. |
| **Gazda** | Tóth Gergő |
| **Honnan a félreértés** | A Steering ülésen „a baseline" hivatkozás kétértelmű volt. Azóta mindig jelezzük, melyikről van szó. |

### Eszközfelügyelet

| | |
|---|---|
| **Angolul** | device management (Intune / MDM) |
| **Mit jelent ebben a projektben** | A **céges eszköz** konfigurációjának és biztonsági beállításainak központi kezelése: titkosítás, frissítés, alkalmazástelepítés, elveszett eszköz távoli törlése. |
| **Mit NEM jelent** | **Nem terjed ki a magánhasználatra**, nem naplózza a böngészési előzményeket, és nem alkalmas munkavállalói megfigyelésre. (Üzemi tanács kikötése, L7 korlát.) |
| **Gazda** | Szabó Márk |
| **Honnan a félreértés** | Az üzemi tanácsi egyeztetésen merült fel a megfigyeléstől való félelem. |

## 2. Rövidítések

| Rövidítés | Feloldás | Mit jelent |
|---|---|---|
| MFA | Multi-Factor Authentication | Többtényezős hitelesítés — jelszó mellett egy második azonosítási lépés |
| CSP | Cloud Solution Provider | Microsoft-partner, aki a licencet forgalmazza és a bevezetést végzi |
| UAT | User Acceptance Testing | Felhasználói átvételi teszt — a felhasználók tesztelik, nem az IT |
| DPIA | Data Protection Impact Assessment | Adatvédelmi hatásvizsgálat |
| DPO | Data Protection Officer | Adatvédelmi tisztviselő |
| WBS | Work Breakdown Structure | Munkalebontási szerkezet |
| PIR | Post-Implementation Review | Utólagos értékelés a bevezetés után |
| SLA | Service Level Agreement | Szolgáltatási szintre vonatkozó megállapodás |
| MTTR | Mean Time To Resolve | Átlagos hibamegoldási idő |

## 3. Változásnapló

| Dátum | Bejegyzés | Kiváltó ok |
|---|---|---|
| 2026.02.13. | „Felhasználó", „Kész" | WBS-workshop |
| 2026.02.13. | „Migráció", „Pilot" | Kick-off Q1 és a területvezetői visszajelzések |
| 2026.02.20. | „Élesítés" | Service Desk kapacitástervezés |
| 2026.03.04. | „Baseline" | Steering ülés kétértelmű hivatkozása |
| 2026.03.11. | „Eszközfelügyelet" | Üzemi tanácsi egyeztetés |
| 2026.03.13. | „Home office", „Támogatás" | Planning-kapu átnézés |

---

> **Tanulság junior PM-nek:** ennek a szótárnak minden egyes bejegyzése egy
> **ténylegesen megtörtént félreértésből** származik. Nem előre találtuk ki a
> fogalmakat — akkor írtuk le őket, amikor kiderült, hogy két ember mást ért
> ugyanazon. Ez a módszer: ne szótárt írj, hanem félreértést rögzíts.

> **Kapcsolódó dokumentumok:** bemenete a *Projektalapító okirat*; kimenete a
> *Követelmény-nyomonkövetési mátrix* és a *Minőségterv*.
