# Tanulságok naplója (Lessons Learned Register)

**Dokumentum azonosítója:** XYO-CP-405\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Workshop:** 2026. június 29., 2 óra\
**Verzió:** 1.1 (kiegészítve a PIR után, 2026.10.09.)

> **Akkor ér valamit, ha a projekt közben folyamatosan gyűjtöd.** A záró
> workshopon már senki nem emlékszik a márciusi problémákra — pedig pont azok
> a leghasznosabbak.
>
> **A 19 tanulságból 14 menet közben került be**, a workshopon 5 új jött elő.
> A mérési szakasz négy tanulsága (T-20 – T-23) a PIR után került be (8. pont).

---

## A workshop

| | |
|---|---|
| Időpont | 2026.06.29., 14:00 – 16:00 |
| Résztvevők | Tóth Gergő, Nagy Péter, Szabó Márk, Kiss Réka, Molnár Katalin, Varga Eszter, Balogh Tamás, 2 pilot felhasználó |
| Módszer | A menet közben gyűjtött tanulságok átnézése, majd szabad kör |
| Előkészítés | A hozzászólásokat **írásban is bekértem előre** — a workshopon a csendesebbek nem szólalnak meg |

> **Alapszabály volt:** a kérdés nem az, hogy „ki rontotta el", hanem hogy
> **„mi tette lehetővé, hogy elromoljon"**. Ez tartotta meg a workshopot
> tanulásnak, és nem hibakeresésnek.

---

## 1. Tervezés

### T-01 — A jelentés-módot a valós használati környezetben kell futtatni

| | |
|---|---|
| **Mi történt** | A feltételes hozzáférési szabályt 5 napig jelentés-módban futtattuk (az R11 kockázat válaszlépése), de **irodai hálózaton**. Az élesítés első napján 3 tesztelő nem tudott belépni otthonról, mert a mobilszolgáltatói CGNAT-IP külföldinek látszott. |
| **Hatás** | 3 tesztelő 1 napig nem tudott dolgozni; az UAT első napja csúszott |
| **Kategória** | Tervezés / technika |
| **Javaslat** | **Minden „próbaüzem" jellegű ellenőrzést abban a hálózati és eszközkörnyezetben kell lefuttatni, ahol a felhasználók ténylegesen dolgozni fognak.** Otthoni munkavégzésre szánt szabályt irodából tesztelni nem elég. |
| **Kinek szól** | Projektmenedzser, rendszergazda |
| **Forrás** | P-05, R11, D-14 |

> **Ez a projekt legfontosabb tanulsága.** A kockázatot felismertük, a
> válaszlépést megterveztük és végre is hajtottuk — mégis bekövetkezett.
> A tanulság nem az, hogy „legyen több kockázat a listán", hanem hogy
> **a válaszlépéseket ugyanolyan gondosan kell megtervezni, mint az
> azonosítást.**

### T-02 — A hardver-kompatibilitást ellenőrizni kell, nem feltételezni

| | |
|---|---|
| **Mi történt** | Feltételeztük, hogy a meglévő irodai monitorok újrahasznosíthatók (A7 feltevés). Mintavételes ellenőrzésen kiderült, hogy 14 db csak VGA-csatlakozós. |
| **Hatás** | 182 000 Ft váratlan költség; **szerencsére még a tervezési fázisban derült ki** |
| **Kategória** | Tervezés |
| **Javaslat** | Minden „a meglévő eszköz felhasználható" típusú feltevéshez **mintavételes ellenőrzés** tartozzon, ellenőrzési határidővel és felelőssel. |
| **Kinek szól** | Projektmenedzser |
| **Forrás** | A7 feltevés, D-07 |

### T-03 — A WBS-t közösen kell készíteni

| | |
|---|---|
| **Mi történt** | A projektmenedzser egyéni vázlatából **három munkacsomag hiányzott**: a visszaállítási teszt (Szabó Márk vetette fel), a Service Desk felkészítése (Kiss Réka), és az üzemi tanácsi véleményezés (Varga Eszter). |
| **Hatás** | Mindhárom pótolható volt a workshopon |
| **Kategória** | Tervezés |
| **Javaslat** | A WBS-t **kötelezően közösen**, a teljes szakmai csapattal kell összeállítani. Ha egyedül írod meg, pontosan azok a munkacsomagok maradnak ki, amiket nem a te szemszögedből lát valaki. |
| **Kinek szól** | Projektmenedzser |
| **Forrás** | WBS 3. pont |

