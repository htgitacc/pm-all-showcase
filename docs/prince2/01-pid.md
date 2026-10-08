# PID — Projekt-kezdeményezési dokumentáció

*(Project Initiation Documentation)*

**Dokumentum azonosítója:** XYO-P2-001\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, Project Manager\
**Jóváhagyta:** **Project Board** — 2026. március 13.\
**Verzió:** 1.0 — *baseline*

> ⚠ **PRINCE2-kiegészítés.** Ez a dokumentum nem része a projekt PMI szerinti
> dokumentációjának. Azt mutatja meg, **hogyan nézne ki ugyanez a projekt
> PRINCE2 szerint** — a valós Xyo-adatokkal.
>
> **A PID a PMI Project Charter és a Project Management Plan együttese.**
> Ez a projekt „szerződése" a Project Manager és a Project Board között: a
> Board ezt hagyja jóvá, és ehhez képest kéri számon a PM-et.

---

## 1. A projekt definíciója

### 1.1 Háttér

A Xyo Kft. 50 asztali gépe elavult (átlagéletkor 6,2 év), a csere a következő
két évben elkerülhetetlen. A cég cloud-first irányt vesz. A pilot célja, hogy
**éles működésben derüljön ki**, alkalmas-e a felhőalapú munkakörnyezet a
vállalatra, mielőtt a teljes, kb. 240 fős létszámra kiterjesztenénk.

### 1.2 Célkitűzések és teljesítménycélok

| Cél | Mérőszám | Célérték | Mikor |
|---|---|---:|---|
| Élesben működő felhőkörnyezet | Élesített felhasználók | 50 fő | 2026.06.12. |
| Egységes azonosítás | MFA-lefedettség | 100% | 2026.06.19. |
| A projekt a kereten belül zárul | Tényleges költés | ≤ 52 000 000 Ft | 2026.06.30. |
| Csökkenő támogatási terhelés | Ticket / hó | ≤ 72 | 2026.09.30. |
| Gyorsabb hibaelhárítás | MTTR | ≤ 6,0 óra | 2026.09.30. |
| Rugalmas munkavégzés | Home office arány | ≥ 40% | 2026.09.30. |
| Felhasználói elfogadás | Elégedettség | ≥ 4,0 | 2026.09.30. |
| Döntési alap | Kiterjesztési javaslat | elkészül | 2026.10.09. |

### 1.3 A projekt hatóköre és kizárásai

**Benne van:** 50 munkaállomás-készlet beszerzése és kiosztása · M365 Business
Premium licenc · Entra ID, MFA, feltételes hozzáférés · Intune eszközfelügyelet
és Autopilot · SharePoint/OneDrive · Azure VPN · oktatás és hypercare ·
a 3 hónapos mérési szakasz megtervezése és lebonyolítása.

**Kifejezetten nincs benne:**

| # | Kizárás |
|---|---|
| K1 | Adatmigráció a régi fájlszerverről |
| K2 | Gyártósori és termelésirányítási rendszerek |
| K3 | Telefonközpont felhőbe költöztetése |
| K4 | Pénzügyi és bérszámfejtő rendszer átalakítása |
| K5 | Kiterjesztés a pilot körön kívülre |
| K6 | Szakmai szoftverek telepítése |
| K7 | Az irodai monitorok cseréje |
| K8–K11 | *(a projekt közben felmerült, elutasított kérések — élő lista)* |

### 1.4 Korlátok és feltevések

| # | Korlát |
|---|---|
| L1 | A projektnek 2026.06.30-ig le kell zárulnia |
| L2 | A költségkeret 52 000 000 Ft, nem növelhető |
| L3 | Az IT részlegről 2 fő áll rendelkezésre, napi munka mellett |
| L4 | A pilot köre 50 fő |
| L5 | A beszerzési szabályzat szerinti eljárás kötelező |
| L6 | Az adatok kizárólag EU-s adatközpontban tárolhatók |
| L7 | Az eszközfelügyelet nem terjedhet ki a magánhasználatra |

Feltevések: a dolgozói mobilcsomagok korlátlanok · a home office szabályzat
2026.04.30-ig hatályba lép · a laptopszállítás 6 héten belül teljesül ·
a CSP partner rendelkezésre áll.

### 1.5 A projekt végterméke

> **Projekt-végtermék leírása** *(Project Product Description)* — a PRINCE2
> termékalapú tervezésének kiindulópontja.

