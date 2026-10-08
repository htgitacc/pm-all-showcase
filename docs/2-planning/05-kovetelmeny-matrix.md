# Követelmény-nyomonkövetési mátrix (Requirements Traceability Matrix)

**Dokumentum azonosítója:** XYO-CP-105\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Validálta:** Nagy Péter, szakmai vezető\
**Verzió:** 1.3 — **lezárva 2026.06.19-én** (UAT-elfogadás, M8)

> Minden követelményről látszik, **ki kérte, hol valósul meg, és mi bizonyítja,
> hogy teljesült.** Ezzel az átvételkor minden vita lezárható.
> A „forrás" oszlop kritikus: amikor egy követelmény drágának bizonyul, tudni
> kell, kivel lehet róla tárgyalni.
>
> **A lánc:** követelmény (K) → teszteset (T, *Tesztterv*) → átvételi kritérium
> (AK, *Minőségterv*) → szerződéses feltétel (Sz-6: AK-01 – AK-23, *Szerződés*).
> Minden K prioritású követelményhez tartozik átvételi kritérium — ettől igaz,
> hogy „enélkül nincs átvétel". Az F és H tételeket a teszteset bizonyítja.

---

## Prioritások

| Jelölés | Jelentése |
|---|---|
| **K** | Kötelező — enélkül nincs átvétel |
| **F** | Fontos — ha kimarad, dokumentált döntés kell róla |
| **H** | Ha belefér — a maradék kapacitás függvényében |

---

## 1. Azonosítás és hozzáférés

| # | Követelmény | Pri. | Forrás (ki kérte) | WBS | Teszteset | Átvételi krit. | Státusz (06.19.) |
|---|---|:-:|---|---|---|---|---|
| K01 | A felhasználó Entra ID azonosítóval lép be a gépbe | K | Nagy Péter (Charter) | 3.1.1 | T-01 | AK-01 | teljesült |
| K02 | Minden belépéshez többtényezős hitelesítés (MFA) szükséges | K | dr. Fekete Zsolt (DPIA) | 3.1.2 | T-02 | AK-02 | teljesült |
| K03 | Elveszett eszköz esetén a hozzáférés központilag visszavonható | K | dr. Fekete Zsolt | 3.1.2, 3.2.1 | T-03 | AK-04 | teljesült |
| K04 | Létezik dokumentált vészhozzáférési (break-glass) fiók | K | Szabó Márk | 3.1.2 | T-04 | AK-03 | teljesült |
| K05 | A bejelentkezés Magyarországon kívülről alapértelmezetten tiltott | F | dr. Fekete Zsolt | 3.1.2 | T-05 | — | teljesült — **módosított megvalósítással** (D-14: megbízható eszköz + MFA) |
| K06 | Egyszeri bejelentkezés (SSO) a Microsoft 365 alkalmazásokhoz | F | Szilágyi Anna | 3.1.1 | T-06 | — | teljesült |

## 2. Eszköz és beüzemelés

| # | Követelmény | Pri. | Forrás | WBS | Teszteset | Átvételi krit. | Státusz (06.19.) |
|---|---|:-:|---|---|---|---|---|
| K07 | Egy új gép beüzemelése Autopilottal legfeljebb 1,5 óra | K | Nagy Péter (C-cél) | 2.3.1, 3.2.2 | T-07 | AK-06, AK-07 | teljesült |
| K08 | A gép merevlemeze titkosított (BitLocker), a kulcs központilag mentve | K | dr. Fekete Zsolt | 3.2.1 | T-08 | AK-08 | teljesült |
| K09 | Az eszközfelügyelet **nem** terjed ki a magánhasználatra | K | Üzemi tanács (L7) | 3.2.1 | T-09 | AK-10 | teljesült — hozzáadva 03.11. (L7) |
| K10 | Az alapszoftverek automatikusan települnek (Office, böngésző, VPN kliens) | K | Szabó Márk | 3.2.3 | T-10 | AK-09 | teljesült |
| K11 | A biztonsági frissítések automatikusan, ütemezetten települnek | K | Szabó Márk | 3.2.1 | T-11 | AK-09 | teljesült |
| K12 | A laptop az otthoni monitorhoz dokkolón keresztül csatlakoztatható | K | Fodor Gábor | 2.3.2 | T-12 | AK-11 | teljesült — **módosítva** 03.06.: 14 gépnél adapter (A7) |

