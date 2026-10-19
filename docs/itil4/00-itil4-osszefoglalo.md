# ITIL 4 — összefoglaló egy PMI-t ismerő projektmenedzsernek

**Dokumentum azonosítója:** XYO-METH-002\
**Cél:** megérteni, mi az ITIL 4, hol kapcsolódik egy projekthez, és mit tenne hozzá a Xyo Cloud Pilothoz\
**Terjedelem:** kb. 12 oldal\
**Verzió:** 1.0 — 2026. október

> Ez nem vizsgafelkészítő jegyzet, de **a Foundation-szint minden fogalmát tartalmazza**, a
> hivatalos angol névvel együtt. Arra jó, hogy megértsd a logikáját, magabiztosan használd a
> fogalmait egy üzemeltetési megbeszélésen, és tudd, mit kell egy projektnek átadnia ahhoz, hogy
> a szolgáltatás utána is jól működjön.
>
> *Az ITIL® a PeopleCert bejegyzett védjegye. Ez a szöveg saját megfogalmazás, nem a hivatalos
> kiadvány részlete.*

---

## 1. Mi az ITIL egy mondatban?

Az **ITIL** az IT-szolgáltatásmenedzsment legelterjedtebb keretrendszere: azt írja le, **hogyan
teremt értéket egy szervezet a szolgáltatásain keresztül** — a kialakítástól az üzemeltetésen át
a folyamatos fejlesztésig.

Fontos, hogy mi **nem**:

- **nem projektmódszertan** — a projektmenedzsmentet egy gyakorlatként kezeli a 34 közül, és arra
  számít, hogy a módszert a PMI vagy a PRINCE2 adja;
- **nem szabvány**, és egy szervezet nem „ITIL-tanúsított” — személyek tesznek vizsgát. A
  szervezeti tanúsításra az **ISO/IEC 20000-1** szabvány való, amely sokat merít az ITIL-ből;
- **nem receptkönyv** — ajánlásokat ad, és kifejezetten elvárja, hogy a szervezet a saját
  méretéhez szabja őket.

### Honnan jött?

| Év | Mi történt |
|---|---|
| 1989 | A brit kormányzat (CCTA) kiadja az első ITIL-köteteket — a közigazgatási IT-üzemeltetés bevált gyakorlatait |
| 2000–2001 | **ITIL v2** — a szolgáltatástámogatás és -nyújtás folyamatai; ekkor terjed el világszerte |
| 2007, 2011 | **ITIL v3** — az életciklus-szemlélet (stratégia, tervezés, átadás, üzemeltetés, fejlesztés) |
| 2019 | **ITIL 4** — érték, Szolgáltatásérték-rendszer, gyakorlatok folyamatok helyett, agilis és DevOps szemlélet |
| 2021 | A PeopleCert megvásárolja az AXELOS-t; azóta ő a gazdája |
| 2026 | **ITIL (Version 5)** — a Foundation-vizsga 2026.02.12-től elérhető (lásd a 13. pontot) |

> **Miért ITIL 4 ez az összefoglaló?** A magyar nagyvállalati és közszférás hirdetések és
> pályázatok ma ITIL 4-et kérnek, a PeopleCert tervezetten 2027 végéig tartja az ITIL 4 vizsgákat,
> és a meglévő ITIL 4 tanúsítványok érvényesek maradnak. Az ITIL 5 legfontosabb változásait a
> 13. pont foglalja össze.

---

## 2. A legfontosabb különbség egy mondatban

> **A projekt egyszer véget ér, a szolgáltatás nem.**

A Xyo Cloud Pilot 2026.06.30-án lezárult. A felhőalapú munkahely azóta is működik: minden nap
valaki bejelent egy hibát, kér egy új fiókot, módosít egy beállítást. A projektmódszertan azt
kérdezi, *hogyan juttatjuk el a megoldást az átadásig*; az ITIL azt, *hogyan teremt utána értéket
— és mit kell ehhez a projektnek átadnia*.

| | Projektmódszertan (PMI, PRINCE2) | ITIL 4 |
|---|---|---|
| Időtáv | A projekt kezdetétől a zárásig | Amíg a szolgáltatás él |
| Fő kérdés | Határidőre, keretből, a hatókört teljesítve? | Eléri-e a fogyasztó a kívánt eredményt? |
| Siker mérése | Átadás, elfogadás | Folyamatosan mért szolgáltatási szint és elégedettség |
| Változás | A terv változása (változáskérelem) | Az éles környezet változása (változásengedélyezés) |

