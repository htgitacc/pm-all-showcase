# Változásengedélyezési modell — szabványos, normál és sürgős változás

**Dokumentum azonosítója:** XYO-ITIL-003\
**Szolgáltatás:** Felhőalapú munkahely (XYO-ITIL-001)\
**Készítette:** Szabó Márk, rendszergazda, Tóth Gergővel\
**Változásengedélyező:** Nagy Péter, IT osztályvezető\
**Dátum:** **2026. június 19.** — az UAT elfogadásának napja\
**Verzió:** 1.0

> ⚠ **ITIL 4-kiegészítés.** A Xyo **Változáskezelési eljárása** (XYO-CP-115) a **projekt**
> hatókörének, ütemtervének és költségének változásait kezeli. Arra a kérdésre, hogy **ki
> módosíthatja az éles konfigurációt**, és milyen ellenőrzés után, nincs szabálya — a projekt
> idején ezt a Cloudia Solutions és Szabó Márk szakmai döntése fedte le.
>
> **Miért éppen ma?** Ezen a napon szűnik meg a Cloudia Solutions Intune-adminisztrátori joga
> (Szerződés 3.4). **Mától minden éles változás a Xyo felelőssége** — és egy 50 fős,
> egyetlen rendszergazdával dolgozó IT-nál ennek egyszerűnek kell lennie, különben senki nem
> tartja be.

---

## 1. Két eljárás, két kérdés

A két eljárás nem versenytársa egymásnak: **más kérdésre válaszolnak**, és egy élesítési
hullám alatt mindkettő él.

| | Projekt-változáskezelés (XYO-CP-115) | **Változásengedélyezés (ITIL 4)** |
|---|---|---|
| Mit véd | A jóváhagyott **baseline**-t: hatókör, ütem, költség, átvételi kritériumok | Az **éles szolgáltatást**: hogy működjön a változás után is |
| A fő kérdés | **Megéri-e?** Mibe kerül, mennyit csúszik? | **Biztonságos-e?** Mi romolhat el, és hogyan állunk vissza? |
| Ki dönt | PM / szponzor / Projekt Irányító Bizottság, összeghatár szerint | **Változásengedélyező**, a kockázat szerint |
| Nyilvántartás | Változásnapló (VK-01 – VK-04) | **Változási nyilvántartás** (CH-001-től, 7. pont) |
| Meddig él | A projekt zárásáig | **A szolgáltatás élettartamáig** |

> **A változásnapló 4. pontja pontosan a kettő határán van.** A projekt öt módosításról
> állapította meg — helyesen —, hogy **nem kell hozzá projekt-változáskérelem**. Az ITIL
> szemével viszont ugyanezek közül négy **éles változás** volt, egy pedig nem az.

| # (Változásnapló 4.) | Módosítás | Projekt: kell CR? | **ITIL: milyen változás?** |
|---|---|---|---|
| 1 | A CA-05 feltételes hozzáférési szabály átalakítása | nem (D-14) | **Sürgős** — három felhasználó nem tudott belépni; biztonsági szabály lazítása |
| 2 | Az ügyviteli kliens telepítési módja kötelezőről opcionálisra | nem (D-15) | **Normál** — az Intune alkalmazáscsomag módosítása |
| 3 | A `CP-Kozos` csapatoldal létrehozása | nem (D-16) | **Normál** az első alkalommal; utána **szabványos** lehet |
| 4 | Az OneDrive előszinkronizálás bevezetése a kiosztás előtt | nem (D-17) | **Normál** — a telepítési eljárás változása |
| 5 | Az oktatás 2. blokkjának bővítése 25-ről 30 percre | nem | **Nem éles változás** — a szolgáltatás konfigurációját nem érinti |

> **A tanulság:** a projekt összeghatárral és hatókörrel szűr (1 000 000 Ft, 3 nap,
> mérföldkő). Az éles környezetben a szűrő a **kockázat**: egy ingyenes, egyperces
> szabálymódosítás 50 embert zárhat ki. A CA-05-nél a projekt is érezte ezt: „Biztonsági
> vonatkozása miatt viszont a szakmai vezető döntött, nem a PM, DPO-véleménnyel.”
> (Változásnapló 4. pont). Ez már változásengedélyezés volt, csak nem így hívták.

## 2. A három változástípus

