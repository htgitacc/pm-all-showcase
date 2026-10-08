# Projektalapító okirat (Project Charter)

**Dokumentum azonosítója:** XYO-CP-005\
**Projekt neve:** Xyo Cloud Pilot\
**Verzió:** 1.0 — **aláírva 2026. február 2.**\
**Készítette:** Tóth Gergő, projektmenedzser\
**Jóváhagyó (szponzor):** Kovács Anita, gazdasági igazgató

> Ez a dokumentum **hozza létre hivatalosan a projektet**, és ez ad felhatalmazást
> a projektmenedzsernek a cég erőforrásainak felhasználására.

---

## 1. A projekt célja és üzleti indoka

A Xyo Kft. 50 fős pilot környezetben bevezeti a felhőalapú munkakörnyezetet
(Microsoft 365, Entra ID, Intune, SharePoint, OneDrive, Azure VPN), migráció nélkül,
teljes egészében új beszerzésből.

A projekt üzleti indoka kettős: a **géppark cseréje elkerülhetetlen**, és a cégnek
**tényadatra van szüksége** ahhoz, hogy eldöntse, kiterjeszthető-e a felhőalapú
működés a teljes, kb. 240 fős szervezetre.

Részletes indoklás: *Üzleti indoklás (XYO-CP-002)*.

## 2. Mérhető célok és sikerkritériumok

| # | Cél | Mérőszám | Célérték | Mérés ideje |
|---|---|---|---:|---|
| C1 | Élesben működő felhőkörnyezet | Élesített felhasználók száma | 50 fő | 2026.06.12. |
| C2 | Egységes azonosítás | MFA-lefedettség | 100% | 2026.06.19. |
| C3 | A projekt a kereten belül zárul | Tényleges költés | ≤ 52 000 000 Ft | 2026.06.30. |
| C4 | Csökkenő támogatási terhelés | Ticket / hó | ≤ 72 (T0: 103) | 2026.09.30. |
| C5 | Gyorsabb hibaelhárítás | MTTR | ≤ 6,0 óra (T0: 11,4) | 2026.09.30. |
| C6 | Rugalmas munkavégzés | Home office napok aránya | ≥ 40% (T0: 0%) | 2026.09.30. |
| C7 | Felhasználói elfogadás | Elégedettség 1–5 | ≥ 4,0 (T0: 3,1) | 2026.09.30. |
| C8 | Döntési alap | Elfogadott kiterjesztési javaslat | elkészül | 2026.10.09. |

A C4–C7 célok a **projekt lezárása után**, a mérési szakaszban igazolhatók.
Módszertan: *Haszonrealizálási terv (XYO-CP-009)*.

## 3. Hatókör

### 3.1 Ami a projekt része

- 50 db laptop, dokkoló, otthoni monitor és headset beszerzése és kiosztása.
- Microsoft 365 Business Premium licenc 50 főre, 12 hónapra.
- Entra ID bérlő kiterjesztése, feltételes hozzáférés és MFA bevezetése.
- Intune eszközfelügyelet és Windows Autopilot alapú gépbeüzemelés.
- SharePoint csapatoldalak és OneDrive tárhely kialakítása a pilot körnek.
- Azure VPN Gateway kialakítása a belső rendszerek eléréséhez.
- Mobilinternet-hozzájárulás biztosítása a 12 hónapos pilot időszakra.
- Felhasználói oktatás és a bevezetés utáni fokozott támogatás (hypercare).
- A projekt utáni 3 hónapos mérési szakasz megtervezése és lebonyolítása.

### 3.2 Ami kifejezetten NEM része a projektnek

> Ez a szakasz a projekt legfontosabb védelme. Minden felmerülő, de nem vállalt
> kérés ide kerül, a felmerülés dátumával.

| # | Hatókörön kívüli elem | Miért | Rögzítve |
|---|---|---|---|
| K1 | Bármilyen adatmigráció a régi fájlszerverről | A projekt szándékosan migráció nélküli; a régi adat a helyén marad | 2026.02.02. |
| K2 | A gyártósori és termelésirányítási rendszerek érintése | Külön ütemterv és külön kockázati profil | 2026.02.02. |
| K3 | A telefonközpont felhőbe költöztetése (Teams Phone) | Külön projekt, külön költségkeret | 2026.02.02. |
| K4 | A pénzügyi és bérszámfejtő rendszer átalakítása | Nem érinti a munkakörnyezetet | 2026.02.02. |
| K5 | Kiterjesztés a pilot körön kívüli munkatársakra | A kiterjesztésről a mérési szakasz után születik döntés | 2026.02.02. |
| K6 | Szakmai szoftverek (CAD, tervezőrendszerek) telepítése a laptopokra | Nem a pilot köre; külön licenc- és teljesítményigény | 2026.02.02. |
| K7 | A meglévő irodai monitorok cseréje | A cégnél rendelkezésre állnak, csak az otthoni monitor új | 2026.02.02. |

## 4. Mérföldkövek

| # | Mérföldkő | Tervezett dátum |
|---|---|---|
| M1 | Projektalapító okirat aláírva | 2026.02.02. |
| M2 | Kick-off megtartva | 2026.02.09. |
| M3 | Terv jóváhagyva, baseline befagyasztva (Planning-kapu) | 2026.03.13. |
| M4 | Beszerzési eljárás lezárva, szerződés aláírva | 2026.04.17. |
| M5 | Felhőkörnyezet kialakítva, tesztelésre kész | 2026.05.08. |
| M6 | Pilot indul az első 10 fővel (UAT) | 2026.05.11. |
| M7 | Teljes 50 fő élesben | 2026.06.12. |
| M8 | UAT lezárva, átvétel aláírva | 2026.06.19. |
| M9 | Üzemeltetésbe adás | 2026.06.26. |
| M10 | Projekt lezárva | 2026.06.30. |
| M11 | Utólagos értékelés (PIR), kiterjesztési javaslat | 2026.10.09. |