---

## 3. Alapfogalmak

Az ITIL 4 alapgondolata: az értéket **nem a szolgáltató állítja elő és adja át**, hanem a
szolgáltató és a fogyasztó **közösen hozza létre** (*value co-creation*). Egy laptop önmagában
nem érték; az érték az, hogy a munkatárs otthonról is el tudja végezni a munkáját.

| Fogalom | Angolul | Jelentése | A Xyo-ban |
|---|---|---|---|
| Szolgáltatás | Service | Az értékteremtés közös létrehozását lehetővé tevő eszköz: a fogyasztó kívánt eredményeit segíti, anélkül hogy bizonyos költségeket és kockázatokat neki kellene kezelnie | A „felhőalapú munkahely” |
| Termék | Product | A szervezet erőforrásainak olyan konfigurációja, amely értéket teremthet egy fogyasztónak | A Microsoft 365 alapú munkakörnyezet a beállításokkal |
| Szolgáltatásajánlat | Service offering | Egy vagy több szolgáltatás leírása egy célcsoportnak: **javak**, **hozzáférés erőforráshoz**, **szolgáltatási tevékenységek** | Laptop és monitor · licenc, SharePoint, VPN · Service Desk, gépbeüzemelés |
| Kimenet | Output | Amit egy tevékenység előállít | 50 beállított laptop, 50 fiók |
| Eredmény | Outcome | Amit az érintett a kimenetek révén elér | Az új belépő 0,8 munkanap alatt áll munkába (korábban 3,5) |
| Haszon | Utility | Mit tud a szolgáltatás — célnak megfelelés | Közös dokumentumkezelés, távoli elérés |
| Garancia | Warranty | Mennyire megbízhatóan — használatra alkalmasság: rendelkezésre állás, kapacitás, biztonság, folytonosság | 99,6% rendelkezésre állás, 100% MFA, nulla adatvesztés |
| Költség, kockázat | Cost, risk | A szolgáltatás egyeseket levesz a fogyasztóról, másokat rárak | Levett: géppark-karbantartás, adatvesztés · rárakott: mobilnet, kizárás egy rossz szabály miatt |
| Szolgáltatási kapcsolat | Service relationship | Nyújtás, igénybevétel és a kapcsolat kezelése együtt | Az IT szolgáltat a pilot-körnek, közben maga is fogyasztó (Microsoft, Cloudia, TechLine) |

**A fogyasztói oldal szerepei:** a **megrendelő** (*customer*) határozza meg az igényt, a
**felhasználó** (*user*) használja a szolgáltatást, a **szponzor** (*sponsor*) engedélyezi a
költséget. A Xyo-ban három különböző ember: Horváth Júlia, az 50 pilot-résztvevő és Kovács Anita.

> **Tipikus hiba:** a haszonra figyelni és a garanciát elfelejteni. Egy szolgáltatás, amely mindent
> tud, de naponta egyszer leáll, nem teremt értéket. A Xyo projekt itt jól mért: a rendelkezésre
> állás (M9), az MFA-lefedettség (M8) és az adatvesztés (M10) garanciamutatók.

---

## 4. A négy dimenzió

Minden szolgáltatást négy nézőpontból egyszerre kell végiggondolni. Ha bármelyik kimarad, a
szolgáltatás akadozik — akkor is, ha a technika hibátlan.

| Dimenzió | Angolul | Kérdés | A Xyo-ban |
|---|---|---|---|
| Szervezetek és emberek | Organizations and people | Ki csinálja, és tudja-e? | Service Desk-felkészítés, oktatás, home office szabályzat |
| Információ és technológia | Information and technology | Mire épül, milyen információt kezel? | Microsoft 365, Intune, as-built dokumentáció, ticketadatok |
| Partnerek és beszállítók | Partners and suppliers | Kik vesznek még részt? | Microsoft (CSP-n át), Cloudia Solutions, TechLine Zrt., mobilszolgáltató |
| Értékáramok és folyamatok | Value streams and processes | Milyen lépésekben jut el egy igény az értékig? | Új belépő, kilépő, elveszett laptop |

A négy dimenzióra **külső tényezők** hatnak; az ITIL a **PESTLE**-modellt használja (politikai,
gazdasági, társadalmi, technológiai, jogi, környezeti).