### T-04 — A 10%-os tartalék túlzottan óvatos volt

| | |
|---|---|
| **Mi történt** | A 4 613 000 Ft-os tartalékból mindössze **182 000 Ft (3,9%)** került felhasználásra. |
| **Hatás** | 4 191 000 Ft fél éven át feleslegesen lekötve |
| **Kategória** | Tervezés / pénzügy |
| **Javaslat** | **Migráció nélküli, jól előre tervezhető IT-beszerzési projektnél 5-6% tartalék elegendő.** A 10% inkább migrációs vagy fejlesztési projektek profilja. |
| **Kinek szól** | Projektmenedzser, kontrolling |
| **Forrás** | Pénzügyi zárás 3. pont |
| **Új a workshopon** | ✔ |

### T-05 — A T0 baseline mérés nélkül nincs mérési szakasz

| | |
|---|---|
| **Mi történt** | A kiindulási méréseket **2026.01.30-án, a Charter aláírása előtt** elvégeztük: ticketszám, MTTR, gépbeüzemelési idő, elégedettség. |
| **Hatás** | **Pozitív tanulság** — a mérési szakasz emiatt egyáltalán értelmezhető |
| **Kategória** | Tervezés / mérés |
| **Javaslat** | A T0 mérés a Kezdeményezés fázis kötelező eleme. **Ez az egyetlen alkalom, amikor a projekt előtti állapot mérhető** — utólag legfeljebb közelíteni lehet. |
| **Kinek szól** | Projektmenedzser, szponzor |
| **Forrás** | Haszonrealizálási terv 3. pont |

---

## 2. Beszerzés

### T-06 — A kizáró feltétel véd attól, amit egy árengedmény „megvenne"

| | |
|---|---|
| **Mi történt** | A legolcsóbb ajánlatot (NovaComp, 25 340 000 Ft) kizártuk, mert nem vállalta az Autopilot-regisztrációt. **1 550 000 Ft-tal volt olcsóbb a nyertesnél.** |
| **Hatás** | Ha pontozandó szempont lett volna, az árelőnyével megnyeri — és a projekt 325 óra kézi gépbeüzemeléssel szembesül, amire nincs kapacitás |
| **Kategória** | Beszerzés |
| **Javaslat** | Azokat a vállalásokat, amelyek **nélkül a projekt céljai teljesíthetetlenek**, kizáró feltételként kell megfogalmazni, nem pontozandó szempontként. És a szempontrendszert **az ajánlatok beérkezése előtt** kell jóváhagyatni. |
| **Kinek szól** | Projektmenedzser, beszerzés |
| **Forrás** | D-10, Ajánlat-összehasonlítás 3. pont |

### T-07 — A Run-book mintadokumentum bekérése megkülönböztet

| | |
|---|---|
| **Mi történt** | Az ajánlatkérés M8 mellékleteként **korábbi Run-book mintát** kértünk. A legolcsóbb CSP-ajánlat (Azurion) nem csatolt ilyet, csak egy bekezdésben ígérte a tudásátadást — 45 pontot kapott a 95 helyett. |
| **Hatás** | A 450 000 Ft-tal drágább, de dokumentáltan felkészült szállító nyert |
| **Kategória** | Beszerzés |
| **Javaslat** | A „vállaljuk a tudásátadást" mondat semmit nem jelent. **Kérj mintadokumentumot** egy korábbi projektből — ez mutatja meg, mit ért alatta a szállító. |
| **Kinek szól** | Projektmenedzser, beszerzés |
| **Forrás** | Ajánlatkérés 7. pont, Ajánlat-összehasonlítás 5. pont |

### T-08 — A beszerzési átfutási időt feladatként kell tervezni

