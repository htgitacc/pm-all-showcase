# Haszonrealizálási terv (végleges)

**Dokumentum azonosítója:** XYO-CP-BEN-001\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, mérési koordinátor\
**Jóváhagyta:** Nagy Péter, IT osztályvezető — **a hasznok gazdája**\
**Dátum:** 2026. július 2. (a mérési indító egyeztetésen)\
**Verzió:** 2.0

> A Kezdeményezés fázisban készült terv (XYO-CP-009) **operatív változata**.
> Ott még általános elvárás volt; itt már mérőszám, forrás, szűrő, felelős és
> dátum szerepel.
>
> **A siker kritériumát nem most találjuk ki** — az 2026.02.05-én, a szponzori
> jóváhagyással rögzült. Ez a dokumentum csak konkretizál.

---

## 1. A várt hasznok

| # | Haszon | Kinek | Mikor jelentkezik | Mérőszám |
|---|---|---|---|---|
| H1 | Csökkenő IT-támogatási terhelés | IT, Service Desk | 2-3 hónap múlva | M1, M2, M3 |
| H2 | Rugalmas, helyfüggetlen munkavégzés | Munkatársak, HR | azonnal | M6, M11 |
| H3 | Gyorsabb IT-folyamatok | IT, HR | azonnal | M4, M5 |
| H4 | Magasabb biztonsági és szolgáltatási szint | Egész vállalat | azonnal | M8, M9, M10 |
| H5 | Megalapozott döntési alap a kiterjesztéshez | Vezetés | 2026.10.09. | mind |

## 2. Mérőszámok, kiindulási és célértékek

| # | Mérőszám | Mértékegység | **T0** | **Cél (T+3)** | **Kudarcküszöb** | Felelős |
|---|---|---|---:|---:|---:|---|
| M1 | Helpdesk ticketek | db / hó | 103 | **≤ 72** | > 95 | Kiss Réka |
| M2 | Átlagos megoldási idő (MTTR) | óra | 11,4 | **≤ 6,0** | > 10,0 | Kiss Réka |
| M3 | Hozzáférési ticketek aránya | % | 41 | **≤ 20** | > 35 | Kiss Réka |
| M4 | Gépbeüzemelési idő | óra / gép | 6,5 | **≤ 1,5** | > 3,0 | Szabó Márk |
| M5 | Új belépő munkába állása | munkanap | 3,5 | **≤ 1,0** | > 2,0 | Varga Eszter |
| M6 | Home office napok aránya | % | 0 | **≥ 40** | < 20 | Varga Eszter |
| M7 | SharePoint/OneDrive adaptáció | % | 0 | **≥ 90** | < 70 | Szabó Márk |
| M8 | MFA-lefedettség | % | 0 | **100** | < 100 | Szabó Márk |
| M9 | Rendelkezésre állás | % | 97,8 | **≥ 99,5** | < 99,0 | Szabó Márk |
| M10 | Adatvesztési esetek | db / negyedév | 0,75 | **0** | ≥ 1 | Kiss Réka |
| M11 | Felhasználói elégedettség | 1–5 | 3,1 | **≥ 4,0** | < 3,5 | Varga Eszter |
| M12 | Fajlagos IT-költség | Ft / fő / hó | 12 667 | **≤ 20 000** | > 24 000 | Balogh Tamás |

> **Az M12 célértéke tudatosan magasabb a T0-nál.** A felhős folyó költség
> nagyobb, mint a régi üzemeltetésé — ezt az Üzleti indoklás nyíltan kimondta.
> A projekt nem költségmegtakarítási projekt. **Kudarc az, ha 24 000 Ft fölé
> megy**, nem az, ha nő.

## 3. Mi számít sikernek?

*(Rögzítve 2026.02.05-én, a szponzori jóváhagyással. Nem módosítható.)*

| Minősítés | Feltétel |
|---|---|
| **Sikeres** | A 12 mérőszámból **legalább 9 eléri a célértéket**, **egyik sem esik a kudarcküszöb alá**, és az **M11 (elégedettség) eléri a 4,0-t** |
| **Nem sikeres** | 6-nál kevesebb célérték, **vagy** 2-nél több kudarcküszöb alatt, **vagy** az M11 3,5 alatt marad |
| **Részben sikeres** | **Minden más eset** (pl. 6–8 célérték; vagy legalább 9 célérték mellett is, ha 1-2 mutató a kudarcküszöb alá esik; vagy az M11 3,5 és 4,0 között) |

### A minősítéshez tartozó javaslat

| Minősítés | Javaslat a kiterjesztésre |
|---|---|
| Sikeres | Szakaszos kiterjesztés a teljes szervezetre |
| Részben sikeres | **Feltételes** kiterjesztés: előbb a gyenge mutatók okának kezelése, majd újramérés 3 hónap múlva |
| Nem sikeres | A kiterjesztés elvetése; a pilot kör üzemeltetése folytatódik, a tanulságok írásba foglalásával |