| | |
|---|---|
| **Cím** | Működő, felhőalapú munkakörnyezet 50 munkatárs számára |
| **Cél** | A felhasználó céges laptopon, Entra ID azonosítóval, irodából és otthonról egyaránt tud dolgozni, a dokumentumait felhőben tárolva |
| **Fő összetevők** | Beüzemelt munkaállomás-készlet · konfigurált felhőkörnyezet · felkészített felhasználók · üzemeltetési dokumentáció |
| **Minőségi elvárások** | Mind az 50 felhasználó belép MFA-val · a beüzemelés ≤ 1,5 óra · a VPN otthoni mobilnetről működik · a törölt fájl 30 napig visszaállítható |
| **Elfogadási módszer** | Felhasználói átvételi teszt (UAT) + az átvételi kritériumok tételes végigvezetése |
| **Elfogadásra jogosult** | Senior User (Nagy Péter) és a felhasználói képviselő (Fodor Gábor) |

---

## 2. Üzleti indoklás *(Business Case)*

> **PRINCE2-ben ez élő dokumentum.** Minden szakaszhatáron felül kell
> vizsgálni; ha az indokoltság megszűnik, a projektet le kell állítani.

| | |
|---|---:|
| Tervezett költség | 50 743 000 Ft |
| Ebből tartalék | 4 613 000 Ft |
| Jóváhagyott keret | 52 000 000 Ft |
| 2. évtől folyó költség | 10 680 000 Ft / év |
| Várt kapacitás-haszon | 9 176 700 Ft / év |

**A projekt nem költségmegtakarítási projekt.** Három évre nagyjából
nullszaldós. A döntést az indokolja, hogy (1) a gépcsere elkerülhetetlen,
(2) a home office lehetőség munkaerő-megtartási értéke a számításban nem
szerepel, és (3) a pilot **döntési opciót vásárol**: 50 M Ft-ért megtudjuk,
érdemes-e 120 M Ft-ot költeni a teljes szervezetre.

### Felülvizsgálati pontok

| Szakaszhatár | Mikor | Mit nézünk újra |
|---|---|---|
| 1. szakasz vége | 2026.03.13. | A tervezés pontosította-e a költséget? |
| 2. szakasz vége | 2026.04.17. | **A beszerzés eredménye hogyan hat a megtérülésre?** |
| 3. szakasz vége | 2026.06.19. | A minőség és az átvétel igazolja-e a várt hasznokat? |
| Projekt vége | 2026.06.30. | Átadható-e a haszonmérés? |
| PIR | 2026.10.09. | **Megjöttek-e a hasznok?** |

---

## 3. Szervezeti felépítés

```
        Vállalatvezetés — Horváth Júlia, ügyvezető
                          │
        ┌─────────────────▼─────────────────┐
        │         PROJECT BOARD             │
        │  Executive:      Kovács Anita     │      Project Assurance
        │  Senior User:    Nagy Péter       │ ◄──► (üzleti: Balogh Tamás,
        │  Senior Supplier: Cloudia Kft.    │       felhasználói: Fodor Gábor,
        └─────────────────┬─────────────────┘       szállítói: Molnár Katalin)
                          │
              ┌───────────▼───────────┐
              │ Project Manager        │
              │ Tóth Gergő             │
              └───────────┬───────────┘
                          │
        ┌─────────────────┴─────────────────┐
        │ Team Manager: Szabó Márk (belső)  │
        │ Team Manager: Cloudia projektvez. │
        └───────────────────────────────────┘
```

| Szerep | Ki | Miért felel |
|---|---|---|
| **Executive** | **Kovács Anita**, gazdasági igazgató | Az üzleti indoklás gazdája. **Egyetlen ember, ő hozza a végső döntést.** |
| **Senior User** | **Nagy Péter**, IT osztályvezető | A megoldás használhatósága és **a hasznok tényleges megjelenése** |
| **Senior Supplier** | **Cloudia Solutions Kft.** ügyfélkapcsolati vezetője | A megoldás megvalósíthatósága és leszállítása |
| **Project Manager** | Tóth Gergő | Napi irányítás a toleranciákon belül |
| **Team Manager** | Szabó Márk; Cloudia projektvezető | Munkacsomagok leszállítása |
| **Project Assurance** | Balogh Tamás (üzleti), Fodor Gábor (felhasználói), Molnár Katalin (szállítói) | **Független ellenőrzés a Board nevében, a PM-től függetlenül** |
| **Change Authority** | **Tóth Gergő, 1 000 000 Ft-ig** | A Board delegálja a kisebb változáskérelmek eldöntését |
| Project Support | *nincs* | A projekt mérete nem indokolja; a PM látja el |

