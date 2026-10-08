# Hatókör-nyilatkozat (Scope Statement)

**Dokumentum azonosítója:** XYO-CP-102\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Jóváhagyta:** Kovács Anita (szponzor), Nagy Péter (szakmai vezető) — 2026.03.13.\
**Verzió:** 1.0 — **baseline, befagyasztva a Planning-kapun**

> A hatókör csak jóváhagyott változáskérelemmel módosítható
> (lásd: *Változáskezelési eljárás, XYO-CP-115*).

---

## 1. Termékleírás

A projekt eredménye egy **működő, felhőalapú munkakörnyezet 50 munkatárs
számára**, amelyben a résztvevő:

- céges laptopon dolgozik, irodából és otthonról egyaránt;
- **Entra ID** azonosítóval, többtényezős hitelesítéssel lép be;
- a dokumentumait **OneDrive-on és SharePointon** tárolja, nem a fájlszerveren;
- a belső rendszereket **VPN-en** keresztül éri el;
- a gépe **Intune** eszközfelügyelet alatt áll, és Autopilottal üzemel be.

## 2. Szállítandó eredmények (deliverables)

| # | Eredmény | Átvevő | Mérföldkő |
|---|---|---|---|
| D1 | 50 db beüzemelt, Autopilot-regisztrált laptop + dokkoló, monitor, headset | Nagy Péter | M7 |
| D2 | Konfigurált Entra ID környezet MFA-val és feltételes hozzáféréssel | Szabó Márk | M5 |
| D3 | Intune eszközfelügyelet, eszközprofilok és alkalmazáscsomagok | Szabó Márk | M5 |
| D4 | SharePoint csapatoldalak és OneDrive tárhely, jogosultsági modellel | Nagy Péter | M5 |
| D5 | Azure VPN Gateway, működő klienskapcsolattal | Szabó Márk | M5 |
| D6 | As-built (konfigurációs) dokumentáció | Nagy Péter | M9 |
| D7 | Oktatási anyag, gyorssegédlet, megtartott oktatások | Varga Eszter | M7 |
| D8 | Lezárt UAT, aláírt átvételi elfogadás | Nagy Péter | M8 |
| D9 | Üzemeltetésbe adási dokumentáció (Run-book) | Nagy Péter | M9 |
| D10 | KPI-adatlapok és a mérési felelősségek átadása | Nagy Péter | M10 |

## 3. Magas szintű átvételi kritériumok

Részletesen: *Minőségterv és átvételi kritériumok (XYO-CP-114)*.

| # | Kritérium | Hogyan bizonyítjuk |
|---|---|---|
| A1 | Mind az 50 kijelölt felhasználó be tud lépni Entra ID-val | Entra ID bejelentkezési napló |
| A2 | Mind az 50 felhasználónál aktív az MFA | Entra ID riport, 100% |
| A3 | Minden felhasználó eléri a saját OneDrive tárhelyét és a csapatoldalát | UAT teszteset |
| A4 | A VPN-kapcsolat működik, a 2 belső rendszer elérhető | UAT teszteset |
| A5 | Egy új gép beüzemelése Autopilottal ≤ 1,5 óra | Intune napló, 5 gépen mérve |
| A6 | Az UAT tesztesetek ≥ 95%-a megfelelt, kritikus hiba nincs nyitva | Tesztjegyzőkönyv |
| A7 | Az as-built dokumentáció alapján az üzemeltetés át tudja venni | Átvevő nyilatkozata |

## 4. Ami NINCS a hatókörben

> Ez a fejezet a projekt legfontosabb védelme. **Élő lista:** minden felmerülő,
> de nem vállalt kérés ide kerül, a felmerülés dátumával és a kérővel.

