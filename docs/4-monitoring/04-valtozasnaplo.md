# Változásnapló (Change Log)

**Dokumentum azonosítója:** XYO-CP-304\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Utolsó frissítés:** 2026. június 19.\
**Verzió:** 1.4 — **élő dokumentum**

> **A projekt végén ez magyarázza meg, miért nem az lett, ami eredetileg
> tervben volt** — és ez a magyarázat téged véd.
> **Az elutasított kérelmeket is vezesd be.** Vitánál az elutasítás
> dokumentálása még fontosabb, mint a jóváhagyásé.

---

## 1. Benyújtott változáskérelmek

| # | Tárgy | Benyújtó | Benyújtva | Döntéshozó | Döntés | Dátum | Ütemhatás | Költséghatás | Baseline frissítve |
|---|---|---|---|---|---|---|---:|---:|---|
| VK-01 | A pilot bővítése 50 → 65 főre | Papp Zsófia | 05.19. | Projekt Irányító Bizottság | **elutasítva** | 06.03. | (+3 hét) | (+8 325 000 Ft) | nem |
| VK-02 | Hypercare +1 Service Desk munkatárs | Kiss Réka | 05.28. | Nagy Péter | **jóváhagyva** | 06.01. | 0 nap | 0 Ft | nem szükséges |
| VK-03 | Monitorcsere az adapteres 14 főnél | Fodor Gábor | 06.01. | Tóth Gergő (PM) | **elutasítva** | 06.03. | (+2 hét) | (+910 000 Ft) | nem |
| VK-04 | Feltételes keret a H-06 kezelésére | Nagy Péter | 06.17. | Tóth Gergő (PM) | **jóváhagyva, feltételesen** | 06.17. | 0 nap | 240 000 Ft | igen (Költségvetés v1.1) |

*A zárójeles értékek az elutasított kérelmek hatásvizsgálatában szereplő,
meg nem valósult hatások.*

## 2. Összesítés

| | Darab | Költséghatás | Ütemhatás |
|---|---:|---:|---:|
| Jóváhagyva | 2 | 240 000 Ft | 0 nap |
| Elutasítva | 2 | — | — |
| Elhalasztva | 0 | — | — |
| **Összesen benyújtva** | **4** | **240 000 Ft** | **0 nap** |

**A jóváhagyott változások összesen 240 000 Ft-tal és 0 nappal módosították a
baselinet.** Ez a projekt teljes hosszára vetítve a költségbázis **0,5%-a**.

## 3. A tartalékkeret alakulása

| Dátum | Esemény | Változás | Szabad tartalék |
|---|---|---:|---:|
| 2026.02.02. | Projektalapító okirat: tartalékkeret jóváhagyva | — | 4 613 000 Ft |
| 2026.03.03. | D-07: 14 db HDMI–VGA adapter (A7 feltevés megdőlt) | −182 000 Ft | 4 431 000 Ft |
| 2026.03.13. | Baseline jóváhagyva (a D-07 lekötésével együtt) | — | 4 431 000 Ft |
| 2026.06.17. | VK-04: feltételes keret a H-06 kezelésére | −240 000 Ft | **4 191 000 Ft** |

**A tartalék 9,1%-a (422 000 Ft) került felhasználásra vagy elkülönítésre;**
ténylegesen elköltve csak az adapterek 182 000 Ft-ja (3,9%).

> A D-07 (adapterek) **nem változáskérelemként** került be, hanem
> projektmenedzseri hatáskörben hozott döntésként, mert nem érintette a
> hatókört, az ütemet és a mérföldköveket — csak a tartalékot, 1 M Ft alatt.
> A Döntésnaplóban szerepel.

## 4. Amit megvizsgáltunk, de NEM igényelt változáskérelmet

Ez a rész legalább olyan fontos, mint a benyújtott kérelmek listája:
megmutatja, **hol húztuk meg a határt**.

