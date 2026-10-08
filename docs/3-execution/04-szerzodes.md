# Szerződés és megrendelés (Contract / Purchase Order)

**Dokumentum azonosítója:** XYO-CP-204\
**Projekt:** Xyo Cloud Pilot\
**Aláírás dátuma:** **2026. április 17.** (M4 mérföldkő)\
**Előkészítette:** Molnár Katalin (beszerzés), jogi ellenőrzés: külső ügyvédi iroda\
**Szakmai tartalom:** Tóth Gergő, Nagy Péter

> **A jogász nem tudja, mit jelent, hogy „működik".** A projektmenedzser
> feladata, hogy az **átvételi kritériumok és a határidők** bekerüljenek a
> szerződésbe — ha csak a te minőségtervedben szerepelnek, a szállítót nem
> kötelezik semmire.

---

## 1. Szerződés-összefoglaló

| | **1. sz. szerződés** | **2. sz. szerződés** |
|---|---|---|
| **Szállító** | TechLine Zrt. | Cloudia Solutions Kft. |
| **Tárgy** | 50 munkaállomás-készlet | M365 licenc (12 hó) + felhőkörnyezet bevezetése |
| **Típus** | Adásvételi, fix áras | **Átalánydíjas (fix price)** vállalkozási |
| **Nettó érték** | 26 890 000 Ft | 14 200 000 Ft |
| **Teljesítési határidő** | 2026.05.29. | 2026.06.19. |
| **Aláírás** | 2026.04.17. | 2026.04.17. |
| **Költséghely** | IT-2026-CP | IT-2026-CP |

## 2. Az 1. sz. szerződés kulcskikötései (TechLine Zrt.)

### 2.1 Teljesítési határidők és részszállítás

| Részteljesítés | Mennyiség | Határidő |
|---|---:|---|
| 1. részszállítás (tesztgépek) | 10 db teljes készlet | **2026.05.06.** |
| 2. részszállítás | 40 db teljes készlet | **2026.05.29.** |

> A részszállítás az R1 kockázat (szállítás csúszik) legfontosabb
> válaszlépése. Enélkül a tesztelés csak 05.29. után indulhatna, és a
> projekt nem férne bele a 06.30-i határidőbe.

### 2.2 Átvételi kritériumok a szerződésben

A Megrendelő akkor köteles átvenni a szállítmányt, ha:

| # | Kritérium | Forrás |
|---|---|---|
| Sz-1 | A mennyiség hiánytalan, minden tétel sértetlen | átvételi eljárás |
| Sz-2 | **Minden laptop megjelenik a Megrendelő Intune Autopilot eszközlistájában** | AK-06, V1 vállalás |
| Sz-3 | A monitorok HDMI vagy DisplayPort csatlakozóval rendelkeznek | K12 követelmény |
| Sz-4 | A dokkolók a laptopot töltik, és 2 külső kijelzőt kezelnek | K12 követelmény |
| Sz-5 | A gépek gyári specifikációja megfelel az ajánlatkérésnek | műszaki melléklet |

**Az Sz-2 a legfontosabb.** Enélkül a szállítás formálisan teljesül, de a
projekt céljai (≤1,5 óra beüzemelés) teljesíthetetlenek maradnak.

### 2.3 Kötbér

| | |
|---|---|
| Késedelmi kötbér | a késedelemmel érintett részteljesítés nettó értékének **napi 0,5%-a** |
| Maximum | a szerződéses érték 10%-a (2 689 000 Ft) |
| Meghiúsulási kötbér | 15%, ha a késedelem meghaladja a 20 napot |

### 2.4 Fizetési ütemezés

| Esemény | Arány | Összeg |
|---|---:|---:|
| 1. részszállítás átvétele | 20% | 5 378 000 Ft |
| 2. részszállítás átvétele | 80% | 21 512 000 Ft |

**Fizetés kizárólag aláírt teljesítésigazolás ellenében**, 30 napos
fizetési határidővel.

### 2.5 Garancia

3 év helyszíni, következő munkanapi kiszállással; a garanciális időszak a
teljes szállítás átvételétől (2026.05.29.) indul.

## 3. A 2. sz. szerződés kulcskikötései (Cloudia Solutions Kft.)

### 3.1 Teljesítési mérföldkövek

| Mérföldkő | Tartalom | Határidő |
|---|---|---|
| M5 | Felhőkörnyezet tesztelésre alkalmas állapotban | **2026.05.08.** |
| — | Oktatási anyag és gyorssegédlet átadva | 2026.05.15. |
| — | 5 oktatási csoport megtartva | 2026.06.10. |
| M8 | As-built dokumentáció és **Run-book** átadva, UAT elfogadva | **2026.06.19.** |

### 3.2 Teljesítési feltételek

A Vállalkozó teljesítése akkor fogadható el, ha:

