# Ütemterv és mérföldkőlista (Schedule and Milestone List)

**Dokumentum azonosítója:** XYO-CP-106\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser, a munkacsomag-felelősök becsléseiből\
**Verzió:** 1.0 — **baseline, befagyasztva 2026.03.13-án**

> A becsléseket a munkacsomag-felelősök adták, nem a projektmenedzser.
> A dátumok a **kemény határidőktől visszafelé** számolva állnak össze.

---

## 1. Mérföldkövek

| # | Mérföldkő | Terv | Kritikus úton? |
|---|---|---|---|
| M1 | Projektalapító okirat aláírva | 2026.02.02. | ✔ |
| M2 | Kick-off megtartva | 2026.02.09. | ✔ |
| M3 | Baseline jóváhagyva (Planning-kapu) | 2026.03.13. | ✔ |
| M4 | Szerződések aláírva | 2026.04.17. | ✔ |
| M5 | Felhőkörnyezet kész, tesztelésre alkalmas | 2026.05.08. | ✔ |
| M6 | Első hullám élesben (10 fő), UAT indul | 2026.05.11. | ✔ |
| M7 | Teljes 50 fő élesben | 2026.06.12. | ✔ |
| M8 | UAT lezárva, átvétel aláírva | 2026.06.19. | ✔ |
| M9 | Üzemeltetésbe adás | 2026.06.26. | ✔ |
| M10 | Projekt lezárva | 2026.06.30. | ✔ |
| M11 | Utólagos értékelés (PIR) | 2026.10.09. | (mérési szakasz) |

## 2. Ütemterv munkacsomagonként

| WBS | Feladat | Kezdés | Befejezés | Naptári nap | Függ ettől | KU |
|---|---|---|---|---:|---|:-:|
| 1.1 | Projektterv és baseline | 02.10. | 03.13. | 32 | M2 | ✔ |
| 4.1 | DPO állásfoglalás és DPIA | 02.12. | 03.20. | 37 | M2 | |
| 4.2 | Üzemi tanácsi véleményezés | 02.16. | 03.11. | 24 | M2 | |
| 2.1.1 | Ajánlatkérés — hardver | 03.16. | 03.20. | 5 | M3 | ✔ |
| 2.1.2 | Ajánlatkérés — felhő | 03.16. | 03.20. | 5 | M3 | ✔ |
| — | **Ajánlati szakasz (szállítói oldal)** | 03.23. | 04.02. | 11 | 2.1.x | ✔ |
| 2.2.1 | Ajánlatbontás és értékelés | 04.02. | 04.08. | 7 | ajánlati határidő (04.02. 12:00) | ✔ |
| — | **Belső jóváhagyási kör (25 M Ft felett)** | 04.09. | 04.16. | 8 | 2.2.1 | ✔ |
| 2.2.2 | Szerződéskötés | 04.17. | 04.17. | 1 | jóváhagyás | ✔ |
| — | **Hardver szállítási idő (6 hét)** | 04.20. | 05.29. | 40 | M4 | |
| 4.3 | Biztonsági alapkonfiguráció | 04.20. | 04.30. | 11 | 4.1 | |
| 3.1.1 | Entra ID bérlő és fiókok | 04.20. | 04.24. | 5 | M4 | ✔ |
| 3.1.2 | MFA és feltételes hozzáférés | 04.27. | 05.06. | 10 | 3.1.1; 4.3 (KK) | |
| 3.2.1 | Intune eszközprofilok | 04.27. | 04.30. | 4 | 3.1.1 | ✔ |
| 3.2.2 | Autopilot beüzemelési folyamat | 05.04. | 05.08. | 5 | 3.2.1 | ✔ |
| 3.2.3 | Alkalmazáscsomagok | 04.29. | 05.06. | 8 | 3.1.1 | |
| 3.3.1 | SharePoint struktúra és jogosultságok | 04.20. | 05.04. | 15 | M4 | ✔ |
| 3.3.2 | Megőrzés, mentés, visszaállítási teszt | 05.05. | 05.08. | 4 | 3.3.1 | ✔ |
| 3.4.1 | Azure VPN Gateway | 04.22. | 04.30. | 9 | M4 | |
| 3.4.2 | Kliensprofil és belső rendszerek | 05.04. | 05.08. | 5 | 3.4.1 | |
| 5.1 | Oktatási anyag és gyorssegédlet | 04.27. | 05.15. | 19 | 3.1.1 | |
| 6.1 | Tesztterv és tesztesetek | 04.13. | 04.24. | 12 | M3 | |
| 6.2 | Technikai teszt (10 gép) | 05.06. | 05.08. | 3 | 3.2.2 (KK); 10 gép (05.06.) | ✔ |
| 5.3 | Service Desk felkészítés | 04.27. | 05.08. | 12 | 5.1 (KK) | |
| 5.4 | Kommunikáció a pilot körnek | 03.16. | 06.12. | 89 | M3 | |
| 7.1 | Első hullám élesben — 10 fő | 05.11. | 05.13. | 3 | M5, 6.2 | ✔ |
| 6.3 | UAT (10 fő, 2 hét) | 05.11. | 05.22. | 12 | 7.1 (KK) | ✔ |
| — | **Hibajavítás és újratesztelés** (05.25. Pünkösdhétfő: 6 munkanap) | 05.25. | 06.02. | 9 | 6.3 | ✔ |
| 5.2 | Oktatások (2–5. csoport + pótló; az UAT-csoporté 05.07.) | 06.01. | 06.10. | 10 | 5.1; 40 gép (05.29.) | |
| 7.2 | Második hullám — 20 fő | 06.03. | 06.05. | 3 | újratesztelés; 40 gép (05.29.) | ✔ |
| 7.3 | Harmadik hullám — 20 fő | 06.10. | 06.12. | 3 | 7.2 | ✔ |
| 6.4 | UAT-zárás és elfogadás aláírva | 06.15. | 06.19. | 5 | 7.3 | ✔ |
| 3.5 | As-built dokumentáció | 05.11. | 06.19. | 40 | M5 | |
| 8.1 | KPI-adatlapok | 06.01. | 06.19. | 19 | M3 | |
| 1.3 | Üzemeltetésbe adás és zárás | 06.22. | 06.30. | 9 | M8, 3.5 | ✔ |
| 8.3 | Mérési felelősségek átadása | 06.24. | 06.30. | 7 | 8.1 | |
| 7.4 | Hypercare (3 hét) | 06.15. | 07.03. | 19 | 7.3 | |
| 1.2 | Státuszriportálás és kontroll | 03.16. | 06.30. | 107 | M3 | |

