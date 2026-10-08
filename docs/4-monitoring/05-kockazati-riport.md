# Kockázati riport (Risk Report)

**Dokumentum azonosítója:** XYO-CP-305\
**Projekt:** Xyo Cloud Pilot\
**Készíti:** Tóth Gergő, projektmenedzser\
**Gyakoriság:** kéthetente, a kockázat-felülvizsgálat után\
**Ez a kiadás:** 2026. június 12. (a 8. felülvizsgálat után)

> A kockázatnyilvántartás **vezetői kivonata**: mi változott, mi a
> legveszélyesebb most, és mit teszünk ellene.
> **A besorolás változását mutatja, nem csak az aktuális állapotot** — az a
> fontos információ, hogy egy kockázat romlik vagy javul.

---

## 1. Összkép

| | 03.13. (baseline) | 06.12. (most) | Változás |
|---|---:|---:|---:|
| Nyilvántartott kockázat | 14 | 14 | 0 |
| Nyitott, magas (≥6) | 5 | **1** | −4 |
| Nyitott, közepes (3–4) | 4 | 2 | −2 |
| Nyitott, alacsony (1–2) | 3 | 3 | 0 |
| **Lezárva** | **2** | **8** | +6 |
| Bekövetkezett | 0 | **2** | +2 |

**A kockázati profil jelentősen javult.** Az öt induló magas kockázatból
három lezárult (R1, R7, R10), egy közepesre javult (R4), egy (R5,
felhasználói ellenállás) még nyitva van, és a mérési szakaszig az is marad.

## 2. Top kockázatok most

### R5 — Felhasználói ellenállás, alacsony adaptáció

| | |
|---|---|
| **Besorolás** | 2 × 3 = **6 (magas)** |
| **Trend** | → változatlan |
| **Miért marad magas** | A siker itt nem az élesítéssel dől el, hanem a következő 3 hónapban. A C7 (elégedettség ≥4,0) és az M7 (adaptáció ≥90%) sikerkritérium a mérési szakaszban derül ki. |
| **Bekövetkezési jelzés** | A SharePoint/OneDrive aktív felhasználói arány 4 héttel az élesítés után 70% alatt |
| **Aktuális mérés (06.12.)** | 1. hullám: **94%**, 2. hullám: 88% — a jelzésküszöb felett |
| **Válaszlépések állása** | Oktatás 50/50 ✔ · Gyorssegédlet ✔ · Hypercare fut (06.15 – 07.03.) · Kéthetenkénti hírlevél ✔ |
| **Gazda** | Varga Eszter |
| **Meddig marad nyitva** | 2026.09.30. (a mérési szakasz végéig) |

### R12 — Service Desk kapacitás a hypercare alatt

| | |
|---|---|
| **Besorolás** | 2 × 2 = **4 → 2** |
| **Trend** | ↓ javul |
| **Változás oka** | A **VK-02** jóváhagyásával +1 munkatárs csatlakozott 3 hétre, költséghatás nélkül |
| **Aktuális adat** | Az 1. hullámnál 3,4 ticket/fő, a 2. hullámnál **2,1 ticket/fő** az első héten — a fajlagos terhelés csökken (a 3. hullám első hete 06.17-én zárul) |
| **Gazda** | Kiss Réka |

### R10 — A home office szabályzat nem lép hatályba 04.30-ig

| | |
|---|---|
| **Besorolás** | 2 × 3 = 6 → **lezárva** |
| **Trend** | ↓ lezárva |
| **Mi történt** | A szabályzat **2026.04.28-án hatályba lépett**, 2 nappal a határidő előtt. Az A2 feltevés igazolt. |
| **Előzmény** | 2026.04.10-én eszkaláltam (E-01), mert a HR-státusz szerint a szabályzat véleményezési körben állt. Varga Eszter 2 munkanapon belül válaszolt: a véleményezés lezárult, az aláírás 04.28-ra ütemezve. |
| **Lezárva** | 2026.04.28. |

## 3. Bekövetkezett kockázatok

Két kockázat vált problémává. **Mindkettő azonosítva volt előre.**

| # | Kockázat | Mikor következett be | Probléma | Hatás | Lezárva |
|---|---|---|---|---|---|
| **R11** | A feltételes hozzáférési szabály kizárja a felhasználókat | 2026.05.11. | P-05 | 3 tesztelő 1 napig nem tudott belépni | 05.12. |
| **R14** | A CSP partner kulcsembere kiesik | 2026.04.24. | P-02 | 0 nap csúszás | 04.28. |

### R11 részletesen — amit ebből tanulni kell

| | |
|---|---|
| **A kockázat azonosítva** | 2026.02.19., a kockázati műhelyen |
| **Válaszlépés** | „Kötelező 5 napos jelentés-mód; dokumentált break-glass fiók" |
| **A válaszlépés megtörtént?** | **Igen** — a jelentés-mód 05.04–05.08. között lefutott |
| **Mégis bekövetkezett?** | **Igen** — mert a jelentés-mód **irodai hálózaton** futott, a hiba pedig **mobilneten** jelentkezett |
| **Ok** | A mobilszolgáltató CGNAT-kimenő IP-je külföldi tartományba sorolt |
| **Következmény** | 3 tesztelő 1 napig nem tudott dolgozni; az UAT első napja csúszott |
| **Javítás** | A CA-05 szabály átállítva megbízható eszköz + MFA kombinációra (D-14) |