> **A Project Assurance a valós projektben nem létezett.** A PMI-változatban a
> Steering Committee kizárólag a PM riportjaira támaszkodott. PRINCE2-ben ez
> a szerep kötelező — nem külön fő, hanem a Board tagjainak delegált
> ellenőrzési felelőssége.

---

## 4. Szakaszolás és tervek

### 4.1 Irányítási szakaszok

| # | Szakasz | Időszak | A szakaszhatáron a Board dönt |
|---|---|---|---|
| 0 | Előkészítés *(SU)* | 2025.11.10 – 2026.02.02. | Engedélyezi a kezdeményezést |
| 1 | Kezdeményezés *(IP)* | 2026.02.02 – 03.13. | **Engedélyezi a projektet és a 2. szakaszt** *(ez a PID jóváhagyása)* |
| 2 | Beszerzés | 2026.03.16 – 04.17. | Engedélyezi a 3. szakaszt |
| 3 | Kialakítás és teszt | 2026.04.20 – 06.19. | Engedélyezi a zárási szakaszt |
| 4 | Élesítés és zárás *(CP)* | 2026.06.22 – 06.30. | Engedélyezi a projekt lezárását |

### 4.2 Mérföldkövek

M4 szerződéskötés 2026.04.17. · M5 környezet kész 05.08. · M6 első hullám és
UAT 05.11. · M7 teljes 50 fő élesben 06.12. · M8 UAT lezárva 06.19. ·
M9 üzemeltetésbe adás 06.26. · M10 projekt lezárva 06.30.

### 4.3 Költségterv szakaszonként

| Szakasz | Tervezett költés | Halmozott |
|---|---:|---:|
| 1. Kezdeményezés | 0 Ft | 0 Ft |
| 2. Beszerzés | 0 Ft | 0 Ft |
| 3. Kialakítás és teszt | 39 496 000 Ft | 39 496 000 Ft |
| 4. Élesítés és zárás | 4 634 000 Ft | 44 130 000 Ft |
| Projekt utáni folyó tétel (mobilnet, 2026.07 – 2027.04.) | 2 000 000 Ft | 46 130 000 Ft |
| *Tartalék (Board-szinten kezelve)* | *4 613 000 Ft* | *50 743 000 Ft* |

> **Miért 0 Ft a Beszerzés szakasz?** A szakasz terméke az aláírt szerződés —
> külső költséget nem generál. Az első kifizetés (a felhő-tétel 30%-a) a
> szerződéskötés utáni számla alapján, a 3. szakasz elején esedékes.
> A szakaszonkénti bontás a költségbázis (XYO-CP-107) havi elosztásából és
> fizetési ütemezéséből következik.

---

## 5. Toleranciák

> **Ez a PID legfontosabb szakasza a Project Manager számára.** Ezen belül
> önállóan dolgozik; ha a túllépés fenyeget, **Exception Reportot** készít.

### 5.1 Projekt-szintű tolerancia *(a vállalatvezetés adja a Boardnak)*

| Terület | Tolerancia |
|---|---|
| Idő | **0 nap** — a 2026.06.30-i határidő kemény (L1 korlát) |
| Költség | **0 Ft felfelé** — az 52 000 000 Ft nem növelhető (L2 korlát) |
| Hatókör | Nulla — a kötelező követelmények mind teljesülnek |

### 5.2 Szakasz-szintű tolerancia *(a Board adja a PM-nek)*

| Terület | Tolerancia | Megjegyzés |
|---|---|---|
| **Idő** | **± 5 munkanap** szakaszonként | A projekt végdátumát nem érintheti |
| **Költség** | **± 5%** szakaszonként, és a tartalékból **1 000 000 Ft / eset** | E felett Executive-döntés |
| **Hatókör** | **nulla** | Csak jóváhagyott változáskérelemmel |
| **Minőség** | Az átvételi kritériumok tűréshatára; **S1 hibából nulla** | Az S2 hibák elfogadott határidővel maradhatnak nyitva |
| **Kockázat** | 6-os vagy magasabb besorolást **jelenteni kell** a Boardnak | A kockázati étvágy |
| **Haszon** | A mérőszámok kudarcküszöbe | Lásd a Haszonkezelési megközelítést |

### 5.3 Munkacsomag-tolerancia *(a PM adja a Team Managernek)*

