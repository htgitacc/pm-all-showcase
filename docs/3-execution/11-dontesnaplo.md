# Döntésnapló (Decision Log)

**Dokumentum azonosítója:** XYO-CP-211\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Utolsó frissítés:** 2026. június 19.\
**Verzió:** 1.8 — **élő dokumentum**

> **Három hónap múlva senki nem fog emlékezni, ki mit engedélyezett.**
> Ez az egyik legerősebb védőirat a projektmenedzser kezében: rögzíti, **ki,
> mikor, mit döntött és milyen alapon**.
>
> **A folyosón vagy chatben született döntést is vezesd be.** Éppen azok a
> döntések a legveszélyesebbek, amelyekről nem készült jegyzőkönyv.

---

| # | Tárgy | Döntés | Döntéshozó | Dátum | Hol dokumentált |
|---|---|---|---|---|---|
| D-01 | Az üzemi tanácsot fel kell venni az érintettek közé | Igen, formális egyeztetés a tervezési fázisban | Tóth Gergő, Varga Eszter egyetértésével | 2026.02.09. | Kick-off jkv. |
| D-02 | A pilot kijelölési szempontrendszerének kommunikálása | A névsor **előtt** kommunikáljuk a teljes szervezetnek | Kovács Anita | 2026.02.09. | Kick-off jkv. |
| D-03 | A régi fájlszerver hozzáférési igényének felmérése | Fel kell mérni, és a tervezésbe beépíteni | Nagy Péter | 2026.02.09. | Kick-off jkv. |
| D-04 | A B2 és B3 beszerzési tétel összevonása | Egy eljárásban kezeljük — ugyanaz a partner végzi | Molnár Katalin | 2026.02.24. | Beszerzési terv |
| D-05 | A bevezetési szerződés típusa | **Átalánydíjas (fix price)**, nem óradíjas | Kovács Anita | 2026.02.27. | Beszerzési terv 5. pont |
| D-06 | A 3 csapat régi fájlszerver-hozzáférése | **Olvasási** hozzáférés VPN-en, nem adatmigráció | Nagy Péter | 2026.03.05. | Hatókör-nyilatkozat K8, K17 követelmény |
| **D-07** | **14 db HDMI–VGA adapter beszerzése** | Jóváhagyva, 182 000 Ft a tartalékkeretből | **Tóth Gergő**, PM-hatáskörben (≤1 M Ft) | 2026.03.03. | Költségvetés 4. pont |
| D-08 | Az UAT tesztcsoport összetétele | 2 kevésbé IT-affin munkatárs kötelezően bekerül | Nagy Péter, Fodor Gábor | 2026.03.09. | Tesztterv 4. pont |
| D-09 | A szállítóértékelési súlyok | Az ár súlya B2+B3-nál 35%, nem 50% | Projekt Irányító Bizottság | 2026.03.13. | Szállítóértékelési szempontrendszer |
| **D-10** | **A NovaComp Kft. ajánlatának kizárása** | **Kizárva** (X3 — nem vállalja az Autopilot-regisztrációt), érdemi értékelés nélkül, annak ellenére, hogy ez volt a legolcsóbb ajánlat | **Értékelő bizottság, egyhangúlag** | 2026.04.02. | Ajánlat-összehasonlítás 3. pont |
| D-11 | A nyertes ajánlattevők | TechLine Zrt. (B1), Cloudia Solutions Kft. (B2+B3) | Horváth Júlia, ügyvezető | 2026.04.16. | Ajánlat-összehasonlítás 7. pont |
| D-12 | A kiesett CSP-konzultáns helyettesítése | A felajánlott helyettes elfogadva | Nagy Péter | 2026.04.28. | Problémanapló P-02 |
| D-13 | A jelszóházirend-ütközés kezelése | A pilot csak felhő azonosítást használ; a helyi AD-házirend nem érvényes rá | Nagy Péter | 2026.04.23. | Problémanapló P-01 |
| **D-14** | **A CA-05 feltételes hozzáférési szabály átalakítása** | Az országkorlátozás helyett **megbízható eszköz + MFA**. Indok: a mobilszolgáltatói CGNAT külföldi IP-t ad, ami valós felhasználókat zár ki | **Nagy Péter**, dr. Fekete Zsolt véleményével | 2026.05.12. | As-built 2.3, Problémanapló P-05 |
| D-15 | Az ügyviteli kliens telepítési módja | Kötelező helyett **opcionális**, a portálról telepíthető. Indok: a beüzemelési idő 2,1 óráról 1,4 órára csökken | Szabó Márk, Nagy Péter jóváhagyásával | 2026.05.19. | Problémanapló P-06 |
| D-16 | `CP-Kozos` csapatoldal létrehozása | Jóváhagyva, az UAT visszajelzései alapján | Nagy Péter | 2026.05.20. | Problémanapló P-10 |
| D-17 | Az OneDrive előszinkronizálás bevezetése | A kiosztás előtt, céges hálózaton, a 2. hullámtól | Szabó Márk | 2026.05.26. | Problémanapló P-09 |
| **D-18** | **A 2. részszállítás átvétele 12 db hiányzó tápkábellel** | **Fenntartással átvéve**, tételes hiánylistával; a 80%-os fizetési részlet a pótlásig visszatartva | **Nagy Péter**, Tóth Gergő javaslatára | 2026.05.28. | Teljesítésigazolás 2. sz. jkv., Problémanapló P-08 |
| D-19 | A pilot bővítése 50 → 65 főre (VK-01) | **Elutasítva.** Indok: a 8 325 000 Ft egyszeri költségre a fedezet 1 147 000 Ft-tal hiányzik, a 2026.06.30-i határidő (L1 korlát) nem tartható, és a 65 fős kör a T0 baseline-ra épülő mérést értelmezhetetlenné tenné | Projekt Irányító Bizottság | 2026.06.03. | Változásnapló VK-01 |
| D-20 | Hypercare +1 Service Desk munkatárs (VK-02) | **Jóváhagyva.** Belső átcsoportosítás, nincs költséghatás. Az R12 kockázat kezelése | Nagy Péter | 2026.06.01. | Változásnapló VK-02 |
| D-21 | Monitorcsere az adapteres 14 főnél (VK-03) | **Elutasítva.** Az adapterek működnek; a csere +910 000 Ft indokolatlan | Tóth Gergő, PM-hatáskörben | 2026.06.03. | Változásnapló VK-03 |
| D-22 | Feltételes keret a H-06 kezelésére (VK-04) | **Jóváhagyva feltételesen.** 240 000 Ft elkülönítve a tartalékból; felhasználás csak akkor, ha a mobilszolgáltatói egyeztetés 2026.07.31-ig nem hoz eredményt | Tóth Gergő, PM-hatáskörben (≤1 M Ft) | 2026.06.17. | Változásnapló VK-04 |
| **D-23** | **Az UAT elfogadása az AK-19 nem teljesülése ellenére** | **Elfogadva.** A kritérium F prioritású, 2 főt érint, az ok szolgáltatói lefedettség — nem a megoldás hibája. Elfogadott kezelési terv és határidő (2026.07.31.) | **Fodor Gábor** (felhasználói képviselő) és **Nagy Péter** | 2026.06.19. | UAT-elfogadás 4. pont |

