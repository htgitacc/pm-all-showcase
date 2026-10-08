# Visszaállási terv (Rollback / Contingency Plan)

**Dokumentum azonosítója:** XYO-CP-120\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő (PM) és Nagy Péter (szakmai vezető)\
**Verzió:** 1.0

> **Verziójegyzet:** a nyertes szállító neve (Cloudia Solutions Kft.) a szerződéskötés után, 2026.04.20-án került a dokumentumba. A korábbi változatban a beszerzési tételek (B1–B4) szerepeltek; a baseline tartalma — hatókör, ütem, költség — ezzel nem változott.

> **Élesítés napján, nyomás alatt senki nem tud higgadtan eldönteni, hogy
> „ez már elég nagy baj-e".** Ezért a döntési kritériumot előre kell megírni.

---

## 1. Miért egyszerű ez a projektben?

A Xyo Cloud Pilot **migráció nélküli**, ezért a visszaállás lényegesen
egyszerűbb, mint egy rendszercserénél:

| | |
|---|---|
| A régi asztali gép | **A helyén marad** az élesítés után 4 hétig, bekapcsolható állapotban |
| A régi fájlszerver | **Változatlanul üzemel**, a nem érintett 190 kolléga használja |
| Adatvesztés kockázata | **Nincs** — az új környezetben keletkezett adat a felhőben marad, a régi adat a szerveren |
| A visszaállás lényege | A felhasználó visszaül a régi gépéhez, és a szokott módon dolgozik |

> **Ettől függetlenül le kell írni.** Az egyszerű visszaállás is káoszba fullad,
> ha az élesítés napján kell kitalálni, ki dönt róla és mi a sorrend.

## 2. Mikor mondjuk ki a visszaállást?

**Egyedi (egy felhasználó) visszaállítása** — ha az alábbiak bármelyike igaz:

| # | Kritérium |
|---|---|
| E1 | A felhasználó **2 munkanapon át** nem tud érdemi munkát végezni az új környezetben |
| E2 | Az otthoni internetkapcsolata bizonyítottan nem elegendő (mérés alapján) |
| E3 | Olyan üzletileg kritikus feladata van, amit az új környezet nem támogat |

**Hullám-szintű visszaállás (10–20 fő)** — ha az alábbiak bármelyike igaz:

| # | Kritérium |
|---|---|
| H1 | A hullám résztvevőinek **több mint 30%-a** nem tud belépni, és a hiba oka 4 órán belül nem azonosított |
| H2 | Adatvesztéssel vagy adatszivárgással járó **S1 hiba** merült fel |
| H3 | A VPN-kapcsolat 1 munkanapnál hosszabb ideig nem működik, és emiatt a belső rendszerek elérhetetlenek |

**Teljes projekt visszaállása** — ha:

| # | Kritérium |
|---|---|
| T1 | Két egymást követő hullámnál is bekövetkezik H1 vagy H2 |
| T2 | Adatvédelmi incidens történt, amelynél a DPO a szolgáltatás felfüggesztését javasolja |
| T3 | A szolgáltatás rendelkezésre állása egy naptári hónapban 95% alá esik |

## 3. Ki dönt?

| Szint | Döntéshozó | Konzultáció | Válaszidő |
|---|---|---|---|
| Egyedi visszaállítás | **Kiss Réka**, Service Desk vezető | Szabó Márk | 4 óra |
| Hullám-szintű visszaállás | **Nagy Péter**, IT osztályvezető | Tóth Gergő, Kiss Réka | 4 óra |
| Teljes visszaállás | **Kovács Anita**, szponzor | Nagy Péter, dr. Fekete Zsolt (ha adatvédelmi) | 24 óra |

> A döntést **mindig írásban** kell rögzíteni, a Döntésnaplóban, a kiváltó
> kritérium megjelölésével.

## 4. A visszaállás lépései

### 4.1 Egyedi visszaállítás (1 fő) — időigény: 2 óra

| # | Lépés | Ki |
|---|---|---|
| 1 | A felhasználó régi gépének bekapcsolása és frissítése | Szabó Márk |
| 2 | A régi fájlszerver-hozzáférés visszaállítása | Szabó Márk |
| 3 | Az új környezetben keletkezett dokumentumok elérésének biztosítása (webes OneDrive) | Szabó Márk |
| 4 | A felhasználó tájékoztatása és a helyzet rögzítése a Problémanaplóban | Kiss Réka |
| 5 | A visszaállás okának elemzése, hogy a következő hullámnál elkerülhető legyen | Tóth Gergő |