## 4. Mérési ütemterv

| Mérés | Dátum | Mit | Felelős |
|---|---|---|---|
| **T0 — baseline** | **2026.01.30.** ✔ | mind a 12 | Tóth Gergő |
| T+0 — átadás | 2026.06.30. ✔ | M8, M9 | Szabó Márk |
| **T+1** | 2026.07.31. | mind a 12, a betanulási hatás jelzésével | Tóth Gergő |
| **T+2** | 2026.08.31. | mind a 12 | Tóth Gergő |
| **T+3** | 2026.09.30. | mind a 12 + elégedettségi kérdőív | Tóth Gergő |
| PIR | 2026.10.09. | értékelés, kiterjesztési javaslat | Tóth Gergő |

**Havi egyeztetés:** minden hónap 5. munkanapján, 45 perc, a mérési
felelősökkel és Nagy Péterrel.

## 5. Ismert torzító tényezők

**Előre rögzítjük**, különben a mérés után válnak vitatottá.

| Mérőszám | Torzító tényező | Kezelés |
|---|---|---|
| M1, M2, M3 | **Júliusi-augusztusi szabadságolás** csökkenti a ticketszámot (a munkanapok kb. 18%-kal kevesebbek) | **A T+3 (szeptemberi) érték a mérvadó**; a T+1 és T+2 trendjelző |
| M1 | A **betanulási időszak** átmenetileg **növeli** a ticketszámot | A T+1 hónap külön értelmezendő, nem hasonlítható a célértékhez |
| M1 | A **hypercare 2026.07.03-ig tart** — a kiemelt támogatás több bejelentést generál | A T+1 értéket ez felfelé torzítja |
| M6 | Nyáron kevesebb a munkanap | **Arányszámot** használunk, nem abszolút napszámot |
| M11 | Az újdonság okozta lelkesedés felfelé torzíthat | **Ugyanazokat a kérdéseket** használjuk, mint a T0-nál |
| M12 | Az egyszeri beruházás nem szerepel a folyó költségben | **Kizárólag az OPEX-et mérjük**, jelzett módon |
| M4, M5 | Kis elemszám (7-8 esemény) | Átlagot közlünk, a tartománnyal együtt |

## 6. Felelősségek

| Szerep | Ki | Mit |
|---|---|---|
| **A hasznok gazdája** | **Nagy Péter**, IT osztályvezető | Azért felel, hogy a hasznok **ténylegesen megjelenjenek**; beavatkozik, ha egy mutató rossz irányba megy |
| Mérési koordinátor | Tóth Gergő | A mérések begyűjtése, riportálás, PIR |
| Adatszolgáltatók | Kiss Réka, Szabó Márk, Varga Eszter, Balogh Tamás | A saját mérőszámaik azonos módszertanú kiolvasása |
| Döntéshozó | Projekt Irányító Bizottság | A kiterjesztésről szóló döntés a PIR alapján |

**Az átadás 2026.06.30-án megtörtént**, minden mérőszámhoz nevesített,
írásban visszaigazolt felelőssel — ez volt a projektzárás feltétele.

## 7. Adatvédelmi kikötés

| | |
|---|---|
| **Csak csoportszintű összesítés** publikálható; egyéni bontás nem | M6, M7 |
| Az elégedettségi kérdőív **névtelen** | M11 |
| **DPO-állásfoglalás a mérési adatgyűjtésre** | dr. Fekete Zsolt, **2026.06.30.** — a gyűjtés a leírt formában megfelelő |

> Az egyéni szintű használati adat munkavállalói megfigyelésnek minősül.
> Ezt a DPIA (XYO-CP-118) 4. pontja is kiköti, és az üzemi tanács kikötése
> (L7 korlát) is erre vonatkozik.

## 8. Mi változott a kezdeti tervhez képest?

| # | Változás | Miért |
|---|---|---|
| 1 | A pontos **szűrőfeltételek** rögzítése minden mérőszámnál | A T0 jegyzőkönyv tapasztalata: ugyanazzal a lekérdezéssel kell mérni |
| 2 | A **hypercare torzító hatásának** jelzése az M1-nél | A hypercare 07.03-ig tart, tehát a T+1 hónapba belelóg |
| 3 | Az **M4, M5 kis elemszámának** jelzése | 7-8 esemény átlaga; a tartományt is közöljük |
| 4 | A **T+3 mérvadóságának** kimondása az M1–M3-nál | A szabadságolási torzítás miatt |

**A célértékek, a kudarcküszöbök és a sikerkritérium nem változott.**

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, mérési koordinátor | 2026.07.02. |
| **Jóváhagyta** | **Nagy Péter**, a hasznok gazdája | 2026.07.02. |

> **Kapcsolódó dokumentumok:** bemenete a *Haszonrealizálási terv (kezdeti)*
> és a *Projektzáró jelentés*; kimenete a *KPI-adatlap*, a *Havi mérési
> riportok* és a *PIR*.