*KU = kritikus úton van. A függőség alapesetben **befejezés–kezdés**: a feladat
a megelőző befejezése után indul. **KK = kezdés–kezdés**: a feladat a megelőző
elindulása után kezdődhet, és vele párhuzamosan fut (pl. a Service Desk
felkészítése az oktatási anyag első változatával már indulhat).*

*Munkaszüneti napok a projektidőszakban: 04.03. (Nagypéntek), 04.06.
(Húsvéthétfő), 05.01., 05.25. (Pünkösdhétfő). Határidő és bontás ezekre nem
eshet.*

## 3. A kritikus út

```
M3 Baseline (03.13.)
  → Ajánlatkérés kiadása (03.16–03.20., 5 nap)
  → Ajánlati szakasz (03.23–04.02., 11 nap)
  → Bontás és értékelés (04.02–04.08., 7 nap — benne a húsvéti ünnepek)
  → Belső jóváhagyási kör (04.09–04.16., 8 nap)
  → M4 Szerződéskötés (04.17.)
  → Két párhuzamos, tartalék nélküli ág (04.20–05.08., 19 nap):
      a) 3.1.1 Entra ID → 3.2.1 Intune-profilok → 3.2.2 Autopilot
      b) 3.3.1 SharePoint-struktúra → 3.3.2 megőrzés és visszaállítási teszt
    + 6.2 Technikai teszt a 10 tesztgépen (05.06–05.08.)
  → M5 Környezet kész (05.08.)
  → 7.1 első hullám (05.11–05.13.)
  → UAT (05.11–05.22., 12 nap)
  → Hibajavítás és újratesztelés (05.25–06.02., 9 nap)
  → 7.2 második hullám (06.03–06.05.)
  → 7.3 harmadik hullám (06.10–06.12.)  →  M7
  → UAT-zárás és elfogadás (06.15–06.19.)  →  M8
  → Üzemeltetésbe adás és zárás (06.22–06.30.)  →  M10
```