> **A Xyo tanulsága:** a home office arány a cél alatt maradt (37% a ≥ 40% helyett), mert a vezetők
> nem egységesen alkalmazták a szabályzatot. A technika rendben volt — a *Szervezetek és emberek*
> dimenzió maradt el. A PIR ezt így fogalmazta: a technikai lehetőség nem egyenlő a kihasználással.

---

## 5. A Szolgáltatásérték-rendszer (SVS)

A **Szolgáltatásérték-rendszer** (*Service Value System*) azt írja le, hogyan alakul át egy
**lehetőség vagy igény** a szervezetben **értékké**. Öt eleme van:

| Elem | Angolul | Szerepe |
|---|---|---|
| Irányelvek | Guiding principles | Minden döntést vezérelnek (hét darab, lásd 6. pont) |
| Irányítás | Governance | A vezetés értékel, irányt szab, figyel |
| Szolgáltatási értéklánc | Service value chain | Hat tevékenység, amiből az értékáramok felépülnek (7. pont) |
| Gyakorlatok | Practices | Szervezeti erőforrások egy-egy feladatra: emberek, folyamatok, eszközök, információ (8. pont) |
| Folyamatos fejlesztés | Continual improvement | Minden szinten zajló, visszatérő tevékenység |

Az SVS célja a **silók lebontása**: a szervezet részei nem önmagukért, hanem egy közös értékért
dolgoznak. A Xyo-ban a HR, a Service Desk és a rendszergazda együtt viszi végig az új belépőt —
egyikük folyamata sem írja le önmagában.

---

## 6. A hét irányelv

| # | Irányelv | Angolul | Lényege | A Xyo-ban |
|---|---|---|---|---|
| 1 | Az értékre összpontosíts | Focus on value | Minden tevékenység értéket szolgáljon; tudd, ki a fogyasztó | A haszonterv eredményeket mért, nem kiosztott gépeket |
| 2 | Kezdd ott, ahol vagy | Start where you are | Mérd fel és használd, ami működik | T0 mérés 2026.01.30-án, a meglévő Service Desk vitte a támogatást |
| 3 | Haladj lépésenként, visszajelzéssel | Progress iteratively with feedback | Kezelhető, önmagukban értékes lépések | Három élesítési hullám (10, 20, 20 fő); a pilot maga is lépés |
| 4 | Működj együtt, tedd láthatóvá a munkát | Collaborate and promote visibility | A rejtett munka rejtett kockázat | Közös WBS-workshop, a runbookot a Service Deskkel írták |
| 5 | Gondolkodj és dolgozz egészben | Think and work holistically | A részek optimuma nem az egész optimuma | HR-szabályzat, üzemi tanács, adatvédelem is a projekt része lett |
| 6 | Legyen egyszerű és gyakorlatias | Keep it simple and practical | Ami nem teremt értéket, azt hagyd el | 50 főnél nem kell külön változástestületi ülés |
| 7 | Optimalizálj és automatizálj | Optimize and automate | Előbb egyszerűsíts, utána automatizálj | Autopilot: 6,5 → 1,4 óra gépbeüzemelés |

> **Tipikus félreértés:** az irányelveket egymás után alkalmazni. Egyszerre érvényesek, és
> gyakran feszülnek egymásnak — például a 6. („legyen egyszerű”) és az 5. („gondolkodj egészben”).
> A jó döntés az, amelyik mindkettőt tiszteletben tartja.

---

## 7. A szolgáltatási értéklánc és az értékáramok

A **szolgáltatási értéklánc** hat tevékenysége:

| Tevékenység | Angolul | Mit tesz |
|---|---|---|
| Tervezés | Plan | Közös megértés a jövőképről, az állapotról és az irányról |
| Fejlesztés | Improve | A termékek, szolgáltatások és gyakorlatok folyamatos javítása |
| Bevonás | Engage | Az érintettek igényeinek megértése, kapcsolat velük |
| Kialakítás és átadás | Design and transition | Hogy a szolgáltatás megfeleljen az elvárt minőségnek, költségnek és piaci időnek |
| Beszerzés és építés | Obtain/build | Az összetevők beszerzése vagy elkészítése |
| Szolgáltatásnyújtás és támogatás | Deliver and support | A szolgáltatás nyújtása a megállapodott előírások szerint |

