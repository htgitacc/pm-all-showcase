# Feltevés- és korlátnapló (Assumption and Constraint Log)

**Dokumentum azonosítója:** XYO-CP-008\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Létrehozva:** 2026. február 6.\
**Utolsó frissítés:** 2026. március 13. (Planning-kapu)\
**Verzió:** 1.4 — **élő dokumentum**

> **Miért ez az egyik legerősebb védőiratod?** Mert ha egy feltevés később hamisnak
> bizonyul, ez bizonyítja, hogy **jelezted a bizonytalanságot** — nem elhallgattad.
> Minden sorhoz ezért kötelező az ellenőrzési mód, a felelős és a határidő.

---

## 1. Feltevések (Assumptions)

| # | Feltevés | Kategória | Ki állította / mikor | Ellenőrzés módja | Felelős | Határidő | Státusz | Következmény |
|---|---|---|---|---|---|---|---|---|
| A1 | A dolgozói mobilcsomagok korlátlan adatforgalmat tartalmaznak és munkavégzésre használhatók | szerződéses | Nagy Péter, 2025.11.10. | A mobilszolgáltatói szerződések átnézése | Molnár Katalin | 2026.02.27. | **igazolt** (2026.02.24.) | — |
| A2 | A home office szabályzat 2026.04.30-ig hatályba lép | szervezeti | Varga Eszter, 2026.02.03. | HR státusz lekérdezése havonta | Varga Eszter | 2026.04.30. | nyitva | Ha csúszik, az élesítés jogilag rendezetlen |
| A3 | A pilot 50 fő kijelölése 2026.02.27-ig megtörténik | szervezeti | Varga Eszter, 2026.02.03. | Névsor átvétele | Varga Eszter | 2026.02.27. | **igazolt** (2026.02.26.) | — |
| A4 | A kiválasztott CSP partner rendelkezésre áll a tervezett időablakban | szállítói | Tóth Gergő, 2026.02.06. | Kapacitás-visszaigazolás az ajánlatban | Molnár Katalin | 2026.04.17. | nyitva | Csúszás az M5 mérföldkőben |
| A5 | A laptopszállítás a szerződéskötéstől 6 héten belül teljesül | szállítói | TechLine előzetes tájékoztatás, 2026.02.25. | Írásos szállítási vállalás a szerződésben | Molnár Katalin | 2026.04.17. | nyitva | Az M7 (teljes élesítés) csúszik |
| A6 | A Business Premium licenc tartalmazza az Intune és az Entra ID P1 funkciókat, külön beszerzés nélkül | technikai | Cloudia Solutions, 2026.01.09. | Licencfeltételek írásos megerősítése | Szabó Márk | 2026.03.06. | **igazolt** (2026.03.04.) | — |
| A7 | Az irodai monitorok újrahasznosíthatók a laptopokhoz (megfelelő csatlakozó) | technikai | Szabó Márk, 2026.02.10. | 5 monitor mintavételes ellenőrzése | Szabó Márk | 2026.03.06. | **megdőlt** (2026.03.02.) | 14 monitor csak VGA — adapter szükséges, +182 000 Ft. Kezelés: tartalékkeretből, PM hatáskörben. |
| A8 | Nem szükséges adatmigráció, a régi fájlszerver párhuzamosan üzemel | hatóköri | Nagy Péter, 2025.11.10. | A pilot résztvevők igényeinek felmérése | Nagy Péter | 2026.03.06. | **igazolt, feltétellel** (2026.03.05.) | 3 csapatnál kell olvasási hozzáférés a régi adatokhoz — VPN-en keresztül megoldva |
| A9 | A Service Desk kapacitása elegendő a hypercare időszakban | szervezeti | Tóth Gergő, 2026.02.09. | Kiss Rékával közös kapacitásbecslés | Kiss Réka | 2026.04.10. | nyitva | Ha nem, +1 fő ideiglenes támogatás kell |
| A10 | Az üzemi tanács nem emel kifogást a home office és az eszközfelügyelet ellen | jogi | Tóth Gergő, 2026.02.09. | Formális megkeresés és írásos vélemény | Varga Eszter | 2026.03.06. | **igazolt, feltétellel** (2026.03.11.) | Kikötés: az eszközfelügyelet nem terjedhet ki a magánhasználatra. Átvezetve a Biztonsági alapkonfigurációba. |

