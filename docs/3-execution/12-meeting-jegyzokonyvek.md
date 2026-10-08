# Meeting jegyzőkönyvek (Meeting Minutes)

**Dokumentum azonosítója:** XYO-CP-212\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Verzió:** 1.0

> **A jegyzőkönyv nem szó szerinti leirat.** A lényeg a **döntések, a nyitott
> kérdések és a felelősök** — ezt a három dolgot keresi benne mindenki.
> **Küldd ki 2 munkanapon belül**: a késve kiküldött jegyzőkönyvet senki nem
> korrigálja, mert már nem emlékszik, és így hibás emlék rögzül.

---

## 1. Jegyzőkönyv-nyilvántartás

| Típus | Gyakoriság | Darab | Ki vezeti |
|---|---|---:|---|
| Heti előrehaladási megbeszélés | keddenként | 16 | Tóth Gergő |
| Steering Committee ülés | havonta | 5 | Tóth Gergő |
| Szállítói projektstátusz | kéthetente | 8 | Molnár Katalin |
| Kockázat-felülvizsgálat | kéthetente | 8 | Tóth Gergő |
| Napi hibaáttekintés (UAT alatt) | naponta | 10 | Nagy Péter |
| Tesztelői visszajelző kör | hetente (UAT) | 2 | Nagy Péter |
| Eseti (ajánlatbontás, átadás, workshopok) | — | 6 | változó |
| **Összesen** | | **55** | |

Az összes jegyzőkönyv a SharePointon: *Projektek / Xyo Cloud Pilot / jegyzokonyvek*.

---

## 2. Minta — Heti előrehaladási megbeszélés

**Sorszám:** HE-09\
**Időpont:** 2026. május 12., kedd, 9:00 – 9:35\
**Helyszín:** Teams\
**Levezette:** Tóth Gergő

### Jelenlét

| Jelen | Hiányzott |
|---|---|
| Tóth Gergő (PM) | — |
| Nagy Péter (IT osztályvezető) | |
| Szabó Márk (rendszergazda) | |
| Kiss Réka (Service Desk) | |
| Cloudia Solutions projektvezetője | |

### Mi készült el a múlt héten

| WBS | Munkacsomag | Állapot |
|---|---|---|
| 6.2 | Technikai teszt (10 gép) | ✔ lezárva 05.08. |
| 3.3.2 | Mentés, visszaállítási teszt | ✔ lezárva 05.08., 42 perc mért visszaállítási idő |
| 7.1 | Első hullám élesben — 10 fő | ✔ lezárva 05.13. (folyamatban a megbeszéléskor) |
| — | M5 mérföldkő | ✔ **teljesült 05.08-án, határidőre** |

### Mi jön a jövő héten

| WBS | Munkacsomag | Határidő |
|---|---|---|
| 6.3 | UAT — 1. hét | 05.22. |
| 5.1 | Oktatási anyag és gyorssegédlet | 05.15. |
| 3.5 | As-built dokumentáció — folyamatos | 06.19. |

### Mi akadt el

| # | Akadály | Bejelentette | Intézkedés |
|---|---|---|---|
| 1 | **3 tesztelő nem tud belépni otthonról** (P-05) | Nagy Péter | A CA-05 feltételes hozzáférési szabály zárja ki őket a mobilszolgáltatói IP miatt. **Szabó Márk ma átállítja** megbízható eszköz + MFA kombinációra. |
| 2 | **A bérszámfejtő rendszer nem érhető el VPN-en** (P-04) | 2 tesztelő | A VPN útvonaltáblából hiányzik a 10.10.5.20 cím. Szabó Márk 05.13-ig javítja. |
| 3 | Az Autopilot beüzemelés 2,1 óra a célzott 1,5 helyett (P-06) | Szabó Márk | A Cloudia megvizsgálja az alkalmazáscsomagok telepítési módját. Válasz: 05.15. |

### Döntések

| # | Döntés | Ki | Hivatkozás |
|---|---|---|---|
| 1 | A CA-05 szabály átalakítása országkorlátozásról megbízható eszköz + MFA kombinációra | Nagy Péter, dr. Fekete Zsolt véleményével | **D-14** |

### Nyitott kérdések

| # | Kérdés | Felelős | Határidő |
|---|---|---|---|
| 1 | Az Autopilot beüzemelési idő csökkentésének módja | Cloudia Solutions | 2026.05.15. |
| 2 | A hypercare kapacitásbecslés véglegesítése | Kiss Réka | 2026.05.20. |

### Egyéb

Kiss Réka jelezte, hogy az első hullám élesítésének napján 34 ticket érkezett
(10 fő), ami a becsültnél magasabb. A többség „hova mentsem?" típusú kérdés —
javasolja, hogy ez kerüljön be a gyorssegédletbe. **Elfogadva**, Tóth Gergő
egyezteti a szállítóval.

*Kiküldve: 2026.05.13. Észrevételi határidő: 05.15. Észrevétel nem érkezett.*

---

## 3. Minta — Steering Committee ülés

**Sorszám:** SC-04\
**Időpont:** 2026. június 3., szerda, 14:00 – 15:00\
**Helyszín:** Xyo Kft., nagytárgyaló

### Jelenlét

