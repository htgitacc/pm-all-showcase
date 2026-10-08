# Kiterjesztési javaslat (Rollout Recommendation)

**Dokumentum azonosítója:** XYO-CP-BEN-007\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Döntéshozó:** Projekt Irányító Bizottság\
**Dátum:** **2026. október 9.**\
**Verzió:** 1.0

> **A pilot egyetlen igazi célja ez a döntés.** Kb. 45 M Ft-ért megtudtuk,
> érdemes-e kb. 133 M Ft-ot költeni a teljes szervezetre.
>
> Ez a dokumentum lesz a következő projekt **üzleti indoklásának alapja**.

---

## 1. Javaslat

# ⟹ **SZAKASZOS KITERJESZTÉS, ÖT ELŐFELTÉTELLEL**

A megoldás kiterjesztése a fennmaradó **190 munkatársra**, három hullámban,
2027.01.11. és 2027.09.30. között — **öt előfeltétel teljesülése esetén**
(4. pont).

> **Hogyan következik ez a minősítésből?** A PIR minősítése *Sikeres*, és a
> Haszonrealizálási terv (3. pont) erre a **szakaszos kiterjesztést** írja
> elő — ezt javasoljuk. Az előfeltételek nem a pilot gyengeségét jelzik
> (az a *Részben sikeres* ág lenne, újraméréssel), hanem azt, amit a
> 190 fős lépték új kockázatként hoz (F2–F5), illetve ami az M6
> elmaradásának okaként a kiterjesztésnél megsokszorozódna (F1).

## 2. A pilot eredményeinek összefoglalója

| | |
|---|---|
| **Minősítés** | **SIKERES** (10/12 mérőszám elérte a célértéket, 0 kudarcküszöb alatt) |
| Projekt | Határidőre, a kereten belül: 44 822 000 Ft / 52 000 000 Ft |
| Elégedettség | 3,1 → **4,2** |
| Rugalmasság (a legfontosabb üzleti indok) | 2,2 → **4,3** |
| Adatvesztés | 3 eset/év → **0** |
| Gépbeüzemelés | 6,5 óra → **1,4 óra** |
| **Ami nem teljesült** | M1 (74 vs. 72 ticket — új használati kérdések, H-09) · M6 (37% vs. 40% home office — vezetői korlátozás) |

## 3. Miért érdemes kiterjeszteni?

| # | Érv | Bizonyíték |
|---|---|---|
| 1 | **A megoldás működik éles üzemben** | 4 hónap valós működés, 99,6% rendelkezésre állás, 0 adatvesztés |
| 2 | **A felhasználók akarják** | Elégedettség 4,2; a kitöltési arány 73% → 88%-ra nőtt |
| 3 | **A géppark cseréje elkerülhetetlen** | A maradék 190 gép átlagéletkora 2027-ben 6,8 év lesz |
| 4 | **A támogatási terhelés összetétele javult** | A hozzáférési ticketek aránya 41% → 17% |
| 5 | **Van belső kompetencia és dokumentáció** | Szabó Márk önállóan üzemeltet; Run-book és as-built rendelkezésre áll |
| 6 | **Van belső támogatói bázis** | A pilot kör lett a belső referencia (PIR 5. pont) |

## 4. Az öt előfeltétel

**A kiterjesztés csak akkor indulhat, ha ezek teljesülnek.**

### F1 — A home office szabályzat egységes vezetői alkalmazása

| | |
|---|---|
| **Miért** | Az M6 (37% vs. 40%) elmaradásának egyetlen oka: két területvezető heti max. 2 napban korlátoz. A haszon jelentős része (M11, M2) éppen a rugalmasságból fakad. |
| **Mit kell tenni** | A HR és az ügyvezetés tisztázza, hogy a szabályzat heti 3 napja **irányadó vagy maximum** — és ezt egységesen alkalmazzák |
| **Felelős** | Varga Eszter, Horváth Júlia |
| **Határidő** | 2026.12.15. |

