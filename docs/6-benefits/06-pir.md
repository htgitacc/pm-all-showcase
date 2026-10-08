# Utólagos értékelés (PIR — Post-Implementation Review)

**Dokumentum azonosítója:** XYO-CP-BEN-006\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, mérési koordinátor\
**Elfogadta:** Projekt Irányító Bizottság — **2026. október 9.**\
**Verzió:** 1.0

> **A mérési szakasz végterméke: tényalapú válasz arra, hogy a projekt
> sikeres volt-e.** Nem véleményt fogalmaz meg, hanem adatot mutat, és abból
> von le következtetést.
>
> A nem teljesült célokat ugyanolyan alaposan mutatjuk be, mint a
> teljesülteket. **A hitelesség itt dől el** — és ettől függ, hogy a
> kiterjesztési javaslatot elhiszik-e.

---

## 1. A minősítés

*(A sikerkritérium 2026.02.05-én, a szponzori jóváhagyással rögzült.
Utólag nem módosítható.)*

| Feltétel | Elvárás | Tény | Teljesült? |
|---|---|---|:-:|
| Célértéket elérő mérőszámok | ≥ 9 / 12 | **10 / 12** | ✔ |
| Kudarcküszöb alatti mérőszám | 0 | **0** | ✔ |
| M11 elégedettség | ≥ 4,0 | **4,2** | ✔ |

# ⟹ MINŐSÍTÉS: **SIKERES**

## 2. A vállalt hasznok és a tényleges eredmények

| # | Mérőszám | T0 | **T+3** | Cél | Elérve | Változás |
|---|---|---:|---:|---:|:-:|---|
| M1 | Ticket / hó | 103 | 74 | ≤ 72 | **✖** | −28% *(cél: −30%)* |
| M2 | MTTR (óra) | 11,4 | **5,1** | ≤ 6,0 | ✔ | −55% |
| M3 | Hozzáférési ticketek | 41% | **17%** | ≤ 20% | ✔ | −59% |
| M4 | Gépbeüzemelés (óra) | 6,5 | **1,4** | ≤ 1,5 | ✔ | −78% |
| M5 | Új belépő (munkanap) | 3,5 | **0,8** | ≤ 1,0 | ✔ | −77% |
| M6 | Home office arány | 0% | 37% | ≥ 40% | **✖** | +37 pp |
| M7 | Adaptáció | 0% | **94%** | ≥ 90% | ✔ | +94 pp |
| M8 | MFA-lefedettség | 0% | **100%** | 100% | ✔ | +100 pp |
| M9 | Rendelkezésre állás | 97,8% | **99,6%** | ≥ 99,5% | ✔ | +1,8 pp |
| M10 | Adatvesztés / negyedév | 0,75 | **0** | 0 | ✔ | −100% |
| M11 | Elégedettség | 3,1 | **4,2** | ≥ 4,0 | ✔ | +1,1 |
| M12 | Fajlagos költség | 12 667 Ft | 17 633 Ft | ≤ 20 000 | ✔ | +39% *(tervezett)* |

## 3. A haszonkategóriák teljesülése

| # | Haszon | Mérőszámok | Értékelés |
|---|---|---|---|
| **H1** | Csökkenő IT-támogatási terhelés | M1 ✖, M2 ✔, M3 ✔ | **Nagyrészt teljesült.** A terhelés összetétele javult a legjobban: a hozzáférési ticketek aránya 41%-ról 17%-ra esett. |
| **H2** | Rugalmas munkavégzés | M6 ✖, M11 ✔ | **Részben teljesült.** A technikai lehetőség megvan (K5 kérdés: 2,2 → 4,3), a kihasználás vezetői korláton múlik. |
| **H3** | Gyorsabb IT-folyamatok | M4 ✔, M5 ✔ | **Teljesült.** A két legnagyobb javulás az egész projektben (−78% és −77%). |
| **H4** | Magasabb biztonsági és szolgáltatási szint | M8 ✔, M9 ✔, M10 ✔ | **Teljesült.** Nulla adatvesztés, 100% MFA, 99,6% rendelkezésre állás. |
| **H5** | Döntési alap a kiterjesztéshez | — | **Teljesült** — ez a dokumentum. |

## 4. Ami nem teljesült

### M1 — Ticket/hó: 74 a célzott 72 helyett

| | |
|---|---:|
| Eltérés | **2 ticket, 2,8%** |
| Kudarcküszöb | > 95 — messze felette |
| Trend | egyértelműen csökkenő |