| Típus | ITIL-név | Mikor | Ki engedélyezi | Hogyan |
|---|---|---|---|---|
| **Szabványos** | *Standard change* | Alacsony kockázatú, gyakori, jól ismert lépés, **leírt eljárással** | **Előre engedélyezett** — a végrehajtó a listán szereplő eljárás szerint dolgozik | Ticket a Service Desk-rendszerben; nem kell egyenként engedélyezni |
| **Normál** | *Normal change* | Minden, ami nem szabványos és nem sürgős | **Nagy Péter**; biztonsági vagy adatvédelmi hatásnál dr. Fekete Zsolt véleményével | Változási kérelem, értékelés, engedély, ütemezés |
| **Sürgős** | *Emergency change* | Amit **azonnal** végre kell hajtani: biztonsági esemény, szolgáltatáskiesés, a felhasználók kizárása | **Nagy Péter**, telefonon is; ha nem érhető el, Kovács Anita | Végrehajtás után 24 órán belül írásban rögzítve, a következő heti egyeztetésen utólag átnézve |

> **Miért nincs változásügyi testület (CAB)?** Az ITIL 4 nem írja elő: azt mondja, hogy a
> **változásengedélyező** (*change authority*) legyen a változás kockázatához illő szinten. Egy
> 50 fős pilotnál ez egy ember (Nagy Péter) és egy **heti tizenöt perces egyeztetés** Szabó
> Márkkal. A 190 fős kiterjesztésnél újra kell gondolni — de akkor is a kockázat, nem a
> szervezeti díszlet szerint.

## 3. Szabványos változások — az előre engedélyezett lista

Ezek a Run-book rendszeres feladataiból és a 15 leggyakoribb esetből jönnek. **A lista csak
akkor bővíthető, ha az új lépés legalább háromszor normál változásként hiba nélkül lefutott**,
és az eljárása le van írva.

| # | Szabványos változás | Eljárás | Ki hajthatja végre | Forrás |
|---|---|---|---|---|
| SV-1 | Új belépő munkába állítása (gép regisztrálása, csoportba sorolás) | Autopilot-folyamat, ≈1,5 óra | Szabó Márk | Run-book 4. pont, 12. eset |
| SV-2 | Kilépő fiókjának letiltása, adatmegőrzés 30 napig | Fiók letiltása; a törlés 30 nap után | Szabó Márk — a törléshez Nagy Péter jóváhagyásával | Run-book 4. pont, 13. eset |
| SV-3 | MFA-újraregisztrálás | A felhasználó azonosítása után | Service Desk (Kiss Réka + 2 fő) | Run-book 4. pont, 4. eset |
| SV-4 | VPN-kliensprofil újratöltése egy gépen | Előre konfigurált profil | Szabó Márk | Run-book 4. pont, 5. eset |
| SV-5 | Licenc kiosztása vagy visszavétele (az 50-es kereten belül) | Havi licencellenőrzés szerint | Szabó Márk | Run-book 3. pont |
| SV-6 | Break-glass fiók féléves tesztje jelszócserével | Bejelentkezés, jelszócsere, új boríték, jegyzőkönyv | Szabó Márk | Run-book 2. és 3. pont |

> **A kilépő esete (SV-2) mutatja a különbséget az engedély és a jóváhagyás között.** A
> letiltás szabványos változás: nem kell hozzá változásengedélyezés. Az adatok **törlése**
> viszont üzleti döntés, amit Nagy Péter hagy jóvá — ez a kérés része, nem a változásé.

**Nem változás, csak üzemeltetési tevékenység:** a havi mentés-ellenőrzés, a megfelelőségi és
MFA-riport, a licencfelhasználás átnézése — ezek nem módosítják a konfigurációt. A **negyedéves
feltételes hozzáférési felülvizsgálat** sem változás; ha módosítást javasol, az **normál
változásként** megy tovább.

## 4. Normál változások

**Mi tartozik ide a Xyo-nál:** a feltételes hozzáférési szabályok (CA-01 – CA-05), az Intune
eszközprofiljai és alkalmazáscsomagjai, a VPN elérhető erőforrásai, a csapatoldalak
létrehozása és a megőrzési szabályok módosítása.

### 4.1 A változási kérelem kötelező tartalma

| # | Kérdés | Miért |
|---|---|---|
| 1 | **Mit változtatunk, és miért?** | A változás célja, a kapcsolódó ticket vagy fejlesztési javaslat |
| 2 | **Kit érint?** | Hány felhasználó, melyik csapat, milyen hálózatról dolgoznak |
| 3 | **Hogyan teszteltük?** | Feltételes hozzáférésnél: **jelentés-mód, a valós használati környezetben** — irodai hálózaton *és* mobilneten |
| 4 | **Hogyan állunk vissza?** | A visszaállítás lépései és időigénye — mielőtt elkezdjük |
| 5 | **Mikor hajtjuk végre?** | A szolgáltatási időn kívül (17:00 után), hacsak nem sürgős |
| 6 | **Kit tájékoztatunk?** | A Service Desk mindig előre tudjon róla — ők kapják az első hívást |
| 7 | **Mit frissítünk utána?** | Az As-built dokumentáció érintett pontja — **a változás e nélkül nem zárható le** |

