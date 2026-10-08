# Kockázatnyilvántartás (Risk Register)

**Dokumentum azonosítója:** XYO-CP-110\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Létrehozva:** 2026.02.19-i kockázati műhelyen\
**Utolsó felülvizsgálat:** 2026.06.12. (8. felülvizsgálat)\
**Verzió:** 1.8 — **élő dokumentum**, kéthetente felülvizsgálva

> **Verziójegyzet:** a nyertes szállító neve (TechLine Zrt.) a szerződéskötés után, 2026.04.20-án került a dokumentumba. A korábbi változatban a beszerzési tételek (B1–B4) szerepeltek; a baseline tartalma — hatókör, ütem, költség — ezzel nem változott.

---

## 1. Értékelési skála

| Valószínűség | Jelentése | Hatás | Jelentése |
|---|---|---|---|
| 1 — alacsony | < 20% | 1 — alacsony | < 3 nap csúszás vagy < 500 e Ft |
| 2 — közepes | 20–50% | 2 — közepes | 3–10 nap vagy 500 e – 2 M Ft |
| 3 — magas | > 50% | 3 — magas | > 10 nap vagy > 2 M Ft, vagy a cél veszélybe kerül |

**Besorolás = valószínűség × hatás.** 6 vagy fölötte: **magas**, a Steering
riportba is bekerül. 3–4: közepes. 1–2: alacsony, csak figyeljük.

> **A szakaszok a baseline (03.12.) besorolást követik.** Ami azóta történt —
> átsorolás, bekövetkezés, lezárás —, az a kockázat státuszában áll, dátummal.
> Így egyszerre látszik, honnan indult a kockázat, és hol tart most.

---

## 2. Magas besorolású kockázatok

### R1 — A laptopszállítás csúszik

| | |
|---|---|
| **Kategória** | szállítói |
| **Leírás** | A TechLine Zrt. a 6 hetes szállítási időt nem tartja, így a tesztgépek nem érkeznek meg 2026.05.06-ig |
| **Valószínűség × hatás** | 2 × 3 = **6 (magas)** |
| **Hatás** | Az M6 (első hullám) és minden utána következő mérföldkő tolódik; a kritikus úton nincs puffer |
| **Stratégia** | **Csökkentés + átadás** |
| **Válaszlépések** | 1) A szerződésben **részszállítás**: 10 gép 05.06-ig, 40 gép 05.29-ig. 2) Kötbér a késedelemre. 3) Az ajánlatkérésben készlethelyzet igazolása kötelező. 4) Kétheti szállítói státusz írásos jegyzőkönyvvel. |
| **Bekövetkezési jelzés** | A szállító a kétheti státuszon nem tudja megerősíteni a részszállítás dátumát, vagy „gyártói készlethiányra" hivatkozik |
| **Kockázatgazda** | Molnár Katalin |
| **Határidő** | folyamatos, M7-ig |
| **Státusz** | **lezárva 2026.06.02.** — mind a 40 gép 05.28-án, 1 nappal a határidő előtt megérkezett; a 12 hiányzó tápkábel 06.02-re pótolva (P-08) |

### R2 — Az adatvédelmi hatásvizsgálat elhúzódik

| | |
|---|---|
| **Kategória** | jogi / megfelelőségi |
| **Leírás** | Az Intune eszközfelügyelet miatt DPIA szükséges, és a folyamat hosszabb a tervezettnél |
| **Valószínűség × hatás** | 2 × 3 = **6 (magas)** |
| **Hatás** | A beszerzés nem indítható el, a teljes ütemterv csúszik |
| **Stratégia** | **Elkerülés** — korai indítás |
| **Válaszlépések** | 1) A DPO megkeresése már 2026.02.12-én megtörtént, 5 hét ráhagyással. 2) Az adatkezelési leírás előre elkészült. 3) Ha a DPIA nem zárul le 03.20-ig, a beszerzés a hardverre külön indítható (nem érinti a DPIA). |
| **Bekövetkezési jelzés** | A DPO 03.06-ig nem ad írásos állásfoglalást |
| **Kockázatgazda** | dr. Fekete Zsolt / Tóth Gergő |
| **Határidő** | 2026.03.20. |
| **Státusz** | **lezárva 2026.03.06.** — az állásfoglalás megérkezett, a DPIA elkészült, nem okozott csúszást |

### R4 — Belső kapacitáshiány

| | |
|---|---|
| **Kategória** | erőforrás |
| **Leírás** | Az IT-ról 2 fő (Nagy Péter, Szabó Márk) a napi munkája mellett dolgozik a projekten; egy üzemi tűzoltás kiveszi őket |
| **Valószínűség × hatás** | 3 × 2 = **6 (magas)** |
| **Hatás** | A 3.x munkacsomagok csúsznak; a minőség romlik |
| **Stratégia** | **Csökkentés + átadás** |
| **Válaszlépések** | 1) A bevezetés 312 órányi munkáját a CSP partner végzi, nem a belső csapat. 2) Írásos kapacitás-jóváhagyás Nagy Pétertől (heti 12 óra Szabó Márkra). 3) A kritikus úton lévő 3.1.x és 3.2.2 munkacsomag felelőse a szállító, nem Szabó Márk. |
| **Bekövetkezési jelzés** | Szabó Márk két egymást követő heti státuszon nem tud haladást jelenteni |
| **Kockázatgazda** | Nagy Péter |
| **Határidő** | folyamatos |
| **Státusz** | nyitva — **06.12.: 2 × 2 = 4** (közepes); a kialakítás és a teszt lezárult, a belső terhelés csökkent |