> **Ez a legfontosabb feltétel.** Nélküle a kiterjesztés technikailag
> sikeres lesz, üzletileg viszont a haszon fele elvész — és ezt már most
> tudjuk, mérésből.

### F2 — Adatvesztés-megelőzés (DLP) bevezetése

| | |
|---|---|
| **Miért** | A pilotnál 50 főnél tudatosan elhagytuk (aránytalan volt). 240 fő és a teljes vállalati adatkör mellett **kötelező**. |
| **Mit** | DLP-szabályok kialakítása a bizalmas adatkörökre (pénzügy, HR, szerződések) |
| **Felelős** | Szabó Márk, dr. Fekete Zsolt |
| **Határidő** | a kiterjesztés 1. hulláma előtt |

### F3 — Behatolásteszt

| | |
|---|---|
| **Miért** | A pilot mérete nem indokolta; a teljes szervezetnél a támadási felület lényegesen nagyobb |
| **Mit** | Külső szakértő általi behatolásteszt a felhőkörnyezetre |
| **Felelős** | Nagy Péter |
| **Határidő** | 2026.12.31. |

### F4 — Service Desk kapacitásbővítés

| | |
|---|---|
| **Miért** | A pilotnál a hypercare-hez +1 fő átcsoportosítás elég volt (VK-02). **190 fő nem skálázható átcsoportosítással.** |
| **Számítás** | A pilot fajlagos terhelése az élesítés utáni időszakban hullámról hullámra 3,4 → 2,1 → 1,5 ticket/fő volt. Az 55–70 fős hullámoknál ez hullámonként kb. **80–240 többletticket** — már a legjobb (1,5-ös) értékkel is 80–105, a pilot kör teljes havi szintje (103) körül. |
| **Mit** | +1 fő tartós Service Desk kapacitás, vagy külső támogatás a bevezetési időszakra |
| **Felelős** | Kiss Réka, Nagy Péter |
| **Határidő** | 2026.12.15. |

### F5 — Csapat-szintű haladás

| | |
|---|---|
| **Miért** | A PIR 5. pontja: a vegyes összetételű pilot körben **két munkamód alakult ki egy csapaton belül**, ami a fájlmegosztást körülményessé tette |
| **Mit** | A hullámokat **teljes szervezeti egységenként** kell kialakítani, nem vegyesen |
| **Felelős** | Tóth Gergő (a következő projekt tervezésénél) |
| **Határidő** | a tervezési fázisban |

## 5. Becsült költség

### Egyszeri

| Tétel | Menny. | Egységár | Összesen |
|---|---:|---:|---:|
| Laptop | 190 | 420 000 Ft | 79 800 000 Ft |
| Dokkoló | 190 | 45 000 Ft | 8 550 000 Ft |
| Monitor (otthoni) | 190 | 65 000 Ft | 12 350 000 Ft |
| Headset | 190 | 25 000 Ft | 4 750 000 Ft |
| Bevezetési szolgáltatás | 1 | 12 000 000 Ft | 12 000 000 Ft |
| Oktatás (19 csoport) | 1 | 3 500 000 Ft | 3 500 000 Ft |
| **F2** DLP bevezetése | 1 | 2 400 000 Ft | 2 400 000 Ft |
| **F3** Behatolásteszt | 1 | 1 800 000 Ft | 1 800 000 Ft |
| **Részösszeg** | | | **125 150 000 Ft** |
| Tartalék (6%) | | | 7 509 000 Ft |
| **Mindösszesen** | | | **132 659 000 Ft** |

> **Az egységárak a pilot *tervezett* árai**, nem a szerződöttek (azok
> kb. 3%-kal alacsonyabbak voltak). Ez tudatosan óvatos becslés: új
> beszerzési eljárás lesz, egy évvel később.
>
> **A tartalék 6%, nem 10%.** A pilot tanulsága (T-04): a 10%-os
> tartalékból csak 182 000 Ft fogyott — a tartalék 3,9%-a, a költségbázis
> 0,4%-a. A kiterjesztés viszont nagyobb és összetettebb (három hullám,
> 190 eszköz, árfolyamkockázat), ezért nem a pilot szintjére vágjuk le,
> hanem 6%-ot javaslunk.