| # | Módosítás | Miért nem kellett változáskérelem | Hol dokumentált |
|---|---|---|---|
| 1 | **A CA-05 feltételes hozzáférési szabály átalakítása** (országkorlátozás → megbízható eszköz + MFA) | Technikai megvalósítási mód a jóváhagyott hatókörön belül. Nem érinti a hatókört, ütemet, költséget és átvételi kritériumot. **Biztonsági vonatkozása miatt viszont a szakmai vezető döntött, nem a PM**, DPO-véleménnyel. | D-14, As-built 2.3 |
| 2 | Az ügyviteli kliens telepítési módja kötelezőről opcionálisra | Hibajavítás (P-06), nem hatókörváltozás. Az AK-06 kritérium teljesülését szolgálja. | D-15 |
| 3 | A `CP-Kozos` csapatoldal létrehozása | A D4 szállítandó eredményen („SharePoint csapatoldalak") belül van; nem bővíti a hatókört. | D-16 |
| 4 | Az OneDrive előszinkronizálás bevezetése a kiosztás előtt | Munkaszervezési döntés, nincs hatóköri, költség- és ütemhatása. | D-17 |
| 5 | Az oktatás 2. blokkjának bővítése 25-ről 30 percre | A jóváhagyott oktatási terv részletén belüli finomítás. | Oktatási anyag 5. pont |

> **Ha ezek mind változáskérelemként mentek volna végig**, a projekt
> adminisztrációja megbénult volna, és a Steering Committee 5 érdemtelen
> kérdéssel foglalkozott volna. **Ha viszont egy sem** — akkor a hatókör
> észrevétlenül nőtt volna.
>
> A határ a *Változáskezelési eljárás* 1. pontjában van: a **jóváhagyott
> hatókör, baseline ütemterv, költségbázis, átvételi kritérium vagy K/F
> prioritású követelmény** érintettsége.

## 5. Hatókörön kívülre került kérések

Ezek nem változáskérelemként érkeztek, hanem beszélgetésekben merültek fel.
A *Hatókör-nyilatkozat* 4. pontjába kerültek, a felmerülés dátumával.

| # | Kérés | Ki vetette fel | Mikor |
|---|---|---|---|
| K8 | A régi fájlszerver teljes tartalmának átmozgatása SharePointra | Fodor Gábor | 02.24. |
| K9 | Céges mobiltelefon a pilot résztvevőknek | Szilágyi Anna | 02.27. |
| K10 | Otthoni irodabútor beszerzése | Papp Zsófia | 03.04. |
| K11 | Otthoni nyomtatási megoldás | Szilágyi Anna | 03.10. |

> **Négy hét alatt négy kérés** — mindegyik ésszerű, mindegyik „ez csak egy
> apróság" felvezetéssel. Ha nem írod le őket azonnal, az Execution közepén
> már azt fogod hallani, hogy „de hát ezt megbeszéltük".

## 6. Elutasított követelmények

A tervezési fázisban, a követelményfelvételkor elutasított kérések
(*Követelmény-nyomonkövetési mátrix* 6. pont): 5 db (E01–E05).

Ezek közül **egy sem tért vissza** változáskérelemként az Execution során —
ami azt jelzi, hogy az elutasítás indoklása elfogadott volt.

---

## 7. Amit a változáskezelésről megtanultunk

| Megfigyelés | Következmény |
|---|---|
| **4 kérelem az egész projektre kevés** — de ez nem azt jelenti, hogy nem volt nyomás | A hatókörön kívüli kérések listája (4 db) és a nem-CR módosítások (5 db) mutatják a valódi forgalmat |
| A **VK-01 hatásvizsgálatának 4.7 pontja** (közvetett hatások) hozta a döntő érvet: a mérés torzulása | A közvetett hatásokat soha ne hagyd ki a vizsgálatból |
| A **VK-03-nál a benyújtó nem töltötte ki a „mi történik, ha nem" mezőt** | Ez a mező szűri ki a „jó lenne, ha" kéréseket |
| A **CA-05 módosítása nem volt CR, de nem is a PM döntötte el** | Az összeghatár nem minden: biztonsági szintet érintő döntést a szakmai vezető hoz |
| Minden elutasított kérelem **írásos indoklást** kapott, és a benyújtó személyes tájékoztatást | Egyik elutasítás sem vezetett konfliktushoz |

---

> **Kapcsolódó dokumentumok:** bemenete a *Változáskérelem* és a
> *Változáskezelési eljárás*; kimenete a *Projektzáró jelentés*, a
> *Tanulságok naplója* és a *Steering riport*.