### R5 — Felhasználói ellenállás, alacsony adaptáció

| | |
|---|---|
| **Kategória** | szervezeti |
| **Leírás** | A pilot résztvevői nem használják az új környezetet, visszaszoknak a régi munkamódszerre (helyi mentés, e-mailben küldött dokumentumok) |
| **Valószínűség × hatás** | 2 × 3 = **6 (magas)** |
| **Hatás** | Az M7 (adaptáció ≥ 90%) és a C7 (elégedettség ≥ 4,0) sikerkritérium nem teljesül; a kiterjesztési döntés megalapozatlan lesz |
| **Stratégia** | **Csökkentés** |
| **Válaszlépések** | 1) Oktatás célcsoportonként, 5 csoportban. 2) Felhasználói gyorssegédlet. 3) 3 hetes hypercare. 4) Kéthetenkénti hírlevél. 5) Az adaptációs mutató havi mérése már a hypercare alatt. |
| **Bekövetkezési jelzés** | A SharePoint/OneDrive aktív felhasználói arány 4 héttel az élesítés után 70% alatt |
| **Kockázatgazda** | Varga Eszter |
| **Határidő** | 2026.09.30. (a mérési szakasz végéig) |
| **Státusz** | nyitva — változatlanul 6; a mérési szakaszban dől el |

### R7 — A mentés/visszaállítás nincs rendben

| | |
|---|---|
| **Kategória** | technikai |
| **Leírás** | Elterjedt tévhit, hogy „a felhő magától ment". A OneDrive/SharePoint megőrzése nem azonos a kipróbált visszaállítással. |
| **Valószínűség × hatás** | 2 × 3 = **6 (magas)** — 03.03-án, az A7 feltevés megdőlése után felvéve |
| **Hatás** | Adatvesztésnél nincs bizonyítottan működő visszaállítás; az M10 cél és az üzembe adás veszélybe kerül |
| **Stratégia** | **Csökkentés** |
| **Válaszlépések** | Kötelező visszaállítási teszt a 3.3.2 kész-definíciójában (egy fájl és egy teljes könyvtár), mért idővel |
| **Bekövetkezési jelzés** | A visszaállítási teszt 05.08-ig nem fut le sikeresen |
| **Kockázatgazda** | Szabó Márk |
| **Határidő** | 2026.05.08. |
| **Státusz** | **lezárva 2026.05.08.** — a visszaállítási teszt sikeres: egy fájl 2 perc, teljes könyvtár 42 perc |

### R10 — A home office szabályzat nem lép hatályba 04.30-ig

| | |
|---|---|
| **Kategória** | szervezeti |
| **Leírás** | A szabályzat az üzemi tanácsi véleményezés és a HR-jóváhagyás miatt nem lép hatályba az élesítés előtt |
| **Valószínűség × hatás** | 2 × 3 = **6 (magas)** — a hatás 03.11-én 2-ről 3-ra emelve, az üzemi tanács kikötése után |
| **Hatás** | A pilot résztvevői nem dolgozhatnak otthonról — a projekt fő üzleti célja (H2, M6) nem teljesülhet |
| **Stratégia** | **Csökkentés** |
| **Válaszlépések** | Havi HR-státusz; ha csúszik, az élesítés első hulláma irodai munkával is indítható |
| **Bekövetkezési jelzés** | A szabályzat 04.15-ig nincs aláírásra kész állapotban |
| **Kockázatgazda** | Varga Eszter |
| **Határidő** | 2026.04.30. |
| **Státusz** | **lezárva 2026.04.28.** — a szabályzat hatályba lépett, 2 nappal a határidő előtt (E-01) |

---

## 3. Közepes besorolású kockázatok