### Folyó, a 190 főre

| Tétel | Éves összeg |
|---|---:|
| M365 Business Premium (190 fő) | 20 064 000 Ft |
| Azure infrastruktúra és VPN (skálázva) | 6 000 000 Ft |
| Mobilinternet-hozzájárulás (190 fő) | 9 120 000 Ft |
| **Összesen** | **35 184 000 Ft / év** |

**A teljes szervezetre (240 fő) vetített folyó költség:**
35 184 000 + 10 580 000 (a pilot kör) = **45 764 000 Ft / év**,
azaz **15 890 Ft / fő / hó** — a pilot 17 633 Ft-os fajlagos költsége alatt,
mert az Azure-infrastruktúra költsége több főre oszlik. (Mennyiségi
licenckedvezménnyel nem számoltunk; ha lesz, az tovább csökkenti.)

### A bevezetési szolgáltatás nem lineáris

| | 50 fő (pilot) | 190 fő (kiterjesztés) |
|---|---:|---:|
| Bevezetési díj | 6 020 000 Ft | 12 000 000 Ft |
| Fajlagos | 120 400 Ft/fő | **63 158 Ft/fő** |

**A környezet már létezik** — a kiterjesztés lényegében felhasználók és
eszközök hozzáadása. Ez a pilot legkézzelfoghatóbb pénzügyi hozadéka.

## 6. Javasolt ütem

| Hullám | Kör | Létszám | Időszak |
|---|---|---:|---|
| Előkészítés | F1–F5 feltételek, beszerzés | — | 2026.11 – 2026.12. |
| **1. hullám** | Pénzügy, Kontrolling, HR (teljes egységek) | 55 fő | 2027.01.11 – 2027.03.31. |
| **2. hullám** | Értékesítés, Marketing | 70 fő | 2027.04.01 – 2027.06.30. |
| **3. hullám** | Logisztika, Termelésirányítás (adminisztratív kör) | 65 fő | 2027.07.01 – 2027.09.30. |
| Mérés | T+3 mérés a teljes szervezetre | — | 2027.10 – 2027.12. |

**Hullámonként:** beszerzés → környezet bővítése → oktatás → élesítés →
2 hét hypercare.

> **A logisztika a 3. hullámba került**, pedig onnan érkezett a legerősebb
> igény (VK-01). Az ok: az ő rendszereik érintik a termelésirányítást, ami a
> pilot hatókörén kívül volt — itt külön felmérés szükséges.
>
> **Papp Zsófia előzetes tájékoztatást kap erről**, mert a VK-01
> elutasításakor a kiterjesztést ígértük neki.

## 7. Amit a pilotból másképp csinálunk

| # | A pilotban | A kiterjesztésben | Forrás |
|---|---|---|---|
| 1 | Vegyes összetételű kör | **Teljes szervezeti egységek** | PIR 5. pont, F5 |
| 2 | 10% tartalék | **6% tartalék** | T-04 |
| 3 | A jelentés-mód irodai hálózaton futott | **A valós használati környezetben** (mobilnet, otthoni wifi) | T-01 |
| 4 | Monitor-kompatibilitás feltételezve | **Mintavételes ellenőrzés minden „meglévő eszköz felhasználható" feltevésnél** | T-02 |
| 5 | Az EVM-alap a fizetési ütem volt | **Eredmény-alapú felosztás előre** | T-17 |
| 6 | Az 1. hullám kapta a legtöbb hibát | **Az 1. hullám résztvevőinek csökkentett munkaterhelés**, előre kommunikálva | Elégedettségi felmérés 5. pont |
| 7 | Hypercare +1 fő átcsoportosítással | **Tartós kapacitásbővítés** | F4 |

## 8. Kockázatok nagyobb léptékben

