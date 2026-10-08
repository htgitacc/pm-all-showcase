# Ütem- és költségeltérés elemzés (EVM — Earned Value Analysis)

**Dokumentum azonosítója:** XYO-CP-306\
**Projekt:** Xyo Cloud Pilot\
**Készíti:** Tóth Gergő, projektmenedzser, Balogh Tamás adataival\
**Gyakoriság:** havonta\
**Ez a kiadás:** 2026. június 19. (M8)

> Az ütemet és a költséget **együtt** nézi, és két számmal fejezi ki, hogy
> állsz. **Téged úgy véd**, hogy az eltérést objektíven, nem érzésre mutatja meg.

---

## 1. A három alapszám

| Rövidítés | Magyarul | Mit jelent |
|---|---|---|
| **PV** | Tervezett érték | Amit a terv szerint mostanra el kellett volna végezni, **a terv szerinti áron** |
| **EV** | Elkészültségi érték | Amit ténylegesen elvégeztünk, **a terv szerinti áron** |
| **AC** | Tényleges költség | Amennyibe az elvégzett munka ténylegesen került |

| Mutató | Képlet | Mit mond |
|---|---|---|
| **SPI** | EV / PV | Ütemhatékonyság. 1,0 alatt lemaradás. |
| **CPI** | EV / AC | Költséghatékonyság. 1,0 alatt túlköltés. |
| **EAC** | BAC / CPI | Várható végösszeg a jelenlegi hatékonysággal |

**BAC (a teljes költségbázis) = 46 130 000 Ft** (a tartalékkeret nem része).

---

## 2. Az első próbálkozás — és miért nem működött

A költségbázis (XYO-CP-107, 3. pont) **fizetési ütem szerint** készült:
mikor melyik számlát fizetjük ki. Az első EVM-számítást erre alapoztam.

| Dátum | PV (fizetési ütem) | EV | AC (kifizetve) | SPI | CPI |
|---|---:|---:|---:|---:|---:|
| 2026.04.30. | 4 434 000 Ft | 2 600 000 Ft | 4 442 000 Ft | **0,59** | **0,59** |
| 2026.05.31. | 16 096 000 Ft | 37 650 000 Ft | 15 700 000 Ft | **2,34** | **2,40** |
| 2026.06.19. | 43 930 000 Ft | 41 900 000 Ft | 38 362 000 Ft | **0,95** | **1,09** |

*Az EV mindkét számításban ugyanaz — az elvégzett munka terv szerinti értéke.
Az AC itt a kifizetett számlák összege (a Pénzügyi zárás 4. pontja szerint),
a 182 000 Ft-os, tartalékból fizetett adapterekkel együtt.*

**A CPI 0,59 → 2,40 → 1,09, az SPI 0,59 → 2,34 → 0,95 között ugrált**,
miközben a projektben semmi drámai nem történt. Ez nem információ, hanem zaj.

### Miért?

| Probléma | Magyarázat |
|---|---|
| **A PV a számlázást követi, nem a munkát** | Áprilisban a felhő-tétel teljes 30%-os részlete (4 434 000 Ft) „tervezett értékként" szerepelt, pedig a bevezetési munka csak 04.20-án indult |
| **Az AC a fizetési mérföldköveket követi** | A Cloudia 30%-os előlege 04.20-án kiment, de a munka nagy része májusban zajlott. Áprilisban „drágának és lemaradtnak", májusban „kétszer olyan hatékonynak" tűntünk |
| **A hardver értéke és kifizetése elcsúszik** | A 26 890 000 Ft-os hardver értéke a szállításkor (05.28.) egy napon jelenik meg az EV-ben, a kifizetése viszont két részletben (05.12. és 06.09.) — a május végi mutatók ezért kiugróak |

> **Ez a leggyakoribb EVM-hiba beszerzés-nehéz projekteknél.** A költségbázis
> pénzügyi célra készült (mikor mennyi pénz megy ki), az EVM viszont
> **teljesítménymérésre** való. A kettő nem ugyanaz.

---

## 3. A javítás

Két dolgot változtattunk meg — **a költségvetést nem, csak az EVM-számítás
alapját**:

1. **A PV-t szállítandó eredményekhez rendeltük**, nem fizetési dátumokhoz.
   Minden eredmény akkor „érik be", amikor a terv szerint elkészül.
2. **Az AC-t teljesítésarányosan számoljuk** (elszámolt költség), nem a
   kifizetés napja szerint.

### A költségbázis felosztása szállítandó eredményekre

| Eredmény | Budget-érték | Terv szerinti elkészülés |
|---|---:|---|
| D1 — 50 munkaállomás-készlet | 27 750 000 Ft | 2026.05.29. |
| D2–D5 — felhőkörnyezet (bevezetési szolgáltatás) | 6 500 000 Ft | 2026.05.08. (70%), 2026.06.19. (100%) |
| M365 licenc (12 hó) | 5 280 000 Ft | 2026.05.01. (aktiválás) |
| Azure infrastruktúra és VPN (12 hó) | 3 000 000 Ft | folyamatos, 05.01-től |
| Mobilinternet (12 hó) | 2 400 000 Ft | folyamatos, 05.01-től |
| D7 — oktatás és változáskezelés | 1 200 000 Ft | 2026.06.10. |
| **BAC összesen** | **46 130 000 Ft** | |