## 5. Költségkeret

| | Összeg |
|---|---:|
| Jóváhagyott keret | **52 000 000 Ft** |
| Tervezett költség | 50 743 000 Ft |
| Ebből tartalékkeret | 4 613 000 Ft |
| Mozgástér | 1 257 000 Ft |

A 2. évtől jelentkező **10 680 000 Ft/év folyó költséget** a projekt zárásakor
az IT üzemeltetési keretbe kell átvezetni; ez a zárás feltétele.

## 6. A projektmenedzser megnevezése és hatásköre

**Projektmenedzser:** Tóth Gergő

| Jogosultság | Mérték |
|---|---|
| Tartalékkeret felhasználása | **1 000 000 Ft-ig önállóan**; e felett a szponzor jóváhagyásával |
| Ütemterv módosítása | Belső mérföldkövek között önállóan; az M7 és M10 dátum csak Steering-döntéssel |
| Hatókör módosítása | **Nem** — kizárólag jóváhagyott változáskérelemmel |
| Erőforrás igénybevétele | A jóváhagyott erőforrásterv keretein belül önállóan |
| Szállítói kapcsolattartás | Szakmai kérdésekben önállóan; szerződéses kérdésekben a beszerzésen keresztül |
| Eszkaláció | Közvetlenül a szponzorhoz, bármikor |

> **Miért fontos ez a szakasz?** Enélkül a projektmenedzsernek minden apróságért
> engedélyt kell kérnie, vagy — rosszabb esetben — jogosulatlanul dönt.
> A pontos határ mindkét felet védi.

## 7. Fő érintettek

| Szerep | Név | Beosztás |
|---|---|---|
| Szponzor | Kovács Anita | gazdasági igazgató |
| Steering elnök | Horváth Júlia | ügyvezető |
| Projektmenedzser | Tóth Gergő | projektmenedzser |
| Szakmai vezető, a hasznok gazdája | Nagy Péter | IT osztályvezető |
| Rendszergazda | Szabó Márk | rendszergazda |
| Service Desk | Kiss Réka | Service Desk vezető |
| HR | Varga Eszter | HR vezető |
| Beszerzés | Molnár Katalin | beszerzési vezető |
| Kontrolling | Balogh Tamás | pénzügyi kontroller |
| Adatvédelem | dr. Fekete Zsolt | adatvédelmi tisztviselő |

Részletes lista: *Érintettek nyilvántartása (XYO-CP-006)*.

## 8. Feltevések

| # | Feltevés |
|---|---|
| A1 | A dolgozói mobilcsomagok korlátlan adatforgalmat tartalmaznak, és a munkavégzésre használhatók. |
| A2 | A home office szabályzat 2026. április 30-ig hatályba lép. |
| A3 | A pilot 50 fő kijelölése 2026. február 27-ig megtörténik. |
| A4 | A kiválasztott CSP partner rendelkezésre áll a tervezett időablakban. |
| A5 | A laptopszállítás a szerződéskötéstől számított 6 héten belül teljesül. |

Nyilvántartás és ellenőrzés: *Feltevés- és korlátnapló (XYO-CP-008)*.

## 9. Korlátok

| # | Korlát |
|---|---|
| L1 | A projektnek 2026.06.30-ig le kell zárulnia. |
| L2 | A költségkeret 52 000 000 Ft, nem növelhető. |
| L3 | Az IT részlegről 2 fő áll rendelkezésre, a napi munkája mellett. |
| L4 | A pilot köre 50 fő, nem bővíthető Steering-döntés nélkül. |
| L5 | A beszerzésnek a cég beszerzési szabályzata szerint kell történnie. |

## 10. Magas szintű kockázatok

| # | Kockázat | Hatás | Első válasz |
|---|---|---|---|
| R1 | A laptopszállítás csúszik | M7 mérföldkő eltolódik | Korai beszerzésindítás, kötbér a szerződésben |
| R2 | Adatvédelmi hatásvizsgálat szükséges és elhúzódik | Tervezési fázis csúszik | DPO bevonása már február első hetében |
| R3 | A mobilinternet külterületen nem elegendő | Egyes résztvevők nem tudnak otthonról dolgozni | A kijelölésnél a lakóhely vizsgálata (F-1) |
| R4 | Belső kapacitáshiány (2 fő IT) | Csúszás, minőségromlás | A bevezetést CSP partner végzi; írásos kapacitás-jóváhagyás |
| R5 | Felhasználói ellenállás | Alacsony adaptáció, rossz elégedettség | Oktatás, hypercare, folyamatos kommunikáció |

Teljes nyilvántartás a tervezési fázisban készül.

## 11. Aláírások

| Szerep | Név | Dátum | Aláírás |
|---|---|---|---|
| **Szponzor (jóváhagyó)** | **Kovács Anita, gazdasági igazgató** | **2026.02.02.** | |
| Ügyvezető (tudomásul vétel) | Horváth Júlia | 2026.02.02. | |
| Projektmenedzser (átvette) | Tóth Gergő | 2026.02.02. | |
| Szakmai vezető | Nagy Péter | 2026.02.02. | |

---

> **Kapcsolódó dokumentumok:**
> **Bemenete:** Üzleti indoklás (XYO-CP-002), Költség-haszon elemzés (XYO-CP-003),
> Megvalósíthatósági tanulmány (XYO-CP-004).
> **Kimenete:** Érintettek nyilvántartása, Feltevés- és korlátnapló,
> Haszonrealizálási terv, Kick-off jegyzőkönyv, Projektterv, Hatókör-nyilatkozat.
