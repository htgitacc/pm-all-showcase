# Státuszriport (Status Report)

**Dokumentum azonosítója:** XYO-CP-301\
**Projekt:** Xyo Cloud Pilot\
**Készíti:** Tóth Gergő, projektmenedzser\
**Gyakoriság:** hetente, hétfőn 10:00-ig (munkaszüneti hétfő után kedden)\
**Címzettek:** projektcsapat, Kovács Anita (szponzor), Nagy Péter, Balogh Tamás

> **Mindig ugyanabban a szerkezetben.** Így az olvasó ránézésre látja, mi
> változott. Ha minden héten máshogy néz ki, senki nem fogja elolvasni.

---

## Riportnapló

| # | Hét | Státusz | Fő téma |
|---|---|:-:|---|
| SR-01 – SR-04 | 03.16 – 04.07. | 🟢 | Beszerzés indul, ajánlati szakasz |
| SR-05 | 04.13. | 🟡 | A belső jóváhagyási kör csúszni látszik |
| SR-06 – SR-08 | 04.20 – 05.04. | 🟢 | Szerződés aláírva, környezet épül |
| SR-09 | 05.11. | 🟢 | M5 teljesült, első hullám indul |
| **SR-10** | **05.18.** | **🔴** | **Két kritikus hiba az élesítés első napján** |
| SR-11 | 05.26. | 🟡 | Hibák javítva, javítási ablak megkezdve |
| SR-12 – SR-14 | 06.01 – 06.15. | 🟢 | 2. és 3. hullám, UAT újratesztelés |
| SR-15 | 06.22. | 🟢 | UAT elfogadva, zárás előkészítése |
| SR-16 | 06.29. | 🟢 | Átadás-átvétel (06.26.) után; záró jelentés, pénzügyi zárás |
| **Összesen** | **16 riport** | | |

---

# SR-10 — 2026. május 18.

## Összefoglaló státusz: 🔴 PIROS

**Indok:** az élesítés első napján (05.11.) **két kritikus (S1) hiba** merült
fel, amelyek 5 tesztelőt akadályoztak a munkában. Mindkettő javítva, de az UAT
első hete részben elveszett, és a 9 napos hibajavítási ablakra nagyobb teher
hárul.

**Javasolt beavatkozás:** nincs szükség vezetői döntésre. A javítás megtörtént,
a tartalékidőt a tervezettnek megfelelően használjuk. **Jelzem, ha a javítási
ablak nem lesz elég** — ez esetben az M7 mérföldkő kerülne veszélybe.

## Ütem

| Mérföldkő | Terv | Előrejelzés | Eltérés |
|---|---|---|---|
| M5 — környezet kész | 05.08. | **05.08. ✔ teljesült** | 0 nap |
| M6 — 1. hullám + UAT indul | 05.11. | **05.11. ✔ teljesült** | 0 nap |
| M7 — teljes 50 fő élesben | 06.12. | 06.12. | 0 nap |
| M8 — UAT lezárva | 06.19. | 06.19. | 0 nap |
| M10 — projekt lezárva | 06.30. | 06.30. | 0 nap |

**Kritikus út:** a hibajavítási ablak (05.25 – 06.02., 9 nap). Ebből eddig
**0 nap fogyott**, de 6 nyitott hiba vár javításra.

## Költség

| | Összeg |
|---|---:|
| Jóváhagyott keret | 52 000 000 Ft |
| Költségbázis (tartalék nélkül) | 46 130 000 Ft |
| **Szerződött összesen** | **44 640 000 Ft** |
| Eddig kifizetett (számlák alapján) | 15 500 000 Ft |
| **Előrejelzés a projekt végére** | **44 822 000 Ft** |
| Tartalék felhasználva | 182 000 Ft (adapterek) |
| Tartalék szabad | 4 431 000 Ft |

**A beszerzés 1 490 000 Ft-tal a terv alatt zárult.** Az előrejelzés
7 178 000 Ft maradványt mutat a kerethez képest.

## Ami elkészült a múlt héten

| WBS | Munkacsomag | Megjegyzés |
|---|---|---|
| 6.2 | Technikai teszt (10 gép) | lezárva |
| 3.3.2 | Mentés, visszaállítási teszt | **42 perc mért visszaállítási idő** teljes könyvtárra |
| 7.1 | Első hullám élesben — 10 fő | lezárva 05.13. |
| 6.3 | UAT — 1. hét | fut |

