# Változáskezelési eljárás (Change Management Procedure)

**Dokumentum azonosítója:** XYO-CP-115\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Jóváhagyta:** Projekt Irányító Bizottság — 2026.03.13.\
**Verzió:** 1.0

> **Enélkül minden módosítás hatókör-elszivárgás**, és a csúszást rajtad kérik
> számon. Az eljárás nem a változás megakadályozásáról szól, hanem arról, hogy
> a változás **látható, mérlegelt és eldöntött** legyen.

---

## 1. Mit érint az eljárás?

**Változáskérelem kell**, ha a kérés érinti:

- a **jóváhagyott hatókört** (Hatókör-nyilatkozat, XYO-CP-102),
- a **baseline ütemtervet** (bármely mérföldkő dátumát),
- a **költségbázist** (bármely tétel összegét),
- az **átvételi kritériumokat**,
- a jóváhagyott **követelménylistát** (K vagy F prioritású tétel).

**Nem kell változáskérelem:**

- a napi munkaszervezéshez, feladatátcsoportosításhoz;
- a nem mérföldkőhöz kötött belső részhatáridők eltolásához;
- a dokumentumok szövegének pontosításához, ha a tartalom nem változik;
- a tartalékkeret 1 000 000 Ft alatti, PM-hatáskörben hozott felhasználásához
  (de ezt a Döntésnaplóba be kell vezetni).

## 2. Ki nyújthat be változáskérelmet?

**Bárki** — a projektcsapat tagjai, az érintettek, a szállítók, a pilot
résztvevői. A kérelem befogadója mindig a projektmenedzser.

Ha a kérés **szóban** hangzik el, a projektmenedzser feladata leírni és
visszaküldeni a kérelmezőnek megerősítésre. Ez nem formalitás: a szóban
elhangzott kérés nélkül nincs mit mérlegelni, és később mindenki másra emlékszik.

## 3. Az eljárás menete

| # | Lépés | Ki | Határidő |
|---|---|---|---|
| 1 | A kérelem beérkezik (űrlapon vagy szóban → PM leírja) | kérelmező / PM | — |
| 2 | Nyilvántartásba vétel a Változásnaplóba, sorszámmal | Tóth Gergő | 1 munkanap |
| 3 | **Hatásvizsgálat**: idő, költség, kockázat, minőség, hatókör | Tóth Gergő, az érintett felelősökkel | 5 munkanap |
| 4 | Döntési javaslat megfogalmazása | Tóth Gergő | a hatásvizsgálattal együtt |
| 5 | Döntés a hatáskör szerint (lásd 5. pont) | PM / szponzor / Steering | lásd 5. pont |
| 6 | A döntés rögzítése a Változásnaplóban és a Döntésnaplóban | Tóth Gergő | a döntés napján |
| 7 | Értesítés: kérelmező + érintettek | Tóth Gergő | 2 munkanap |
| 8 | Jóváhagyás esetén: **a baseline frissítése** | Tóth Gergő | 3 munkanap |

## 4. A hatásvizsgálat kötelező tartalma

| Szempont | Mit kell megvizsgálni |
|---|---|
| **Idő** | Hány nappal tolódik el, melyik mérföldkő; a kritikus utat érinti-e |
| **Költség** | Egyszeri és folyó költséghatás; a tartalékból fedezhető-e |
| **Kockázat** | Új kockázat keletkezik-e; meglévő súlyosbodik-e |
| **Minőség** | Érint-e átvételi kritériumot; kell-e újratesztelés |
| **Hatókör** | Mit von be, mit hagy el; kell-e a Hatókör-nyilatkozatot módosítani |
| **Közvetett hatások** | **Újratesztelés, oktatás bővítése, dokumentációfrissítés, kommunikáció** |

> ⚠️ **A közvetett hatásokról szoktak megfeledkezni.** Egy „apró" funkcióbővítés
> gyakran maga után vonja a teszteset újraírását, az oktatási anyag frissítését
> és egy újabb kommunikációs kört. Ezek együtt többe kerülnek, mint maga a
> változtatás.

## 5. Döntési hatáskörök

| Hatás | Ki dönt | Válaszidő |
|---|---|---|
| Nincs idő- vagy költséghatás, a hatókört nem érinti | **Tóth Gergő**, projektmenedzser | 3 munkanap |
| ≤ 1 000 000 Ft, ≤ 3 nap csúszás, a mérföldköveket nem érinti | **Tóth Gergő**, utólagos tájékoztatással | 3 munkanap |
| > 1 000 000 Ft **vagy** > 3 nap csúszás **vagy** hatókörváltozás | **Kovács Anita**, szponzor | 5 munkanap |
| Az M7 vagy M10 mérföldkövet érinti | **Projekt Irányító Bizottság** | a következő havi ülés |
| A projekt céljait vagy a keretösszeget érinti | **Projekt Irányító Bizottság** | a következő havi ülés |