**Teljes hossz a baseline-tól: 109 naptári nap. A határidő: 2026.06.30.
Puffer: 0 nap.**

> ⚠️ **A kritikus úton nincs puffer.** Ezt a Planning-kapun kimondtuk, és a
> Steering Committee így fogadta el. A tartalékidő nem az ütemtervben van,
> hanem két helyen, jelölten (lásd 5. pont).
>
> **M5 előtt két ág fut össze, mindkettő tartalék nélkül.** Ez kockázatosabb,
> mint egyetlen kritikus út: M5 akkor is csúszik, ha a két ág közül bármelyik
> késik. A közel kritikus ágak (3.1.2 MFA, 3.4.x VPN) 2 munkanap tartalékkal
> futnak — ezeket is hetente figyeljük.

## 4. A hardverszállítás mint párhuzamos szál

A laptopszállítás (04.20–05.29., 6 hét) **nincs a kritikus úton**, mert a
felhőkörnyezet kialakítása hosszabb. Viszont:

| | |
|---|---|
| Szállítás vége | 2026.05.29. |
| Mikor kellene először? | 2026.05.11. (első hullám, 10 gép) |
| **Feszültség** | **A 10 tesztgépnek 18 nappal a teljes szállítás előtt meg kell érkeznie** |

**Kezelés:** a szerződésben **részszállítás** kikötése: 10 gép legkésőbb
2026.05.06-ig, a maradék 40 gép 2026.05.29-ig. Ez a beszerzési terv és a
szerződés kötelező eleme (R1 kockázat válaszlépése).

## 5. Hol van a tartalékidő?

| Hol | Mennyi | Miért ott |
|---|---:|---|
| Hibajavítás és újratesztelés az UAT után | 9 nap | Ha kevés hiba lesz, ebből 5 nap felszabadul |
| A 7.2 és 7.3 hullám között | 4 nap | Ha az első hullám gördülékeny, összevonható |
| **Összesen** | **9–13 nap** | |

> **Nem rejtettük el a pufferi időt a feladatokban.** A „mindenhova +20%"
> módszer kezelhetetlen: nem tudod megmondani, mennyi tartalék maradt, a csapat
> pedig úgyis rájön, és a felduzzasztott becsléshez igazítja a munkatempót.

## 6. A legnagyobb ütemkockázatok

| # | Kockázat | Hatás az ütemre | Válasz |
|---|---|---|---|
| R1 | Laptopszállítás csúszik | M6 és minden utána tolódik | Részszállítás kikötése; kötbér |
| R2 | DPIA elhúzódik | A beszerzés nem indulhat | 4.1 már 02.12-én indult, 5 hét ráhagyással |
| R8 | A belső jóváhagyási kör hosszabb 8 napnál | M4 tolódik | Molnár Katalin előre jelezte a pénzügynek a várható időpontot |
| R6 | Az UAT több kritikus hibát talál | A 9 napos javítási ablak kevés | Az UAT az élesítéssel párhuzamosan fut, nem utána |

## 7. Amit a tervezéskor tanultunk

**A beszerzés a leghosszabb elem, és nem munka, hanem várakozás.**
A 03.16-tól 04.17-ig tartó 33 naptári napból (23 munkanap) mindössze kb.
9 munkanap tényleges munka — a többi ajánlati határidő, húsvét és belső
jóváhagyás. Ezt a legtöbb junior PM
nem tervezi be feladatként, és utólag derül ki, hogy egy hónap elment.

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.03.06. |
| Becslések | a munkacsomag-felelősök | 2026.02.12–02.18. |
| Jóváhagyta | Projekt Irányító Bizottság | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete a *WBS* és a *WBS-szótár*; kimenete a
> *Költségvetés*, az *Erőforrásterv*, a *Státuszriport*, a *Mérföldkő-riport*
> és az *Ütem- és költségeltérés elemzés*.
