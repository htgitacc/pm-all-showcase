# Szolgáltatási elfogadás és korai életszakasz-támogatás (hypercare)

**Dokumentum azonosítója:** XYO-ITIL-005\
**Szolgáltatás:** Felhőalapú munkahely (XYO-ITIL-001)\
**Készítette:** Tóth Gergő, projektmenedzser, Kiss Rékával\
**Elfogadta:** Nagy Péter, szolgáltatásgazda\
**Dátum:** **2026. június 26.** — az átadás-átvétel napja\
**Verzió:** 1.0

> ⚠ **ITIL 4-kiegészítés.** A Xyo átadás-átvételi jegyzőkönyve (XYO-CP-401) 26 átvételi
> kritériumot vezet végig tételesen — ez egy PMI-projektben is kiemelkedően jó. Az ITIL egy
> kérdéssel egészíti ki: **a projekt eredménye kész — de kész-e a szolgáltatás?** A kettő nem
> ugyanaz: egy hibátlanul átadott rendszer mellett is lehet, hogy senki nem tudja, ki dönt egy
> éles változásról, vagy mit ígértünk a felhasználóknak.
>
> **A hypercare ITIL-neve korai életszakasz-támogatás** (*early life support*, ELS): a
> szolgáltatás első hetei, amikor a projekt még fokozott figyelemmel kíséri, mielőtt a normál
> üzemeltetésbe kerül.

---

## 1. Az átvételi kritériumok ITIL-szemmel

A 26 kritériumot az ITIL szerint négy csoportba soroltuk. A kérdés: **mit vizsgált az átvétel?**

| Csoport | Mit kérdez | Kritériumok | Darab |
|---|---|---|---:|
| **Haszon** (*utility*) | Tudja-e, amit kell? | AK-01, AK-05, AK-11, AK-12, AK-16, AK-17, AK-18, AK-19 | 8 |
| **Garancia** (*warranty*) — biztonság, teljesítmény, folytonosság | Megbízhatóan tudja-e? | AK-02, AK-03, AK-04, AK-06, AK-07, AK-08, AK-09, AK-10, AK-13, AK-14, AK-15 | 11 |
| **Támogathatóság** | Tudják-e üzemeltetni és támogatni? | AK-20, AK-21, AK-22, AK-23 | 4 |
| **Minőségi kapu** | Elég jó-e a teszt eredménye? | AK-24, AK-25, AK-26 | 3 |
| **Összesen** | | | **26** |

> **Ami ebből kiolvasható:** a Xyo átvétele **többet vizsgált a garanciából, mint a haszonból**
> (11 a 8-hoz), és négy kritérium kifejezetten az üzemeltethetőségről szólt — például az AK-22:
> a Service Desk útmutatója legalább 2 héttel az élesítés előtt. A legtöbb projekt csak az első
> csoportot nézi („működik-e?”). **Az egyetlen nem teljesült kritérium, az AK-19 (videóhívás
> mobilneten) haszon-kritérium** — és az oka a mobilszolgáltató, nem a megoldás.

## 2. Amit az ITIL még kérne — a szolgáltatási elfogadási kritériumok

Az átvételi kritériumok a **projekt eredményét** mérik. A szolgáltatási elfogadási
kritériumok (*service acceptance criteria*) azt, hogy **a szolgáltatás működtethető-e a projekt
nélkül.** Az átadás napján így állt:

| # | Szolgáltatási elfogadási kritérium | Állapot 2026.06.26-án | Bizonyíték |
|---|---|:-:|---|
| SZE-01 | Az üzemeltetés átvette, és nyilatkozott, hogy önállóan üzemelteti | ✔ | Run-book 9. pont — Nagy Péter, Szabó Márk, Kiss Réka aláírásával |
| SZE-02 | A szolgáltatásleírás és a kizárások jóváhagyva | ✔ | XYO-ITIL-001 |
| SZE-03 | Az SLA aláírva, legalább ideiglenes célokkal | ✔ | XYO-ITIL-002, 1.0 verzió |
| SZE-04 | A változásengedélyezés rendje és a szabványos változások listája | ✔ | XYO-ITIL-003 (06.19.) |
| SZE-05 | A nyitott hibák ismert hibaként, kerülőmegoldással és gazdával | ✔ | Run-book 7. pont: négy nyitott hiba, mindegyikhez kerülőmegoldás és felelős |
| SZE-06 | Tudásbázis a Service Desknek | ✔ | Run-book 4. pont (15 eset), gyorssegédlet |
| SZE-07 | A Service Desk kapacitása az élesítés utáni időszakra | ✔ | Hypercare +1 fő (VK-02, D-20) |
| SZE-08 | A beszállítói hozzáférés megszűnése ellenőrizve | ✔ | NY-3, Run-book 2. pont |
| SZE-09 | Ki és mi alapján figyeli a szolgáltatás állapotát | **részben** | Havi ellenőrzések (Run-book 3. pont); riasztás csak a break-glass belépésre |
| SZE-10 | Helyettes a 2. támogatási szinten | **✖ nyitott** | Szabó Márk egyedül — ideiglenesen Nagy Péter (XYO-ITIL-002, 5.1) |