**A tevékenységek nem sorrendet jelentenek.** Egy **értékáram** (*value stream*) fűzi össze őket
abban a sorrendben, ahogy egy adott igény eljut az értékig. Példa a Xyo üzemeltetéséből:

> **Új belépő munkába állítása.** *Bevonás:* a HR szolgáltatáskérést rögzít a Service Desknél →
> *Beszerzés és építés:* fiók, licenc, csoporttagság, Autopilot-regisztráció → *Kialakítás és
> átadás:* a jogosultságok és a gép megfelelőségének ellenőrzése → *Szolgáltatásnyújtás és
> támogatás:* átadás az első napon, MFA-regisztráció → *Fejlesztés:* az átfutási idő mérése (M5).
> Eredmény: 3,5 munkanap helyett 0,8.

**Hová esik egy projekt?** A Xyo projekt főként a *Kialakítás és átadás* és a *Beszerzés és
építés* tevékenységet szolgálta; a Kezdeményezés a *Bevonás* és a *Tervezés*, a haszonmérés a
*Fejlesztés*. A zárásnál a szolgáltatás átkerül a *Szolgáltatásnyújtás és támogatás*-ba — ez a
projekt és az ITIL legfontosabb találkozási pontja.

---

## 8. A gyakorlatok

Az ITIL 4 **34 gyakorlatot** ír le: 14 **általános menedzsment-**, 17 **szolgáltatásmenedzsment-**
és 3 **technikai menedzsment-gyakorlatot**. A gyakorlat több, mint egy folyamat: emberek, eszközök,
információ és partnerek együtt. A Foundation-vizsga 15 gyakorlatot kér: hetet részletesen, nyolcat
a céljuk szintjén.

### 8.1 A hét részletesen ismert gyakorlat

**Incidenskezelés** (*Incident management*). **Incidens:** a szolgáltatás nem tervezett
megszakadása vagy minőségének romlása. Cél: a szolgáltatás mielőbbi helyreállítása — nem az ok
megtalálása. Az incidenseket **prioritás** szerint kezeljük (hatás × sürgősség), prioritásonként
célidővel. A **kiemelt incidens** (*major incident*) külön eljárást kap. Az ITIL 4 ajánlja a
**rajzást** (*swarming*) is: a bonyolult incidenst egyszerre több szakértő vizsgálja, nem
szintről szintre adják tovább.

**Problémakezelés** (*Problem management*). **Probléma:** egy vagy több incidens oka vagy
lehetséges oka. **Ismert hiba** (*known error*): olyan probléma, amelyet elemeztek, de még nem
oldottak meg. **Kerülőmegoldás** (*workaround*): az incidens hatását csökkentő megoldás, amíg a
végleges nincs meg. Három fázis: **problémaazonosítás**, **problémakontroll** (elemzés,
kerülőmegoldás), **hibakontroll** (a végleges javítás és az ismert hibák kezelése).

> **Névütközés a Xyo-ban:** a „Problémanapló” a PMI *issue log*-ja — projektakadályok
> nyilvántartása, nem ITIL-problémák. Egy beszélgetésben mindig tisztázd, melyikről van szó.

**Változásengedélyezés** (*Change enablement*, korábbi neve *change control*). **Változás:**
bármi hozzáadása, módosítása vagy eltávolítása, ami közvetlenül vagy közvetve hathat a
szolgáltatásokra. Három típus:

| Típus | Angolul | Mikor | Ki engedélyezi |
|---|---|---|---|
| Szabványos | Standard change | Alacsony kockázatú, jól ismert, előre engedélyezett | Senki egyenként — a modell egyszer engedélyezve |
| Normál | Normal change | Értékelni és engedélyezni kell | A **változásengedélyező** (*change authority*) a kockázat szerint |
| Sürgős | Emergency change | Azonnal kell, például egy incidens elhárításához | Gyorsított engedélyezés, utólagos dokumentálással |

A **változási ütemterv** (*change schedule*) mutatja, mi mikor kerül élesbe. A cél nem a
fékezés, hanem a sikeres változás: az ITIL 4 kifejezetten óv a túlbürokratizált
változástestülettől.

**Szolgáltatáskérés-kezelés** (*Service request management*). **Szolgáltatáskérés:** a
felhasználó előre meghatározott kérése — információ, hozzáférés, szabványos változás. Nem hiba:
tervezhető, és a jó részük önkiszolgálással vagy automatizálással teljesíthető (a Xyo-ban az új
belépő, a kilépő és a jelszó-visszaállítás).