## 2. Korlátok (Constraints)

| # | Korlát | Kategória | Forrás | Mozgástér | Következmény, ha feszül |
|---|---|---|---|---|---|
| L1 | A projektnek 2026.06.30-ig le kell zárulnia | idő | Charter, szponzori döntés | nincs | A gépcsere kényszerhelyzetbe kerül |
| L2 | A költségkeret 52 000 000 Ft, nem növelhető | költség | Charter | 1 257 000 Ft mozgástér + 4 613 000 Ft tartalék | Hatókörcsökkentés szükséges |
| L3 | Az IT részlegről 2 fő áll rendelkezésre, napi munka mellett | erőforrás | Charter | nincs | A bevezetést külső partner végzi |
| L4 | A pilot köre 50 fő, Steering-döntés nélkül nem bővíthető | hatókör | Charter | nincs | Változáskérelem szükséges |
| L5 | A beszerzésnek a cég beszerzési szabályzata szerint kell történnie | eljárás | Beszerzési szabályzat 4.2 § | nincs | 25 M Ft felett 3 ajánlat kötelező, +3 hét átfutás |
| L6 | Az adatok kizárólag EU-s adatközpontban tárolhatók | jogi | DPO állásfoglalás, 2026.03.06. | nincs | Szolgáltatás-konfigurációs kikötés |
| L7 | Az eszközfelügyelet nem terjedhet ki a magánhasználatra | jogi | Üzemi tanács véleménye, 2026.03.11. | nincs | Intune profil szűkítése |

## 3. Megdőlt feltevés — részletes kezelés

### A7 — Az irodai monitorok újrahasznosíthatók

| | |
|---|---|
| **Mikor derült ki** | 2026.03.02., mintavételes ellenőrzésen |
| **Mi derült ki** | A 50 irodai monitorból **14 db csak VGA csatlakozóval** rendelkezik, a laptopokhoz HDMI vagy DisplayPort kell |
| **Hatás** | 14 db adapter szükséges, 13 000 Ft/db = **182 000 Ft** |
| **Ütemhatás** | Nincs — az adapterek raktárkészletről beszerezhetők |
| **Kezelés** | Tartalékkeretből fedezve, projektmenedzseri hatáskörben (1 M Ft alatt) |
| **Döntés** | Tóth Gergő, 2026.03.03. — rögzítve a Döntésnaplóban (D-07) |
| **Tanulság** | A hardver-kompatibilitást **mintavételesen ellenőrizni kell**, nem feltételezni. Átvezetve a Tanulságok naplójába. |

> **Ez a példa mutatja, mire jó ez a dokumentum.** A feltevés február 10-én
> került be, ellenőrzési határidővel. Március 2-án kiderült, hogy hamis — de
> mivel nyilvántartottuk, **még a tervezési fázisban derült ki**, nem az
> eszközkiosztás napján, 50 ember előtt.

## 4. Változásnapló

| Dátum | Változás | Ki |
|---|---|---|
| 2026.02.06. | A napló létrehozása, A1–A5 és L1–L5 felvétele a Charterből | Tóth Gergő |
| 2026.02.10. | A6, A7 felvétele a megvalósíthatósági tanulmány feltételeiből | Tóth Gergő |
| 2026.02.24. | A1 igazolt | Molnár Katalin |
| 2026.02.26. | A3 igazolt | Varga Eszter |
| 2026.03.02. | **A7 megdőlt** — adapterigény, kezelve | Szabó Márk |
| 2026.03.05. | A8 igazolt, feltétellel (3 csapat olvasási hozzáférése) | Nagy Péter |
| 2026.03.06. | L6 felvétele a DPO állásfoglalásából | Tóth Gergő |
| 2026.03.11. | A10 igazolt feltétellel; L7 felvétele az üzemi tanács kikötéséből | Varga Eszter |
| 2026.03.13. | Áttekintés a Planning-kapun; 4 feltevés maradt nyitva (A2, A4, A5, A9) | Tóth Gergő |

---

> **Kapcsolódó dokumentumok:** bemenete a *Projektalapító okirat* és a
> *Megvalósíthatósági tanulmány*; kimenete a *Kockázatnyilvántartás* és a
> *Projektterv*. A megdőlt feltevések a *Problémanaplóba* és a
> *Tanulságok naplójába* vezetendők át.