## Ami jön a jövő héten

| WBS | Munkacsomag | Határidő |
|---|---|---|
| 6.3 | UAT — 2. hét lezárása | 05.22. |
| 5.2 | Meghívók a 2–3. oktatási csoportnak (oktatás 06.01–02., a gépek érkezése után) | 05.22. |
| 3.5 | As-built dokumentáció (folyamatos) | 06.19. |

## Top 3 kockázat

| # | Kockázat | Besorolás | Változás | Megjegyzés |
|---|---|:-:|:-:|---|
| R11 | Feltételes hozzáférés kizárja a felhasználókat | 4 → **lezárva** | ↓ | **Bekövetkezett 05.11-én**, javítva 05.12-én. Lezárva. |
| R6 | Az UAT több kritikus hibát talál a tervezettnél | 4 → **6** | ↑ | 2 S1 hiba az első napon; a javítási ablak terhelése nő |
| R12 | Service Desk kapacitás a hypercare alatt | 4 | → | A kapacitásbecslés véglegesítése 05.20-ig |

## Nyitott problémák

| # | Probléma | Szint | Felelős | Határidő |
|---|---|:-:|---|---|
| P-06 | Autopilot beüzemelés 2,1 óra a célzott 1,5 helyett | S2 | Cloudia | 05.19. |
| P-07 | SharePoint keresés lassú | S2 | Cloudia | 05.27. |
| P-09 | Az első OneDrive szinkronizálás 40+ perc | S3 | Szabó Márk | 05.26. |
| P-10 | Hiányzik egy közös csapatoldal | S3 | Nagy Péter | 05.20. |

**Lezárva a múlt héten:** P-04 (bérszámfejtés VPN-en), P-05 (feltételes hozzáférés).

## Amiben segítségre van szükségem

Jelenleg nincs. Ha a hibajavítási ablak szűkösnek bizonyul, 05.29-én jelzem.

---

# SR-05 — 2026. április 13. *(részlet — a sárga státusz példája)*

## Összefoglaló státusz: 🟡 SÁRGA

**Indok:** a belső jóváhagyási kör (04.09 – 04.16.) a 3. munkanapján jár, és a
gazdasági igazgatói jóváhagyás még nem érkezett meg. A szerződéskötés
(M4, 04.17.) **a kritikus úton van, nulla pufferrel** — egyetlen nap csúszás
is továbbgyűrűzik az M5 és M6 mérföldkőre.

**Javasolt beavatkozás:** Kovács Anitának ma jelzem az időkritikusságot.
Ha 04.15-ig nem születik döntés, **eszkalálom Horváth Júliához**.

> **Miért sárga ez, ha még semmi nem csúszott?** Mert a sárga státusz
> **előrejelzés**, nem utólagos megállapítás. Ha megvárnám a tényleges
> csúszást, már nem lenne mit tenni. → Az eszkaláció 04.13-án megtörtént
> (E-02), és a jóváhagyás 04.16-án megérkezett.

---

## Amit a riportálásról megtanultunk

| Megfigyelés | Következmény |
|---|---|
| **Az SR-10 pirosra írása nem okozott bajt.** A szponzor a következő napon felhívott, hogy mit tud segíteni. | A rossz hír korai jelzése bizalmat épít, nem rombol |
| A **fix szerkezet** miatt a szponzor 2 perc alatt elolvasta | 1 oldal, mindig azonos sorrendben |
| A „Top 3 kockázat" oszlopa **a besorolás változását** mutatja, nem csak az állapotot | Ez mondja meg, mi romlik és mi javul |
| A „Amiben segítségre van szükségem" rovat üresen is szerepel | Ha csak akkor jelenik meg, amikor baj van, riasztásnak hat |

> **A vízesés-riport csapdája:** ha hetekig zöldet írsz, majd hirtelen pirosat,
> elveszted a hitelességedet. Ebben a projektben 16 riportból **1 piros és
> 2 sárga** volt — mindhárom akkor, amikor a helyzet indokolta.

---

> **Kapcsolódó dokumentumok:** bemenete a *Projektterv*, az *Ütemterv*, a
> *Költségvetés*, a *Munkacsomag-kiadás*, a *Kockázatnyilvántartás*, a
> *Problémanapló*, a *Kommunikációs terv* és a *Meeting jegyzőkönyvek*;
> kimenete a *Steering riport* és a *Projektzáró jelentés*.