| | |
|---|---|
| **Mi történt** | Eredetileg 03.30-ra terveztem az ajánlatkérés kiadását. Molnár Katalin megmutatta a szabályzat 10 napos ajánlati minimumát és a 8 munkanapos jóváhagyási kört — **2 hetet csúsztunk volna**, mielőtt egyetlen ajánlat is beérkezik. |
| **Hatás** | A tervezésben korrigálva; a beszerzés 03.16-án indult |
| **Kategória** | Beszerzés / ütemezés |
| **Javaslat** | A beszerzési szabályzat átfutási idejét **feladatként kell felvenni az ütemtervbe**, és visszafelé kell számolni a szükséges dátumtól. A beszerzés nem munka, hanem **várakozás** — a 32 napos szakaszból 11 nap volt tényleges munka. |
| **Kinek szól** | Projektmenedzser |
| **Forrás** | Beszerzési terv 3. pont |

### T-09 — A szerződéses kikötések akkor térülnek meg, amikor baj van

| | |
|---|---|
| **Mi történt** | Két kikötés is megtérült: a **helyettesítési kötelezettség** (a CSP-konzultáns kiesésekor, 0 nap csúszás) és a **részszállítás** (10 gép 05.06-ig, enélkül a tesztelés 05.29. után indulhatott volna). |
| **Kategória** | Beszerzés / szerződés |
| **Javaslat** | A projektmenedzser feladata, hogy a **projekt sikeréhez szükséges kikötések** bekerüljenek a szerződésbe. A beszerzés a jogi oldalt ismeri, a jogász nem tudja, mit jelent, hogy „működik". Hat ilyen kikötést vittünk be — mindegyik hasznosnak bizonyult. |
| **Kinek szól** | Projektmenedzser |
| **Forrás** | Szerződés 4. pont, P-02, R14 |

---

## 3. Megvalósítás

### T-10 — A szállítás közbeni ellenőrzés a legolcsóbb hibajavítás

| | |
|---|---|
| **Mi történt** | A 8 minőségellenőrzésből kettő olyan hibát talált, ami az átvételkor mérföldkövet veszélyeztetett volna: az Autopilot beüzemelési idő (2,1 óra a célzott 1,5 helyett) és a 12 hiányzó tápkábel. |
| **Hatás** | Az Autopilot-hiba **26 nappal a 2–3. hullám 40 gépe (06.03.) előtt** derült ki; a javítás 11 nap alatt elkészült, és még így is maradt csaknem két hét |
| **Kategória** | Minőség |
| **Javaslat** | Az ellenőrzési tervet a Minőségtervben kell rögzíteni, dátumokkal. **Az eredményt akkor is le kell írni, ha rendben volt.** |
| **Kinek szól** | Projektmenedzser, szakmai vezető |
| **Forrás** | Minőségellenőrzési jegyzőkönyv |

### T-11 — A szabad tesztelés olyat talál, amit egyik teszteset sem

| | |
|---|---|
| **Mi történt** | A 10 tesztelő fejenként 2 napot dolgozott szabadon az új környezetben. Ebből jött elő a hiányzó közös csapatoldal és a lassú első szinkronizálás — **a 27 teszteset egyike sem fedte le őket**. |
| **Kategória** | Teszt |
| **Javaslat** | A strukturált tesztesetek mellé **kötelező szabad használat**, naplózással. A teszteset azt ellenőrzi, amit vártunk; a szabad használat azt, amire nem gondoltunk. |
| **Kinek szól** | Projektmenedzser, szakmai vezető |
| **Forrás** | Tesztterv 6. pont, P-09, P-10 |

### T-12 — A munkacsomag-visszaigazolás munkakezdés előtt hoz elő problémákat

| | |
|---|---|
| **Mi történt** | A biztonsági alapkonfiguráció kiadásánál Szabó Márk **a visszaigazolásban** jelezte, hogy a jelszóházirend ütközhet a meglévő AD-házirenddel. A kérdés a kiadás előtt nem merült fel. |
| **Hatás** | 2 nap alatt tisztázva, munkakezdés előtt |
| **Kategória** | Megvalósítás |
| **Javaslat** | A munkacsomag-kiadásnál **mindig kérj írásos visszaigazolást**. Nem formalitás: itt derül ki, ha a felelős mást ért a feladaton. |
| **Kinek szól** | Projektmenedzser |
| **Forrás** | P-01, Munkacsomag-kiadás 3. pont |