| Név | Szerep |
|---|---|
| Horváth Júlia | ügyvezető, elnök |
| Kovács Anita | gazdasági igazgató, szponzor |
| Nagy Péter | IT osztályvezető |
| Varga Eszter | HR vezető |
| Tóth Gergő | projektmenedzser (előterjesztő) |

### 1. Státusz

| Terület | Állapot | Megjegyzés |
|---|---|---|
| Ütem | 🟢 zöld | M5 és M6 határidőre; a 2. hullám 06.03–05. között indul |
| Költség | 🟢 zöld | Szerződött érték 42 240 000 Ft (B1–B4), **1 490 000 Ft-tal a terv alatt** |
| Hatókör | 🟢 zöld | Változatlan; 4 hatókörön kívüli kérés (K8–K11) dokumentálva |
| Kockázat | 🟡 sárga | R11 bekövetkezett és kezelve; R12 (Service Desk kapacitás) aktív |

### 2. Döntést igénylő kérdések

#### VK-01 — A pilot bővítése 50 → 65 főre

| | |
|---|---|
| Benyújtó | Papp Zsófia, területvezető (Logisztika), 2026.05.19. |
| Indok | A logisztikai csapatból további 15 fő szeretne bekapcsolódni |
| Hatásvizsgálat | +8 325 000 Ft egyszeri, +2 304 000 Ft/év folyó; **+3 hét ütem** — az M7 és M10 is tolódik |
| Fedezet | **Nincs.** Tartalék 4 431 000 Ft + keretmozgástér 1 257 000 Ft + beszerzési megtakarítás 1 490 000 Ft = 7 178 000 Ft < 8 325 000 Ft (hiány: 1 147 000 Ft) |
| Korlátsértés | L1 (2026.06.30. határidő), L2 (keret), L4 (50 fő) |
| PM javaslata | **Elutasítás.** Alternatíva: a 15 fő a kiterjesztési szakasz első hullámába kerül |

**Döntés:** a Bizottság a projektmenedzser javaslatát **elfogadta, a kérelmet
elutasítja** (D-19). Horváth Júlia kérte, hogy Papp Zsófia személyes
tájékoztatást kapjon az indokokról és a kiterjesztési perspektíváról.

### 3. Eszkalált problémák

Nincs nyitott eszkaláció. A P-05 (feltételes hozzáférés) eszkalációja
2026.05.11-én megtörtént, és másnap lezárult.

### 4. A következő időszak mérföldkövei

| Mérföldkő | Dátum |
|---|---|
| M7 — teljes 50 fő élesben | 2026.06.12. |
| M8 — UAT lezárva, átvétel aláírva | 2026.06.19. |
| M9 — üzemeltetésbe adás | 2026.06.26. |
| M10 — projekt lezárva | 2026.06.30. |

### 5. Egyéb

Kovács Anita kérdezte, mi lesz a **2. évtől jelentkező 10 680 000 Ft/év folyó
költséggel**. Tóth Gergő: a projektzárás feltétele, hogy ez nevesített gazdához
kerüljön az IT üzemeltetési keretben; a pénzügyi zárás tartalmazza. Balogh
Tamás felelős, határidő 2026.06.30.

*Kiküldve: 2026.06.04.*

---

## 4. Minta — Napi hibaáttekintés az UAT alatt

**Sorszám:** UAT-D03\
**Időpont:** 2026. május 13., szerda, 16:00 – 16:15\
**Résztvevők:** Nagy Péter, Szabó Márk, Kiss Réka

| # | Hiba | Szint | Állapot | Következő lépés |
|---|---|:-:|---|---|
| H-01 | Bérszámfejtő rendszer VPN-en | S1 | **javítva ma** | Újratesztelés 06.03. |
| H-02 | 3 tesztelő nem tud belépni | S1 | **javítva tegnap** | 05.13–22. figyelés |
| H-05 | Autopilot beüzemelés 2,1 óra | S2 | vizsgálat alatt | Cloudia válasza 05.15. |
| H-07 | OneDrive első szinkronizálás lassú | S3 | új bejelentés | Szabó Márk megvizsgálja |

**Napi ticketszám:** 11 db (kumulált az 1. hullámnál: 34)\
**Megjegyzés:** Kiss Réka szerint a ticketek 60%-a „hova mentsem" jellegű.

*A 15 perces formátum bevált: a hibák egy napon belül gazdát kapnak.*

---

## 5. Amit a jegyzőkönyvezésről megtanultunk

| Megfigyelés | Következmény |
|---|---|
| A **napi 15 perces** hibaáttekintés az UAT alatt hatékonyabb volt, mint a heti hosszú kör | Az Execution végén is megtartottuk a hypercare-ig |
| A heti megbeszélés **30 percben** tartható, ha három kérdésre szorítkozik | „Mi kész, mi jön, mi akadt el" |
| A **Steering riportot 1 oldalban** kérték — a hosszabb anyagot nem olvasták el | Az ülés előtt 3 munkanappal, egy oldalon |
| A jegyzőkönyv **2 munkanapon belüli** kiküldése bevált | 55 jegyzőkönyvből 53-nál teljesült |

---

> **Kapcsolódó dokumentumok:** kimenete a *Döntésnapló* és a *Státuszriport*.
