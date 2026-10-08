# PRINCE2 — rövid összefoglaló egy PMI-t ismerő junior PM-nek

**Dokumentum azonosítója:** XYO-METH-001\
**Cél:** megérteni, mi a PRINCE2, miben más, mint a PMI/PMBOK, és mikor melyiket érdemes használni\
**Terjedelem:** kb. 10 oldal\
**Verzió:** 1.0

> Ez nem tanúsítványra felkészítő anyag. Arra jó, hogy **megértsd a logikáját**,
> felismerd a fogalmait egy megbeszélésen, és el tudd dönteni, mikor melyik
> módszertan illik a helyzethez.

---

## 1. Mi a PRINCE2 egy mondatban?

A **PRINCE2** (*PRojects IN Controlled Environments*) egy **irányítási módszer**:
előírja, **kik a szereplők, milyen döntési pontokon kell a projektnek átmennie,
és ki mit dönthet el.**

Fontos, hogy mi **nem**: nem tudásanyag, nem eszköztár, és **szinte semmilyen
technikát nem tartalmaz** — nincs benne becslési módszer, Gantt-diagram vagy
elkészültségi érték (EVM). Ezeket máshonnan kell hoznod.

### Honnan jött?

| Év | Mi történt |
|---|---|
| 1989 | A brit kormányzat kiadja a PRINCE-t (a korábbi PROMPT II módszertanból) |
| 1996 | **PRINCE2** — általános, nem csak IT-projektekre |
| 2009, 2017 | Nagyobb átdolgozások; a legtöbb magyar anyag és tanfolyam ezt tükrözi |
| 2023 | **PRINCE2 7** — új elem: az emberek (*people*), és a fenntarthatóság mint teljesítménycél |

Gazdája ma a **PeopleCert** (korábban AXELOS). Erős Nagy-Britanniában, az EU-s
és ausztrál közszférában, a nemzetközi szervezeteknél és a nagy
rendszerintegrátoroknál.

> **Terminológiai megjegyzés:** a PRINCE2 7-ben a „témák" (*themes*) neve
> „gyakorlatok" (*practices*) lett. Mivel a magyar szakmai nyelvben és a
> tanfolyamokon még a 2017-es kiadás fogalmai élnek, itt **mindkettőt**
> jelzem, de a régebbi, ismertebb elnevezéseket használom.

---

## 2. A legfontosabb különbség egy mondatban

| | |
|---|---|
| **PMI / PMBOK** | *Mit tudjon a projektmenedzser?* — Tudásanyag, eszközök, technikák gyűjteménye. A PM kompetenciájára fókuszál. |
| **PRINCE2** | *Hogyan irányítsuk a projektet?* — Módszer: szerepek, folyamatok, döntési pontok. A **kontrollra és a felelősségre** fókuszál. |

**Ezért nem versenyeznek egymással.** A PRINCE2 megmondja, hogy a szakaszhatáron
a döntéshozó testületnek engedélyeznie kell a továbblépést — de nem mondja meg,
hogyan becsüld meg a hátralévő munkát. Arra a PMI eszköztára való.

**A gyakorlatban a legjobb kombináció:** PRINCE2 a kormányzási váz,
PMI/PMBOK a technikák.

---

## 3. A PRINCE2 felépítése

A módszer négy (a PRINCE2 7-ben öt) elemből áll. A hetes szám végigkíséri:

```
       7 ALAPELV              7 TÉMA                 7 FOLYAMAT
    (mindig érvényes)   (mit kell kezelni)      (mikor mi történik)
           │                    │                       │
           └────────────────────┴───────────────────────┘
                                │
                      TESTRESZABÁS a projektre
```

---

## 4. A hét alapelv (principles)

**Ez a PRINCE2 lelke.** Ha ezek közül bármelyik nem érvényesül, akkor a projekt
**definíció szerint nem PRINCE2-projekt** — akkor sem, ha minden dokumentum
elkészült.