**Tíz kritériumból nyolc teljesült, egy részben, egy nyitott.** Az utóbbi kettő nem akadályozza
az átvételt, de felelőssel és határidővel a folyamatos fejlesztési nyilvántartásba kerül
(XYO-ITIL-006).

> **Tipikus hiba:** az átvételt a projekt határideje diktálja, és a szolgáltatási kritériumok
> „majd menet közben” teljesülnek. A Xyo esetében az SZE-01 – SZE-08 nagy része a projekt saját
> munkájából adódott — a Run-book, az ismert hibák listája és a Service Desk felkészítése
> eleve kész volt. **Az ITIL itt nem új munkát kér, hanem azt, hogy ezt a listát valaki
> kimondja és aláírja.**

## 3. Ki dönt az üzembe vételről?

| Döntés | Ki dönt a projektben | Ki dönt ITIL szerint | A Xyo-nál |
|---|---|---|---|
| A projekt eredménye elfogadható | A megrendelő képviselője (átvevő) | — | Nagy Péter, 06.26. |
| A megoldás a valós munkára alkalmas | A felhasználói képviselő (UAT) | — | UAT-elfogadás, 06.19. |
| **A szolgáltatás működtethető** | — | **Az üzemeltetés és a szolgáltatásgazda** | Run-book 9. pont: Nagy Péter, Szabó Márk, Kiss Réka |
| **Az ELS lezárható** | — | **A Service Desk vezetője, a szolgáltatásgazda tájékoztatásával** | Kiss Réka (RACI: „A”) |

> **A Xyo itt jól csinálta:** a Run-bookot nemcsak az átvevő, hanem a rendszergazda és a Service
> Desk vezetője is aláírta. Ez az ITIL-elv lényege: **akik működtetni fogják, azok mondják ki,
> hogy működtethető.**

## 4. Korai életszakasz-támogatás — a hypercare

### 4.1 A terv (a WBS-szótár 7.4 és az Oktatási terv 5. pontja szerint)

| | |
|---|---|
| **Időszak** | 2026.06.15 – 07.03. (3 hét, az utolsó élesítési hullám után) |
| **Mit ad a felhasználóknak** | 2 órás válaszidő a „CP” címkés ticketekre; napi hibaáttekintés; helyszíni segítség igény szerint |
| **Kapacitás** | Kiss Réka + 2 Service Desk munkatárs, és +1 fő átcsoportosítással (VK-02) |
| **Kilépési feltétel** | A napi új hibabejelentések száma **két egymást követő héten a normál szint 150%-a alá** csökken |
| **Ha nem teljesül** | Meghosszabbítás a projektzáráson túl, Nagy Péter felelősségével |
| **Döntéshozó** | Kiss Réka (RACI: „A”) |

> **A kilépési feltétel mérhető állapot, nem dátum** — ez a hypercare legjobb tulajdonsága. Az
> ITIL ugyanezt kéri az ELS-től: **kilépési kritérium** nélkül a korai támogatás vagy túl korán
> ér véget, vagy soha.

### 4.2 Mit jelent a „normál szint” számokban?

A kilépési feltételt csak akkor lehet ellenőrizni, ha a „normál szint” számmal is meg van adva.

| | Számítás | Érték |
|---|---|---:|
| T0: a pilot kör éves ticketszáma (2025) | T0 baseline jegyzőkönyv | 1 240 db |
| Havi átlag | 1 240 / 12 | 103,3 db/hó |
| Munkanapi átlag (havi 21 munkanappal számolva) | 103,3 / 21 | kb. 4,9 db/nap |
| **A kilépési küszöb (150%)** | 4,9 × 1,5 | **kb. 7,4 db/nap** |

**Két pontosítás, amit az ITIL hozzátesz:**

1. **Csak az incidenseket számoljuk, a kéréseket nem.** A hypercare alatt sok „hova mentsem?”
   típusú kérdés érkezik — ezek információkérések (XYO-ITIL-001, 4. pont). Ha beleszámítanak, a
   hypercare a szükségesnél tovább tart, pedig a szolgáltatás már stabil.
2. **A mért heti értéket a kilépéskor rögzíteni kell** (6. pont) — a kiterjesztés hypercare-
   tervezéséhez éppen ezek a számok kellenek.

### 4.3 Mit tesz hozzá a hypercare a mérésekhez?