> **A 3. lépés kritikus.** Az új környezetben már készültek dokumentumok — azok
> nem veszhetnek el. Webes hozzáféréssel a régi gépről is elérhetők.

### 4.2 Hullám-szintű visszaállás (10–20 fő) — időigény: 1 munkanap

| # | Lépés | Ki |
|---|---|---|
| 1 | Döntés meghozatala és írásos rögzítése | Nagy Péter |
| 2 | Azonnali tájékoztatás az érintetteknek (e-mail + telefon) | Tóth Gergő |
| 3 | A régi gépek bekapcsolása és ellenőrzése | Szabó Márk + 1 Service Desk munkatárs |
| 4 | A fájlszerver-hozzáférések visszaállítása | Szabó Márk |
| 5 | A felhőben keletkezett adatok elérhetőségének biztosítása | Szabó Márk |
| 6 | A hibaok elemzése, javítási terv | Nagy Péter, Cloudia Solutions |
| 7 | Steering tájékoztatás | Tóth Gergő |
| 8 | Az újraindítás feltételeinek meghatározása | Nagy Péter |

### 4.3 Teljes visszaállás — időigény: 3 munkanap

A hullám-szintű lépések a teljes 50 főre, kiegészítve:

| # | Lépés | Ki |
|---|---|---|
| 9 | Rendkívüli Steering ülés összehívása | Tóth Gergő |
| 10 | A szállítói felelősség vizsgálata, kötbérigény mérlegelése | Molnár Katalin |
| 11 | Döntés: javítás és újraindítás, vagy a projekt leállítása | Projekt Irányító Bizottság |
| 12 | Adatvédelmi incidens esetén: NAIH-bejelentés 72 órán belül | dr. Fekete Zsolt |

## 5. Kit kell értesíteni?

| Esemény | Kit | Mikor | Ki értesít |
|---|---|---|---|
| Egyedi visszaállítás | Az érintett + a vezetője | azonnal | Kiss Réka |
| Hullám-szintű | Az érintettek, a területvezetők, Kovács Anita | 2 órán belül | Tóth Gergő |
| Hullám-szintű | Steering Committee | 1 munkanapon belül | Tóth Gergő |
| Teljes visszaállás | Minden érintett + Horváth Júlia | azonnal | Kovács Anita és Tóth Gergő |
| Adatvédelmi incidens | dr. Fekete Zsolt → NAIH | **azonnal / 72 óra** | dr. Fekete Zsolt |

## 6. Előfeltételek — amit a visszaállás lehetőségéért meg kell tennünk

| # | Előfeltétel | Felelős | Határidő |
|---|---|---|---|
| V1 | A régi asztali gépek **nem kerülnek leselejtezésre** az élesítés után 4 hétig | Szabó Márk | folyamatos |
| V2 | A régi fájlszerver-jogosultságok **nem kerülnek törlésre**, csak felfüggesztésre | Szabó Márk | hullámonként |
| V3 | A régi gépek havonta bekapcsolva, frissítve, működőképesen tartva | Szabó Márk | havonta |
| V4 | A visszaállás lépéseit **egy próbán teszteljük** az UAT alatt, 1 felhasználóval | Szabó Márk | 2026.05.20. |

> **V4 a legfontosabb.** A leírt, de soha ki nem próbált visszaállási terv
> ugyanannyit ér, mint a nem tesztelt mentés. Egy UAT-résztvevővel végigcsináljuk,
> és mérjük az időt.

## 7. Mikor selejtezhetők a régi gépek?

A régi gépek leselejtezésének feltétele — **mind a három**:

| # | Feltétel |
|---|---|
| S1 | Az utolsó élesítési hullám után eltelt 4 hét |
| S2 | A hypercare időszak lezárult a kilépési feltétel teljesülésével |
| S3 | Nagy Péter írásban nyilatkozik, hogy nincs nyitott, visszaállást indokoló hiba |

**Várható időpont:** 2026.07.10. — **a projektzárás (06.30.) után.**
Ezért a selejtezés az üzemeltetésbe adás nyitott pontjai közé kerül,
Nagy Péter felelősségével.

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.03.10. |
| Készítette | Nagy Péter, IT osztályvezető | 2026.03.10. |
| Jóváhagyta | Projekt Irányító Bizottság | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete az *Ütemterv* és a
> *Kockázatnyilvántartás*; kimenete az *Üzemeltetésbe adás (Run-book)*.