> **Ez nem a kockázatkezelés kudarca, hanem a leghasznosabb tanulsága.**
> A kockázatot felismertük, a válaszlépést megterveztük és végre is hajtottuk —
> de a válaszlépés **rossz környezetben futott**. A tanulság nem az, hogy
> „legyen több kockázat a listán", hanem hogy **a válaszlépéseket ugyanolyan
> gondosan kell megtervezni, mint az azonosítást**.
> → Átvezetve a Tanulságok naplójába.

### R14 részletesen — amikor a szerződés megtérült

A CSP partner egyik nevesített konzultánsa 2026.04.24-én tartós
betegállományba került. A szerződés **helyettesítési kötelezettséget** írt elő
azonos vagy magasabb minősítésű szakemberrel, a Megrendelő jóváhagyásával
(V8 vállalás az ajánlatkérésben).

**Eredmény:** a szállító 2 munkanapon belül helyettest állított, csúszás nem
történt. A kikötés nélkül a szállító azt mondhatta volna, hogy „majd ha
visszajön".

## 4. Lezárt kockázatok

| # | Kockázat | Lezárva | Miért |
|---|---|---|---|
| R1 | Laptopszállítás csúszik | 06.02. | A teljes szállítás 05.28-án megérkezett; a 12 hiányzó kábel 06.02-ig pótolva |
| R2 | A DPIA elhúzódik | 03.06. | A DPO állásfoglalása és a DPIA határidőre elkészült |
| R3 | Mobilinternet külterületen nem elegendő | 02.26. | A kijelölt 50 főből senki nem lakik érintett külterületen |
| R7 | Mentés/visszaállítás nincs rendben | 05.08. | Visszaállítási teszt sikeres: fájl 2 perc, teljes könyvtár 42 perc |
| R8 | A belső jóváhagyási kör hosszabb 8 napnál | 04.16. | A jóváhagyás 6 munkanap alatt megtörtént (E-02 eszkaláció után) |
| R10 | A home office szabályzat nem lép hatályba | 04.28. | Hatályba lépett, 2 nappal a határidő előtt |
| R11 | Feltételes hozzáférés kizárja a felhasználókat | 05.12. | Bekövetkezett és javítva |
| R14 | A CSP kulcsembere kiesik | 04.28. | Bekövetkezett, a szerződéses helyettesítés működött |

## 5. Nyitott kockázatok

| # | Kockázat | Besorolás | Trend | Gazda | Meddig |
|---|---|:-:|:-:|---|---|
| R5 | Felhasználói ellenállás, alacsony adaptáció | 6 | → | Varga Eszter | 2026.09.30. |
| R4 | Belső kapacitáshiány | 6 → **4** | ↓ | Nagy Péter | 2026.06.30. |
| R6 | Az UAT több kritikus hibát talál | 4 → 6 → **2** | ↓ | Nagy Péter | **06.19-én lezárul** |
| R12 | Service Desk kapacitás | 4 → **2** | ↓ | Kiss Réka | 2026.07.03. |
| R13 | Árfolyamhatás a licencköltségen | 2 | → | Balogh Tamás | 2027.04.30. |
| R15 | A pilotból kimaradók méltányossági kifogása | 2 → **4** | ↑ | Varga Eszter | 2026.10.09. |

### R15 — az egyetlen romló kockázat

| | |
|---|---|
| **Besorolás** | 2 × 1 = 2 → **2 × 2 = 4** |
| **Miért romlott** | A VK-01 (bővítés 65 főre) elutasítása után a logisztikai csapatban érzékelhetően nőtt a feszültség. Az első hullám kedvező tapasztalatai gyorsan terjedtek. |
| **Válaszlépés** | Papp Zsófia személyes tájékoztatást kapott (06.05.); a kiterjesztési perspektíva kommunikálva |
| **Következő lépés** | A PIR (2026.10.09.) után a kiterjesztési javaslat kommunikációja **a teljes szervezetnek**, nem csak a vezetőknek |
| **Gazda** | Varga Eszter |

> **Egy elutasított változáskérelem kockázatot teremthet.** A VK-01 döntése
> szakmailag helyes volt, de a szervezeti következményét kezelni kell — ezért
> került vissza a kockázatnyilvántartásba.

## 6. Amihez vezetői döntés kell

Jelenleg nincs. A VK-02 (Service Desk +1 fő) jóváhagyása az R12 kockázatot
kezelte; további beavatkozás nem szükséges.

## 7. Felülvizsgálati napló

| # | Dátum | Fő megállapítás |
|---|---|---|
| 1–2 | 02.19., 03.05. | A nyilvántartás felállítása, R7 magasra sorolása |
| 3 | 03.12. | Planning-kapu előtti áttekintés: 12 nyitott, 2 lezárt |
| 4 | 04.09. | R10 jelzése: a szabályzat még véleményezési körben → E-01 eszkaláció (04.10.); R8 figyelés alatt (a jóváhagyási kör aznap indult) |
| 5 | 04.28. | R14 bekövetkezett és lezárva; R10 és R8 lezárva |
| 6 | 05.13. | **R11 bekövetkezett**; R6 besorolása 4 → 6; R7 lezárva |
| 7 | 05.28. | R1 lezárása előkészítve; R12 → VK-02 |
| 8 | 06.12. | R1 lezárva; R15 romlott; R4, R6, R12 javult |

---

> **Kapcsolódó dokumentumok:** bemenete a *Kockázatnyilvántartás*; kimenete a
> *Steering riport*, a *Projektzáró jelentés* és a *Tanulságok naplója*.
