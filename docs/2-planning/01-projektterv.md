# Projektterv (Project Management Plan)

**Dokumentum azonosítója:** XYO-CP-101\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Jóváhagyta:** Projekt Irányító Bizottság — 2026.03.13.\
**Verzió:** 1.0 — **baseline**

> **Ez gyűjtődokumentum, nem tartalomtár.** Megmondja, hol találod a hatókört,
> az ütemet, a költséget és a szabályokat, és hogyan kapcsolódnak egymáshoz.
> A jó Projektterv 10-15 oldal, ami hivatkozik — nem egy 120 oldalas,
> olvashatatlan tömb.

---

## 1. A projekt egy oldalban

| | |
|---|---|
| **Cél** | 50 fő felhőalapú munkakörnyezetben, migráció nélkül, és tényadat a kiterjesztési döntéshez |
| **Időtartam** | 2026.02.02 – 2026.06.30., + 3 hónap mérési szakasz 2026.09.30-ig |
| **Költségkeret** | 52 000 000 Ft, tervezett költés 50 743 000 Ft |
| **Szponzor** | Kovács Anita, gazdasági igazgató |
| **Projektmenedzser** | Tóth Gergő |
| **Szakmai vezető, a hasznok gazdája** | Nagy Péter, IT osztályvezető |
| **Platform** | Microsoft 365 Business Premium, Entra ID, Intune, SharePoint, OneDrive, Azure VPN |

## 2. A résztervek

| # | Dokumentum | Azonosító | Mit szabályoz |
|---|---|---|---|
| 1 | Hatókör-nyilatkozat | XYO-CP-102 | Mit szállítunk, és **mit nem** |
| 2 | Munkalebontási szerkezet (WBS) | XYO-CP-103 | A teljes munka lebontása munkacsomagokra |
| 3 | WBS-szótár | XYO-CP-104 | Munkacsomagonként a **kész-definíció** |
| 4 | Követelmény-nyomonkövetési mátrix | XYO-CP-105 | Ki mit kért, hol valósul meg, mi bizonyítja |
| 5 | Ütemterv és mérföldkőlista | XYO-CP-106 | Mikor mi történik; a kritikus út |
| 6 | Költségvetés és költségbázis | XYO-CP-107 | Miből mennyi, mikor; a tartalék szabálya |
| 7 | Erőforrásterv | XYO-CP-108 | Ki mikor, mennyit; kapacitás-jóváhagyások |
| 8 | Felelősségi mátrix (RACI) | XYO-CP-109 | Ki dönt, ki csinálja, kit kérdezünk |
| 9 | Kockázatnyilvántartás | XYO-CP-110 | Mi mehet félre, ki figyeli, mit teszünk |
| 10 | Kommunikációs terv | XYO-CP-111 | Kinek, mit, mikor, milyen csatornán |
| 11 | Beszerzési terv | XYO-CP-112 | Mit, mikor, milyen eljárással szerzünk be |
| 12 | Szállítóértékelési szempontrendszer | XYO-CP-113 | Mi alapján választunk szállítót |
| 13 | Minőségterv és átvételi kritériumok | XYO-CP-114 | Mit jelent, hogy kész van |
| 14 | Változáskezelési eljárás | XYO-CP-115 | Hogyan módosítható a terv |
| 15 | Tesztterv | XYO-CP-116 | Hogyan bizonyítjuk, hogy működik |
| 16 | Oktatási és adaptációs terv | XYO-CP-117 | Hogyan készítjük fel az embereket |
| 17 | Adatvédelmi hatásvizsgálat | XYO-CP-118 | GDPR-megfelelés és a feltételei |
| 18 | Biztonsági alapkonfiguráció | XYO-CP-119 | Milyen beállításokkal indul a környezet |
| 19 | Visszaállási terv | XYO-CP-120 | Mit teszünk, ha az élesítés nem sikerül |

## 3. Mi a baseline?

**A baseline a jóváhagyott hatókör, ütemterv és költségvetés befagyasztott
változata.** Ehhez mérjük az eltérést a projekt hátralévő részében.

| Elem | Dokumentum | Befagyasztva |
|---|---|---|
| Hatókör-bázis | Hatókör-nyilatkozat v1.0 + WBS v1.2 | 2026.03.13. |
| Ütem-bázis | Ütemterv v1.0 | 2026.03.13. |
| Költség-bázis | Költségvetés v1.0 | 2026.03.13. |

**A baseline csak jóváhagyott változáskérelemmel módosítható**
(Változáskezelési eljárás, XYO-CP-115). A módosítás után minden érintett
dokumentum verziószámot vált.

## 4. Irányítási rend — ki mit dönt