**Service Desk** (*Service desk*). Az incidensek és kérések egyetlen, egyértelmű befogadási
pontja. A jó Service Desk nem csak technikai: érti a felhasználó helyzetét, és több csatornán
elérhető. A Xyo-ban: Kiss Réka és két munkatárs, belső 4200, `servicedesk@xyo.hu`.

**Szolgáltatásszint-kezelés** (*Service level management*). Világos, üzleti alapú célok a
szolgáltatás teljesítményére, rendszeres mérés és felülvizsgálat. **SLA** (*service level
agreement*): írásos megállapodás a szolgáltató és a megrendelő között. Az ITIL 4 figyelmeztet a
**„görögdinnye-hatásra”**: kívül zöld (minden SLA-mutató teljesül), belül piros (a felhasználó
elégedetlen). Ezért a technikai mutatók mellé élménymutató kell — a Xyo-ban ilyen a kérdőív
(M11).

**Folyamatos fejlesztés** (*Continual improvement*). A fejlesztés mindenki feladata, nem egy
osztályé. A **hétlépéses fejlesztési modell**: *Mi a jövőkép? — Hol tartunk most? — Hová akarunk
eljutni? — Hogyan jutunk el oda? — Cselekedjünk! — Elértük? — Hogyan tartjuk fenn a lendületet?*
A javaslatok a **folyamatos fejlesztési nyilvántartásba** (*continual improvement register, CIR*)
kerülnek, prioritással és gazdával.

### 8.2 A nyolc gyakorlat a céljuk szintjén

| Gyakorlat | Angolul | Célja egy mondatban |
|---|---|---|
| Információbiztonsági menedzsment | Information security management | Az információ bizalmasságának, sértetlenségének és rendelkezésre állásának védelme |
| Kapcsolatkezelés | Relationship management | Kapcsolat az érintettekkel stratégiai és taktikai szinten |
| Beszállítókezelés | Supplier management | A beszállítók és teljesítményük megfelelő kezelése |
| IT-eszközgazdálkodás | IT asset management | Az IT-eszközök teljes életciklusának kezelése |
| Monitorozás és eseménykezelés | Monitoring and event management | Az állapotváltozások (események) észlelése és a megfelelő válasz |
| Kiadáskezelés | Release management | Új és módosított szolgáltatások elérhetővé tétele |
| Szolgáltatáskonfiguráció-kezelés | Service configuration management | Pontos információ a konfigurációról és a konfigurációs tételekről |
| Telepítéskezelés | Deployment management | Hardver, szoftver, dokumentáció éles környezetbe juttatása |

> **Kiadás vagy telepítés?** A *telepítés* az, hogy a változás eljut a környezetbe; a *kiadás* az,
> hogy a felhasználók számára elérhetővé válik. A Xyo-ban az Autopilot telepít, a három
> élesítési hullám három kiadás.

---

## 9. Szerepek — nincs előírt szervezet

Az ITIL 4 **nem ír elő szervezeti felépítést**. Azt kéri, hogy minden gyakorlatnak legyen gazdája,
és mindenki tudja, miért felel. Egy kis IT-csapatnál ezek **szerepek**, amelyeket a meglévő
emberek viselnek. A Xyo-ban egy lehetséges kiosztás:

| Szerep | Ki |
|---|---|
| Szolgáltatásgazda (*service owner*) | Nagy Péter |
| Szolgáltatásszint-felelős, Service Desk vezető | Kiss Réka |
| Problémagazda, konfiguráció, technikai biztonság | Szabó Márk |
| Változásengedélyező (normál, sürgős) | Nagy Péter |
| Beszállítókezelés | Molnár Katalin (szerződés), Nagy Péter (szakmai) |
| Adatvédelem | dr. Fekete Zsolt — az adatvédelmi tisztviselő nem azonos az információbiztonsági felelőssel |

**Új ember nem kell** — a kockázat a koncentráció: Szabó Márk négy szerepet visel. A 190 fős
kiterjesztésnél viszont a Service Desk kapacitását bővíteni kell (+1 fő, a kiterjesztési
javaslat F4 előfeltétele) — ez kapacitásszámítás, nem ITIL-követelmény.

---

## 10. ITIL és a projektmódszertanok — együtt