---

## Kiemelt döntések magyarázata

### D-10 — A legolcsóbb ajánlat kizárása

Ez volt a projekt legkényesebb döntése. A NovaComp Kft. **1 550 000 Ft-tal
olcsóbb** ajánlatot adott a nyertesnél, és mégis kizártuk.

**Miért volt védhető a döntés?**

1. Az Autopilot-vállalás **kizáró feltétel** volt, nem pontozandó szempont —
   és ezt **2026.03.13-án, az ajánlatok beérkezése előtt** hagyta jóvá a
   Steering Committee.
2. A kizárás oka az ajánlat saját szövegéből idézhető.
3. A bizottság egyhangúlag döntött, jegyzőkönyvvel.

> Ha a szempontrendszert az ajánlatok ismeretében alakítottuk volna ki, ez a
> döntés megtámadható lett volna — és a felelősség a bizottságé, benne a
> projektmenedzseré.

### D-14 — Egy biztonsági szabály lazítása

Ez a döntés **biztonsági szintet csökkentett** (az országkorlátozás megszűnt),
ezért nem hozhatta meg a projektmenedzser egyedül.

- A döntést **Nagy Péter** hozta, a szakmai vezető.
- **dr. Fekete Zsolt (DPO) véleményét kikértük**, mivel adatvédelmi
  vonatkozása van.
- A helyettesítő védelem (megbízható eszköz + MFA + kockázatalapú
  újrahitelesítés) dokumentálva van az as-built 2.3 pontjában.

> **A biztonsági szintet érintő döntést soha ne hozd meg egyedül**, még akkor
> sem, ha az összeg a hatáskörödben van. Az összeghatár nem minden.

### D-18 — Fenntartással történő átvétel

A projektmenedzser javaslata volt, hogy **ne tagadjuk meg az átvételt**, hanem
fenntartással vegyük át:

| Ha megtagadjuk | Ha fenntartással átvesszük |
|---|---|
| A 28 használható készlet is a raktárban marad | 28 készlet azonnal kiosztható |
| A 3. hullám (06.10.) biztosan csúszik | A 3. hullám tartható |
| Kötbér-vita indul | A fizetés visszatartása elég nyomás |

A döntést **Nagy Péter** hozta meg, mert a teljesítésigazolás szakmai
felelőssége az övé (RACI).

---

## Statisztika

| | |
|---|---:|
| **Összes döntés** | **23** |
| Projektmenedzser, saját hatáskörben | 4 (D-01, D-07, D-21, D-22) |
| Szakmai vezető (Nagy Péter — egyedül, társdöntéshozóként vagy jóváhagyóként) | 11 (D-03, D-06, D-08, D-12, D-13, D-14, D-15, D-16, D-18, D-20, D-23) |
| Szponzor / ügyvezető | 3 (D-02, D-05, D-11) |
| Projekt Irányító Bizottság | 2 (D-09, D-19) |
| Egyéb (beszerzési vezető, értékelő bizottság, rendszergazda) | 3 (D-04, D-10, D-17) |
| Elutasított változáskérelem | 2 (D-19, D-21) |
| Feltételesen jóváhagyott változáskérelem | 1 (D-22) |

> **A döntéshozó szerinti sorok összege kiadja az összes döntést
> (4 + 11 + 3 + 2 + 3 = 23)** — így ellenőrizhető, hogy egy döntés sem maradt
> ki, és egy sem szerepel kétszer. A D-18 a szakmai vezető sorában van, nem a
> PM-ében: a projektmenedzser *javasolta*, de **a javaslat nem döntés**.
> A baseline jóváhagyása (M3, 2026.03.13.) nem a Döntésnapló bejegyzése, ezért
> a statisztikában sem szerepel: amit a napló nem tartalmaz, azt az összesítő
> sem számolhatja.

---

> **Kapcsolódó dokumentumok:** bemenete a *Kick-off jegyzőkönyv* és a
> *Meeting jegyzőkönyvek*; kimenete a *Projektzáró jelentés* és a
> *Tanulságok naplója*.