> **A 3. és a 7. sor a Xyo saját tanulsága.** A 3. a P-05-ből jön (6. pont). A 7. azért kell,
> mert az As-built a konfigurációt egy időpontban rögzíti: ha a változás után senki nem
> frissíti, fél év múlva már nem írja le a valóságot.

### 4.2 Értékelés és engedély

| Kockázat | Példa | Ki engedélyez | Határidő |
|---|---|---|---|
| Alacsony — egy csoportot érint, gyorsan visszaállítható | Új csapatoldal; opcionális alkalmazás hozzáadása | Nagy Péter, a heti egyeztetésen | 1 hét |
| Közepes — több csoport vagy a belépés módja | Eszközprofil módosítása; új VPN-cél | Nagy Péter, írásban | 1 hét |
| **Magas — biztonsági szabály vagy adatkezelés** | **Feltételes hozzáférési szabály lazítása**; megőrzési szabály | **Nagy Péter, dr. Fekete Zsolt írásos véleményével** | 2 hét |

## 5. Sürgős változások

**Mikor sürgős:** a felhasználók egy csoportja nem tud dolgozni, biztonsági esemény zajlik,
vagy egy beszállítói hiba azonnali beavatkozást kér.

| Lépés | Ki | Mikor |
|---|---|---|
| 1. Telefonos engedély | Nagy Péter (ha nem érhető el: Kovács Anita) | a végrehajtás előtt |
| 2. Végrehajtás, a visszaállítási lépés ismeretében | Szabó Márk | azonnal |
| 3. Írásos rögzítés a változási nyilvántartásban | Szabó Márk | **24 órán belül** |
| 4. Az As-built frissítése | Szabó Márk | 3 munkanapon belül |
| 5. Utólagos átnézés: kellett-e sürgősen? megelőzhető lett volna? | Nagy Péter, Szabó Márk | a következő heti egyeztetésen |

> **A 24 óra nem véletlen:** a projekt saját eljárása is ennyit ad a sürgős projektdöntés
> írásos rögzítésére (XYO-CP-115, 5. pont). A két eljárás itt összeér — és jó, ha a
> munkatársaknak csak egy szabályt kell megjegyezniük.
>
> **Az elveszett gép (10. eset) nem sürgős változás**, hanem incidens: a távoli
> hozzáférés-visszavonás előre leírt, előre engedélyezett lépés, ezt a Service Desk azonnal
> elvégzi. A sürgős változás az, amit **nem** lehetett előre leírni.

## 6. A P-05 újrajátszva — mit változtatott volna a modell?

**Ami történt (Problémanapló P-05, As-built 2.3):**

| Mikor | Mi |
|---|---|
| 05.04 – 05.08. | A CA-05 (országkorlátozás) jelentés-módban fut — **irodai hálózaton** |
| 05.11. | Az UAT első napja: **3 tesztelő** nem tud belépni otthonról, mobilneten. A mobilszolgáltatói CGNAT-kimenő IP külföldi tartományba sorolt (H-02, S1) |
| 05.11. 10:40 | Eszkaláció Nagy Péterhez |
| 05.12. | A CA-05 átállítva: országkorlátozás helyett **megbízható eszköz + MFA** (D-14, dr. Fekete Zsolt véleményével) |
| 05.13 – 05.22. | Utólagos ellenőrzés: további kizárás nem történt |

**Amit a modell másképp csinált volna:**

| Lépés | A projektben | A modell szerint |
|---|---|---|
| A CA-05 élesítése | Szakmai döntés, a kockázat (R11) azonosítva, jelentés-mód 5 napig | **Normál változás, magas kockázat.** A 4.1 pont 2. kérdése — „milyen hálózatról dolgoznak?” — és a 3. kérdése — „irodai hálózaton *és* mobilneten” — **a tesztelés hiányát az élesítés előtt kimutatta volna** |
| A javítás 05.12-én | Szakmai vezetői döntés DPO-véleménnyel, dokumentálva (D-14) | **Sürgős változás** — ugyanez a döntés, ugyanazokkal az emberekkel. **Itt a modell semmit nem tett volna hozzá**: a projekt jól csinálta |
| Az As-built frissítése | Megtörtént (As-built 2.3 és 7. pont) | A változás lezárásának feltétele |
| A tanulság | A Tanulságok naplójába átvezetve | **A 4.1 pont 3. sorává vált** — minden későbbi CA-módosításnál kötelező |