A három módszertan nem ugyanarra a kérdésre felel, ezért együtt működik:

| Réteg | Kérdés | Forrás |
|---|---|---|
| Technika | Hogyan becsüljek, ütemezzek, kezeljem a kockázatot? | **PMI / PMBOK** |
| Kormányzás | Ki dönt, mikor, milyen tűréssel? | **PRINCE2** |
| Szolgáltatás-életciklus | Mi történik az átadás után, és mit kell átadni? | **ITIL 4** |

**Hol érnek össze a gyakorlatban?** A projekt tervezésekor a követelmények közé bekerülnek a
**szolgáltatásszint-követelmények** és a **szolgáltatási elfogadási kritériumok**. A megvalósítás
alatt az éles környezet módosítása **változás**, akkor is, ha a projekt végzi. Az élesítés után a
felhasználói bejelentés **incidens**, akkor is, ha a projekt még nem zárult le. A zárás
**átadás**: belső SLA, ismerthiba-lista, a korai életszakasz-támogatás (a hypercare) kilépési
feltétele és egy gazdával rendelkező fejlesztési nyilvántartás.

**Ahol ütközhetnek:**

- **Projekt-változáskérelem vagy üzemeltetési változás?** A hatókörről a projekt dönt, az éles
  konfigurációról a változásengedélyező. Egy jóváhagyott projekt-változáskérelem nem engedélyezi
  automatikusan az éles módosítást.
- **Steering vagy szolgáltatásfelülvizsgálat?** A projekt végéig a Steering; az átadástól a
  szolgáltatásgazda és a megrendelő negyedéves felülvizsgálata.
- **Projekt-siker vagy szolgáltatás-siker?** A projekt sikerét a zárás mutatja, a szolgáltatásét a
  folyamatos mérés.

---

## 11. A Xyo Cloud Pilot ITIL-szemmel

### Ami megvolt — ITIL-név nélkül

| Amit a projekt tett | ITIL-ben ez… |
|---|---|
| Haszonterv eredménymutatókkal (M1–M12), T0-tól PIR-ig | Érték, eredmények, mérés és jelentés |
| Service Desk felkészítése 2 héttel az élesítés előtt | Service Desk, tudásmenedzsment |
| Runbook: 15 leggyakoribb eset, négyszintű eszkaláció, break-glass rend | Incidenskezelés, információbiztonság |
| Hypercare mérhető kilépési feltétellel | Korai életszakasz-támogatás (*early life support*) |
| Három élesítési hullám visszaállási tervvel | Kiadáskezelés |
| Autopilot-beüzemelés | Telepítéskezelés |
| A szállítói hozzáférés megszüntetésének ellenőrzése | Információbiztonság, beszállítókezelés |

### Ami hiányzott

| Hiány | Mennyire | Mit tenne hozzá |
|---|---|---|
| Belső SLA és OLA | nagy | A mért adatokból levezetett célszintek, negyedéves felülvizsgálat |
| Üzemeltetési változásengedélyezés | nagy | Szabványos / normál / sürgős modell — a P-05-ös kizárás ilyen hiba |
| Problémakezelés és ismerthiba-nyilvántartás | közepes | Gazda és kiváltó feltétel az ismétlődő hibákra |
| Kérés és incidens szétválasztása a statisztikában | közepes | Az M1 ma mindkettőt együtt számolja |
| Folyamatos fejlesztési nyilvántartás a PIR után | közepes | A javaslatoknak gazdája lesz |
| Konfigurációs nyilvántartás frissítése | közepes | Az as-built nem avul el a változásokkal |

### Egy példa: a késő MFA-értesítés (H-09)

A hiba a tesztben került elő (S3), 2026.06.04-én bekerült a projekt problémanaplójába (P-13), nyitott
ponttal átment az elfogadáson, a runbook kerülőmegoldást adott rá. A felhasználói kérdőívben a 44
válaszadóból 12 említette, és a PIR szerint hozzájárult, hogy az M1 cél nem teljesült. A PIR
idején a hét nyitott pontból egyedül ez maradt nyitva: „figyelés alatt”, szállítói bejelentés
nélkül.

**A projekt jól csinálta a dolgát** — dokumentált, felelőst adott, átadott. A hiány a projekt
utáni gazdátlanság: nincs kiváltó feltétel („ha rendszeressé válik” — mikor?), és nincs fórum,
ahol dönteni kell róla. A problémakezelés és a szolgáltatásfelülvizsgálat pontosan ezt adja.

