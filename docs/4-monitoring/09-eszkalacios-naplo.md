# Eszkalációs napló (Escalation Log)

**Dokumentum azonosítója:** XYO-CP-309\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Utolsó frissítés:** 2026. június 19.\
**Verzió:** 1.2 — **élő dokumentum**

> **Ez az egyik legerősebb védőiratod.** Bizonyítja, hogy időben jelezted a
> problémát — akkor is, ha a döntés késett vagy elmaradt.
>
> **Az eszkaláció a munkád része, nem a kudarcod.** A késve eszkalált
> probléma viszont már a te hibád.

---

## 1. Eszkalációk

### E-01 — A home office szabályzat hatályba lépése

| | |
|---|---|
| **A probléma** | A HR-státusz szerint a home office szabályzat véleményezési körben áll; a tervezett hatályba lépés 2026.04.30. A szabályzat nélkül a résztvevők **jogilag rendezetlen helyzetben** dolgoznának otthonról. |
| **Kapcsolódó kockázat / feltevés** | R10 (magas) / A2 feltevés |
| **Mikor vettem észre** | 2026.04.09., a havi HR-státusz lekérdezésekor |
| **Kinek jeleztem** | Varga Eszter (HR vezető), majd másolatban Kovács Anita |
| **Mikor** | **2026.04.10.**, e-mailben |
| **Mit kértem** | Írásos visszajelzést arról, hogy a szabályzat 04.30-ig hatályba lép-e; ha nem, mi a legkorábbi reális dátum |
| **Miért nem vártam tovább** | Az első élesítési hullám 05.11-én indul. Ha a szabályzat nincs kész, az első hullámot irodai munkavégzéssel kellett volna indítani — ezt 3 héttel előre kellett tudni. |
| **Válasz** | Varga Eszter, 2026.04.14.: a véleményezés lezárult, az aláírás 04.28-ra ütemezve |
| **Eredmény** | **A szabályzat 2026.04.28-án hatályba lépett**, 2 nappal a határidő előtt. Az A2 feltevés igazolt, az R10 kockázat lezárva. |
| **Válaszidő** | 2 munkanap (04.10. péntek → 04.14. kedd) |
| **Státusz** | **lezárva** — 2026.04.28. |

---

### E-02 — A belső jóváhagyási kör csúszni látszik

| | |
|---|---|
| **A probléma** | A szerződéskötés belső jóváhagyási köre (04.09 – 04.16., 6 munkanap) a 3. munkanapján járt, és a gazdasági igazgatói jóváhagyás nem érkezett meg. Az M4 mérföldkő (04.17.) **a kritikus úton van, nulla pufferrel**. |
| **Kapcsolódó kockázat** | R8 (közepes) |
| **Mikor vettem észre** | 2026.04.13., a heti státuszriport készítésekor |
| **Kinek jeleztem** | Kovács Anita (szponzor) |
| **Mikor** | **2026.04.13.**, e-mailben + telefonon |
| **Mit kértem** | A jóváhagyás 04.15-ig történjen meg; ha akadálya van, jelezze, hogy Horváth Júliához fordulhassak |
| **Amit hozzátettem** | A késés következménye számszerűen: 1 nap csúszás az M4-en → 1 nap az M5-ön → a tesztelés 05.11-i indulása kerül veszélybe → az M7 és M10 is |
| **Válasz** | Kovács Anita, 2026.04.13.: a jóváhagyás a hét végéig megtörténik |
| **Eredmény** | **A jóváhagyás 2026.04.16-án megérkezett**; a szerződés 04.17-én aláírva, határidőre |
| **Válaszidő** | aznap |
| **Státusz** | **lezárva** — 2026.04.16. |

> **Ez a jó eszkaláció mintája:** nem azt írtam, hogy „csúszik a jóváhagyás",
> hanem hogy **mi a következménye számokban, mit kérek, és mikorra**.
> A szponzornak így nem kellett utánajárnia, hogy komoly-e a helyzet.

---

### E-03 — Három felhasználó nem tud belépni

| | |
|---|---|
| **A probléma** | Az első élesítési hullám napján 3 tesztelő nem tudott belépni otthonról. Kritikus (S1) hiba, a feltételes hozzáférési szabály zárta ki őket. |
| **Kapcsolódó kockázat** | R11 (közepes) — **bekövetkezett** |
| **Mikor vettem észre** | 2026.05.11., 10:15 — a Service Desk jelezte |
| **Kinek jeleztem** | Nagy Péter (szakmai vezető) |
| **Mikor** | **2026.05.11., 10:40** — 25 perccel a bejelentés után |
| **Miért Nagy Péterhez** | Biztonsági beállítás módosításáról van szó. Az összeghatár a hatáskörömben lenne, de **biztonsági szintet érintő döntést nem hozok egyedül.** |
| **Mit kértem** | Döntést arról, hogy a CA-05 szabály módosítható-e, és milyen helyettesítő védelemmel |
| **Kit vontunk be** | dr. Fekete Zsolt (DPO), adatvédelmi szempontból |
| **Válasz** | Nagy Péter, 2026.05.11., 15:20: a módosítás jóváhagyva megbízható eszköz + MFA + kockázatalapú újrahitelesítés kombinációval (D-14) |
| **Eredmény** | A javítás 2026.05.12-én megtörtént; 05.13 – 05.22. között további kizárás nem történt |
| **Válaszidő** | 4 óra 40 perc |
| **Státusz** | **lezárva** — 2026.05.12. |

---

### E-04 — A hibajavítási ablak szűkössége *(figyelmeztető jelzés)*