### T-13 — A fenntartással történő átvétel jobb, mint a megtagadás

| | |
|---|---|
| **Mi történt** | A 2. részszállításnál 12 dokkoló tápkábel hiányzott. Nem tagadtuk meg az átvételt, hanem **fenntartással vettük át, tételes hiánylistával**, és a 80%-os fizetési részletet visszatartottuk. |
| **Hatás** | A 28 használható készlet azonnal kiosztható volt; a 3. hullám tartható maradt; a pótlás 1 nappal a vállalt határidő előtt megérkezett |
| **Kategória** | Megvalósítás / beszerzés |
| **Javaslat** | Fenntartással átvenni csak **tételes hiánylistával, hatással és pótlási határidővel** szabad. A puszta „fenntartással" szó semmit nem ér. A **visszatartott fizetés** hatékonyabb nyomás, mint a kötbér-vita. |
| **Kinek szól** | Projektmenedzser, szakmai vezető |
| **Forrás** | D-18, Teljesítésigazolás 2. sz. jkv. |

---

## 4. Emberek és kommunikáció

### T-14 — A Service Desket be kell vonni, nem tájékoztatni

| | |
|---|---|
| **Mi történt** | Kiss Réka kezdetben **ellenállt** a projektnek — nem a technológia, hanem egy korábbi bevezetés miatt, ahol felkészítés nélkül kapta a terhelést. Bevontuk a WBS-workshoptól kezdve, minden oktatáson jelen volt, és nevesített szerepet kapott a mérésben. |
| **Hatás** | A fajlagos ticketszám hullámról hullámra csökkent: **3,4 → 2,1 → 1,5 ticket/fő** |
| **Kategória** | Kommunikáció / érintettkezelés |
| **Javaslat** | A támogatói oldalt a **tervezéstől** kell bevonni. Aki részt vesz a tervezésben, nem elszenvedője lesz a projektnek, hanem résztvevője. |
| **Kinek szól** | Projektmenedzser |
| **Forrás** | Érintettek nyilvántartása E5, Hatalom-érdek mátrix 3. pont |

### T-15 — Az üzemi tanács kimaradt az érintettek első listájából

| | |
|---|---|
| **Mi történt** | Az érintettek első összeállításánál az üzemi tanács nem szerepelt. A **kick-offon** derült ki, Varga Eszter felvetésére. |
| **Hatás** | Időben pótolható volt; a véleményezés 2026.03.11-én megtörtént, és egy kikötést eredményezett (L7: az eszközfelügyelet nem terjedhet ki a magánhasználatra) |
| **Kategória** | Érintettkezelés |
| **Javaslat** | Az érintettek összeállításánál **ne csak a szervezeti ábrán menj végig, hanem a folyamaton is**: ki nyúl hozzá, kinek van véleményezési vagy vétójoga. Kötelezően nézd meg: üzemi tanács, DPO, Service Desk, HR. |
| **Kinek szól** | Projektmenedzser |
| **Forrás** | Kick-off jkv. D1, Érintettek nyilvántartása E13 |

### T-16 — Az MFA-t az oktatáson kell beállítani, nem otthon

| | |
|---|---|
| **Mi történt** | Az oktatás 2. blokkjában mindenki a saját gépén, közösen állította be az MFA-t. Az időigény 10-15 perc volt, nem a tervezett 5 — a blokk 25-ről 30 percre bővült. |
| **Hatás** | Az első napi „nem tudok belépni" hívások gyakorlatilag megszűntek |
| **Kategória** | Oktatás / adaptáció |
| **Javaslat** | A belépéshez szükséges beállításokat **az oktatáson, felügyelet mellett** kell elvégezni. Ha otthonra bízod, az élesítés napján a Service Deskre zúdul. |
| **Kinek szól** | Projektmenedzser, HR, Service Desk |
| **Forrás** | Oktatási anyag 5. pont, P-03 |
| **Új a workshopon** | ✔ |

---

## 5. Kontroll és riportálás

### T-17 — Az EVM-hez a pénzügyi költségbázis alkalmatlan