### Megérte volna?

Egy 50 fős pilotnál a teljes ITIL-apparátus **aránytalan** lett volna — és ezt maga az ITIL is
mondja („legyen egyszerű és gyakorlatias”). Ami a pilotnál is megérte volna: a belső SLA, egy
egyszerű változásmodell és a problémagazda. A **190 fős kiterjesztésnél** ezek már nem
választhatók: ott a Service Desk terhelése, a változások száma és a szállítói függés is
nagyságrenddel nagyobb.

---

## 12. Magyar környezet: nagyvállalat és közszféra

A magyar nagyvállalati és állami IT-ban az ITIL a **közös nyelv**: az üzemeltetési szerződések,
a pályázatok és az álláshirdetések rendszeresen hivatkoznak rá. Egy projektmenedzsernek ezért nem
a vizsga a fontos, hanem hogy a projekt átadása ezen a nyelven értelmezhető legyen.

**Szabványok.** Szervezeti tanúsításra az **ISO/IEC 20000-1** (szolgáltatásmenedzsment-rendszer)
és az **ISO/IEC 27001** (információbiztonság) szolgál. Az ITIL gyakorlatai mindkettőhöz jó
alapot adnak, de a tanúsítás a szabvány szerint történik.

**Kiberbiztonsági szabályozás.** A **2024. évi LXIX. törvény** ültette át a magyar jogba az EU
**NIS2-irányelvét** (2022/2555/EU); a végrehajtás részleteit a **418/2024. (XII. 23.) Korm.
rendelet** tartalmazza. A hatálya ágazattól és mérettől függ: a közigazgatás mellett a felsorolt
ágazatok közepes és nagy szervezeteire terjed ki. A hatály alá eső szervezetnek kiberbiztonsági
incidenseit a **Nemzeti Kibervédelmi Intézetnek (NKI)** kell jelentenie; az első, korai
figyelmeztetés határideje **24 óra** attól, hogy az incidensről tudomást szerzett. A NIS2-irányelv
ezt egy 72 órán belüli bejelentéssel és egy egy hónapon belüli zárójelentéssel folytatja; a hazai
részletszabályokat a rendelet adja.

**Mit jelent ez egy projektnek?** Ha a szolgáltatás hatály alá eső szervezetnél fut, az
incidenskezelésnek tudnia kell, mi minősül jelentendő kiberbiztonsági incidensnek, ki jelenti és
milyen határidővel — ez az ITIL *incidenskezelés*, *információbiztonsági menedzsment* és
*beszállítókezelés* gyakorlatainak közös pontja. A projekt feladata, hogy a runbook és a szállítói
szerződések ezt tartalmazzák. (Hogy a Xyo hatály alá esik-e, az ágazatától függ — ezt a
mintaprojekt nem rögzíti. Az adatvédelmi incidensre vonatkozó 72 órás NAIH-bejelentés a Xyo
visszaállási tervében már szerepel.)

---

## 13. Tanúsítás és verziók

**ITIL 4 Foundation.** Feleletválasztós vizsga: 40 kérdés, 60 perc, a sikeres vizsgához 65% (26
helyes válasz) kell, segédanyag nélkül. A Foundation után a **Managing Professional** (négy
modul), a **Strategic Leader** és a gyakorlatokra épülő **Practice Manager** utak következnek; a
részleteket a felület *Haladó szint és ITIL 5* fejezete mutatja.

**ITIL (Version 5).** A PeopleCert 2026 elején adta ki; a Foundation-vizsga 2026.02.12-től
érhető el, a haladó modulok szakaszosan követik. A PeopleCert tájékoztatása szerint az ITIL 4
vizsgák kivezetése **tervezetten 2027.12.31.**, a meglévő ITIL 4 tanúsítványok érvényesek
maradnak. A fő irány: a szolgáltatások mellett a **digitális termékek** is a keretrendszer
tárgyai, a gyakorlatok új csoportosítást kapnak, és megjelenik a mesterséges intelligencia
szerepe. Aki ma ITIL 4-et tanul, nem tanul feleslegesen: az alapfogalmak és a gyakorlatok
gondolkodásmódja átvihető.