| | |
|---|---|
| **A probléma** | Az UAT első köre 81,5%-on zárult (a kilépési feltétel 95%), 6 nyitott hibával. A javítási ablak 9 nap, puffer nélkül. |
| **Mikor vettem észre** | 2026.05.22., az UAT első körének zárásakor |
| **Kinek jeleztem** | Kovács Anita és Nagy Péter |
| **Mikor** | **2026.05.26.**, a heti státuszriportban (SR-11) és külön e-mailben |
| **Mit jeleztem** | Nem kértem döntést. **Előre jeleztem, hogy ha 06.02-ig nem zárul le a javítás, az M7 mérföldkő csúszik** — és hogy 05.29-én adok visszajelzést arról, tartható-e. |
| **Visszajelzés 05.29-én** | A 6 nyitott hibából 3 javítva (H-03, H-07, H-11). A közben, 05.28-án érkezett H-04 (hiányzó tápkábelek) pótlását a szállító 06.03-ig vállalta. A H-06 oka szolgáltatói lefedettség, kezelése nem a javítási ablakban történik; a maradék 2 S3–S4 hiba nem akadályozza az újratesztelést → az M7 tartható |
| **Eredmény** | A javítás 06.02-ig lezárult; az újratesztelés 06.16-án 96,3%-on zárt; az M8 határidőre teljesült |
| **Státusz** | **lezárva** — 2026.06.02. |

> **Ez nem klasszikus eszkaláció volt, hanem előrejelzés.** Nem kértem
> döntést, csak jeleztem a kockázatot és megígértem egy konkrét visszajelzési
> időpontot. **Így a szponzort nem érte volna meglepetés**, ha mégis csúszunk —
> és nem kellett feleslegesen döntenie sem.

---

## 2. Összesítés

| | Darab |
|---|---:|
| Eszkaláció összesen | 4 |
| Ebből döntést kért | 3 (E-01, E-02, E-03) |
| Ebből előrejelzés volt | 1 (E-04) |
| **Válasz nélkül maradt** | **0** |
| Átlagos válaszidő a 3 döntéskérésre | 0,7 munkanap |
| Eszkaláció miatt elmaradt csúszás | 2 mérföldkő (M4, M5) |

| Eszkalációs szint | Darab | Kihez |
|---|---:|---|
| 2. szint — szakmai vezető | 1 | Nagy Péter |
| 3. szint — szponzor | 3 | Kovács Anita |
| 4. szint — Steering Committee | 0 | — |

**Egyetlen eszkaláció sem jutott el a Steering Committee-ig** — mindegyik
megoldódott alacsonyabb szinten.

> **Az átlagos válaszidő a három döntéskérésből számol:** E-01 2 munkanap,
> E-02 és E-03 aznap (0) → (2 + 0 + 0) / 3 ≈ 0,7 munkanap. Az E-04 nem kért
> döntést, ezért válaszideje sincs — ha beszámítanád, a mutató a saját
> visszajelzésedet mérné, nem a döntéshozókét. Mindhárom válasz belefért az
> eszkalációs út előírt határidejébe (2. szint: 2, 3. szint: 3 munkanap).

## 3. Amit a projekt alatt NEM eszkaláltam, és miért

Ez a rész is fontos: megmutatja, hol húztam meg a határt.

| # | Helyzet | Miért nem eszkaláltam |
|---|---|---|
| 1 | 12 hiányzó dokkoló tápkábel (P-08) | A szállító a helyszínen elismerte és határidőt vállalt; a visszatartott fizetés elég nyomás volt. **Ha a pótlás 06.03-ig nem érkezik meg, aznap eszkaláltam volna.** |
| 2 | A CSP-konzultáns kiesése (P-02) | A szerződés helyettesítési kötelezettsége automatikusan kezelte; nem volt döntést igénylő kérdés |
| 3 | Az Autopilot beüzemelési idő (QC-02) | Szakmai probléma, a szállító hatáskörében; a 40 gépes élesítésig (06.03.) 26 nap volt hátra |
| 4 | A SharePoint keresés lassúsága (P-07) | S2 hiba, megkerülő megoldással; nem veszélyeztetett mérföldkövet |

> **Az eszkaláció akkor jó, ha ritka és indokolt.** Ha mindent felviszel,
> a szponzor megszokja, és a valóban fontos jelzést is átlapozza.
> **Négy eszkaláció 15 hét alatt** — ez az arány működött.

## 4. Amit az eszkalációról megtanultunk

| Megfigyelés | Következmény |
|---|---|
| **Az eszkaláció mindig javaslattal ment**, nem csak problémával | „Ez a probléma, ezt javaslom, ehhez a te döntésed kell" |
| A **következményt számokban** írtam le (hány nap, melyik mérföldkő) | A döntéshozónak nem kellett utánajárnia, komoly-e |
| Az E-03-nál **nem éltem a saját hatáskörömmel** | Biztonsági szintet érintő döntést a szakmai vezető hoz, DPO-véleménnyel — az összeghatár nem minden |
| Az E-04 **előrejelzés volt, nem kérés** | Így a szponzort nem érte volna meglepetés, és nem is kellett döntenie |
| **Minden eszkalációt dátummal és időponttal rögzítettem** | Ha nem érkezett volna válasz, ez bizonyította volna, hogy jeleztem |

> **Ha nem kapsz választ, azt is jegyezd fel dátummal, és küldj emlékeztetőt.**
> A válasz nélkül maradt eszkaláció is dokumentált eszkaláció — és vita esetén
> pontosan ez véd meg.

---

| Szerep | Név | Dátum |
|---|---|---|
| Vezeti | Tóth Gergő, projektmenedzser | 2026.06.19. |

> **Kapcsolódó dokumentumok:** bemenete a *Problémanapló* és a *RACI mátrix*;
> kimenete a *Tanulságok naplója* és a *Projektzáró jelentés*.
