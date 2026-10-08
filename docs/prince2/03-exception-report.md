# Exception Report — kivételjelentés

**Dokumentum azonosítója:** XYO-P2-003\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, Project Manager\
**Címzett:** **Project Board**\
**Szakasz:** 3. — Kialakítás és teszt\
**Dátum:** **2026. május 29.**

> ⚠ **PRINCE2-kiegészítés.** **Ennek a dokumentumnak nincs PMI-megfelelője** —
> ez az egyik legértékesebb, amit a PRINCE2-től át lehet venni.
>
> **A lényege:** nem akkor szólunk, amikor túlléptük a toleranciát, hanem
> amikor **előrejelezhető, hogy túl fogjuk lépni.** Így a Boardnak még van
> mozgástere dönteni.

---

## 1. Miért készült ez a jelentés?

A 2026.05.26-i Highlight Reportban jeleztem, hogy az idő-tolerancia veszélyben
van, és **05.29-re visszajelzést vállaltam.** Ez az a visszajelzés.

| | |
|---|---|
| **Melyik toleranciát fenyegeti** | **Idő** — a 3. szakasz ± 5 munkanapos tolerenciája |
| **Mikor derült ki** | 2026.05.22., az UAT első körének zárásakor |
| **Mekkora a fenyegetett túllépés** | **0 – 3 munkanap** *(a 05.29-i állapot szerint)* |

---

## 2. A kivétel leírása

Az UAT első köre **81,5%-on zárult** (22/27 teszteset), a kilépési feltétel
95%. Hat hiba maradt nyitva, ezek javítására **9 naptári nap — Pünkösdhétfő miatt
6 munkanap** áll rendelkezésre (2026.05.25 – 06.02.), **puffer nélkül**.

A javítási ablak a szakasz utolsó tartalékideje. Ha nem elegendő, az M7
mérföldkő (teljes 50 fő élesben, 2026.06.12.) csúszik — és mivel a kritikus
úton **nulla puffer** van, az M10 (projektzárás, 2026.06.30., **L1 kemény
korlát**) is veszélybe kerül.

## 3. Az ok

| # | Ok | Hozzájárulás |
|---|---|---|
| 1 | **Két kritikus (S1) hiba az élesítés első napján** (05.11.) | Az UAT első hetéből 1,5 nap elveszett |
| 2 | A **feltételes hozzáférési szabály** 3 tesztelőt kizárt | Az R11 kockázat bekövetkezése |
| 3 | Az **Autopilot beüzemelési idő** (2,1 óra) újramérést igényelt | 2 nap |
| 4 | A **szabad tesztelés** két új, nem tervezett hiányt talált | +2 javítandó tétel |

> A 4. pont **nem negatívum.** A szabad tesztelés pontosan azért van, hogy
> megtaláljuk, amire nem gondoltunk — de a javítási ablakot terheli.

---

## 4. A helyzet 2026. május 29-én

| | |
|---|---:|
| Nyitott hiba az ablak kezdetén | 6 |
| **Javítva 05.29-ig** | **3** *(H-03, H-07, H-11)* |
| Az ablakon kívül kezelve | 1 *(H-06 — szolgáltatói lefedettség, nem a megoldás hibája)* |
| Nyitva, az újratesztelést nem akadályozza | 2 *(S3–S4)* |
| Új hiba, 05.28. | H-04 — 12 hiányzó tápkábel (S2); a pótlást a szállító 06.03-ig vállalta |
| Hátralévő munkanap | 2 (06.01 – 06.02.) |

**Előrejelzés:** a javítási ablakba tartozó hibák kijavítva; ha a H-04 pótlása
06.03-ig megérkezik, az M7 tartható, és a tolerancia nem sérül.

**Fennmaradó bizonytalanság:** az újratesztelés (06.03 – 06.16.) hozhat még
elő hibát. Ha kritikus (S1) hiba kerül elő, a szakasz **3–5 munkanappal
túllépheti** az idő-toleranciát.

---

## 5. A hatás összefoglalása

