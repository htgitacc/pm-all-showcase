# WBS-szótár (WBS Dictionary)

**Dokumentum azonosítója:** XYO-CP-104\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Kitöltötték:** a munkacsomag-felelősök, 2026.02.12–02.18.\
**Verzió:** 1.1

> **Verziójegyzet:** a nyertes szállító neve (Cloudia Solutions Kft.) a szerződéskötés után, 2026.04.20-án került a dokumentumba. A korábbi változatban a beszerzési tételek (B1–B4) szerepeltek; a baseline tartalma — hatókör, ütem, költség — ezzel nem változott.

> **A legfontosabb mező a kész-definíció.** Enélkül minden munkacsomag
> „majdnem kész" marad a projekt 80%-ánál. Itt csak a kritikus úton lévő és a
> vitára okot adó munkacsomagok teljes lapja szerepel — a többi ugyanilyen
> szerkezetben, a projekt SharePointján.

---

## 2.3.1 — 50 db átvett, Autopilot-regisztrált laptop

| | |
|---|---|
| **Felelős** | Szabó Márk |
| **Mit tartalmaz** | A szállított laptopok mennyiségi és minőségi átvétele, leltárba vétele, az Autopilot-regisztráció ellenőrzése, a szállítói teljesítésigazolás előkészítése |
| **Mit NEM tartalmaz** | A gépek felhasználóhoz rendelését (az a 7.1–7.3), az alkalmazástelepítést (3.2.3) |
| **Kész-definíció** | Mind az 50 gép leltárszámmal rögzítve, **mind az 50 megjelenik az Intune Autopilot eszközlistában**, és a szállítói teljesítésigazolás aláírva |
| **Becsült ráfordítás** | 24 óra |
| **Függőség** | 2.2.2 (aláírt szerződés), 3.2.2 (Autopilot folyamat kész) |
| **Kockázat** | R1 — a szállítás csúszik |

> **Miért fontos itt a kész-definíció?** Mert „megérkezett a laptop" és
> „használható a laptop" két különböző dolog. Ha a szállító nem regisztrálta
> Autopilotba (F-2 feltétel), akkor 50 gépet kézzel kell beüzemelni — az 6,5 óra
> gépenként, összesen 325 óra váratlan munka.

## 3.1.2 — MFA és feltételes hozzáférési szabályok

| | |
|---|---|
| **Felelős** | Cloudia Solutions, átvevő: Szabó Márk |
| **Mit tartalmaz** | MFA bekapcsolása minden pilot fiókra, feltételes hozzáférési szabályok (megbízható eszköz, országkorlátozás), a kizárási (break-glass) fiók beállítása |
| **Mit NEM tartalmaz** | A pilot körön kívüli felhasználók MFA-ját |
| **Kész-definíció** | Az Entra ID riport **100% MFA-lefedettséget** mutat a pilot körben; a feltételes hozzáférési szabályok jelentés-módban legalább 5 munkanapig futottak hiba nélkül; a break-glass fiók dokumentálva és tesztelve |
| **Becsült ráfordítás** | 32 óra |
| **Függőség** | 3.1.1 (fiókok léteznek) |
| **Kockázat** | Rosszul beállított szabály kizárhatja a felhasználókat — ezért kötelező a jelentés-mód |

## 3.3.2 — Megőrzési és mentési szabályok, visszaállítási teszt

| | |
|---|---|
| **Felelős** | Szabó Márk |
| **Mit tartalmaz** | OneDrive és SharePoint megőrzési szabályok beállítása, a lomtár-időszakok rögzítése, **visszaállítási teszt elvégzése** |
| **Mit NEM tartalmaz** | Külső mentési szolgáltatás beszerzését (nincs a hatókörben) |
| **Kész-definíció** | A megőrzési szabályok élnek; **egy szándékosan törölt tesztfájl és egy teljes tesztkönyvtár sikeresen visszaállítva**, jegyzőkönyvezve; a visszaállítás időigénye dokumentálva |
| **Becsült ráfordítás** | 24 óra |
| **Függőség** | 3.3.1 (struktúra kész) |
| **Kockázat** | R7 — „a felhő magától ment" tévhit |

> Ez a munkacsomag a WBS-workshopon került be, Szabó Márk felvetésére.
> Az eredeti vázlatban nem szerepelt.

## 5.3 — Felkészített Service Desk