---

## 4. A javított számok

| Ellenőrzési pont | PV | EV | AC | **SPI** | **CPI** |
|---|---:|---:|---:|---:|---:|
| 2026.05.08. (M5) | 10 280 000 Ft | 10 280 000 Ft | 9 950 000 Ft | **1,00** | **1,03** |
| 2026.05.29. *(az SC-04 Steering riporthoz)* | 38 480 000 Ft | 37 650 000 Ft | 36 500 000 Ft | **0,98** | **1,03** |
| 2026.06.19. (M8) | 41 900 000 Ft | 41 900 000 Ft | 40 660 000 Ft | **1,00** | **1,03** |

### Az értékek olvasata

**SPI = 1,00 (05.08. és 06.19.)** — az ütem pontosan a terv szerint.
Az M5 és az M8 mérföldkő is határidőre teljesült.

**SPI = 0,98 (05.29.)** — 2% lemaradás. Az ok: a 2. részszállítás
2026.05.28-án megérkezett, de **12 dokkoló tápkábel hiányzott** (P-08),
ezért a D1 eredményt nem számoltuk 100%-osan elkészültnek, csak 97%-osan.
A hiány 06.02-ig pótolva; a lemaradás megszűnt.

> **Figyeld meg: a hiányos szállítást nem számoltuk késznek.** Ha 100%-nak
> vettük volna, az SPI 1,00 lett volna — és az EVM elrejtette volna, hogy
> 12 munkatárs dokkolója nem használható.

**CPI = 1,03 végig** — 3% költséghatékonysági előny. Az ok egyszerű és
egyértelmű: a **beszerzés 1 490 000 Ft-tal a terv alatt zárult**
(B1: −860 000, B2+B3: −580 000, B4: −50 000).

## 5. Előrejelzés a projekt végére

| Módszer | Számítás | Eredmény |
|---|---|---:|
| **EAC képlettel** | BAC / CPI = 46 130 000 / 1,03 | **44 786 000 Ft** |
| **Alulról felfelé** (szerződött értékek + tartalékfelhasználás) | 44 640 000 + 182 000 | **44 822 000 Ft** |
| **Eltérés a két módszer között** | | 36 000 Ft = **0,08%** |

> **A két, egymástól független módszer 0,1%-on belül egyezik.** Ez azt jelenti,
> hogy a mutatók megbízhatóak — ha 10-20% eltérés lenne, valamelyik számítás
> hibás.

| | Összeg |
|---|---:|
| Jóváhagyott keret | 52 000 000 Ft |
| Előrejelzett végösszeg | 44 822 000 Ft |
| **Várható maradvány** | **7 178 000 Ft (13,8%)** |

## 6. Trend

```
SPI                                    CPI
1,05 │                                 1,05 │
1,00 │ ●─────────────●                 1,00 │ ─ ─ ─ ─ ─ ─ ─ ─  (terv)
0,98 │      ●                          1,03 │ ●──────●──────●
0,95 │                                 0,95 │
     └──────────────────                    └──────────────────
      05.08  05.29  06.19                    05.08  05.29  06.19
```

**A trend a lényeg, nem az egyes hónap értéke.** Egyetlen mérés önmagában
félrevezető — ezért kell legalább három ellenőrzési pont.

## 7. Amit az EVM-ről megtanultunk

| Megfigyelés | Következmény |
|---|---|
| **A pénzügyi költségbázis nem alkalmas EVM-alapnak** beszerzés-nehéz projektben | Az EVM-hez külön, eredmény-alapú felosztás kell |
| **Az AC-t elszámolás, nem kifizetés szerint** kell számolni | Különben a fizetési mérföldkövek torzítanak |
| A **hiányos teljesítést nem szabad késznek számolni** | Az EVM különben elrejti a problémát (P-08) |
| A **CPI 1,03 nem érdem, hanem a beszerzés eredménye** | Ne írd magadnak, ami a szállítói versenyből jött |
| Az EVM ebben a projektben **nem tárt fel semmit, amit a heti státusz ne mutatott volna** | 50 fős pilotnál ez inkább visszaigazolás, mint korai riasztás |

> **Kell-e EVM egy ilyen méretű projektben?** Őszintén: **nem feltétlenül.**
> A 15 hetes, 46 M Ft-os projektben a heti státusz és a mérföldkő-riport
> ugyanezt megmutatta. Az EVM értéke itt két dolog volt: **objektív számot
> adott a Steering riportba**, és a 05.29-i SPI = 0,98 **kényszerített arra,
> hogy a hiányos szállítást ne söpörjük le**.
>
> Ezért szerepel a módszertanban „ajánlott" jelöléssel, nem kötelezőként.

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.06.19. |
| Az adatokat szolgáltatta | Balogh Tamás, pénzügyi kontroller | 2026.06.18. |

> **Kapcsolódó dokumentumok:** bemenete az *Ütemterv* és a *Költségvetés*;
> kimenete a *Státuszriport*, a *Steering riport* és a *Projektzáró jelentés*.