## 3. Fájlkezelés és együttműködés

| # | Követelmény | Pri. | Forrás | WBS | Teszteset | Átvételi krit. | Státusz (06.19.) |
|---|---|:-:|---|---|---|---|---|
| K13 | Minden felhasználónak van saját OneDrive tárhelye | K | Nagy Péter | 3.3.1 | T-13 | AK-12 | teljesült |
| K14 | Minden csapatnak van SharePoint csapatoldala, jogosultsági modellel | K | Nagy Péter | 3.3.1 | T-14 | AK-13 | teljesült |
| K15 | A törölt fájl legalább 30 napig visszaállítható | K | Szabó Márk (R7) | 3.3.2 | T-15 | AK-14 | teljesült |
| K16 | Egy teljes könyvtár visszaállítása tesztelt és dokumentált | K | Szabó Márk (R7) | 3.3.2 | T-16 | AK-15 | teljesült |
| K17 | 3 csapat olvasási hozzáférést kap a régi fájlszerverhez VPN-en | F | Fodor Gábor (A8) | 3.4.2 | T-17 | AK-16 | teljesült — **hozzáadva 03.05.** |
| K18 | A dokumentumok egyidejűleg szerkeszthetők több felhasználó által | F | Szilágyi Anna | 3.3.1 | T-18 | — | teljesült |
| K19 | Külső partnerrel megosztható link, lejárati idővel | H | Fodor Gábor | 3.3.1 | T-19 | — | teljesült |

## 4. Távoli munkavégzés

| # | Követelmény | Pri. | Forrás | WBS | Teszteset | Átvételi krit. | Státusz (06.19.) |
|---|---|:-:|---|---|---|---|---|
| K20 | VPN-kapcsolat felépíthető otthoni mobilinternetről | K | Nagy Péter (Charter) | 3.4.1, 3.4.2 | T-20 | AK-17 | teljesült |
| K21 | A 2 belső rendszer (bérszámfejtés, ügyviteli webfelület) elérhető VPN-en | K | Szilágyi Anna | 3.4.2 | T-21 | AK-18 | teljesült |
| K22 | A VPN-kapcsolat Entra ID azonosítással épül fel | F | Szabó Márk | 3.4.1 | T-22 | — | teljesült |
| K23 | Videóhívás elfogadható minőségben működik mobilneten | F | Varga Eszter | 3.2.3 | T-23 | AK-19 | **nem teljesült** — elfogadott kezeléssel (H-06, határidő 07.31.) |

## 5. Támogatás és felkészítés

| # | Követelmény | Pri. | Forrás | WBS | Teszteset | Átvételi krit. | Státusz (06.19.) |
|---|---|:-:|---|---|---|---|---|
| K24 | Minden felhasználó részt vesz oktatáson, dokumentált jelenléttel | K | Varga Eszter | 5.2 | T-24 | AK-20 | teljesült |
| K25 | Létezik magyar nyelvű, képernyőképes gyorssegédlet | K | Kiss Réka | 5.1 | T-25 | AK-21 | teljesült |
| K26 | A Service Desk hibakezelési útmutatót kap az élesítés előtt 2 héttel | K | Kiss Réka | 5.3 | T-26 | AK-22 | teljesült |
| K27 | A jelszó-visszaállítás önkiszolgáló módon működik | F | Kiss Réka | 3.1.1 | T-27 | AK-05 | teljesült — QC-01: az MFA-regisztráció az oktatáson történik |

> **A státusz oszlop a 2026.06.19-i állapot** (UAT-elfogadás, M8). A
> tervezéskor mind „tervezve" volt; a mátrix az átvételkor zárul le, és innen
> olvasható ki, melyik követelmény hogyan teljesült.
>
> **K27 magyarázata:** a T0 mérés szerint a ticketek **41%-a hozzáférés/jelszó**
> jellegű. Az önkiszolgáló jelszó-visszaállítás önmagában a legnagyobb hatású
> tétel az M1 és M3 mérőszámra. Kiss Réka kérte, és jól tette.