**Elemzett ok:** a T0 méréskor a ticketek 22%-a fájlszerver-elérési probléma
volt. Ezek gyakorlatilag megszűntek. Helyettük viszont **új típusú
bejelentések** jelentek meg: „hova mentsem?" jellegű használati kérdések,
és az MFA-értesítés késése (H-09). A nettó csökkenés így 28% lett a
tervezett 30% helyett.

> **Nem írjuk át a célértéket utólag.** A mutató formálisan nem teljesült.
> Ugyanakkor a szakmai megítélés szerint **lényegében elérte a célt**, és a
> trend a következő hónapokban tovább javulhat, ahogy a használati kérdések
> fogynak.

### M6 — Home office arány: 37% a célzott 40% helyett

| Csoport | Létszám | M6 | K5 elégedettség |
|---|---:|---:|---:|
| Korlátozás nélküli (heti 3 nap) | 28 fő | **43%** ✔ | 4,7 |
| **Korlátozott (heti max. 2 nap)** | **22 fő** | **29%** ✖ | 3,8 |

**Elemzett ok:** két területvezető a saját mérlegelési jogára hivatkozva heti
maximum 2 napban korlátozza a home office-t, miközben a HR szabályzat heti
3 napot enged.

| | |
|---|---|
| Beavatkozás | Nagy Péter és Varga Eszter egyeztetést kezdeményezett (2026.09.08.) |
| Eredmény | A vezetők fenntartották a korlátozást |
| **Következtetés** | **A projekt a technikai lehetőséget megteremtette. A kihasználás vezetői gyakorlat kérdése, nem technikai kérdés.** |

> A kérdőívben **9 fő jelezte** nyitott kérdésben, hogy „a vezetőm nem engedi
> a heti 3 napot". Ez a második leggyakoribb panasz volt — és nem a
> rendszerről szól.

## 5. Nem várt hatások

Ezek egyik mérőszámban sem szerepeltek, mégis a legértékesebb megfigyelések.

### Pozitív

| # | Megfigyelés | Jelentőség |
|---|---|---|
| 1 | **Az írásbeli kommunikáció mennyisége megnőtt.** A csapatok a SharePointon dokumentálják azt, amit korábban szóban egyeztettek. | A tudás megosztottabb lett; az új belépők gyorsabban felzárkóznak |
| 2 | **A pilot kör lett a belső referencia.** A nem érintett kollégák a pilot résztvevőket kérdezik a felhős munkáról, nem az IT-t. | A kiterjesztés kommunikációjához kész belső támogatói bázis |
| 3 | **A Service Desk munkája átalakult.** A hozzáférési ticketek eltűnésével több idő jut a valódi problémákra. | Ez magyarázza az MTTR 55%-os javulását |

### Negatív

| # | Megfigyelés | Kezelés |
|---|---|---|
| 4 | **Két munkamód alakult ki egy csapaton belül.** A logisztikai csapatban a pilotos és nem pilotos kollégák másképp dolgoznak; a fájlmegosztás körülményes. | A kiterjesztésnél **csapat-szinten kell haladni**, nem vegyesen |
| 5 | **A „mindig elérhető" elvárás megjelent.** Néhány munkatárs jelezte, hogy a home office óta munkaidőn kívül is számítanak a válaszára. | HR-hatáskör; a home office szabályzat pontosítása javasolt |

> **A 4. megfigyelés a legfontosabb a kiterjesztés szempontjából.**
> Az 50 fős kör három szervezeti egységből, vegyesen került ki. Ez a
> méréshez jó volt, a napi működéshez viszont súrlódást okozott.

## 6. Költség és haszon összevetése

| | Terv | Tény |
|---|---:|---:|
| Projektköltség (1. év, egyszeri + folyó) | 50 743 000 Ft | **44 822 000 Ft** |
| Folyó költség a 2. évtől | 10 680 000 Ft/év | **10 580 000 Ft/év** |
| Kapacitás-haszon | 9 176 700 Ft/év | **9 207 250 Ft/év** |

| | |
|---|---|
| **3 éves többletköltség** a hagyományos gépcseréhez képest | kb. **21 000 000 Ft** (terv: 22 325 000 Ft) |
| **3 éves kapacitás-haszon** | kb. **23 000 000 Ft** |
| **Egyenleg** | **enyhén pozitív, kb. 2 000 000 Ft** |

> ⚠ **A kapacitás-haszon nem pénzbeli megtakarítás.** A felszabaduló idő
> csak akkor válik valódi haszonná, ha más értékteremtő feladatra fordítjuk.
> A kontrolling ezért nem számolja el megtakarításként — ahogy azt a
> Költség-haszon elemzés a projekt elején is jelezte.
>
> **A projekt továbbra sem költségmegtakarítási projekt.** Az érv a
> rugalmasság, a biztonsági szint és a kiterjeszthetőség.