| # | Hatókörön kívüli elem | Miért | Ki vetette fel | Mikor |
|---|---|---|---|---|
| K1 | Adatmigráció a régi fájlszerverről | A projekt szándékosan migráció nélküli | — (Charter) | 2026.02.02. |
| K2 | Gyártósori és termelésirányítási rendszerek | Külön ütemterv és kockázati profil | — (Charter) | 2026.02.02. |
| K3 | Telefonközpont felhőbe költöztetése (Teams Phone) | Külön projekt, külön keret | — (Charter) | 2026.02.02. |
| K4 | Pénzügyi és bérszámfejtő rendszer átalakítása | Nem érinti a munkakörnyezetet | — (Charter) | 2026.02.02. |
| K5 | Kiterjesztés a pilot körön kívülre | A mérési szakasz után dől el | — (Charter) | 2026.02.02. |
| K6 | Szakmai szoftverek (CAD, tervezőrendszerek) telepítése | Külön licenc- és teljesítményigény | — (Charter) | 2026.02.02. |
| K7 | Az irodai monitorok cseréje | Rendelkezésre állnak, csak az otthoni új | — (Charter) | 2026.02.02. |
| **K8** | **A régi fájlszerver adatainak átmozgatása SharePointra** | 3 csapatnak elég az olvasási hozzáférés VPN-en (A8 feltevés) | Fodor Gábor | 2026.02.24. |
| **K9** | **Céges mobiltelefon biztosítása a pilot résztvevőknek** | A mobilinternet-hozzájárulás a meglévő dolgozói csomagra épül | Szilágyi Anna | 2026.02.27. |
| **K10** | **Otthoni irodabútor (szék, asztal) beszerzése** | HR-hatáskör, nem IT-projekt; a home office szabályzat rendezi | Papp Zsófia | 2026.03.04. |
| **K11** | **Nyomtatási megoldás otthonra** | A pilot papírmentes működést feltételez | Szilágyi Anna | 2026.03.10. |

> **Tanulság junior PM-nek:** a K8–K11 négy hét alatt gyűlt össze, a kick-off után.
> Mindegyik ésszerű kérés volt, és mindegyiket „ez csak egy apróság" felvezetéssel
> mondták. Ha nem írod le őket **azonnal**, az Execution közepén már azt fogod
> hallani, hogy „de hát ezt megbeszéltük".

## 5. Feltevések

A hatókör az alábbi feltevésekre épül. Teljes nyilvántartás:
*Feltevés- és korlátnapló (XYO-CP-008)*.

| # | Feltevés | Státusz 2026.03.13-án |
|---|---|---|
| A2 | A home office szabályzat 2026.04.30-ig hatályba lép | nyitva |
| A4 | A CSP partner rendelkezésre áll a tervezett időablakban | nyitva |
| A5 | A laptopszállítás a szerződéskötéstől 6 héten belül teljesül | nyitva |
| A8 | Nem szükséges adatmigráció; 3 csapat olvasási hozzáférést kap | igazolt, feltétellel |
| A9 | A Service Desk kapacitása elegendő a hypercare időszakban | nyitva |

## 6. Korlátok

| # | Korlát |
|---|---|
| L1 | A projektnek 2026.06.30-ig le kell zárulnia |
| L2 | A költségkeret 52 000 000 Ft, nem növelhető |
| L3 | Az IT részlegről 2 fő áll rendelkezésre, napi munka mellett |
| L4 | A pilot köre 50 fő, Steering-döntés nélkül nem bővíthető |
| L5 | A beszerzésnek a beszerzési szabályzat szerint kell történnie |
| L6 | Az adatok kizárólag EU-s adatközpontban tárolhatók |
| L7 | Az eszközfelügyelet nem terjedhet ki a magánhasználatra |

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.03.06. |
| Jóváhagyta (szakmai) | Nagy Péter, IT osztályvezető | 2026.03.11. |
| Jóváhagyta (szponzor) | Kovács Anita, gazdasági igazgató | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete a *Projektalapító okirat*; kimenete a
> *WBS*, a *Követelmény-nyomonkövetési mátrix*, a *Minőségterv* és a
> *Változáskezelési eljárás*.