| | |
|---|---|
| **Mi történt** | Az első EVM-számítás a **fizetési ütem szerinti** költségbázisra épült. A CPI 0,59 → 2,40 → 1,09, az SPI 0,59 → 2,34 → 0,95 között ugrált, miközben a projektben semmi drámai nem történt. |
| **Hatás** | A számítást újra kellett alapozni **eredmény-alapú felosztásra**; ezután SPI 0,98–1,00, CPI 1,03 |
| **Kategória** | Kontroll |
| **Javaslat** | Beszerzés-nehéz projektben a pénzügyi költségbázis (mikor megy ki a pénz) és az EVM-alap (mit végeztünk el) **két külön dolog**. Ha EVM-et használsz, előre készíts eredmény-alapú felosztást. |
| **Kinek szól** | Projektmenedzser, kontrolling |
| **Forrás** | EVM-elemzés 2–3. pont |
| **Új a workshopon** | ✔ |

### T-18 — A piros státusz nem okoz bajt, a késve pirosodó igen

| | |
|---|---|
| **Mi történt** | Az SR-10 riportot pirosra írtam a két kritikus hiba miatt. **A szponzor másnap felhívott, hogy mit tud segíteni.** 16 riportból 1 piros és 2 sárga volt. |
| **Kategória** | Kommunikáció |
| **Javaslat** | A státuszszín **előrejelzés, nem utólagos megállapítás**. Az SR-05 sárga volt, amikor még semmi nem csúszott — csak látszott, hogy csúszni fog. A hetekig zöld, majd hirtelen piros riport a hitelesség elvesztésének biztos receptje. |
| **Kinek szól** | Projektmenedzser |
| **Forrás** | Státuszriport 4. pont |
| **Új a workshopon** | ✔ |

### T-19 — A biztonsági döntést az összeghatár nem teszi a tiéddé

| | |
|---|---|
| **Mi történt** | A feltételes hozzáférési szabály módosítása (CA-05) formálisan a projektmenedzseri hatáskörben lett volna, mert nem érintett hatókört, ütemet és költséget. **Mégis Nagy Péterhez eszkaláltam**, DPO-véleménnyel. |
| **Kategória** | Kontroll / felelősség |
| **Javaslat** | **Biztonsági szintet érintő döntést soha ne hozz egyedül**, akkor sem, ha az összeghatár a hatáskörödben van. Az összeghatár nem minden. |
| **Kinek szól** | Projektmenedzser |
| **Forrás** | E-03, D-14 |
| **Új a workshopon** | ✔ |

---

## 6. Összesítés

| Kategória | Tanulság |
|---|---:|
| Tervezés | 5 |
| Beszerzés | 4 |
| Megvalósítás | 4 |
| Emberek és kommunikáció | 3 |
| Kontroll és riportálás | 3 |
| **Összesen** | **19** |

| | Darab |
|---|---:|
| Menet közben rögzítve | 14 |
| A záró workshopon jött elő | **5** |
| Pozitív tanulság (amit meg kell ismételni) | 8 |
| Negatív tanulság (amit el kell kerülni) | 11 |

> **A workshopon 5 új tanulság jött elő — de mind a öt olyan, amit egy
> hónappal korábban is le lehetett volna írni.** A menet közbeni gyűjtés
> nélkül a 19-ből valószínűleg 6-8 marad meg, és pont a márciusi-áprilisi
> részletek vesznek el.

## 7. Átadás

| Kinek | Mit | Mikor |
|---|---|---|
| Nagy Péter, IT osztályvezető | A teljes napló, a kiterjesztési projekt előkészítéséhez | 2026.06.30. |
| Molnár Katalin, beszerzés | T-06 – T-09 (beszerzési tanulságok) a beszerzési gyakorlatba | 2026.06.30. |
| Kiss Réka, Service Desk | T-14, T-16 a következő bevezetéshez | 2026.06.30. |
| Balogh Tamás, kontrolling | T-04 (tartalékmérték), T-17 (EVM-alap) | 2026.06.30. |
| **PIR (2026.10.09.)** | A napló kiegészítése a mérési szakasz tanulságaival — ✔ T-20 – T-23, lásd 8. pont | 2026.10.09. |