## 7. A nyitott pontok állása

| # | Nyitott pont a zárásból | Határidő | Állapot |
|---|---|---|---|
| NY-1 | Hypercare lezárása | 2026.07.03. | ✔ lezárva, a kilépési feltétel teljesült |
| NY-2 | Régi gépek selejtezése | 2026.07.10. | ✔ megtörtént |
| H-06 | Videóhívás mobilneten (2 fő) | 2026.07.31. | ✔ **lezárva** — a szolgáltatói egyeztetés eredményt hozott; a 240 000 Ft-os feltételes keret **nem került felhasználásra**, visszavezetve |
| H-08 | Alkalmazásportál magyar felirata | 2026.09.30. | ✔ javítva a szállítói frissítéssel |
| H-09 | Authenticator értesítés késése | folyamatos | ⏳ **nyitva** — szolgáltatói oldal, figyelés alatt |
| H-13 | Alkalmazásportál ikon | — | ✔ javítva |
| NY-5 | Mérési szakasz | 2026.09.30. | ✔ lezárva |

**Hét nyitott pontból hat lezárva.** A H-09 szolgáltatói oldali jelenség,
üzemeltetési figyelés alatt marad.

## 8. Következtetés

**A Xyo Cloud Pilot sikeres volt.**

| | |
|---|---|
| A projekt **határidőre és a kereten belül** zárult | 10/10 mérföldkő, 44 822 000 Ft / 52 000 000 Ft |
| A vállalt hasznok **túlnyomó része megjelent** | 10/12 mérőszám elérte a célértéket |
| Egyik mutató sem esett a **kudarcküszöb alá** | 0 / 12 |
| A felhasználói elégedettség **3,1-ről 4,2-re** nőtt | a legnagyobb javulás a rugalmasságnál: 2,2 → 4,3 |
| A két nem teljesült mutató **kis mértékben és azonosított okból** maradt el | M1: 2 ticket — új használati kérdések és egy szolgáltatói hiba (H-09) · M6: vezetői korlátozás, nem technikai ok |

**A megoldás technikailag és felhasználói szempontból alkalmas a
kiterjesztésre.** A kiterjesztés feltételeit és ütemét a *Kiterjesztési
javaslat* (XYO-CP-BEN-007) tartalmazza.

## 9. A mérési szakasz tanulságai

*(Átvezetve a Tanulságok naplójába, T-20 – T-23 azonosítóval.)*

| # | Tanulság |
|---|---|
| **T-20** | **A T+1 mérés önmagában félrevezető.** A betanulás és a hypercare miatt a ticketszám a T0 fölé ment (118). Ha egyetlen mérésre alapoztunk volna, a projekt kudarcnak látszott volna. |
| **T-21** | **A torzító tényezőket előre kell leírni.** Az augusztusi 71-es ticketszám a célérték alatt volt, és könnyű lett volna sikerként jelenteni. A KPI-adatlap előre rögzítette, hogy a T+3 a mérvadó. |
| **T-22** | **A mérőszám nem mindig azt méri, amit hiszel.** Az önkiszolgáló jelszó-visszaállítás miatt a könnyű, gyorsan lezárt ticketek eltűntek a mintából, ami az MTTR **értékét felfelé** tolta — a valós javulás tehát nagyobb, mint amit a szám mutat. |
| **T-23** | **A technikai lehetőség nem egyenlő a kihasználással.** Az M6 elmaradása vezetői gyakorlat, nem rendszerhiba. A kiterjesztésnél a szervezeti feltételeket ugyanúgy meg kell teremteni, mint a technikaiakat. |

---

## 10. Elfogadás

| Szerep | Név | Aláírás | Dátum |
|---|---|---|---|
| Készítette | Tóth Gergő, mérési koordinátor | | 2026.10.05. |
| A hasznok gazdája | Nagy Péter, IT osztályvezető | | 2026.10.07. |
| **Elfogadta** | **Projekt Irányító Bizottság** — elnök: Horváth Júlia | | **2026.10.09.** |

---

> **Kapcsolódó dokumentumok:** bemenete a *Haszonrealizálási terv*, a
> *T0 baseline jegyzőkönyv*, a *Havi mérési riportok*, a *Felhasználói
> kérdőív*, a *Projektzáró jelentés* és a *Tanulságok naplója*; kimenete a
> *Kiterjesztési javaslat*.