## Átvételi kritériumok a teljes megoldásra

Négy kritérium nem egy követelményt, hanem az egészet minősíti — ezek a
*Hatókör-nyilatkozat* magas szintű kritériumaiból jönnek:

| AK | Mit bizonyít | Forrás |
|---|---|---|
| AK-23 | Az üzemeltetés az as-built alapján átveheti | Hatókör A7 |
| AK-24 | Az UAT tesztesetek ≥ 95%-a megfelelt | Hatókör A6 |
| AK-25 | Nincs nyitott S1 hiba | Hatókör A6 |
| AK-26 | A nyitott S2 hibákhoz elfogadott határidő tartozik | Hatókör A6 |

> **Az AK-07** (bekapcsolástól bejelentkezésig ≤ 90 mp) a K07 része: a gyors
> munkába állás (C-cél) nem ér véget a beüzemeléssel. Ha egy kritérium mögött
> nincs követelmény, az vagy hiányzó követelmény, vagy fölösleges munka
> (*gold plating*) — a mátrix ezt teszi láthatóvá.

## 6. Elutasított és elhalasztott követelmények

| # | Kérés | Kérte | Döntés | Indok |
|---|---|---|---|---|
| E01 | Céges mobiltelefon a pilot résztvevőknek | Szilágyi Anna, 02.27. | **elutasítva** | Hatókörön kívül (hatókör-kizárás K9); a meglévő dolgozói csomagra épülünk |
| E02 | Otthoni nyomtatási megoldás | Szilágyi Anna, 03.10. | **elutasítva** | Hatókörön kívül (hatókör-kizárás K11); a pilot papírmentes működést feltételez |
| E03 | A régi fájlszerver teljes tartalmának átmozgatása SharePointra | Fodor Gábor, 02.24. | **elutasítva** | Hatókörön kívül (hatókör-kizárás K8); helyette K17 (olvasási hozzáférés) |
| E04 | Tervezőszoftver telepítése 4 gépre | Papp Zsófia, 03.09. | **elutasítva** | Hatókörön kívül (hatókör-kizárás K6); külön licenc- és teljesítményigény |
| E05 | Kétfaktoros belépés hardveres kulccsal (FIDO2) | Szabó Márk, 03.02. | **elhalasztva** | H prioritás; a kiterjesztésnél újra vizsgálandó |

> **Az elutasított kéréseket ugyanolyan gondosan vezetjük, mint az elfogadottakat.**
> Vita esetén ez bizonyítja, hogy a kérés elhangzott, megvizsgáltuk, és
> **dokumentált döntés** született róla — nem elfelejtettük.

---

## Összesítés

| Prioritás | Darab |
|---|---:|
| **K** — kötelező | 19 |
| **F** — fontos | 7 |
| **H** — ha belefér | 1 |
| **Összesen elfogadott** | **27** |
| Elutasítva / elhalasztva | 5 |

## Változásnapló

| Dátum | Változás |
|---|---|
| 2026.02.20. | Első változat, 25 követelmény az érintett-interjúkból és a Charterből |
| 2026.03.02. | E05 felvéve és elhalasztva |
| 2026.03.05. | **K17 hozzáadva** — a régi fájlszerver olvasási hozzáférése (A8 feltevés következménye) |
| 2026.03.06. | K12 módosítva — 14 gépnél adapter szükséges (A7 megdőlt) |
| 2026.03.11. | K09 hozzáadva az üzemi tanács kikötése alapján (L7) |
| 2026.03.12. | **v1.2 — baseline.** Az azonosítók témakörönként véglegesítve (K01–K27); a *Tesztterv* és a *Minőségterv* ezekre hivatkozik. Ettől kezdve azonosító nem változik: új tétel a következő szabad számot kapja |
| 2026.06.19. | **v1.3 — lezárás** az UAT-elfogadással: átvételi-kritérium oszlop, záró státusz. K05 a D-14 szerint módosított megvalósítással, K23 nem teljesült (elfogadott kezeléssel) |

---

> **Kapcsolódó dokumentumok:** bemenete a *Hatókör-nyilatkozat* és a
> *Projektszótár*; kimenete a *Tesztterv*, a *Minőségterv* és az
> *UAT-elfogadás*.