| # | Feltétel | Forrás |
|---|---|---|
| Sz-6 | Az átvételi kritériumok (AK-01 – AK-23) teljesülnek | Minőségterv, XYO-CP-114 |
| Sz-7 | **Az as-built dokumentáció és a Run-book átadásra került, és a Megrendelő szakmai vezetője írásban elfogadta** | F-4 feltétel, V7 vállalás |
| Sz-8 | A rendszergazda tudásátadása megtörtént, dokumentáltan | V7 vállalás |
| Sz-9 | Az Intune profil nem tartalmaz magánhasználati adatgyűjtést, ezt a Megrendelő DPO-ja írásban igazolja | AK-10, L7 korlát |
| Sz-10 | Az adatok kizárólag EU Data Boundary konfigurációban tárolódnak | L6 korlát, V6 vállalás |

> **Az Sz-7 a projekt egyik legfontosabb szerződéses kikötése.** A tudásátadás
> és a Run-book **teljesítési feltétel**, nem jószándékú ígéret. Enélkül a
> Vállalkozó kialakítja a környezetet, elmegy, és a Xyo minden hibánál
> visszahívja — pénzért.

### 3.3 Fizetési ütemezés

| Esemény | Arány | Összeg |
|---|---:|---:|
| Szerződéskötés (M4) | 30% | 4 260 000 Ft |
| M5 — környezet tesztelésre kész | 40% | 5 680 000 Ft |
| M8 — UAT elfogadva, Run-book átadva | 30% | 4 260 000 Ft |

> A **záró 30% az UAT-elfogadáshoz és a Run-book átadásához kötött**. Ez az
> egyetlen valódi eszköz arra, hogy a dokumentáció tényleg elkészüljön —
> tapasztalat szerint az utolsó részlet nélkül a Run-book „majd később" lesz.

### 3.4 Személyi feltételek

| | |
|---|---|
| Nevesített konzultánsok | 2 fő, az ajánlat M9 melléklete szerint |
| Helyettesítés | Csak azonos vagy magasabb minősítésű szakemberrel, a Megrendelő előzetes jóváhagyásával |
| Adminisztrátori hozzáférés | A Vállalkozó Intune-adminisztrátori jogosultsága **2026.06.19-én, az UAT-elfogadással megszűnik** |

### 3.5 Adatvédelem

| | |
|---|---|
| Adatfeldolgozói megállapodás | A szerződés 3. sz. melléklete, aláírva 2026.04.17. |
| Adattárolás helye | Kizárólag EU Data Boundary |
| Alvállalkozó bevonása | Csak a Megrendelő előzetes írásos hozzájárulásával |
| Titoktartás | A szerződés megszűnését követő 5 évig |

### 3.6 Szavatosság

A bevezetésre 6 hónap szavatosság a teljesítéstől (2026.06.19.) számítva.
A szavatossági időn belül felmerülő konfigurációs hibák javítása díjmentes.

## 4. Amit a szerződésbe a projektmenedzser vitt be

Ezek a kikötések **nem szerepeltek** a beszerzés által előkészített
alapszerződésben, és a projektmenedzser kérésére kerültek bele:

| # | Kikötés | Miért |
|---|---|---|
| 1 | Sz-2: Autopilot-lista mint átvételi feltétel | A szállítás formális teljesülése nem elég |
| 2 | Részszállítás (10 + 40 db) | A tesztelés 05.11-i indulása |
| 3 | Sz-7: Run-book mint teljesítési feltétel | Önálló üzemeltethetőség |
| 4 | A záró 30% az UAT-elfogadáshoz kötve | A dokumentáció tényleges elkészülte |
| 5 | Sz-9: DPO-igazolás az Intune profilról | Az üzemi tanácsi kikötés érvényesítése |
| 6 | Az adminisztrátori jog megszűnésének dátuma | Biztonsági alapkonfiguráció 6. pont |

> **Ez a projektmenedzser dolga a szerződéskötésnél.** A beszerzés a jogi és
> eljárási oldalt ismeri; azt, hogy mi kell a projekt sikeréhez, csak te tudod.
> Ha nem szólsz időben, ezek kimaradnak — és utólag már nem alkudhatók.

## 5. Költséghatás összefoglalva

| | Tervezett | Szerződött | Eltérés |
|---|---:|---:|---:|
| B1 hardver | 27 750 000 Ft | 26 890 000 Ft | −860 000 Ft |
| B2+B3 licenc és bevezetés | 14 780 000 Ft | 14 200 000 Ft | −580 000 Ft |
| **Összesen** | **42 530 000 Ft** | **41 090 000 Ft** | **−1 440 000 Ft** |

**A tartalékkeret érintetlen marad** (4 431 000 Ft, az adapterek levonása után).

---

| Szerep | Név | Dátum |
|---|---|---|
| Előkészítette | Molnár Katalin, beszerzési vezető | 2026.04.14. |
| Szakmai tartalom | Tóth Gergő, Nagy Péter | 2026.04.14. |
| Jogi ellenőrzés | külső ügyvédi iroda | 2026.04.15. |
| **Aláírta** | **Kovács Anita, gazdasági igazgató** | **2026.04.17.** |

> **Kapcsolódó dokumentumok:** bemenete az *Ajánlat-összehasonlítás*, a
> *Beszerzési terv*, az *Adatvédelmi hatásvizsgálat* és a *Minőségterv*;
> kimenete a *Teljesítésigazolás* és a *Szerződészárás*.