Idő: ± 2 munkanap · Költség: nincs (átalánydíjas szerződés) ·
Minőség: a kész-definíció tűréshatár nélkül.

---

## 6. Megközelítések *(management approaches)*

### 6.1 Kockázatkezelési megközelítés

Kockázati műhely a tervezési szakaszban · kéthetente felülvizsgálat ·
valószínűség × hatás skála (1–3) · minden magas kockázathoz nevesített
**kockázatgazda** és **bekövetkezési jelzés** · a 6-os vagy magasabb
besorolású kockázat a Highlight Reportba kerül.

### 6.2 Minőségkezelési megközelítés

Minden terméknek **termékleírása** van, mérhető minőségi kritériummal ·
szállítás közbeni minőségellenőrzés (nem csak átvételkor) · a felhasználói
átvételt **valós felhasználók** végzik, valós feladatokkal · a hibák
S1–S4 súlyossági kategóriában.

### 6.3 Változáskezelési megközelítés

A hatókört, a baseline ütemtervet, a költségbázist, az átvételi kritériumot
vagy a K/F prioritású követelményt érintő módosítás **változáskérelmet**
igényel · kötelező hatásvizsgálat hat szempontból, **a közvetett hatásokkal
együtt** · a Change Authority (PM) 1 000 000 Ft-ig dönt · minden kérelem —
az elutasított is — nyilvántartásba kerül.

### 6.4 Kommunikációkezelési megközelítés

| Mit | Kinek | Gyakoriság |
|---|---|---|
| **Checkpoint Report** | Team Manager → PM | hetente |
| **Highlight Report** | PM → Project Board | kéthetente |
| **Exception Report** | PM → Project Board | eseti, tolerancia-túllépés fenyegetésekor |
| **End Stage Report** | PM → Project Board | szakaszhatáronként |
| Pilot hírlevél | PM → az 50 résztvevő | kéthetente |

### 6.5 Haszonkezelési megközelítés *(Benefits Management Approach)*

12 mérőszám, mindegyikhez **T0 kiindulási érték**, célérték, kudarcküszöb és
nevesített felelős · **a T0 mérés a projekt indulása előtt, 2026.01.30-án
megtörtént** · mérés T+1, T+2, T+3 időpontban · a hasznok gazdája a **Senior
User (Nagy Péter)**, aki a projekt lezárása után is marad, 2026.09.30-ig ·
utólagos értékelés 2026.10.09-én.

---

## 7. Kontrollok

| Kontroll | Mikor |
|---|---|
| Szakaszhatár + Board-döntés | 4 alkalommal |
| Highlight Report | kéthetente |
| Kockázat-felülvizsgálat | kéthetente |
| **Business Case felülvizsgálat** | minden szakaszhatáron |
| Exception Report | tolerancia-túllépés fenyegetésekor |
| Project Assurance ellenőrzés | szakaszonként legalább egyszer |

---

## 8. Jóváhagyás

| Szerep | Név | Aláírás | Dátum |
|---|---|---|---|
| **Executive** | **Kovács Anita** | | **2026.03.13.** |
| Senior User | Nagy Péter | | 2026.03.13. |
| Senior Supplier | Cloudia Solutions Kft. | | 2026.03.13. |
| Készítette | Tóth Gergő, Project Manager | | 2026.03.11. |

**A Project Board a projektet és a 2. szakaszt engedélyezte.**

---

## Mi a különbség a PMI Charterhez képest?

| | PMI Project Charter | **PRINCE2 PID** |
|---|---|---|
| Terjedelem | 2–4 oldal | **10–20 oldal** |
| Mikor készül | A Kezdeményezés végén | A **kezdeményezési szakasz** végén |
| Mit tartalmaz | Cél, hatókör, keret, PM-hatáskör | **Mindezt + az összes megközelítést, a szakaszolást, a toleranciákat és a kontrollokat** |
| PMI-megfelelő | Charter | **Charter + Project Management Plan** |
| Ki hagyja jóvá | Szponzor | **Project Board** (Executive dönt) |
| Élő? | Nem — a projekt alapdokumentuma | **Igen** — szakaszhatáronként frissül |

> A Xyo projektben a Charter (XYO-CP-005) és a Projektterv (XYO-CP-101)
> **együtt** felelt meg ennek a PID-nek. A PRINCE2 azért kezeli egyben, mert
> a Board egyetlen dokumentumot hagy jóvá, és ahhoz képest kér számon.