## 8. Kiegészítés a PIR után — a mérési szakasz tanulságai (2026.10.09.)

> A projektzárás után a napló nem zárul le: a mérési szakasz tanulságai
> ide kerülnek vissza, hogy a kiterjesztési projekt egy helyen találja meg őket.

### T-20 — A T+1 mérés önmagában félrevezető

| | |
|---|---|
| **Mi történt** | A betanulás és a hypercare miatt a júliusi ticketszám a T0 fölé ment (**118** a 103 helyett). |
| **Hatás** | Egyetlen mérésre alapozva a projekt kudarcnak látszott volna |
| **Kategória** | Mérés / haszonrealizálás |
| **Javaslat** | Az élesítés utáni első hónapot **trendjelzőként** kezeld, ne hasonlítsd a célértékhez — és ezt **előre** írd le a KPI-adatlapon. |
| **Kinek szól** | Projektmenedzser, a hasznok gazdája |
| **Forrás** | Havi mérési riportok (T+1), PIR 9. pont |

### T-21 — A torzító tényezőket előre kell leírni

| | |
|---|---|
| **Mi történt** | Az augusztusi ticketszám (**71**) a célérték alatt volt, de a szabadságolás miatt 18%-kal kevesebb munkanap mögött. Torzítás nélkül kb. 87. |
| **Hatás** | Könnyű lett volna sikerként jelenteni; a KPI-adatlap előre rögzítette, hogy a T+3 a mérvadó |
| **Kategória** | Mérés / haszonrealizálás |
| **Javaslat** | A torzító tényezőket és a mérvadó mérési pontot a **mérés előtt** rögzítsd, a hasznok gazdájának jóváhagyásával. |
| **Kinek szól** | Projektmenedzser, mérési koordinátor |
| **Forrás** | Havi mérési riportok (T+2), PIR 9. pont |

### T-22 — A mérőszám nem mindig azt méri, amit hiszel

| | |
|---|---|
| **Mi történt** | Az önkiszolgáló jelszó-visszaállítás miatt a könnyű, gyorsan lezárt ticketek eltűntek a mintából, ami az MTTR értékét felfelé tolta. |
| **Hatás** | A valós javulás nagyobb, mint amit a 11,4 → 5,1 óra mutat |
| **Kategória** | Mérés / haszonrealizálás |
| **Javaslat** | Minden mérőszámnál gondold végig, **mi változik a minta összetételében** a bevezetés hatására — ne csak az átlagot nézd. |
| **Kinek szól** | Mérési koordinátor, Service Desk |
| **Forrás** | KPI-adatlap (M2), PIR 9. pont |

### T-23 — A technikai lehetőség nem egyenlő a kihasználással

| | |
|---|---|
| **Mi történt** | A home office arány 37% lett a célzott 40% helyett, mert két területvezető heti 2 napra korlátozta a szabályzat szerinti 3 napot. |
| **Hatás** | Az M6 nem teljesült; a korlátozott csoport elégedettsége (K5) 0,9 ponttal alacsonyabb |
| **Kategória** | Szervezet / változáskezelés |
| **Javaslat** | A kiterjesztésnél a **szervezeti feltételeket** (vezetői gyakorlat, szabályzat) ugyanúgy előfeltételként kezeld, mint a technikaiakat — lásd a Kiterjesztési javaslat F1 pontját. |
| **Kinek szól** | Szponzor, HR, projektmenedzser |
| **Forrás** | PIR 4. pont, Felhasználói kérdőív 3. pont |

---

| Szerep | Név | Dátum |
|---|---|---|
| Vezette | Tóth Gergő, projektmenedzser | 2026.06.29. |
| A workshop résztvevői | a projektcsapat + 2 pilot felhasználó | 2026.06.29. |

> **Kapcsolódó dokumentumok:** bemenete a *Problémanapló*, a *Kockázati
> riport*, a *Változásnapló*, az *Eszkalációs napló*, az
> *Ajánlat-összehasonlítás* és a *Döntésnapló*; kimenete a
> *Post-Implementation Review* és a *Kiterjesztési javaslat*.
