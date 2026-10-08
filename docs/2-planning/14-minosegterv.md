# Minőségterv és átvételi kritériumok (Quality Plan and Acceptance Criteria)

**Dokumentum azonosítója:** XYO-CP-114\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Jóváhagyta:** Nagy Péter (szakmai vezető, 2026.03.11.), Fodor Gábor (felhasználói képviselő, 2026.03.12.)\
**Verzió:** 1.1

> **Minden kritérium igen/nem eldönthető.** A „gyorsan induljon el a gép" nem
> kritérium; a „bekapcsolástól bejelentkezésig legfeljebb 90 másodperc" az.
> Ha nem tudod eldönteni, teljesült-e, akkor az átvétel vitába fullad.

---

## 1. Átvételi kritériumok

### 1.1 Azonosítás és hozzáférés

| # | Kritérium | Mérés módja | Ki ellenőrzi | Mikor |
|---|---|---|---|---|
| **AK-01** | Mind az 50 kijelölt felhasználó sikeresen belép Entra ID azonosítóval | Entra ID bejelentkezési napló: 50/50 sikeres belépés | Szabó Márk | M7 |
| **AK-02** | MFA-lefedettség a pilot körben **100%** | Entra ID hitelesítési riport | Szabó Márk | M7 |
| **AK-03** | A break-glass fiók dokumentált és tesztelt | Írásos teszteredmény | Szabó Márk | M5 |
| **AK-04** | Elveszett eszköz esetén a hozzáférés 15 percen belül visszavonható | Teszt egy próbaeszközön, időméréssel | Szabó Márk | M5 |
| **AK-05** | Önkiszolgáló jelszó-visszaállítás működik | 5 felhasználó sikeresen visszaállítja a jelszavát | Kiss Réka | M6 |

### 1.2 Eszköz és beüzemelés

| # | Kritérium | Mérés módja | Ki ellenőrzi | Mikor |
|---|---|---|---|---|
| **AK-06** | Egy új gép beüzemelése Autopilottal **≤ 1,5 óra** | 5 gépen mérve, Intune napló, átlag | Szabó Márk | M6 |
| **AK-07** | Bekapcsolástól bejelentkezésig **≤ 90 másodperc** | 10 gépen mérve, átlag | Szabó Márk | M6 |
| **AK-08** | Mind az 50 gépen aktív a lemeztitkosítás, a kulcs központilag mentve | Intune megfelelőségi riport: 50/50 | Szabó Márk | M7 |
| **AK-09** | Az alapszoftverek és a biztonsági frissítések automatikusan települnek | Intune alkalmazástelepítési és frissítési (`CP-Update-Ring`) riport: 50/50 | Szabó Márk | M7 |
| **AK-10** | Az eszközfelügyeleti profil nem tartalmaz magánhasználati adatgyűjtést | A profil beállításainak tételes átnézése | dr. Fekete Zsolt | M5 |
| **AK-11** | Minden gép csatlakoztatható az otthoni monitorhoz | 50/50 kiosztási jegyzőkönyv (adapterrel, ahol kell) | Szabó Márk | M7 |

### 1.3 Fájlkezelés

| # | Kritérium | Mérés módja | Ki ellenőrzi | Mikor |
|---|---|---|---|---|
| **AK-12** | Minden felhasználó eléri a saját OneDrive tárhelyét | UAT teszteset T-13: 50/50 | Nagy Péter | M7 |
| **AK-13** | Minden csapat eléri a saját SharePoint oldalát, és csak azt | Jogosultsági teszt: 6 csapat × 2 ellenőrzés | Nagy Péter | M5 |
| **AK-14** | Törölt fájl **legalább 30 napig** visszaállítható | Beállítás ellenőrzése + 1 gyakorlati visszaállítás | Szabó Márk | M5 |
| **AK-15** | Egy teljes könyvtár visszaállítása sikeres, dokumentált időigénnyel | Visszaállítási teszt jegyzőkönyve | Szabó Márk | M5 |
| **AK-16** | 3 csapat olvasási hozzáférése a régi fájlszerverhez működik VPN-en | UAT teszteset T-17 | Nagy Péter | M6 |

### 1.4 Távoli munkavégzés

| # | Kritérium | Mérés módja | Ki ellenőrzi | Mikor |
|---|---|---|---|---|
| **AK-17** | VPN-kapcsolat felépül otthoni mobilinternetről | 10 UAT-résztvevő otthonról, 10/10 sikeres | Nagy Péter | M6 |
| **AK-18** | A 2 belső rendszer elérhető VPN-en keresztül | UAT teszteset T-21 | Nagy Péter | M6 |
| **AK-19** | Videóhívás mobilneten: 30 perces hívás megszakadás nélkül | 5 UAT-résztvevő, 5/5 sikeres | Varga Eszter | M6 |

### 1.5 Felkészítés és támogatás

| # | Kritérium | Mérés módja | Ki ellenőrzi | Mikor |
|---|---|---|---|---|
| **AK-20** | Mind az 50 felhasználó részt vett oktatáson | Jelenléti ívek, a pótlásokkal együtt: 50/50 | Varga Eszter | M7 |
| **AK-21** | A gyorssegédlet elkészült, magyarul, képernyőképekkel | Nagy Péter átvételi nyilatkozata | Nagy Péter | M6 |
| **AK-22** | A Service Desk megkapta a hibakezelési útmutatót **legalább 2 héttel** az első élesítés előtt | Átvételi dátum: legkésőbb 2026.04.27. | Kiss Réka | M5 |
| **AK-23** | Az as-built dokumentáció alapján az üzemeltetés át tudja venni | Nagy Péter írásos nyilatkozata | Nagy Péter | M9 |