A hypercare **ösztönzi a bejelentést** — ez a dolga. A T+1 riport becslése szerint a júliusi
ticketszámot 12 tickettel növelte. Ezért a KPI-adatlap előre rögzítette, hogy a T+1 nem
mérvadó. **Az SLA-célok mérése ezért az ELS után kezdődik** (XYO-ITIL-002).

## 5. Az ELS lezárásának lépései

| # | Lépés | Ki | Mikor |
|---|---|---|---|
| 1 | A kilépési feltétel ellenőrzése a ticketrendszerből, két egymást követő hétre | Kiss Réka | 07.03. |
| 2 | A hypercare alatt nyitott incidensek átadása a normál sorba | Kiss Réka | 07.03. |
| 3 | Az új ismétlődő tünetek felvétele ismert hibaként vagy problémaként | Szabó Márk | 07.03. |
| 4 | A Run-book 4. pontjának frissítése a hypercare tapasztalataival | Kiss Réka, Szabó Márk | 07.10. |
| 5 | A „CP” címke kivezetése: a 2 órás válaszidő megszűnik, az SLA célidői lépnek életbe | Kiss Réka | 07.03. |
| 6 | Tájékoztatás a felhasználóknak: mi változik | Kiss Réka | 07.03. |

> **Az 5. lépést a felhasználók érzik meg.** Ha senki nem mondja meg nekik, hogy a 2 órás
> válaszidő a hypercare-hez tartozott, a normál üzem „romlásnak” tűnik — és ez az elégedettségi
> mérésben jelentkezik.

## 6. ELS-kilépési jegyzőkönyv (2026.07.03-án töltendő)

| | |
|---|---|
| 1. hét: új incidensek naponta (átlag) | ___ db/nap |
| 2. hét: új incidensek naponta (átlag) | ___ db/nap |
| Küszöb | kb. 7,4 db/nap |
| Nyitott incidensek a lezáráskor | ___ db — átadva a normál sorba |
| Új ismert hibák | ___ |
| Döntés | lezárva / meghosszabbítva ___-ig |
| Döntéshozó | Kiss Réka — tájékoztatva: Nagy Péter |

> **Utólagos megjegyzés (2026. október, a PIR után).** A hypercare 2026.07.03-án lezárult, a
> kilépési feltétel teljesült (PIR 7. pont, NY-1). **A mért heti értékeket a projekt
> dokumentumai nem rögzítik** — csak a teljesülés tényét. A kiterjesztésnél hullámonként
> 2 hét hypercare lesz (Kiterjesztési javaslat 6. pont), és a Service Desk-kapacitás
> számítása (F4) éppen ilyen adatokra épül. **Ezt a jegyzőkönyvet ezért a kiterjesztés minden
> hullámánál ki kell tölteni.**

---

## Mi a különbség a projekt átadás-átvételéhez képest?

| | Projekt átadás-átvétel (XYO-CP-401) | **Szolgáltatási elfogadás és ELS (ITIL 4)** |
|---|---|---|
| A kérdés | Teljesítette-e a projekt, amit vállalt? | **Működtethető-e a szolgáltatás a projekt nélkül?** |
| A mérce | Átvételi kritériumok (AK-01 – AK-26) | **Szolgáltatási elfogadási kritériumok** (SZE-01 – SZE-10) |
| Ki írja alá | Átvevő, felhasználói képviselő, projektmenedzser | **Szolgáltatásgazda és az üzemeltető csapatok** |
| Mi a kimenet | Lezárt projekt, nyitott pontok listája | **Normál üzem: SLA, ismert hibák, változási rend** |
| Hypercare | A projekt utolsó munkacsomagja (7.4) | **Korai életszakasz-támogatás, mérhető kilépéssel** |

> **A tanulság egy PM-nek:** a jó átadás nem a projekt végén kezdődik. A Xyo azért tudott
> tételesen átadni, mert a Service Desket a WBS-workshoptól bevonta, a Run-bookot a szállítói
> szerződés teljesítési feltételévé tette, és a hypercare kilépési feltételét már a tervezéskor
> leírta. Az ITIL ezekhez **nevet és egy aláírt listát** ad.

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser; Kiss Réka, Service Desk vezető | 2026.06.26. |
| **Elfogadta (szolgáltatásgazda)** | **Nagy Péter** | 2026.06.26. |
| Elfogadta (üzemeltetés) | Szabó Márk, rendszergazda | 2026.06.26. |

---

> **Kapcsolódó dokumentumok:** bemenete az *Átadás-átvételi jegyzőkönyv*, a *Run-book*, a
> *WBS-szótár* (7.4), az *Oktatási terv*, a *RACI-mátrix*, a *T0 baseline jegyzőkönyv* és a
> *Változásnapló*; kimenete a *Folyamatos fejlesztési nyilvántartás* (XYO-ITIL-006).