| Terület | Hatás | Tolerancián belül? |
|---|---|:-:|
| **Idő** | 0–3 munkanap csúszás lehetséges | 🟡 **határon** |
| **Költség** | Nincs — a javítás a szállítói szavatosság körébe tartozik | ✔ |
| **Hatókör** | Nincs változás | ✔ |
| **Minőség** | 0 nyitott S1 hiba; a 95%-os küszöb az újratesztelés után várhatóan teljesül | ✔ |
| **Kockázat** | R6 („az UAT több hibát talál") besorolása 4 → 6 | ⚠ jelentendő |
| **Haszon** | Nincs hatás | ✔ |

---

## 6. Lehetőségek

A PRINCE2 négy választ ismer a kivételre. Mind a négyet megvizsgáltam.

| # | Lehetőség | Értékelés |
|---|---|---|
| **A** | **A Board elfogadja a helyzetet** — a jelenlegi terv folytatódik, a Board tudomásul veszi a kockázatot | **Javasolt.** Az ablakba tartozó hibák javítva; a nyitott S3–S4 hibák nem akadályozzák az újratesztelést; a H-04 pótlása vállalva. |
| **B** | **Kivételterv kérése** *(Exception Plan)* — a szakasz újratervezése, a Board jóváhagyásával | Nem indokolt. A szakaszterv tartható; egy szállítói pótlás miatt a teljes szakaszterv újraírása aránytalan. |
| **C** | **Hatókörcsökkentés** — az F prioritású követelmények elhagyása (pl. K19 külső megosztás, K23 videóhívás) | Nem indokolt **most**. Tartalékként megmarad: ha az újratesztelés S1 hibát talál, ez lesz az első javaslatom. |
| **D** | **A projekt leállítása** | Nem indokolt. Az üzleti indoklás változatlanul érvényes; a beszerzés a terv alatt zárult. |

---

## 7. A Project Manager javaslata

> **„A" lehetőség — a Board fogadja el a helyzetet, a terv változatlanul
> folytatódik.**

**Indoklás:**

1. A javítási ablakba tartozó hibák **javítva**; a H-06 nem a megoldás hibája, a 2 nyitott S3–S4 hiba nem akadályoz.
2. **Nincs nyitott kritikus (S1) hiba.**
3. A költség-, hatókör- és haszon-tolerancia érintetlen.
4. A projekt **3,2%-kal a költségterv alatt** áll (szerződött érték a költségbázishoz) — pénzügyi mozgástér van.

**Amit vállalok:**

| # | Vállalás | Határidő |
|---|---|---|
| 1 | Az újratesztelés napi követése, hibaáttekintéssel | 06.03 – 06.16. |
| 2 | **Azonnali új Exception Report**, ha az újratesztelés S1 hibát talál | eseti |
| 3 | Kész hatókörcsökkentési javaslat (C lehetőség), ha szükségessé válik | 06.05-ig előkészítve |
| 4 | Soron kívüli Highlight Report | 06.08. |

---

## 8. A Project Board döntése

| | |
|---|---|
| **Döntés** | **„A" lehetőség elfogadva** — a terv változatlanul folytatódik |
| **Döntéshozó** | **Kovács Anita, Executive** |
| **Dátum** | 2026.05.29. |
| **Indoklás** | A Board a Project Manager elemzését elfogadta. A helyzet a szakasz-tolerancia keretein belül kezelhetőnek látszik. |
| **Kikötés** | A Board **soron kívüli tájékoztatást** kér 2026.06.08-án, és haladéktalanul, ha az újratesztelés kritikus hibát talál. |
| **Tolerancia módosítása** | Nincs |

---

## 9. Utólagos kiegészítés — mi lett a vége?

*(2026.06.19-én rögzítve, az End Stage Reporthoz)*

| | |
|---|---|
| A javítási ablak hibái | H-03 05.27., H-07 05.26., H-11 05.28. — az ablak vége (06.02.) előtt; a H-04 pótlása 06.02., 1 nappal a vállalt határidő előtt |
| Újratesztelés | 06.03 – 06.16., **26/27 = 96,3%** |
| Nyitott S1 hiba | **0** |
| **Az M7 mérföldkő** | **2026.06.12. — határidőre teljesült** |
| **A tolerancia** | **nem sérült; a csúszás 0 nap** |
| További Exception Report | nem volt szükséges |

> **A kivétel nem következett be** — de a jelentés akkor is helyes volt.
>
> Az Exception Report nem a kudarc bejelentése, hanem **a bizonytalanság
> megosztása a döntéshozóval, amíg még van mozgástér.** Ha kiderül, hogy
> mégis rendben lett, az nem „fölösleges riadó" volt, hanem működő
> korai jelzés.

---

## Mit tanulj el ebből, ha PMI szerint dolgozol?

| # | |
|---|---|
| 1 | **Ne akkor szólj, amikor túlléptél — akkor, amikor előrejelezhető, hogy túl fogsz lépni.** Utólag már nincs mit dönteni. |
| 2 | **Vidd a döntési lehetőségeket, ne csak a problémát.** A PRINCE2 négy válasza (elfogadás / újratervezés / hatókörcsökkentés / leállítás) minden helyzetre jó vázlat. |
| 3 | **Adj konkrét visszajelzési időpontot.** A „majd jelzek" nem jelzés. |
| 4 | **Számszerűsítsd a fenyegetett túllépést**, ne érzésre írd le. |
| 5 | **Készítsd elő a következő lépést is** — itt a hatókörcsökkentési javaslatot, mielőtt szükség lenne rá. |

> A Xyo projektben ez a jelentés **E-04 eszkalációként** valósult meg
> (Eszkalációs napló, XYO-CP-309). A tartalma lényegében azonos volt — csak
> nem hívtuk Exception Reportnak, és nem volt mögötte formális tolerancia,
> amihez mérni lehetett volna.