> **Őszintén:** a P-05 kezelése jó volt — gyors, dokumentált, a megfelelő szinten döntött. A
> modell nem a reakción javított volna, hanem a **megelőzésen**: a változási kérelem kérdései
> a tesztkörnyezet hiányát a 05.11. előtt felszínre hozták volna. Az R11 kockázat válaszlépése
> (a jelentés-mód) helyes volt; csak rossz hálózaton futott.

## 7. Változási nyilvántartás — az első sorok

| # | Dátum | Változás | Típus | Engedélyező | Állapot |
|---|---|---|---|---|---|
| CH-001 | 2026.06.19. | A Cloudia Solutions Intune-adminisztrátori jogának megszüntetése | normál | Nagy Péter | végrehajtva; ellenőrzés 06.26-án |
| CH-002 | 2026.06.26. | Az Azure-előfizetés tulajdonosi jogának átadása Nagy Péternek | normál | Nagy Péter | tervezett |
| CH-003 | 2026.12.18. | Break-glass fiók féléves tesztje jelszócserével | szabványos (SV-6) | előre engedélyezett | tervezett |
| CH-004 | 2027.02.28-ig | A Microsoft 365-licencek megújítása (lejárat: 2027.04.30.) | normál | Nagy Péter | tervezett |

> **A CH-001 a legfontosabb sor.** A szerződés szerint a szállítói jog „automatikusan”
> megszűnik az UAT-elfogadással — a Run-book mégis külön ellenőrzést írt elő 06.26-ra. Ez a
> változásengedélyezés lényege egy mondatban: **a változás akkor kész, amikor ellenőriztük,
> nem amikor elrendeltük.**

## 8. Mit mérünk — célként, nem eredményként

| Mutató | Cél | Miért |
|---|---|---|
| Sikeres változások aránya (nem okozott incidenst, nem kellett visszaállni) | ≥ 95% | A változásengedélyezés fő mércéje |
| Sürgős változások aránya az összes változáshoz | ≤ 10% | Ha sok a sürgős, a tervezés gyenge |
| Változás okozta incidensek száma havonta | 0 | A P-05 típusú hibák megelőzése |
| As-built frissítve a lezáráskor | 100% | Enélkül a konfigurációs leírás elavul |

*Ezekre még nincs mért adat — a modell 2026.06.19-én indul. Az első értékelés a 2027. januári
szolgáltatás-felülvizsgálaton lesz (XYO-ITIL-002, 2. pont).*

---

## Mi a különbség a PMI-változáskezeléshez képest?

| | PMI integrált változáskezelés | **ITIL 4 változásengedélyezés** |
|---|---|---|
| A változás tárgya | A **projektterv** és a baseline | Az **éles szolgáltatás** és a konfigurációs tételek |
| Ki dönt | Change Control Board / szponzor | **Változásengedélyező** — a kockázathoz illő szinten |
| A döntés alapja | Idő, költség, hatókör, kockázat | **Kockázat, tesztelés, visszaállíthatóság** |
| Előre engedélyezett változás | Nincs ilyen fogalom | **Szabványos változás** — a gyakori lépések nem terhelik a döntéshozót |
| Mikor ér véget | A projekt zárásával | **Soha** — a szolgáltatással együtt él |

> **A tanulság egy PM-nek:** a projekt alatt az éles környezet változásait is te viszed, csak
> más néven — go/no-go döntésként, javításként, „technikai megvalósítási módként”. Ha a projekt
> végén ezt nem adod át egy leírt modellként, az üzemeltetés vagy mindent engedélyeztetni fog
> (és lelassul), vagy semmit (és egy CA-05-höz hasonló hiba élesben, ötven embernél jön elő).

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Szabó Márk, rendszergazda; Tóth Gergő, projektmenedzser | 2026.06.19. |
| **Jóváhagyta (változásengedélyező)** | **Nagy Péter**, IT osztályvezető | 2026.06.19. |
| Véleményezte (adatvédelem) | dr. Fekete Zsolt, adatvédelmi tisztviselő | 2026.06.19. |

---

> **Kapcsolódó dokumentumok:** bemenete a *Változáskezelési eljárás* (XYO-CP-115), a
> *Változásnapló*, a *Problémanapló* (P-05), az *As-built dokumentáció* és a *Run-book*;
> kimenete a változási nyilvántartás és az *SLA, OLA és alátámasztó szerződések*
> (XYO-ITIL-002).