| # | Kockázat | Kategória | V × H | Válaszlépés | Gazda | Státusz |
|---|---|---|:-:|---|---|---|
| R3 | A mobilinternet külterületen nem elegendő | technikai | 2 × 2 = 4 | A kijelölésnél a lakóhely vizsgálata (F-1); egyedi esetben fix internet-hozzájárulás a tartalékból | Varga Eszter | **lezárva 02.26.** — a kijelölt 50 főből senki nem lakik érintett külterületen |
| R6 | Az UAT több kritikus hibát talál a tervezettnél | minőségi | 2 × 2 = 4 | Az UAT párhuzamosan fut az első hullám élesítésével, nem utána; 9 napos javítási ablak | Nagy Péter | nyitva — **05.13.: 2 × 3 = 6** (2 S1 hiba az első napon); **06.12.: 1 × 2 = 2**; az UAT-elfogadással (06.19.) lezárul |
| R8 | A belső jóváhagyási kör hosszabb 8 napnál | eljárási | 2 × 2 = 4 | A pénzügy előre értesítve a várható időpontról; a beszerzési vezető követi | Molnár Katalin | **lezárva 04.16.** — a jóváhagyás 6 munkanap alatt megtörtént (E-02) |
| R11 | A feltételes hozzáférési szabály kizárja a felhasználókat | technikai | 2 × 2 = 4 | Kötelező 5 napos jelentés-mód; dokumentált break-glass fiók | Szabó Márk | **bekövetkezett 05.11.** (P-05) — javítva, **lezárva 05.12.** |
| R12 | A Service Desk kapacitása nem elég a hypercare alatt | erőforrás | 2 × 2 = 4 | Közös kapacitásbecslés 04.10-ig; szükség esetén +1 fő ideiglenesen | Kiss Réka | nyitva — **06.12.: 1 × 2 = 2** (VK-02: +1 fő 3 hétre) |

## 4. Alacsony besorolású, figyelt kockázatok

| # | Kockázat | V × H | Miért csak figyeljük | Státusz |
|---|---|:-:|---|---|
| R13 | Árfolyamhatás a licencköltségen | 2 × 1 = 2 | Legfeljebb 422 e Ft, belefér a mozgástérbe | nyitva |
| R14 | A CSP partner kulcsembere kiesik | 1 × 2 = 2 | A szerződés helyettesítési kötelezettséget ír elő | **bekövetkezett 04.24.** (P-02) — 2 munkanapon belül helyettes, **lezárva 04.28.** |
| R15 | A pilotból kimaradók méltányossági kifogása | 2 × 1 = 2 | A kijelölési szempontok előre kommunikálva (D2 döntés) | nyitva — **06.12.: 2 × 2 = 4** (a VK-01 elutasítása után) |

## 5. Felülvizsgálati napló

| Dátum | Változás | Ki |
|---|---|---|
| 2026.02.19. | A nyilvántartás létrehozása a kockázati műhelyen — 13 kockázat | Tóth Gergő |
| 2026.02.26. | **R3 lezárva** — a kijelölt kör lakóhelye rendben | Varga Eszter |
| 2026.03.03. | R7 felvétele magasra sorolva (az A7 feltevés megdőlése után óvatosabbak lettünk a technikai feltevésekkel) | Tóth Gergő |
| 2026.03.06. | **R2 lezárva** — DPO állásfoglalás megérkezett, DPIA elkészült | Tóth Gergő |
| 2026.03.11. | R10 hatása 2-ről 3-ra emelve — az üzemi tanács kikötése után a szabályzat kritikusabb lett | Varga Eszter |
| 2026.03.12. | Felülvizsgálat a Planning-kapu előtt; 14 kockázat: 12 nyitott (5 magas, 4 közepes, 3 alacsony), 2 lezárt | Tóth Gergő |
| 2026.04.09. | 4. felülvizsgálat: R10 jelzése (a szabályzat még véleményezési körben) → E-01 eszkaláció 04.10-én; R8 figyelés alatt | Tóth Gergő |
| 2026.04.28. | 5. felülvizsgálat: **R14 bekövetkezett** (04.24.) és lezárva; R10 és R8 lezárva | Tóth Gergő |
| 2026.05.13. | 6. felülvizsgálat: **R11 bekövetkezett** (05.11.) és lezárva; R6 4 → 6; R7 lezárva (05.08.) | Tóth Gergő |
| 2026.05.28. | 7. felülvizsgálat: R1 lezárása előkészítve (a 40 gép megérkezett); R12 → VK-02 | Tóth Gergő |
| 2026.06.12. | 8. felülvizsgálat: R1 lezárva (06.02.); R15 2 → 4; R4 6 → 4, R6 6 → 2, R12 4 → 2. Állapot: 6 nyitott (1 magas, 2 közepes, 3 alacsony), 8 lezárt, ebből 2 bekövetkezett | Tóth Gergő |

## 6. Amit a kockázati műhelyen tanultunk

**A „bekövetkezési jelzés" mező tette használhatóvá a nyilvántartást.**
Az első vázlatban csak valószínűség és hatás szerepelt, ami statikus lista.
Amikor minden kockázathoz megfogalmaztuk, **mi az a konkrét jel, amiből előre
látjuk**, hogy baj lesz — a nyilvántartás figyelőrendszerré vált.

Például R1-nél: nem azt figyeljük, hogy „megjött-e a laptop", hanem azt, hogy
**a szállító a kétheti státuszon meg tudja-e erősíteni a részszállítás dátumát.**
Ez 3-4 héttel korábbi jelzés.

---

> **Kapcsolódó dokumentumok:** bemenete a *Feltevés- és korlátnapló*, az
> *Érintettek nyilvántartása* és az *Erőforrásterv*; kimenete a
> *Kockázati riport*, a *Státuszriport*, a *Problémanapló* és a
> *Tanulságok naplója*.