| # | Kockázat | Miért más 190 főnél | Válasz |
|---|---|---|---|
| K1 | Service Desk terhelés | Nem skálázható átcsoportosítással | F4 előfeltétel |
| K2 | Hardverszállítás | 190 db egy tételben — készlethiány valós kockázat | Hullámonkénti beszerzés, részszállítással |
| K3 | Belső kapacitás | Szabó Márk egyedül nem tud 3 hullámot vinni | A bevezetést szállító végzi; belső oldalon +1 fő szükséges |
| K4 | Adatvédelem | Nagyobb adatkör, több bizalmas adat | F2 (DLP) és F3 (behatolásteszt) |
| K5 | Szervezeti ellenállás | A pilotban önként jelentkezők voltak; a kiterjesztésnél mindenki érintett | A pilot kör mint belső referencia; a K5 (rugalmasság) eredményének kommunikálása |
| K6 | **Két munkamód egy csapaton belül** | A pilot alatt is problémát okozott | F5: csapat-szintű haladás |

## 9. Mi történik, ha nem terjesztjük ki?

| | |
|---|---|
| A 190 gép cseréje **így is esedékes** 2027-ben | kb. 65 000 000 Ft hagyományos modellben |
| A pilot kör **külön világ marad** | Két párhuzamos üzemeltetési modell, tartósan |
| A fájlszerver **tovább üzemel** | 7 600 000 Ft/év, a pilot kör nélkül is |
| A home office lehetőség **50 főre korlátozódik** | Méltányossági feszültség (R15 kockázat) |
| A pilot beruházása **nem térül meg** | A bevezetési szolgáltatás fajlagos költsége 120 400 Ft/fő marad |

> **A „ne csináljunk semmit" változat sem ingyenes.** A gépcsere költsége
> elkerülhetetlen; a kérdés továbbra is az, milyen modellre költünk.

## 10. Döntési javaslat

A Projekt Irányító Bizottság döntsön arról, hogy:

1. **Elfogadja-e a szakaszos, előfeltételekhez kötött kiterjesztési javaslatot** a 190 munkatársra,
   három hullámban, 2027.01.11 – 2027.09.30. között;
2. **Elrendeli-e az F1–F5 előfeltételek teljesítését** 2026.12.31-ig;
3. **Jóváhagyja-e a kiterjesztési projekt előkészítésének indítását**
   (üzleti indoklás és Charter kidolgozása) 2026.11.15-i határidővel.

---

## Az ülés döntése

| # | Döntés | Eredmény | Dátum |
|---|---|---|---|
| 1 | Szakaszos, előfeltételekhez kötött kiterjesztés elfogadása | **Elfogadva** | 2026.10.09. |
| 2 | F1–F5 előfeltételek elrendelése | **Elfogadva**, 2026.12.31-i határidővel | 2026.10.09. |
| 3 | A kiterjesztési projekt előkészítése | **Elfogadva**; projektmenedzser: Tóth Gergő | 2026.10.09. |
| — | **Kiegészítés (Horváth Júlia)** | A PIR eredményeit **a teljes szervezetnek** kommunikálni kell, nem csak a vezetőknek — a méltányossági feszültség (R15) kezelésére | 2026.10.09. |

| Szerep | Név | Aláírás | Dátum |
|---|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | | 2026.10.05. |
| A hasznok gazdája | Nagy Péter, IT osztályvezető | | 2026.10.07. |
| Szponzor | Kovács Anita, gazdasági igazgató | | 2026.10.09. |
| **Elnök** | **Horváth Júlia**, ügyvezető | | **2026.10.09.** |

---

> **Ezzel a Xyo Cloud Pilot teljes életciklusa lezárult:**
> ötlet (2025.11.10.) → projekt (2026.02.02 – 06.30.) → mérés
> (2026.07.01 – 09.30.) → döntés (2026.10.09.).

> **Kapcsolódó dokumentumok:** bemenete a *PIR*, a *Tanulságok naplója*, a
> *Pénzügyi zárás* és a *Felhasználói kérdőív*. Ez a dokumentum lesz a
> kiterjesztési projekt *Üzleti indoklásának* bemenete.