| # | Alapelv | Mit jelent a gyakorlatban |
|---|---|---|
| 1 | **Folyamatos üzleti indokoltság**<br>*(Continued business justification)* | Az üzleti indoklás **élő dokumentum**. Minden szakaszhatáron újra megkérdezzük: megéri-e még? Ha nem, **a projektet le kell állítani.** |
| 2 | **Tanulás a tapasztalatokból**<br>*(Learn from experience)* | A tanulságokat a projekt **elején keressük** (korábbi projektekből), közben gyűjtjük, a végén átadjuk. |
| 3 | **Meghatározott szerepek és felelősségek**<br>*(Defined roles and responsibilities)* | Mindenki tudja, ő mit dönthet el, és mit nem. Nevesített szerepek, nem beosztások. |
| 4 | **Szakaszokban történő irányítás**<br>*(Manage by stages)* | A projektet **irányítási szakaszokra** bontjuk. Minden szakasz végén a döntéshozó testület engedélyezi (vagy leállítja) a folytatást. |
| 5 | **Kivételalapú irányítás**<br>*(Manage by exception)* | A PM **toleranciákat** kap, és azokon belül **önállóan dolgozik**, jelentés nélkül. Csak akkor kell felfelé fordulnia, ha a tolerancia túllépése fenyeget. |
| 6 | **Termékközpontúság**<br>*(Focus on products)* | Nem tevékenységeket tervezünk, hanem **termékeket** (eredményeket), leírással és minőségi kritériummal. |
| 7 | **Testreszabás**<br>*(Tailor to suit the project)* | A módszert a projekt méretéhez, kockázatához, környezetéhez kell igazítani. **A „mindent dokumentálunk" nem PRINCE2, hanem félreértés.** |

> **A 4. és 5. alapelv adja a PRINCE2 igazi karakterét.** A szakaszolás
> biztosítja, hogy a pénzt darabokban engedjük el; a kivételalapú irányítás
> biztosítja, hogy a PM közben tényleg dolgozhasson.

---

## 5. A hét téma (themes / practices)

A témák azt írják le, **mit kell folyamatosan kezelni** a projekt teljes hossza
alatt. Mindegyiknek van PMI-megfelelője, de a hangsúly máshol van.

| # | Téma | Mit fed le | PMI-megfelelő | Hol tér el? |
|---|---|---|---|---|
| 1 | **Üzleti indoklás**<br>*(Business Case)* | Miért éri meg? Megéri-e még? | Business Case | **PRINCE2-ben élő dokumentum**, minden szakaszhatáron felülvizsgálva |
| 2 | **Szervezet**<br>*(Organization / Organizing)* | Ki kicsoda, ki dönt | Stakeholder + Resource Management | PRINCE2-ben **kötelező szerepstruktúra** (Project Board) |
| 3 | **Minőség**<br>*(Quality)* | Mitől jó, ami elkészül | Quality Management | **Termékleírás minőségi kritériummal** minden termékhez |
| 4 | **Tervek**<br>*(Plans)* | Mit, mikor, mennyiért | Scope + Schedule + Cost | **Termékalapú tervezés**; háromszintű terv (projekt / szakasz / csapat) |
| 5 | **Kockázat**<br>*(Risk)* | Mi mehet félre | Risk Management | Nagyon hasonló; PRINCE2-ben **kockázati étvágy** és tolerancia |
| 6 | **Változás**<br>*(Change / Issues)* | Módosítás- és problémakezelés | Change Management | PRINCE2-ben **egy folyamatban** kezeli a változást, a problémát és a hibát |
| 7 | **Haladás**<br>*(Progress)* | Hol tartunk, kell-e beavatkozni | Monitoring & Controlling | **Toleranciák és kivételjelentés** — ez a legnagyobb eltérés |

---

## 6. A hét folyamat — a sorrendiség

Ez a rész válaszolja meg, hogy **mikor mi történik.**