**Az átmenet szabályai (a PeopleCert ITIL-GYIK-je szerint).** Az ITIL 4-tanúsítványok érvényes
előfeltételei az ITIL 5 haladó moduljainak, a Foundationt nem kell újra letenni. Aki frissítene,
annak az egynapos **ITIL Foundation Bridge (Version 5)** szól (ez is 2027.12.31-ig érhető el). Az
ITIL 5 címei: **Practice Manager**, **Managing Professional**, **Strategic Leader**, mindhárommal
**ITIL Master**; mindegyikhez kell az új **ITIL Transformation** modul. A Practice Manager
csomagjai (MSF, PIC, CAI) együtt pontosan a Foundation 15 gyakorlatát fedik le. Az ITIL 5
Foundation 2026 októberében kilenc nyelven érhető el — **magyarul még nem**; ezért ma egy magyar
jelöltnek az ITIL 4 Foundation is jó választás.

---

## 14. Tipikus hibák egy ITIL-bevezetésnél

| # | Hiba | Miért baj |
|---|---|---|
| 1 | Eszközzel kezdeni (ticketrendszer-csere) | Az eszköz a rossz folyamatot is gyorsítja; előbb egyszerűsíts |
| 2 | Mind a 34 gyakorlatot bevezetni | Aránytalan; a „kezdd ott, ahol vagy” a mérés, nem a teljes kép |
| 3 | Változástestület minden apróságra | A szabványos változások előre engedélyezhetők; a bürokrácia a kerülőutakat szüli |
| 4 | SLA mérhetetlen vagy ellenőrizetlen célokkal | Adatból vezesd le a célszintet — a Xyo-ban a PIR értékei a kiindulópont |
| 5 | Csak technikai mutatók | Görögdinnye-hatás: a mutatók zöldek, a felhasználó elégedetlen |
| 6 | Incidens és probléma összemosása | A helyreállítás sürgős, az okkeresés alapos — más ritmus, más gazda |
| 7 | A projektet kihagyni a szolgáltatás tervezéséből | Az átadás a projekt végén kezdődik, és a hiányokat az üzemeltetés örökli |

---

## 15. Ha ennyit jegyzel meg, az elég

| # | Tétel |
|---|---|
| 1 | A projekt egyszer véget ér, a szolgáltatás nem. Az ITIL arról szól, ami utána jön — és arról, mit kell átadni. |
| 2 | Az értéket a szolgáltató és a fogyasztó **közösen** hozza létre; a kimenet nem azonos az eredménnyel. |
| 3 | A haszon mellé **garancia** kell: rendelkezésre állás, kapacitás, biztonság, folytonosság. |
| 4 | **Incidens** ≠ **probléma** ≠ **projekt-issue**. Az első a helyreállításról, a második az okról, a harmadik a projektakadályról szól. |
| 5 | A projekt hatókör-változása és az éles **változás** két külön döntés. |
| 6 | Az **SLA** a mért adatokból jön, és élménymutató is kell mellé. |
| 7 | Az ITIL nem ír elő szervezetet; kis csapatnál **szerepek** vannak, nem új munkakörök. |
| 8 | PMI + PRINCE2 + ITIL: technika + kormányzás + szolgáltatás-életciklus. Nem versenyeznek. |

---

## Források

- PeopleCert — az ITIL hivatalos gazdája; az ITIL (Version 5) bevezetéséről: <https://www.peoplecert.org/news-and-announcements/itil-version-5-explained>
- PeopleCert — ITIL (Version 5) GYIK: tanúsítási rend, átmenet, kivezetés, nyelvek: <https://www.peoplecert.org/help-and-support/faq-itil>
- Az EU NIS2-irányelve (2022/2555/EU): <https://eur-lex.europa.eu/eli/dir/2022/2555/oj>
- Nemzeti Kibervédelmi Intézet: <https://nki.gov.hu>
- MKIK NIS2-tájékoztató, jogi állásfoglalások a 2024. évi LXIX. törvényről és a 418/2024. Korm. rendeletről: <https://nis2.mkik.hu>

*A verzió- és vizsgaadatok és a jogszabályi hivatkozások 2026 októberi állapotot tükröznek.*

---

> **Kapcsolódó anyagok a felületen:** a fázisoldalakon az *ITIL 4-kiegészítés* blokk mutatja, hová
> esik az adott fázis az értékláncban, és mit tenne hozzá. Az **ITIL 4** oldalon a gyakorlatok, a
> szerepek, a három módszertan együttműködése és a mintadokumentumok találhatók.
