# Vezetői (Steering) riport

**Dokumentum azonosítója:** XYO-CP-302\
**Projekt:** Xyo Cloud Pilot\
**Készíti:** Tóth Gergő, projektmenedzser\
**Címzett:** Projekt Irányító Bizottság\
**Kiküldés:** az ülés előtt 3 munkanappal

> **Ez nem hosszabb státuszriport, hanem döntéselőkészítő anyag.** A vezetőt az
> érdekli, **mit kell eldöntenie és mi a te javaslatod**.
> **Egy oldal.** Ha kettő, a második oldalt nem olvassák el — és pont a
> döntési kérdéseid maradnak ki.

---

# SC-04 riport — 2026. június 3-i ülésre

*(Kiküldve: 2026. május 29.)*

## 1. Státusz egy pillantásra

| Terület | Állapot | Egy mondatban |
|---|:-:|---|
| **Ütem** | 🟢 | Minden mérföldkő határidőre; a 2. hullám 06.03-án indul |
| **Költség** | 🟢 | 44 822 000 Ft előrejelzés az 52 000 000 Ft-os kerethez képest |
| **Hatókör** | 🟢 | Változatlan; 4 hatókörön kívüli kérés dokumentálva |
| **Kockázat** | 🟡 | R11 bekövetkezett és lezárva; R12 (Service Desk kapacitás) aktív |

## 2. Számok

| | Terv | Tény / előrejelzés | Eltérés |
|---|---:|---:|---:|
| M7 — teljes 50 fő élesben | 2026.06.12. | 2026.06.12. | 0 nap |
| M10 — projekt lezárva | 2026.06.30. | 2026.06.30. | 0 nap |
| Költségbázis | 46 130 000 Ft | 44 822 000 Ft | **−1 308 000 Ft** |
| Tartalék felhasználva | — | 182 000 Ft (4%) | — |
| Élesített felhasználók | 50 | 10 (05.13.) → 30 (06.05.) → 50 (06.12.) | ütem szerint |
| Ütemhatékonyság (SPI, 05.29.) | 1,00 | **0,98** | −2% |
| Költséghatékonyság (CPI) | 1,00 | **1,03** | +3% |

## 3. **Döntést igénylő kérdés — VK-01**

### A pilot bővítése 50 → 65 főre

| | |
|---|---|
| **Kéri** | Papp Zsófia, területvezető (Logisztika), 2026.05.19. |
| **Indok** | A logisztikai csapatból további 15 fő szeretne bekapcsolódni |
| **Költséghatás** | **+8 325 000 Ft** egyszeri, **+2 304 000 Ft/év** folyó |
| **Ütemhatás** | **+3 hét** — az M7 és az M10 mérföldkő is tolódik |
| **Fedezet** | **Nincs.** Elérhető: tartalék 4 431 000 + keretmozgástér 1 257 000 + beszerzési megtakarítás 1 490 000 = **7 178 000 Ft < 8 325 000 Ft** |
| **Korlátsértés** | L1 (2026.06.30. határidő), L2 (keret), L4 (50 fő) |
| **Kockázat** | R1 (szállítás) és R4 (belső kapacitás) is súlyosbodna |

**A projektmenedzser javaslata: ELUTASÍTÁS.**

**Alternatíva:** a 15 fő legyen a kiterjesztési szakasz első hulláma. Ehhez az
utólagos értékelés (PIR, 2026.10.09.) ad döntési alapot, és akkor már a pilot
tapasztalataival, olcsóbban és biztonságosabban vihető végig.

> **Kérem, hogy a döntésről Papp Zsófia személyes tájékoztatást kapjon** — a
> kérése szakmailag indokolt volt, csak a keret és a határidő nem engedi.

## 4. Eszkalált problémák

Nincs döntést igénylő nyitott eszkaláció. Az E-04 figyelmeztető jelzés: a
05.29-i visszajelzés szerint a javítási ablakba tartozó hibák javítva, az M7
tartható; a jelzést a javítási ablak végén (06.02.) zárom le.