### 1.6 Teszt

| # | Kritérium | Mérés módja | Ki ellenőrzi | Mikor |
|---|---|---|---|---|
| **AK-24** | Az UAT tesztesetek **≥ 95%-a** megfelelt | Tesztjegyzőkönyv | Nagy Péter | M8 |
| **AK-25** | **Nincs nyitott kritikus (S1) hiba** | Hibalista | Nagy Péter | M8 |
| **AK-26** | A nyitott S2 hibákhoz elfogadott javítási határidő tartozik | Aláírt hibalista | Tóth Gergő | M8 |

---

## 2. Hibák súlyossági kategóriái

| Szint | Megnevezés | Definíció | Kezelés | Blokkolja az átvételt? |
|---|---|---|---|:-:|
| **S1** | Kritikus | A felhasználó nem tud dolgozni; nincs megkerülő megoldás. Vagy: adatvesztés, biztonsági rés. | Azonnali javítás, 1 munkanapon belül | **igen** |
| **S2** | Súlyos | Lényeges funkció nem működik, de van megkerülő megoldás | Javítás 5 munkanapon belül vagy elfogadott határidővel | nem, ha van elfogadott határidő |
| **S3** | Zavaró | Kényelmetlen, de a munkát nem akadályozza | Javítás a hypercare alatt vagy az üzemeltetésnek átadva | nem |
| **S4** | Kozmetikai | Megjelenés, elírás, apró kényelmetlenség | Igény szerint | nem |

**Példák a Xyo projektből:**

| Hiba | Szint | Miért |
|---|:-:|---|
| A felhasználó nem tud belépni MFA-val | S1 | Nem tud dolgozni, nincs megkerülés |
| A VPN-en a bérszámfejtő rendszer nem érhető el | S1 | Nincs megkerülő megoldás otthonról |
| A SharePoint keresés lassú (>10 mp) | S2 | Van megkerülés: mappában navigálás |
| A gyorssegédlet 3. képernyőképe elavult | S4 | Kozmetikai |
| A dokkoló nem tölti a laptopot, csak külön tápról | S2 | Van megkerülés, de zavaró |

## 3. Minőségellenőrzés a szállítás során

**Nem csak az átvételkor ellenőrzünk** — az akkor talált hiba a legdrágább.

| Mit | Mikor | Ki | Mit dokumentálunk |
|---|---|---|---|
| Entra ID és MFA konfiguráció | 05.06. | Szabó Márk | Minőségellenőrzési jegyzőkönyv |
| Intune profilok és Autopilot | 05.08. | Szabó Márk | Minőségellenőrzési jegyzőkönyv |
| SharePoint jogosultsági modell | 05.04. | Nagy Péter | Minőségellenőrzési jegyzőkönyv |
| Mentés és visszaállítás | 05.08. | Szabó Márk | Visszaállítási teszt jegyzőkönyve |
| Hardver mennyiségi és minőségi átvétel | részszállításonként | Szabó Márk | Átvételi jegyzőkönyv |
| As-built dokumentáció készültsége | kéthetente | Tóth Gergő | Státuszriport |

> **Az eredményt akkor is írd le, ha rendben volt.** A „nem találtunk hibát"
> is bizonyíték arra, hogy megnézted.

## 4. Az átvétel menete

| Lépés | Mikor | Ki |
|---|---|---|
| 1. Az UAT lezárása, tesztjegyzőkönyv elkészítése | 06.17. | Nagy Péter |
| 2. Az átvételi kritériumok **egyenkénti** végigvezetése | 06.18. | Tóth Gergő + Nagy Péter |
| 3. A nyitott hibák besorolása és a javítási határidők egyeztetése | 06.18. | Nagy Péter, Kiss Réka |
| 4. UAT-elfogadás aláírása | 06.19. | Fodor Gábor (felhasználói képviselő), Nagy Péter |
| 5. Átadás-átvételi jegyzőkönyv | 06.26. | Tóth Gergő → Nagy Péter |

> **Az átvételi kritériumokat egyesével kell végigvezetni**, megfelelt /
> nem felelt meg jelöléssel. A „minden rendben" típusú átvétel vita esetén
> semmit nem bizonyít.

## 5. Az átvétel aláírói

| Szerep | Név | Mit igazol |
|---|---|---|
| Szakmai átvevő | Nagy Péter, IT osztályvezető | A megoldás üzemeltethető, a dokumentáció elegendő |
| **Felhasználói képviselő** | **Fodor Gábor, területvezető** | **A megoldás a valós napi munkára alkalmas** |
| Projektmenedzser | Tóth Gergő | A vállalt hatókör teljesült |

> **A felhasználói képviselő aláírása nem elhagyható.** A vezetői aláírás nem
> helyettesíti azt, hogy a napi munkát végzők kipróbálták és elfogadták.

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.03.06. |
| Jóváhagyta | Nagy Péter, IT osztályvezető | 2026.03.11. |
| Jóváhagyta | Fodor Gábor, felhasználói képviselő | 2026.03.12. |
| Baseline-ként elfogadta | Projekt Irányító Bizottság (tervezési kapu) | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete a *Hatókör-nyilatkozat*, a
> *Követelmény-nyomonkövetési mátrix* és a *Projektszótár*; kimenete a
> *Tesztterv*, a *Minőségellenőrzési jegyzőkönyv* és az
> *Átadás-átvételi jegyzőkönyv*.