| Döntés tárgya | Ki dönt | Fórum |
|---|---|---|
| Napi munkaszervezés, feladatátcsoportosítás | Tóth Gergő | — |
| Tartalékkeret ≤ 1 000 000 Ft / eset | Tóth Gergő | — (Döntésnaplóba) |
| Változás ≤ 1 M Ft és ≤ 3 nap, mérföldkövet nem érint | Tóth Gergő | — |
| Szakmai/technikai megoldás | Nagy Péter | heti szakmai egyeztetés |
| Beszerzési eljárás szabályossága | Molnár Katalin | — |
| Változás > 1 M Ft **vagy** > 3 nap **vagy** hatókör | Kovács Anita | szponzori egyeztetés |
| Az M7 vagy M10 mérföldkő módosítása | Projekt Irányító Bizottság | havi Steering ülés |
| Keretösszeg, projektcél, leállítás | Projekt Irányító Bizottság | havi Steering ülés |
| Adatvédelmi kérdés | dr. Fekete Zsolt | írásos állásfoglalás |

**A Projekt Irányító Bizottság összetétele:** Horváth Júlia (elnök),
Kovács Anita, Nagy Péter, Varga Eszter. Ülésezik: havonta, első szerdán.

## 5. Riportálási rend

| Riport | Kinek | Gyakoriság | Ki |
|---|---|---|---|
| Heti státuszriport | Projektcsapat, szponzor, kontroller | hétfőnként | Tóth Gergő |
| Steering riport (1 oldal) | Projekt Irányító Bizottság | havonta | Tóth Gergő |
| Kockázati riport | Steering + kockázatgazdák | kéthetente | Tóth Gergő |
| Költségriport | Szponzor, kontroller | havonta | Balogh Tamás |
| Pilot hírlevél | 50 résztvevő | kéthetente | Tóth Gergő |

Részletek: *Kommunikációs terv (XYO-CP-111)*.

## 6. Eszkalációs út

| Szint | Kihez | Válaszidő |
|---|---|---|
| 1 | Tóth Gergő, projektmenedzser | 1 munkanap |
| 2 | Nagy Péter, IT osztályvezető | 2 munkanap |
| 3 | Kovács Anita, szponzor | 3 munkanap |
| 4 | Projekt Irányító Bizottság | következő ülés / rendkívüli ülés |

**Azonnal, a szinteket átugorva:** adatvédelmi incidens; mérföldkő 5 napnál
nagyobb csúszása; a költség-előrejelzés meghaladja az 51 000 000 Ft-ot;
a szállító jelzi, hogy nem tud teljesíteni.

## 7. Dokumentumkezelés

| | |
|---|---|
| **Tárolás** | SharePoint: *Projektek / Xyo Cloud Pilot* |
| **Verziózás** | Fő verzió a jóváhagyott állapotokra (1.0, 2.0), alverzió a közbenső módosításokra |
| **Változásnapló** | Minden élő dokumentum végén kötelező |
| **Korlátozott hozzáférés** | Szerződések és ajánlatok: beszerzés zárt tárhelye; Hatalom-érdek mátrix: PM és szponzor; nyers kockázatnyilvántartás: csak belső |
| **Archiválás** | A projektzáráskor, az Archiválási jegyzék szerint |

## 8. Élő dokumentumok — amiket a projekt alatt folyamatosan vezetünk

| Dokumentum | Frissítés | Ki |
|---|---|---|
| Kockázatnyilvántartás | kéthetente | Tóth Gergő |
| Feltevés- és korlátnapló | eseményvezérelt | Tóth Gergő |
| Érintettek nyilvántartása | havonta | Tóth Gergő |
| Problémanapló | naponta | Tóth Gergő |
| Döntésnapló | eseményvezérelt | Tóth Gergő |
| Változásnapló | eseményvezérelt | Tóth Gergő |
| Hatókörön kívüli elemek listája | **eseményvezérelt, azonnal** | Tóth Gergő |
| Tanulságok naplója | folyamatosan, nem a végén | Tóth Gergő |

> **A tanulságokat menet közben kell gyűjteni.** A záró workshopon már senki
> nem emlékszik a márciusi problémákra — pedig pont azok a leghasznosabbak.

## 9. A projekt utáni időszak

A projekt 2026.06.30-án zárul, de **a mérés még 3 hónapig tart.**

| | |
|---|---|
| Mérési szakasz | 2026.07.01 – 2026.09.30. |
| A hasznok gazdája | **Nagy Péter** (nem a projektmenedzser) |
| Mérési koordinátor | Tóth Gergő |
| Zárás | Utólagos értékelés (PIR) és kiterjesztési javaslat, 2026.10.09. |

A mérési felelősségek írásos átadása a **projektzárás feltétele**.

## 10. Változásnapló

| Dátum | Változás | Verzió |
|---|---|---|
| 2026.03.06. | Első teljes változat | 0.9 |
| 2026.03.11. | Az irányítási rend pontosítása a RACI vitái után | 0.95 |
| 2026.03.13. | **Jóváhagyva, baseline befagyasztva** | 1.0 |

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.03.06. |
| Jóváhagyta | Projekt Irányító Bizottság | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete a *Projektalapító okirat* és a
> *Feltevés- és korlátnapló*; kimenete a *Munkacsomag-kiadás*, a
> *Státuszriport* és a *Változáskezelési eljárás*.