```
  ┌──────────────────────────────────────────────────────────────┐
  │  DP — Projekt irányítása (Directing a Project)                │
  │  A Project Board folyamata — VÉGIG FUT, a projekt egészén     │
  └──────────────────────────────────────────────────────────────┘
        ▲          ▲               ▲            ▲          ▲
        │          │               │            │          │
   ┌────┴───┐ ┌────┴────┐   ┌──────┴─────┐ ┌────┴────┐ ┌───┴────┐
   │  SU    │ │   IP    │   │     CS     │ │   SB    │ │   CP   │
   │Előké-  │→│Kezdemé- │ → │  Szakasz   │→│Szakasz- │→│Projekt │
   │szítés  │ │ nyezés  │   │ irányítása │ │ határ   │ │ zárása │
   └────────┘ └─────────┘   └─────┬──────┘ └────┬────┘ └────────┘
                                  │             │
                                  ▼             │
                          ┌───────────────┐     │
                          │      MP       │     │  a CS és SB
                          │ Termékszállí- │     │  szakaszonként
                          │tás irányítása │     │  ismétlődik
                          └───────────────┘     ◄──┘
```

| # | Folyamat | Ki végzi | Mit csinál |
|---|---|---|---|
| **SU** | **Projekt előkészítése**<br>*(Starting up a Project)* | leendő PM + Executive | Van-e értelme egyáltalán elindítani? Elkészül a **Project Brief** és a kezdeményezési szakasz terve. **Ez még nem a projekt** — ez az előszoba. |
| **DP** | **Projekt irányítása**<br>*(Directing a Project)* | **Project Board** | Végig fut. A Board **engedélyez**: kezdeményezést, projektet, minden szakaszt, végül a zárást. Kivételes helyzetben itt dönt. |
| **IP** | **Projekt kezdeményezése**<br>*(Initiating a Project)* | PM | Elkészül a **PID** — a projekt „szerződése". **Ez maga is egy szakasz**, saját engedéllyel. |
| **CS** | **Szakasz irányítása**<br>*(Controlling a Stage)* | PM | A napi munka: munkacsomagok kiadása, haladás követése, problémakezelés, **Highlight Report** a Boardnak. |
| **MP** | **Termékszállítás irányítása**<br>*(Managing Product Delivery)* | Team Manager | A munkacsomag elfogadása, elkészítése, átadása. **Checkpoint Report** a PM-nek. |
| **SB** | **Szakaszhatár kezelése**<br>*(Managing a Stage Boundary)* | PM | A szakasz lezárása: **End Stage Report**, a következő szakasz terve, **a Business Case felülvizsgálata**. |
| **CP** | **Projekt lezárása**<br>*(Closing a Project)* | PM | Átadás, **End Project Report**, tanulságok, a haszonmérés terve. |

### Mit jelent, hogy „irányítási szakasz"?

Az **irányítási szakasz** (*management stage*) az a darab, amit a PM a Board
nevében **önállóan visz végig**, és amelynek a végén a Board dönt a
továbbmenetelről.

| | |
|---|---|
| Minimum | **2 szakasz**: a kezdeményezési szakasz + legalább egy további |
| Mi zárja | **Szakaszhatár** — kötelező Board-döntés, nem opcionális |
| Mi a különbség a PMI fázistól? | A PMI fázisai **tudásterületi csoportok** (Initiating, Planning…), amelyek átfedik egymást. A PRINCE2 szakaszai **időbeli darabok**, amelyek nem fedik át egymást, és mindegyik végén pénz és bizalom forog kockán. |

