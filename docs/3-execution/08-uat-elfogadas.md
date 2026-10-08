# Felhasználói átvételi elfogadás (UAT Sign-off)

**Dokumentum azonosítója:** XYO-CP-208\
**Projekt:** Xyo Cloud Pilot\
**Dátum:** **2026. június 19.** (M8 mérföldkő)\
**Helyszín:** Xyo Kft. központi iroda, kistárgyaló

> **A felhasználók írásos nyilatkozata arról, hogy a megoldás a valós munkára
> alkalmas.** Enélkül az élesítés után bármikor mondhatja bárki, hogy „ez így
> használhatatlan" — és nincs mire hivatkoznod.

---

## 1. A tesztelt hatókör

| | |
|---|---|
| Tesztidőszak | 2026.05.11 – 2026.06.16. (UAT + újratesztelés) |
| Tesztelők | 10 fő, három szervezeti egységből |
| Tesztesetek | 27 db, a Követelmény-nyomonkövetési mátrix mind a 27 elfogadott (K, F és H) tételéhez rendelve |
| Szabad tesztelés | fejenként 2 teljes munkanap valós munkával |
| Tesztjegyzőkönyv | XYO-CP-207, v1.2 |

## 2. A kilépési feltételek teljesülése

| # | Kilépési feltétel | Elvárás | Tény | Teljesült? |
|---|---|---|---|:-:|
| KI-1 | Minden K prioritású teszteset lefutott | 19/19 | 19/19 | ✔ |
| KI-2 | A tesztesetek megfelelési aránya | ≥ 95% | **96,3%** (26/27) | ✔ |
| KI-3 | Nyitott kritikus (S1) hiba | 0 | **0** | ✔ |
| KI-4 | Minden nyitott S2 hibához elfogadott javítási határidő | igen | igen (H-06) | ✔ |
| KI-5 | Tesztjegyzőkönyv elkészült és aláírva | igen | igen, 06.17. | ✔ |

## 3. Az átvételi kritériumok tételes végigvezetése

| # | Átvételi kritérium | Elvárás | Mért / tapasztalt érték | Megfelelt? |
|---|---|---|---|:-:|
| AK-01 | Mind az 50 felhasználó belép Entra ID-val | 50/50 | 50/50 | ✔ |
| AK-02 | MFA-lefedettség | 100% | **100%** (48 Authenticator, 2 SMS) | ✔ |
| AK-03 | Break-glass fiók dokumentált és tesztelt | igen | tesztelve 05.06. és 06.18. | ✔ |
| AK-04 | Hozzáférés-visszavonás | ≤ 15 perc | **8 perc** | ✔ |
| AK-05 | Önkiszolgáló jelszó-visszaállítás | 5 fő sikeresen | 5/5 | ✔ |
| AK-06 | Autopilot beüzemelés | ≤ 1,5 óra | **1 óra 22 perc** (5 gép átlaga, a javítás után) | ✔ |
| AK-07 | Bekapcsolástól bejelentkezésig | ≤ 90 mp | **71 mp** (10 gép átlaga) | ✔ |
| AK-08 | Lemeztitkosítás | 50/50 | 50/50 | ✔ |
| AK-09 | Alapszoftverek és biztonsági frissítések automatikus telepítése | 50/50 | 50/50 | ✔ |
| AK-10 | Nincs magánhasználati adatgyűjtés | DPO igazolás | **dr. Fekete Zsolt írásos igazolása, 2026.05.07.** | ✔ |
| AK-11 | Monitor csatlakoztatható | 50/50 | 50/50 (36 közvetlenül, 14 adapterrel) | ✔ |
| AK-12 | OneDrive elérése | 50/50 | 50/50 | ✔ |
| AK-13 | SharePoint jogosultsági teszt | 6 csapat × 2 | 12/12 ellenőrzés rendben | ✔ |
| AK-14 | 30 napos visszaállíthatóság | igen | beállítva, tesztelve | ✔ |
| AK-15 | Teljes könyvtár visszaállítása | tesztelt | **sikeres, 42 perc** (1 240 fájl, 4,2 GB) | ✔ |
| AK-16 | Régi fájlszerver olvasása VPN-en | 3 csapat | 14 fő, 14/14 sikeres | ✔ |
| AK-17 | VPN otthoni mobilnetről | 10/10 | 10/10 | ✔ |
| AK-18 | 2 belső rendszer elérése VPN-en | igen | igen (H-01 javítása után) | ✔ |
| AK-19 | 30 perces videóhívás mobilneten | 5/5 | **3/5** — 2 tesztelőnél megszakadt | **✖ nem felelt meg** |
| AK-20 | Oktatáson részt vettek | 50/50 | **50/50** (46 az alkalmon, 4 a pótlón) | ✔ |
| AK-21 | Gyorssegédlet elkészült | igen | 4 oldal, magyar, képernyőképes | ✔ |
| AK-22 | Service Desk útmutató ≥ 2 héttel az élesítés előtt | ≤ 04.27. | **04.27.** (14 nappal 05.11. előtt) | ✔ |
| AK-23 | Az as-built alapján az üzemeltetés átveheti | igen | Nagy Péter nyilatkozata, 06.19. | ✔ |
| AK-24 | UAT tesztesetek megfelelése | ≥ 95% | 96,3% | ✔ |
| AK-25 | Nincs nyitott S1 hiba | 0 | 0 | ✔ |
| AK-26 | Nyitott S2 hibákhoz elfogadott határidő | igen | igen | ✔ |