| # | Eszkaláció | Mikor | Lezárva |
|---|---|---|---|
| E-01 | A home office szabályzat hatályba lépése | 04.10. | 04.28., hatályba lépett |
| E-02 | A belső jóváhagyási kör csúszni látszik | 04.13. | 04.16., csúszás nélkül |
| E-03 | 3 felhasználó nem tud belépni (S1) | 05.11. | 05.12. |
| E-04 | A hibajavítási ablak szűkössége *(figyelmeztető jelzés)* | 05.26. | **nyitva** — 06.02-ig |

## 5. Kockázatok, amikről tudni érdemes

| # | Kockázat | Besorolás | Trend | Mi történik vele |
|---|---|:-:|:-:|---|
| R12 | Service Desk kapacitás a hypercare alatt | 4 | ↑ | **VK-02** kérelem: +1 fő átcsoportosítása 3 hétre, nincs költséghatás |
| R6 | Az UAT több kritikus hibát talál a tervezettnél | 6 | ↑ | 05.13-án 4 → 6 (2 S1 hiba az első napon); a javítási ablak 06.02-ig — lásd E-04 |
| R5 | Felhasználói ellenállás, alacsony adaptáció | 6 | → | Az adaptációs mutatót a hypercare alatt hetente mérjük |
| R4 | Belső kapacitáshiány | 6 | → | A szállítói oldal a terv szerint halad; a belső terhelés a 2–3. hullám után csökken |
| R1 | Laptopszállítás csúszik | 6 | ↓ | Mind a 40 gép 05.28-án megérkezett, 1 nappal a határidő előtt; a 12 hiányzó tápkábel pótlása után (vállalva 06.03-ig) lezárom |

## 6. A következő időszak

| Mérföldkő | Dátum |
|---|---|
| M7 — teljes 50 fő élesben | 2026.06.12. |
| M8 — UAT lezárva, átvétel aláírva | 2026.06.19. |
| M9 — üzemeltetésbe adás | 2026.06.26. |
| M10 — projekt lezárva | 2026.06.30. |
| PIR — utólagos értékelés | 2026.10.09. |

## 7. Amit a Bizottságnak érdemes tudnia

**A 2. évtől jelentkező folyó költség 10 680 000 Ft/év** (licenc, Azure, VPN,
mobilinternet). Ennek **nevesített gazdát kell találni az IT üzemeltetési
keretben a projektzárásig** — ez a zárás feltétele. Felelős: Balogh Tamás,
határidő: 2026.06.30.

---

*Terjedelem: 1 oldal. Melléklet nincs — a részletek a heti státuszriportokban
és a projektdokumentumokban elérhetők a SharePointon.*

---

## Az ülés eredménye *(utólag kiegészítve)*

| # | Napirendi pont | Döntés | Hivatkozás |
|---|---|---|---|
| VK-01 | Pilot bővítése 65 főre | **Elutasítva**, a PM javaslata szerint | D-19 |
| — | Papp Zsófia tájékoztatása | Horváth Júlia kérésére megtörtént 06.05-én | — |
| — | Folyó költség gazdája | Balogh Tamás vállalta, határidő 06.30. | — |

---

## Amit a Steering riportról megtanultunk

| Megfigyelés | Következmény |
|---|---|
| A **döntési kérdés a 3. pontban van**, nem a végén | Ha a végére teszed, odáig nem jutnak el |
| Minden döntési kérdéshez **javaslat és alternatíva** tartozik | A vezetők döntéselőkészítést várnak, nem tanácstalanságot |
| A fedezet-számítás **tételesen** szerepel | Így nem lehet azt mondani, hogy „biztos kigazdálkodható" |
| Az **1 oldalas terjedelmet 5 riportból 5-ször** tartottuk | Ez a legfontosabb formai szabály |
| A riport a **trendet** mutatja (↑ ↓ →), nem csak az állapotot | Ez mondja meg, mi felé tartunk |

> **Egy dolgot nem érdemes megtenni:** a rossz hírt a riport végére rejteni.
> Az SC-04-nél az R12 kockázat és a VK-02 kérelem is előre került — így az
> ülésen nem meglepetés volt, hanem tudomásulvétel.

---

> **Kapcsolódó dokumentumok:** bemenete a *Státuszriport*, a
> *Kommunikációs terv*, a *Változásnapló* és a *Kockázati riport*; kimenete a
> *Döntésnapló* és a *Projektzáró jelentés*.