**Sürgős változás:** ha a döntés nem várhat a normál eljárásra (pl. biztonsági
incidens, szállítói kényszerhelyzet), a projektmenedzser Kovács Anitával
telefonon egyeztet, a döntést **24 órán belül írásban rögzíti**, és a következő
Steering ülésen utólagos jóváhagyásra beterjeszti.

## 6. Változáskérelem űrlap (sablon)

```
VÁLTOZÁSKÉRELEM — Xyo Cloud Pilot

Sorszám:            VK-___
Benyújtó:
Dátum:

1. MIT KÉRSZ?
   (1-3 mondat, konkrétan)

2. MIÉRT?
   (Milyen problémát old meg, vagy milyen igényt elégít ki)

3. MI TÖRTÉNIK, HA NEM VALÓSUL MEG?
   (A kérelmező tölti ki — ez szűri ki a "jó lenne, ha" kéréseket)

--- az alábbiakat a projektmenedzser tölti ki ---

4. HATÁSVIZSGÁLAT
   Idő:              ___ nap, érintett mérföldkő: ___
   Kritikus úton?    igen / nem
   Költség:          ___ Ft (egyszeri) + ___ Ft/év (folyó)
   Fedezet:          tartalék / keretmozgástér / nincs
   Kockázat:
   Minőség:
   Hatókör:
   Közvetett hatás:  újratesztelés / oktatás / dokumentáció / kommunikáció

5. ALTERNATÍVÁK
   (Van-e olcsóbb vagy gyorsabb megoldás ugyanarra az igényre?)

6. A PROJEKTMENEDZSER JAVASLATA
   jóváhagyás / elutasítás / elhalasztás — indoklással

7. DÖNTÉS
   Döntéshozó:
   Dátum:
   Döntés:           jóváhagyva / elutasítva / elhalasztva
   Indoklás:
   Baseline frissítve: igen / nem, dátum: ___
```

> **A 3. pont a legfontosabb kérdés az űrlapon.** Ha a kérelmező nem tudja
> megmondani, mi történik a kérés nélkül, akkor jellemzően „jó lenne, ha"
> típusú kérésről van szó — és ezek adják a hatókör-elszivárgás nagy részét.

## 7. Az elutasított kérelmek kezelése

**Az elutasított kérelmeket ugyanúgy nyilvántartjuk, mint a jóváhagyottakat.**
A Változásnaplóban maradnak, indoklással, és a hatókörön kívüli elemek közé is
bekerülnek (Hatókör-nyilatkozat 4. pont).

Vita esetén ez bizonyítja, hogy a kérés **elhangzott, megvizsgáltuk, és
dokumentált döntés született** — nem elfelejtettük.

## 8. A baseline frissítése

Jóváhagyott változás után:

| Mit kell frissíteni | Ki | Mikor |
|---|---|---|
| Hatókör-nyilatkozat | Tóth Gergő | 3 munkanap |
| Ütemterv | Tóth Gergő | 3 munkanap |
| Költségvetés | Tóth Gergő, Balogh Tamással | 3 munkanap |
| Követelménymátrix | Tóth Gergő | 3 munkanap |
| WBS / WBS-szótár, ha érintett | Tóth Gergő | 3 munkanap |
| Verziószám és változásnapló minden érintett dokumentumban | Tóth Gergő | egyidejűleg |

> **A frissítés nélküli jóváhagyás a legrosszabb állapot:** a döntés megvan, de
> a tervek a régi állapotot mutatják — így senki nem tudja, mihez képest mérünk.

## 9. Példa: hogyan néz ki egy jó hatásvizsgálat?

**VK-01 (fiktív példa a tervezéshez):** „A pilot bővítése 50-ről 65 főre."

| Szempont | Hatás |
|---|---|
| Idő | +3 hét: 15 további gép beszerzése, 2 további oktatási csoport, +1 élesítési hullám. **Az M7 és M10 is tolódik** → Steering-döntés kell |
| Költség | 15 × 555 000 Ft (gép + tartozék) = 8 325 000 Ft egyszeri + 1 × 15 fő licenc és mobilnet = 2 304 000 Ft/év |
| Fedezet | **Nincs** — a tartalék 4 431 000 Ft, a keretmozgástér 1 257 000 Ft |
| Kockázat | R1 (szállítás) súlyosbodik; R4 (kapacitás) súlyosbodik |
| Minőség | Nem érint átvételi kritériumot |
| Hatókör | L4 korlátot sért (50 fő) |
| Közvetett | +2 oktatás, +15 kiosztási esemény, hypercare meghosszabbítása |
| **Javaslat** | **Elutasítás** — a keret nem fedezi, és az M10 határidő (L1 korlát) nem tartható. Javasolt alternatíva: a 15 fő a kiterjesztési szakasz első hullámába kerül. |

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.03.06. |
| Jóváhagyta | Projekt Irányító Bizottság | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete a *Projektterv* és a
> *Hatókör-nyilatkozat*; kimenete a *Változáskérelem* és a *Változásnapló*.