| | |
|---|---|
| **Felelős** | Kiss Réka |
| **Mit tartalmaz** | Hibakezelési útmutató az új környezethez, a leggyakoribb 15 hibatípus megoldásával; a hypercare időszak kapacitástervezése; a Service Desk munkatársainak felkészítése |
| **Mit NEM tartalmaz** | A végfelhasználói oktatást (5.2) |
| **Kész-definíció** | Az útmutató elkészült és a Service Desk mindhárom munkatársa **átvette és végigment rajta**; a hypercare kapacitás írásban egyeztetve; a felkészítés **legalább 2 héttel az első élesítés előtt** megtörtént |
| **Becsült ráfordítás** | 24 óra |
| **Függőség** | 3.5 (as-built), 5.1 (oktatási anyag) |
| **Kockázat** | R5 — felhasználói ellenállás, ha a támogatás nem működik |

## 6.3 — Felhasználói átvételi teszt (UAT)

| | |
|---|---|
| **Felelős** | Nagy Péter, a 10 fős tesztcsoporttal |
| **Mit tartalmaz** | 10 valós felhasználó 2 héten át élesben, a saját munkájával dolgozik az új környezetben; hibabejelentés a tesztesetek alapján; javítás utáni újratesztelés |
| **Mit NEM tartalmaz** | A technikai tesztet (6.2), amit a rendszergazda végez |
| **Kész-definíció** | A tesztesetek **≥ 95%-a megfelelt**; nincs nyitott kritikus hiba; a nem javított hibák listája elfogadott javítási határidővel rögzítve; a tesztjegyzőkönyv elkészült |
| **Becsült ráfordítás** | 80 óra (10 fő × 8 óra tesztelési többletmunka) |
| **Függőség** | 6.2 (technikai teszt lezárva), 7.1 (első hullám élesben) |
| **Kockázat** | Ha a tesztelők nem valós feladattal dolgoznak, a teszt semmit nem bizonyít |

## 7.4 — Hypercare időszak (3 hét)

| | |
|---|---|
| **Felelős** | Kiss Réka, Szabó Márk támogatásával |
| **Mit tartalmaz** | Fokozott támogatás az utolsó élesítési hullám után 3 héten át: kiemelt válaszidő, napi hibaáttekintés, helyszíni segítség |
| **Mit NEM tartalmaz** | A normál üzemeltetési támogatást — az az átadás után indul |
| **Kész-definíció** | A 3 hét letelt; **a napi új hibabejelentések száma két egymást követő héten a normál szint 150%-a alá csökkent**; a maradék nyitott hibák átadva az üzemeltetésnek |
| **Becsült ráfordítás** | 60 óra |
| **Függőség** | 7.3 (teljes élesítés) |
| **Kockázat** | A hypercare átfedi a projektzárást — a kilépési feltételt előre kell rögzíteni |

> **Figyeld meg a kész-definíciót:** nem „letelt a 3 hét", hanem egy **mérhető
> állapot**. Enélkül a hypercare vagy túl korán ér véget, vagy soha.

## 8.3 — Átadott mérési felelősségek

| | |
|---|---|
| **Felelős** | Tóth Gergő |
| **Mit tartalmaz** | A haszonrealizálási terv, a KPI-adatlapok és a T0 adatok átadása a mérési felelősöknek; a havi adatszolgáltatás rendjének rögzítése |
| **Kész-definíció** | Minden mérőszámhoz **nevesített felelős**, aki írásban visszaigazolta a feladatot; az első havi adatszolgáltatás időpontja rögzítve |
| **Becsült ráfordítás** | 8 óra |
| **Függőség** | 8.1, 8.2 |
| **Kockázat** | Gazdátlan mérés nem történik meg — ez a projektzárás feltétele |

---

## Kész-definíciók összefoglalója (gyors ellenőrzéshez)

| WBS | Mikor kész? |
|---|---|
| 2.3.1 | 50 gép leltárban + 50 gép az Autopilot listában + aláírt teljesítésigazolás |
| 3.1.2 | 100% MFA + 5 nap hibátlan jelentés-mód + tesztelt break-glass fiók |
| 3.3.2 | Sikeres, jegyzőkönyvezett fájl- és könyvtár-visszaállítás |
| 5.3 | Átvett útmutató + egyeztetett kapacitás + 2 héttel az élesítés előtt |
| 6.3 | ≥95% teszteset megfelelt + nincs nyitott kritikus hiba |
| 7.4 | Hibaszám 2 hete a normál 150%-a alatt + maradék hibák átadva |
| 8.3 | Minden mérőszámnak nevesített, visszaigazolt felelőse van |

---

> **Kapcsolódó dokumentumok:** bemenete a *WBS*; kimenete az *Ütemterv* és a
> *Munkacsomag-kiadás*.