**Eredmény: 25 kritérium megfelelt, 1 nem felelt meg (AK-19).**

## 4. Az AK-19 nem teljesülésének kezelése

| | |
|---|---|
| **Kritérium** | 30 perces videóhívás mobilneten, megszakadás nélkül, 5 tesztelőnél |
| **Tény** | 3 tesztelőnél megfelelt, 2 tesztelőnél a hívás megszakadt |
| **Kapcsolódó hiba** | H-06 (S2) |
| **Ok** | A 2 érintett tesztelő lakóhelyén a mobilszolgáltatói lefedettség gyenge — **nem a megoldás hibája** |
| **Kapcsolódó követelmény** | K23, **F prioritású** (fontos, de nem kötelező) |
| **Elfogadott kezelés** | 1) Egyeztetés a mobilszolgáltatóval a lefedettségről. 2) Ha nem javul: fix internet-hozzájárulás a tartalékkeretből (2 fő × 12 hó, becsült 240 000 Ft). |
| **Határidő** | 2026.07.31. |
| **Felelős** | Nagy Péter, IT osztályvezető |
| **Az aláírók döntése** | **Az átvételt nem akadályozza.** A követelmény F prioritású, az érintett kör 2 fő, és a kezelésre elfogadott terv és határidő van. |

> **Így kell nem teljesült kritériumot kezelni:** nem elhallgatni és nem is
> megtagadni miatta az átvételt, hanem **leírni, mi nem teljesült, miért, mi a
> terv és ki a felelős** — és az aláírók erről tudatosan döntenek.

## 5. Nyitva maradt hibák — az aláírók által elfogadva

| # | Hiba | Szint | Határidő | Felelős |
|---|---|:-:|---|---|
| H-06 | Videóhívás megszakadása mobilneten (2 fő) | S2 | 2026.07.31. | Nagy Péter |
| H-08 | Alkalmazásportál hiányos magyar felirata | S3 | 2026.09.30. | Cloudia Solutions |
| H-09 | Authenticator értesítés késése | S3 | figyelés alatt | Szabó Márk |
| H-13 | Alkalmazásportál ikon | S4 | — | Szabó Márk |

**Nyitott S1 (kritikus) hiba nincs.**

## 6. A tesztelők nyilatkozata

> Alulírott tesztelők nyilatkozunk, hogy a Xyo Cloud Pilot keretében kialakított
> felhőalapú munkakörnyezetet **2026. május 11. és június 16. között élesben, a
> saját napi munkánk elvégzésére használtuk**, a tesztterv szerinti
> tesztesetekkel és azon túl is.
>
> Nyilatkozunk, hogy a megoldás **a napi munkavégzésre alkalmas**, a fenti
> 5. pontban felsorolt, általunk ismert és elfogadott nyitott hibákkal együtt.

| # | Név | Szervezeti egység | Aláírás |
|---|---|---|---|
| 1 | (tesztelő 1) | Pénzügy | |
| 2 | (tesztelő 2) | Pénzügy | |
| 3 | (tesztelő 3) | Pénzügy | |
| 4 | (tesztelő 4) | Értékesítés | |
| 5 | (tesztelő 5) | Értékesítés | |
| 6 | (tesztelő 6) | Értékesítés | |
| 7 | (tesztelő 7) | Értékesítés | |
| 8 | (tesztelő 8) | Logisztika | |
| 9 | (tesztelő 9) | Logisztika | |
| 10 | (tesztelő 10) | Logisztika | |

## 7. Hivatalos elfogadás

| Szerep | Név | Mit igazol | Aláírás | Dátum |
|---|---|---|---|---|
| **Felhasználói képviselő** | **Fodor Gábor**, területvezető | A megoldás a valós napi munkára alkalmas | | 2026.06.19. |
| **Szakmai átvevő** | **Nagy Péter**, IT osztályvezető | A megoldás üzemeltethető, a dokumentáció elegendő | | 2026.06.19. |
| Projektmenedzser | Tóth Gergő | A vállalt hatókör teljesült | | 2026.06.19. |

> **A felhasználói képviselő aláírása nem elhagyható.** A vezetői aláírás nem
> helyettesíti azt, hogy a napi munkát végzők kipróbálták és elfogadták —
> ezért írt alá mind a 10 tesztelő is.

## 8. Következmények

| | |
|---|---|
| **M8 mérföldkő** | teljesült, 2026.06.19. |
| **Szerződéses hatás** | A Cloudia Solutions Kft. záró 30%-os részlete (4 260 000 Ft) az as-built és a Run-book átadásával együtt kifizethető |
| **Szállítói hozzáférés** | A Cloudia Intune-adminisztrátori jogosultsága a szerződés szerint **2026.06.19-én megszűnik** — ellenőrzendő az üzemeltetésbe adáskor |
| **Következő lépés** | Üzemeltetésbe adás (M9), 2026.06.26. |

---

> **Kapcsolódó dokumentumok:** bemenete a *Tesztjegyzőkönyv*, a
> *Követelmény-nyomonkövetési mátrix* és a *Tesztterv*; kimenete az
> *Átadás-átvételi jegyzőkönyv*.