> Létezik **technikai szakasz** is (pl. „tervezés", „építés", „teszt") — ez a
> szakértői munka tagolása. A kettő nem feltétlenül esik egybe, és a PRINCE2
> az **irányítási** szakaszokra épül.

---

## 7. A szervezet — ki kicsoda

Ez a PRINCE2 egyik legerősebb hozadéka. A szerepek **nem beosztások**: egy
ember több szerepet is vihet, egy szerepet pedig többen is elláthatnak
(a Executive kivételével).

```
        ┌─────────────────────────────────┐
        │   Vállalati / programvezetés    │   ← a Boardon kívül, ő ad megbízást
        └────────────────┬────────────────┘
                         │
        ┌────────────────▼────────────────┐
        │        PROJECT BOARD            │
        │  ┌───────────────────────────┐  │
        │  │ EXECUTIVE  (1 fő, ő dönt) │  │
        │  ├─────────────┬─────────────┤  │      ┌──────────────────┐
        │  │ Senior User │Senior Suppl.│  │ ◄───►│ Project Assurance│
        │  └─────────────┴─────────────┘  │      │  (a Boardtól,    │
        └────────────────┬────────────────┘      │  a PM-től        │
                         │                       │  függetlenül)    │
              ┌──────────▼──────────┐            └──────────────────┘
              │  PROJECT MANAGER    │ ◄────────► Project Support
              └──────────┬──────────┘
                         │
              ┌──────────▼──────────┐
              │    TEAM MANAGER     │
              └─────────────────────┘
```

| Szerep | Kit képvisel | Miért felel |
|---|---|---|
| **Executive** | Az üzletet, a pénzt | **Egyetlen ember.** Ő birtokolja az üzleti indoklást, és **ő hozza a végső döntést.** A Board nem demokrácia. |
| **Senior User** | A felhasználókat | Azért felel, hogy a megoldás **használható legyen**, és hogy a **hasznok ténylegesen megjelenjenek** |
| **Senior Supplier** | A szállítót / kivitelezőt | Azért felel, hogy a megoldás **megvalósítható és leszállítható** legyen |
| **Project Manager** | — | A napi irányítás, a toleranciákon belül |
| **Team Manager** | Egy szakértői csapatot | Egy-egy munkacsomag leszállítása |
| **Project Assurance** | A Boardot | **Független ellenőrzés** — a PM-től függetlenül nézi, hogy a projekt tényleg úgy áll-e, ahogy a riport mondja |
| **Project Support** | — | Adminisztráció, dokumentumkezelés, eszközök |
| **Change Authority** | A Board delegáltja | A Board átadhatja a változáskérelmek eldöntését egy értékhatárig |

> **A Project Assurance a PMI-ban nem létezik ilyen formában**, és ez a
> PRINCE2 egyik legerősebb kontrollja: van valaki, aki a Board nevében,
> a PM-től függetlenül ellenőrzi a helyzetet.

---

## 8. Kivételalapú irányítás és a toleranciák

**Ez a PRINCE2 legpraktikusabb ötlete, és ezt érdemes akkor is átvenni, ha
egyébként PMI szerint dolgozol.**

A Board minden szakaszhoz **toleranciát** ad. A PM ezeken belül **önállóan
dolgozik** — nem kell engedélyt kérnie, nem kell magyarázkodnia.

| Toleranciaterület | Példa |
|---|---|
| **Idő** | ±5 munkanap szakaszonként |
| **Költség** | ±5% |
| **Hatókör** | nincs tolerancia — a kötelező követelmények mind teljesülnek |
| **Minőség** | az átvételi kritériumok tűréshatára |
| **Kockázat** | a kockázati étvágy (pl. „6-os vagy magasabb besorolást jelenteni kell") |
| **Haszon** | a mérőszámok elfogadható sávja |

*(A PRINCE2 7 ehhez hozzáveszi a fenntarthatóságot is.)*

### A toleranciák szintjei

```
Vállalatvezetés  ──ad── projekt-toleranciát ──►  PROJECT BOARD
Project Board    ──ad── szakasz-toleranciát ──►  PROJECT MANAGER
Project Manager  ──ad── munkacsomag-toleranciát ─►  TEAM MANAGER
```

### Mi történik túllépéskor?

**Nem akkor kell szólni, amikor túlléptük — hanem amikor előrejelezhető,
hogy túl fogjuk lépni.**

```
  A PM előrejelzi, hogy a tolerancia túllépése fenyeget
                        │
                        ▼
             ┌──────────────────────┐
             │  EXCEPTION REPORT    │  ← a PM készíti
             │  (Kivételjelentés)   │
             └──────────┬───────────┘
                        │
                        ▼
              A Board dönt: 4 lehetőség
     ┌──────────┬───────────┬───────────┬──────────┐
     │ Elfogadja│ Kivétel-  │ Hatókör   │ Leállítja│
     │ a helyze-│ terv      │ csökken-  │ a pro-   │
     │ tet      │ kérése    │ tése      │ jektet   │
     └──────────┴───────────┴───────────┴──────────┘
```

> **Ez a mechanizmus tesz különbséget a PM önállósága és a felelőtlenség
> között.** Ha nincs tolerancia, a PM vagy mindenért engedélyt kér (és megáll
> a projekt), vagy magától dönt olyasmiről, amiről nem lenne szabad.

---

## 9. Termékalapú tervezés

A PRINCE2 saját tervezési technikája — az egyike a kevés technikának, amit
maga a módszer tartalmaz.

| # | Lépés | Mi készül |
|---|---|---|
| 1 | A **projekt végtermékének leírása** | Mi az egyetlen dolog, amiért a projekt van? |
| 2 | **Terméklebontási szerkezet** (PBS) | A végtermék felbontása kisebb termékekre |
| 3 | **Termékleírások** | Minden termékhez: mi az, miből áll, **mitől jó**, ki ellenőrzi |
| 4 | **Termékfolyam-diagram** | Melyik termék melyiktől függ, milyen sorrendben |
| 5 | *Csak ezután:* tevékenységek és becslés | Az ütemterv innen származik |

**A különbség a PMI WBS-hez képest** inkább hangsúlybeli, mint elvi: a jó
PMI-gyakorlat is eredmény-alapú WBS-t ír elő. A PRINCE2 viszont **kötelezővé
teszi**, és hozzáteszi a **termékleírást minőségi kritériummal** — vagyis
minden termékhez előre rögzíti, mitől lesz elfogadható.

---

## 10. A fő dokumentumok (management products)

A PRINCE2 nagyjából **két tucat irányítási terméket** nevesít, három
kategóriában:

| Kategória | Mit jelent | Példák |
|---|---|---|
| **Alapdokumentumok** *(baselines)* | Jóváhagyott, verziózott, változáskezelés alatt | Business Case, PID, Project Brief, tervek, termékleírások, munkacsomag |
| **Nyilvántartások** *(records)* | Élő, folyamatosan frissülő | Kockázati napló, Problémanapló, Tanulságok naplója, Minőségi napló, Napi napló |
| **Jelentések** *(reports)* | Egy adott pillanat állapotát mutatják | Highlight, Checkpoint, Exception, End Stage, End Project, Lessons Report |

### A hat legfontosabb, PMI-megfelelővel

| PRINCE2 dokumentum | Mit tartalmaz | PMI-megfelelő |
|---|---|---|
| **Project Brief** | Az előkészítés eredménye: mi a projekt, miért, nagyvonalakban | *(nincs pontos megfelelő — a Charter előtti anyag)* |
| **PID** — *Project Initiation Documentation* | A projekt teljes „szerződése": mi, miért, hogyan, ki, mennyiért, milyen kontrollal | **Project Charter + Project Management Plan együtt** |
| **Business Case** | Miért éri meg — **és megéri-e még** | Business Case, de PRINCE2-ben **élő** |
| **Highlight Report** | Rendszeres állapotjelentés a Boardnak | Status Report |
| **Exception Report** | Tolerancia túllépése fenyeget → döntést kérek | **nincs PMI-megfelelője** |
| **End Stage Report** | A szakasz mérlege + a Business Case felülvizsgálata | *(nincs — a PMI fázis-kapu ehhez a legközelebbi)* |

---

## 11. PMI és PRINCE2 — összehasonlító táblázat

| Szempont | PMI / PMBOK | PRINCE2 |
|---|---|---|
| **Mi ez?** | Tudásanyag, jó gyakorlatok | Módszer, előírt folyamatokkal |
| **Mire fókuszál?** | A PM kompetenciájára, eszközeire | Az irányításra, a döntésekre, a felelősségre |
| **Üzleti indoklás** | A charter bemenete, jellemzően egyszeri | **Élő; minden szakaszhatáron felülvizsgálva. Ha megszűnik, leállítás.** |
| **Szervezet** | Szponzor + PM, rugalmas | **Kötelező Project Board**: Executive, Senior User, Senior Supplier |
| **Független ellenőrzés** | nincs nevesítve | **Project Assurance** |
| **Szakaszolás** | Fázisok, átfedéssel; kapuk opcionálisak | **Kötelező irányítási szakaszok, kötelező Board-döntéssel** |
| **A PM önállósága** | Nincs formalizálva | **Toleranciák + kivételalapú irányítás** |
| **Tervezés** | WBS, tevékenységbecslés, hálótervezés | **Termékalapú tervezés**, három tervszinttel |
| **Technikák** | Rengeteg (EVM, becslés, ütemezés…) | **Szinte semmi** — máshonnan kell hozni |
| **Terjedelem** | Nagy tudásanyag | Kompakt módszer + testreszabás |
| **Tanúsítás** | PMP (tapasztalat-követelménnyel), CAPM | Foundation, Practitioner (Foundationhöz nincs tapasztalat-követelmény) |
| **Hol jellemző?** | Globális, USA, magánszektor | UK, EU, Ausztrália; közszféra, nagy integrátorok |

### Ugyanaz a dolog, két néven

| PMI | PRINCE2 |
|---|---|
| Project Charter | *(a PID része)* |
| Project Management Plan | PID |
| Sponsor | Executive |
| Steering Committee | Project Board |
| Fázis-kapu (phase gate) | Szakaszhatár (stage boundary) |
| Status Report | Highlight Report |
| Deliverable | Product |
| WBS | Terméklebontási szerkezet (PBS) |
| Issue Log | Issue Register |
| Risk Register | Risk Register *(azonos)* |
| Lessons Learned Register | Lessons Log / Lessons Report |
| Change Request | Issue *(a PRINCE2 egy folyamatban kezeli a változást és a problémát)* |

---

## 12. Mikor melyiket?

### A PRINCE2 akkor erős, ha…

| # | Helyzet | Miért |
|---|---|---|
| 1 | **Több szervezet vagy szállító** vesz részt | A Senior Supplier szerep és a világos felelősségek kezelik a határokat |
| 2 | **Közszféra, pályázat, szabályozott környezet** | A kormányzati elvárás gyakran kifejezetten PRINCE2 |
| 3 | **A döntéshozók távol vannak a napi munkától** | A szakaszhatárok és a Highlight Report tartja őket a képben, mikromenedzsment nélkül |
| 4 | **Bizonytalan a megtérülés** | A folyamatos üzleti indokoltság kikényszeríti a „megéri-e még?" kérdést |
| 5 | **Hosszú, több szakaszban futó projekt** | A pénzt darabokban engedjük el, nem egyben |
| 6 | **Erős elszámoltathatósági igény** | Project Assurance + nevesített szerepek |

### A PMI akkor erős, ha…

| # | Helyzet | Miért |
|---|---|---|
| 1 | **A PM eszköztárát kell fejleszteni** | Becslés, ütemezés, EVM, erőforrás-kiegyenlítés |
| 2 | **Egy szervezeten belüli projekt**, közeli szponzorral | A Board apparátusa túl nehéz lenne |
| 3 | **Technikai tervezési kérdések dominálnak** | A PRINCE2 ehhez nem ad eszközt |
| 4 | **Nemzetközi, USA-orientált környezet** | A PMP a közös nyelv |

### Amikor egyik sem elég önmagában

**A leggyakoribb valós helyzet.** Ilyenkor:

| Réteg | Honnan |
|---|---|
| Kormányzás: szerepek, szakaszok, toleranciák, üzleti indokoltság | **PRINCE2** |
| Technikák: becslés, ütemterv, kockázatelemzés, EVM, beszerzés | **PMI / PMBOK** |

> **Ez a kombináció nem kompromisszum, hanem a két módszertan szándéka
> szerinti használat.** A PRINCE2 kifejezetten arra számít, hogy a technikákat
> máshonnan hozod.

### Amikor egyik sem való

Ha a követelmények menet közben derülnek ki, és a szállítás folyamatos
(tipikusan szoftverfejlesztés), akkor **agilis keretrendszer** (Scrum, SAFe)
illik jobban. Létezik a kettő házasítása is (*PRINCE2 Agile*), de az már
külön téma.

---

## 13. Mit jelentene mindez a Xyo Cloud Pilot projektnél?

A projektet PMI szerint vittük végig. Íme, mi lett volna másképp PRINCE2-ben —
és mi az, ami **így is jó volt.**

### 13.1 A szerepek

| PRINCE2 szerep | Ki lenne a Xyo-nál | Megjegyzés |
|---|---|---|
| **Executive** | **Kovács Anita**, gazdasági igazgató | Ő birtokolja a keretet és az üzleti indoklást |
| **Senior User** | **Nagy Péter**, IT osztályvezető | Nálunk ő „a hasznok gazdája" — **ez pontosan a Senior User felelőssége** |
| **Senior Supplier** | **Cloudia Solutions** ügyfélkapcsolati vezetője | A megoldás nagy részét ők szállítják |
| **Project Manager** | Tóth Gergő | — |
| **Team Manager** | Szabó Márk (belső), Cloudia projektvezető (külső) | — |
| **Project Assurance** | **nem volt** | **A legnagyobb hiányzó elem.** A Steering a PM riportjaira támaszkodott, független ellenőrzés nélkül. |
| **Change Authority** | Tóth Gergő 1 000 000 Ft-ig | **Ez már most PRINCE2-szerű delegálás** — a Charter 6. pontja |
| Vállalatvezetés (a Boardon kívül) | Horváth Júlia, ügyvezető | PRINCE2-ben ő nem a Board tagja, hanem fölötte áll |

### 13.2 A szakaszolás

| PMI (ahogy csináltuk) | PRINCE2 irányítási szakaszok |
|---|---|
| Egyetlen formális kapu: **Planning-kapu, 2026.03.13.** | **Négy szakasz, négy Board-döntéssel** |

| # | Szakasz | Időszak | A szakaszhatáron |
|---|---|---|---|
| 0 | Előkészítés (SU) | 2025.11.10 – 2026.02.02. | Project Brief → a Board engedélyezi a kezdeményezést |
| 1 | Kezdeményezés (IP) | 2026.02.02 – 03.13. | **PID** → a Board engedélyezi a projektet és az 1. szakaszt |
| 2 | Beszerzés | 2026.03.16 – 04.17. | End Stage Report + **a Business Case felülvizsgálata** → engedély a 3. szakaszra |
| 3 | Kialakítás és teszt | 2026.04.20 – 06.19. | End Stage Report → engedély a zárásra |
| 4 | Élesítés és zárás (CP) | 2026.06.22 – 06.30. | End Project Report + a haszonmérés terve |

> **A 2. szakasz határa (2026.04.17.) a legérdekesebb.** Ott derült ki, hogy a
> beszerzés **1 490 000 Ft-tal a terv alatt** zárult. PRINCE2-ben ez nem csak
> egy jó hír a státuszriportban, hanem **a Business Case kötelező
> felülvizsgálatának bemenete** — a Board formálisan újra megerősítette volna,
> hogy a projekt továbbra is megéri.

### 13.3 Toleranciák

A projekt Chartere adott a PM-nek hatáskört (1 M Ft tartalék, mérföldkövek
közötti mozgástér). **Ez lényegében tolerancia volt, csak nem így hívtuk.**
PRINCE2-ben ez szakaszonként, hat területen rögzülne:

| Terület | Amit adtunk (Charter 6. pont) | PRINCE2-ben így néz ki |
|---|---|---|
| Idő | Belső mérföldkövek között szabad; M7 és M10 csak Steering-döntéssel | Szakasz-tolerancia: ±5 munkanap |
| Költség | Tartalékból 1 000 000 Ft-ig | Szakasz-tolerancia: ±5% |
| Hatókör | Nem módosítható | Nulla tolerancia |
| Minőség | — | Az átvételi kritériumok tűréshatára |
| Kockázat | — | „6-os vagy magasabb besorolást jelenteni kell" |
| Haszon | — | A mérőszámok tűréshatára |

### 13.4 Ahol PRINCE2-t csináltunk anélkül, hogy tudtunk volna róla

| # | Amit tettünk | PRINCE2-ben ez… |
|---|---|---|
| 1 | **E-04 eszkaláció:** nem döntést kértem, hanem előre jeleztem, hogy a javítási ablak szűkös lehet, és megígértem egy visszajelzési időpontot | …pontosan egy **Exception Report** logikája: nem a túllépéskor szólunk, hanem amikor előrejelezhető |
| 2 | A WBS **eredményeket** tartalmaz, nem tevékenységeket („50 db beüzemelt laptop") | …**termékközpontúság** (6. alapelv) |
| 3 | A **WBS-szótár kész-definíciója** minden munkacsomaghoz | …a **termékleírás minőségi kritériuma** |
| 4 | A tanulságokat **menet közben** gyűjtöttük (19-ből 14) | …**tanulás a tapasztalatokból** (2. alapelv) |
| 5 | A PM 1 M Ft-ig önállóan dönt a változásokról | …**Change Authority** delegálás |
| 6 | A **T0 baseline mérés** és a hasznok gazdájának nevesítése | …**Benefits Management Approach** és a Senior User felelőssége |

### 13.5 Amit PRINCE2 hozzátett volna

| # | Mit | Mennyire hiányzott? |
|---|---|---|
| 1 | **Project Assurance** — független ellenőrzés a Board nevében | **Ez a legnagyobb hiány.** A Steering csak a PM riportjaira támaszkodott. |
| 2 | **Szakaszonkénti Business Case-felülvizsgálat** | Közepes. A beszerzési megtakarítás és a mért hasznok is indokolták volna. |
| 3 | **Formális szakaszhatárok** 4 helyen 1 helyett | Közepes. Fegyelmezettebb, de egy 5 hónapos projektnél nehézkes is lehet. |
| 4 | **Szakaszonkénti toleranciák** hat területen | Kicsi. A Charter hatásköri szakasza ezt jórészt pótolta. |
| 5 | **Exception Report** mint formális eszköz | Kicsi. A gyakorlatban megvolt (E-04), csak nem így hívtuk. |

### 13.6 Megérte volna PRINCE2 szerint csinálni?

**Részben.** Egy 50 fős, 5 hónapos, 45 M Ft-os, egy szervezeten belüli
projektnél a teljes PRINCE2-apparátus (négy szakaszhatár, Board-ülések,
Assurance szerep, ~két tucat irányítási termék) **aránytalan lett volna** —
és a 7. alapelv, a **testreszabás**, kifejezetten tiltja is az ilyet.

**Amit érdemes lett volna átvenni:**

| # | Elem | Miért |
|---|---|---|
| 1 | **Project Assurance** — akár egyetlen független személy | A Board vakon bízott a PM riportjaiban |
| 2 | **Szakaszonkénti Business Case-felülvizsgálat** | A beszerzési megtakarítás után érdemes lett volna újra megnézni |
| 3 | **Kimondott toleranciák** hat területen | A Charter hatásköri része ezt félig már megtette |

**A kiterjesztési projektnél (190 fő, kb. 133 M Ft, három hullám) viszont
a teljes PRINCE2-váz védhető** — ott már több szakasz, nagyobb tét és
hosszabb futásidő van, ahol a „megéri-e még?" kérdés valóban élő.

---

## 14. Ha ennyit jegyzel meg, az elég

| # | |
|---|---|
| 1 | A PMI azt mondja meg, **mit tudj**; a PRINCE2 azt, **hogyan irányítsd**. Nem versenyeznek. |
| 2 | A PRINCE2 **szinte semmilyen technikát nem tartalmaz** — a becslést, ütemezést, EVM-et máshonnan kell hoznod. |
| 3 | A **folyamatos üzleti indokoltság** a legfontosabb alapelv: minden szakaszhatáron újra megkérdezzük, megéri-e még. |
| 4 | Az **Executive egyetlen ember**, és ő dönt. A Board nem demokrácia. |
| 5 | A **kivételalapú irányítás + toleranciák** a legjobban átvehető ötlet: a PM önállóan dolgozik a sávon belül, és **előre jelez**, ha a túllépés fenyeget. |
| 6 | A **Project Assurance** független a PM-től — ez a PMI-ból hiányzik. |
| 7 | A **testreszabás** kötelező alapelv. A „mindent dokumentálunk" nem PRINCE2, hanem félreértés. |

---

> **Kapcsolódó anyagok a felületen:** a fázisoldalakon a *PRINCE2-kiegészítés*
> blokk mutatja, hogy az adott PMI-fázis melyik PRINCE2-folyamatnak felel meg,
> és mit tenne hozzá. A négy PRINCE2-specifikus mintadokumentum (PID,
> Highlight Report, Exception Report, End Stage Report) a PRINCE2 oldalról
> tölthető le.
