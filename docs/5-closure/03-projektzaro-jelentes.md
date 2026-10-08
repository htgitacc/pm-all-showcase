# Projektzáró jelentés (Project Closure Report)

**Dokumentum azonosítója:** XYO-CP-403\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Elfogadta:** Projekt Irányító Bizottság — **2026. június 30.** (M10)\
**Verzió:** 1.0

> A projekt hivatalos mérlege: mit vállaltunk, mit teljesítettünk, hol tértünk
> el és miért. **Ez a te értékelésed is** — ez alapján ítélik meg a munkádat.
> Az eltéréseket **magyarázd meg, ne mentegesd**.

---

## 1. Vezetői összefoglaló

A Xyo Cloud Pilot **2026.02.02. és 2026.06.30. között, a tervezett határidőre
és a költségkereten belül lezárult.** Mind az 50 kijelölt munkatárs élesben,
felhőalapú munkakörnyezetben dolgozik.

| | |
|---|---|
| **Időtartam** | 2026.02.02 – 2026.06.30. (a terv szerint) |
| **Tényleges költés** | **44 822 000 Ft** az 52 000 000 Ft-os keretből |
| **Mérföldkövek** | 10/10 határidőre |
| **Átvételi kritériumok** | 25/26 megfelelt |
| **Élesített felhasználók** | 50/50 |

A projekt nyolc vállalt céljából **három már most igazolt** (C1–C3); négy cél
(C4–C7) a 2026.09.30-ig tartó mérési szakaszban dől el, a nyolcadik (C8) a
2026.10.09-i kiterjesztési döntéssel.

## 2. A célok teljesülése

| # | Cél | Mérőszám | Célérték | Tény | Állapot |
|---|---|---|---:|---:|:-:|
| C1 | Élesben működő felhőkörnyezet | Élesített felhasználók | 50 fő | **50 fő** (2026.06.12.) | ✔ **teljesült** |
| C2 | Egységes azonosítás | MFA-lefedettség | 100% | **100%** | ✔ **teljesült** |
| C3 | A projekt a kereten belül zárul | Tényleges költés | ≤ 52 000 000 Ft | **44 822 000 Ft** | ✔ **teljesült** |
| C4 | Csökkenő támogatási terhelés | Ticket / hó | ≤ 72 | *mérés alatt* | ⏳ 2026.09.30. |
| C5 | Gyorsabb hibaelhárítás | MTTR | ≤ 6,0 óra | *mérés alatt* | ⏳ 2026.09.30. |
| C6 | Rugalmas munkavégzés | Home office napok aránya | ≥ 40% | *mérés alatt* | ⏳ 2026.09.30. |
| C7 | Felhasználói elfogadás | Elégedettség | ≥ 4,0 | *mérés alatt* | ⏳ 2026.09.30. |
| C8 | Döntési alap a kiterjesztéshez | Kiterjesztési javaslat | elkészül | *előkészítve* | ⏳ 2026.10.09. |

**A C4–C8 célok nem a projekt kudarcai, hanem szándékosan a mérési szakaszra
esnek.** A projekt a *feltételeket* teremtette meg; a hasznok megjelenése
hónapokat vesz igénybe.

## 3. Ütem — terv és tény

| Mérföldkő | Terv | Tény | Eltérés |
|---|---|---|---:|
| M1 – M10 | 02.02 – 06.30. | 02.02 – 06.30. | **0 nap** |

**Mind a tíz mérföldkő határidőre teljesült.** A részletes bontás és az egyes
mérföldkövek veszélyeztetettsége a *Mérföldkő-riportban* (XYO-CP-308).

### Hol fogyott el a tartalékidő?

| Tartalék | Tervezett | Felhasznált | Maradék |
|---|---:|---:|---:|
| Hibajavítás az UAT után | 9 nap | **9 nap** | **0** |
| A 2. és 3. hullám között | 4 nap | 0 nap | 4 nap |

> **A 9 napos javítási ablak teljesen elfogyott.** Ha az UAT egyetlen további
> kritikus hibát talál, az M7 és — a nulla pufferű kritikus út miatt — az M10
> is csúszott volna. Ez volt a projekt legszűkösebb pontja, és a Steering
> riportokban is így jelentettem.

## 4. Költség — terv és tény

| | Terv | Tény | Eltérés |
|---|---:|---:|---:|
| Költségbázis (részösszeg) | 46 130 000 Ft | 44 640 000 Ft | **−1 490 000 Ft** |
| Tartalékfelhasználás | — | 182 000 Ft | +182 000 Ft |
| **Összesen** | **50 743 000 Ft** | **44 822 000 Ft** | **−5 921 000 Ft** |
| Jóváhagyott keret | 52 000 000 Ft | | |
| **Le nem hívott keret** | | | **7 178 000 Ft (13,8%)** |

**A megtakarítás forrása:**

| Forrás | Összeg |
|---|---:|
| Beszerzési verseny (B1) | 860 000 Ft |
| Beszerzési verseny (B2+B3) | 580 000 Ft |
| Beszerzési verseny (B4 oktatás) | 50 000 Ft |
| **Fel nem használt tartalék** | **4 431 000 Ft** |
| **Összesen** | **5 921 000 Ft** |

> **A megtakarítás nagyobb része (75%) a fel nem használt tartalék.** Ez nem
> érdem, hanem azt jelzi, hogy a 10%-os tartalék ilyen jól előre tervezhető,
> migráció nélküli projektnél **túlzottan óvatos volt**. → Tanulság.

### A tartalék felhasználása

| Dátum | Tétel | Összeg |
|---|---|---:|
| 2026.03.03. | 14 db HDMI–VGA adapter (A7 feltevés megdőlt) | 182 000 Ft |
| 2026.06.17. | Feltételes keret a H-06 kezelésére (VK-04) | 240 000 Ft *(elkülönítve, nem elköltve)* |
| | **Ténylegesen felhasznált** | **182 000 Ft (a tartalék 3,9%-a)** |

## 5. Hatókör — mi változott és milyen döntés alapján

**A jóváhagyott hatókör nem változott.** Mind a 10 szállítandó eredmény
átadásra került.

| | Darab |
|---|---:|
| Benyújtott változáskérelem | 4 |
| Jóváhagyva | 2 (240 000 Ft, 0 nap) |
| Elutasítva | 2 |
| **A baseline-ra gyakorolt teljes hatás** | **240 000 Ft = a költségbázis 0,5%-a** |

**Hatókörön kívülre került kérések:** 4 db (K8–K11), mind dokumentálva a
felmerülés dátumával.

**A legjelentősebb elutasított kérés:** VK-01, a pilot bővítése 65 főre. Az
elutasítás fő szakmai indoka nem a költség volt, hanem hogy **a kör
megváltoztatása a haszonrealizálási mérést tette volna értelmezhetetlenné** —
a T0 baseline 50 főre készült.

## 6. Minőség

| | |
|---|---|
| Átvételi kritériumok | **25/26 megfelelt** |
| UAT tesztesetek | **26/27 = 96,3%** (kilépési feltétel: ≥95%) |
| Nyitott kritikus (S1) hiba | **0** |
| Feltárt hibák összesen | 14 (2 S1, 4 S2, 5 S3, 3 S4) |
| Ebből javítva a zárásig | 10 |
| Nyitva, elfogadott kezeléssel | 4 |

**A nem teljesült kritérium:** AK-19 (30 perces videóhívás mobilneten,
3/5 sikeres). F prioritású követelmény, 2 főt érint, az ok szolgáltatói
lefedettség. Elfogadott kezelési terv, fedezet (240 000 Ft) és határidő
(2026.07.31.) van rá.

**Szállítás közbeni minőségellenőrzés:** 8 ellenőrzés, 3 eltéréssel. Kettő
közülük (QC-02 Autopilot beüzemelési idő, QC-03 hiányzó tápkábelek) az
átvételkor mérföldkövet veszélyeztetett volna.

## 7. Kockázatok és problémák

| | |
|---|---:|
| Nyilvántartott kockázat | 14 |
| Lezárva a projektzárásig | 10 |
| **Bekövetkezett** | **2** (R11, R14) |
| Nyitva a hypercare végéig (07.03.) | 1 (R12) |
| Átadva a mérési szakaszra | 3 (R5, R13, R15) |
| Problémabejegyzés | 13 |
| Ebből lezárva | 10 |
| Eszkaláció | 4, mind válasszal, egyik sem jutott a Steeringig |

### A két bekövetkezett kockázat

| # | Kockázat | Következmény | Miért nem okozott csúszást |
|---|---|---|---|
| R11 | A feltételes hozzáférés kizárja a felhasználókat | 3 tesztelő 1 napig nem tudott belépni | A hiba az UAT első napján, nem az éles működésben derült ki; javítás másnap |
| R14 | A CSP kulcsembere kiesik | 0 nap | A szerződéses helyettesítési kötelezettség (V8) miatt 2 munkanapon belül helyettes állt be |

**Mindkettőt előre azonosítottuk.** Az R14-nél a *szerződéses kikötés* térült
meg; az R11-nél a válaszlépés végrehajtása **rossz környezetben** történt —
ez a projekt legfontosabb tanulsága.

## 8. Nyitva maradt pontok

| # | Nyitott pont | Határidő | Felelős |
|---|---|---|---|
| NY-1 | A hypercare időszak lezárása | 2026.07.03. | Kiss Réka |
| NY-2 | A régi asztali gépek selejtezése (3 feltétel után) | 2026.07.10. | Nagy Péter |
| H-06 | Videóhívás mobilneten (2 fő) — 240 000 Ft elkülönítve | 2026.07.31. | Nagy Péter |
| H-08 | Alkalmazásportál magyar felirata (szavatosság alatt) | 2026.09.30. | Cloudia Solutions |
| NY-5 | A mérési szakasz lebonyolítása | 2026.09.30. | **Nagy Péter** |
| — | Utólagos értékelés (PIR) és kiterjesztési javaslat | 2026.10.09. | Tóth Gergő |
| — | Licenc-megújítás előkészítése | 2027.02.28. | Nagy Péter |

## 9. A mérési szakasz — a projekt folytatása

**A projekt lezárul, de a haszon mérése még 3 hónapig tart.**

| | |
|---|---|
| Időszak | 2026.07.01 – 2026.09.30. |
| **A hasznok gazdája** | **Nagy Péter, IT osztályvezető** (nem a projektmenedzser) |
| Mérési koordinátor | Tóth Gergő |
| Mérőszámok | 12 db, nevesített felelősökkel |
| T0 baseline | **Elvégezve 2026.01.30-án**, a projekt indulása előtt |
| Zárás | PIR és kiterjesztési javaslat, 2026.10.09. |

**A mérési felelősségek írásos átadása 2026.06.30-án megtörtént**, minden
mérőszámhoz nevesített, visszaigazolt felelőssel.

> **A T0 baseline elvégzése volt a projekt egyik legfontosabb korai döntése.**
> Ha a Kezdeményezés fázisban elmarad, most nem lenne mihez hasonlítani a
> szeptemberi méréseket — és a kiterjesztési döntés benyomásokon alapulna.

## 10. Amit a projekt önmagáról állapít meg

### Ami jól ment

| # | Mi | Miért |
|---|---|---|
| 1 | **A beszerzés kizáró feltételei** | A legolcsóbb ajánlat kizárása (D-10) védte meg a projekt céljait egy 1,5 M Ft-os árelőnytől |
| 2 | **A részszállítás kikötése** | Enélkül a tesztelés 05.29. után indulhatott volna; minden mérföldkő csúszott volna |
| 3 | **A szállítás közbeni minőségellenőrzés** | Két, mérföldkövet veszélyeztető hibát talált időben |
| 4 | **A T0 baseline mérés** | A mérési szakasz egyáltalán értelmezhető |
| 5 | **A Service Desk bevonása a tervezésbe** | A fajlagos ticketszám hullámról hullámra csökkent (3,4 → 1,5) |

### Ami rosszul ment

| # | Mi | Következmény |
|---|---|---|
| 1 | **A feltételes hozzáférés jelentés-módja irodai hálózaton futott** | R11 bekövetkezett; 3 tesztelő 1 napig nem tudott dolgozni |
| 2 | **A monitor-kompatibilitást feltételeztük, nem ellenőriztük** | 182 000 Ft váratlan költség; szerencsére a tervezési fázisban derült ki |
| 3 | **Az üzemi tanács kimaradt az érintettek első listájából** | A kick-offon derült ki; időben pótolható volt |
| 4 | **A 10%-os tartalék túlzottan óvatos volt** | 4 431 000 Ft feleslegesen lekötve fél éven át |
| 5 | **Az EVM-hez a költségbázis alkalmatlan volt** | Az első számítás értelmezhetetlen eredményt adott |

**Részletesen:** *Tanulságok naplója (XYO-CP-405)*.

## 11. Elfogadás

| Szerep | Név | Aláírás | Dátum |
|---|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | | 2026.06.29. |
| **Elfogadta** | **Projekt Irányító Bizottság** — elnök: Horváth Júlia | | **2026.06.30.** |
| Szponzor | Kovács Anita, gazdasági igazgató | | 2026.06.30. |
| Szakmai vezető | Nagy Péter, IT osztályvezető | | 2026.06.30. |

**A Projekt Irányító Bizottság a Xyo Cloud Pilot projektet 2026. június 30-án
formálisan lezárta.**

---

> **Kapcsolódó dokumentumok:** bemenete a *Projektalapító okirat*, a
> *Státuszriport*, a *Steering riport*, a *Változásnapló*, a *Kockázati
> riport*, az *EVM-elemzés*, a *Mérföldkő-riport*, az *Eszkalációs napló*, az
> *Átadás-átvételi jegyzőkönyv*, a *Döntésnapló* és a *Minőségellenőrzési
> jegyzőkönyv*; kimenete a *Post-Implementation Review* és a *Kiterjesztési
> javaslat*.
