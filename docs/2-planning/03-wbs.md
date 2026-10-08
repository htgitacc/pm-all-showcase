# Munkalebontási szerkezet (WBS — Work Breakdown Structure)

**Dokumentum azonosítója:** XYO-CP-103\
**Projekt:** Xyo Cloud Pilot\
**Készült:** 2026.02.10-11., közös WBS-workshopon\
**Résztvevők:** Tóth Gergő, Nagy Péter, Szabó Márk, Molnár Katalin, Kiss Réka,
Varga Eszter, Cloudia Solutions bevezetési konzultánsa\
**Verzió:** 1.2 — **baseline, befagyasztva 2026.03.13-án**

> **Verziójegyzet:** a nyertes szállító neve (Cloudia Solutions Kft.) a szerződéskötés után, 2026.04.20-án került a dokumentumba. A korábbi változatban a beszerzési tételek (B1–B4) szerepeltek; a baseline tartalma — hatókör, ütem, költség — ezzel nem változott.
>
> **Közzététel:** a Cloudia Solutions konzultánsa a 2026.02.10-11-i workshopon **az előzetes felmérést végző tanácsadóként** vett részt, még a beszerzés előtt. Ezt az ajánlatkérésben (XYO-CP-202) minden ajánlattevő felé jeleztük, és a workshop anyagát mindenkinek kiadtuk — így a részvétel nem adott információs előnyt.

> **Fontos elv:** a WBS **eredményeket** tartalmaz, nem tevékenységeket.
> Nem „laptopok megrendelése", hanem „50 db átvett laptop" — így ellenőrizhető,
> hogy kész van-e. A legalsó szint a **munkacsomag**, 8–80 óra közötti munka.

---

## 1. A lebontás

```
XYO-CP  Xyo Cloud Pilot
│
├── 1  PROJEKTIRÁNYÍTÁS
│   ├── 1.1  Jóváhagyott projektterv és baseline
│   ├── 1.2  Rendszeres státuszriportálás és kontroll
│   └── 1.3  Lezárt projekt és üzemeltetésbe adás
│
├── 2  BESZERZÉS
│   ├── 2.1  Beszerzési dokumentáció
│   │   ├── 2.1.1  Ajánlatkérési dokumentáció — hardver
│   │   └── 2.1.2  Ajánlatkérési dokumentáció — felhő bevezetés és licenc
│   ├── 2.2  Szerződött szállítók
│   │   ├── 2.2.1  Értékelt és jegyzőkönyvezett ajánlatok
│   │   └── 2.2.2  Aláírt szerződések
│   └── 2.3  Leszállított eszközök
│       ├── 2.3.1  50 db átvett, Autopilot-regisztrált laptop
│       └── 2.3.2  50 db dokkoló, otthoni monitor, headset
│
├── 3  FELHŐKÖRNYEZET
│   ├── 3.1  Konfigurált Entra ID
│   │   ├── 3.1.1  Bérlő kiterjesztés, tartomány, felhasználói fiókok
│   │   └── 3.1.2  MFA és feltételes hozzáférési szabályok
│   ├── 3.2  Működő Intune eszközfelügyelet
│   │   ├── 3.2.1  Eszközprofilok és megfelelőségi szabályok
│   │   ├── 3.2.2  Autopilot beüzemelési folyamat
│   │   └── 3.2.3  Alkalmazáscsomagok (Office, VPN kliens, böngésző)
│   ├── 3.3  Kialakított SharePoint és OneDrive
│   │   ├── 3.3.1  Csapatoldal-struktúra és jogosultsági modell
│   │   └── 3.3.2  Megőrzési és mentési szabályok, visszaállítási teszt
│   ├── 3.4  Működő Azure VPN
│   │   ├── 3.4.1  VPN Gateway kialakítás
│   │   └── 3.4.2  Kliensprofil és a 2 belső rendszer elérése
│   └── 3.5  As-built konfigurációs dokumentáció
│
├── 4  MEGFELELŐSÉG
│   ├── 4.1  DPO állásfoglalás és adatvédelmi hatásvizsgálat
│   ├── 4.2  Üzemi tanácsi véleményezés
│   └── 4.3  Biztonsági alapkonfiguráció jóváhagyva
│
├── 5  FELKÉSZÍTÉS
│   ├── 5.1  Oktatási anyag és felhasználói gyorssegédlet
│   ├── 5.2  Megtartott oktatások (5 csoport × 10 fő)
│   ├── 5.3  Felkészített Service Desk (útmutató + hypercare terv)
│   └── 5.4  Kommunikáció a pilot körnek (hírlevelek, kiosztási tájékoztató)
│
├── 6  TESZT ÉS ÁTVÉTEL
│   ├── 6.1  Tesztterv és tesztesetek
│   ├── 6.2  Lezárt technikai teszt (10 gép)
│   ├── 6.3  Lezárt felhasználói átvételi teszt (UAT, 10 fő, 2 hét)
│   └── 6.4  Aláírt UAT-elfogadás
│
├── 7  ÉLESÍTÉS
│   ├── 7.1  Első hullám élesben — 10 fő
│   ├── 7.2  Második hullám élesben — 20 fő
│   ├── 7.3  Harmadik hullám élesben — 20 fő
│   └── 7.4  Lezárt hypercare időszak (3 hét)
│
└── 8  MÉRÉS ELŐKÉSZÍTÉSE
    ├── 8.1  KPI-adatlapok és mérési terv
    ├── 8.2  T0 baseline mérési jegyzőkönyv
    └── 8.3  Átadott mérési felelősségek
```

## 2. Munkacsomagok becsült ráfordítással

| WBS | Munkacsomag | Felelős | Becsült ráfordítás | Külső / belső |
|---|---|---|---:|---|
| 1.1 | Jóváhagyott projektterv és baseline | Tóth Gergő | 80 óra | belső |
| 1.2 | Státuszriportálás és kontroll | Tóth Gergő | 120 óra | belső |
| 1.3 | Lezárt projekt és üzemeltetésbe adás | Tóth Gergő | 40 óra | belső |
| 2.1.1 | Ajánlatkérési dokumentáció — hardver | Molnár Katalin | 24 óra | belső |
| 2.1.2 | Ajánlatkérési dokumentáció — felhő | Molnár Katalin | 32 óra | belső |
| 2.2.1 | Értékelt ajánlatok | Molnár Katalin | 24 óra | belső |
| 2.2.2 | Aláírt szerződések | Molnár Katalin | 16 óra | belső |
| 2.3.1 | 50 db átvett, Autopilot-regisztrált laptop | Szabó Márk | 24 óra | belső + szállító |
| 2.3.2 | 50 db dokkoló, monitor, headset | Szabó Márk | 16 óra | belső + szállító |
| 3.1.1 | Entra ID bérlő és fiókok | Cloudia Solutions | 40 óra | külső |
| 3.1.2 | MFA és feltételes hozzáférés | Cloudia Solutions | 32 óra | külső |
| 3.2.1 | Intune eszközprofilok | Cloudia Solutions | 40 óra | külső |
| 3.2.2 | Autopilot beüzemelési folyamat | Cloudia Solutions | 32 óra | külső |
| 3.2.3 | Alkalmazáscsomagok | Cloudia Solutions | 24 óra | külső |
| 3.3.1 | SharePoint struktúra és jogosultságok | Cloudia + Nagy Péter | 48 óra | vegyes |
| 3.3.2 | Megőrzés, mentés, visszaállítási teszt | Szabó Márk | 24 óra | belső |
| 3.4.1 | Azure VPN Gateway | Cloudia Solutions | 32 óra | külső |
| 3.4.2 | Kliensprofil és belső rendszerek elérése | Cloudia + Szabó Márk | 24 óra | vegyes |
| 3.5 | As-built dokumentáció | Cloudia + Szabó Márk | 40 óra | vegyes |
| 4.1 | DPO állásfoglalás és DPIA | dr. Fekete Zsolt | 24 óra | belső |
| 4.2 | Üzemi tanácsi véleményezés | Varga Eszter | 8 óra | belső |
| 4.3 | Biztonsági alapkonfiguráció | Szabó Márk | 32 óra | belső |
| 5.1 | Oktatási anyag és gyorssegédlet | Cloudia Solutions | 40 óra | külső |
| 5.2 | Megtartott oktatások (5 csoport) | Cloudia + Varga Eszter | 40 óra | vegyes |
| 5.3 | Felkészített Service Desk | Kiss Réka | 24 óra | belső |
| 5.4 | Kommunikáció a pilot körnek | Tóth Gergő | 24 óra | belső |
| 6.1 | Tesztterv és tesztesetek | Nagy Péter | 32 óra | belső |
| 6.2 | Technikai teszt (10 gép) | Szabó Márk | 24 óra | belső |
| 6.3 | UAT (10 fő, 2 hét) | Nagy Péter + tesztcsoport | 80 óra | belső |
| 6.4 | Aláírt UAT-elfogadás | Tóth Gergő | 8 óra | belső |
| 7.1 | Első hullám — 10 fő | Szabó Márk | 24 óra | belső |
| 7.2 | Második hullám — 20 fő | Szabó Márk | 40 óra | belső |
| 7.3 | Harmadik hullám — 20 fő | Szabó Márk | 40 óra | belső |
| 7.4 | Hypercare (3 hét) | Kiss Réka | 60 óra | belső |
| 8.1 | KPI-adatlapok és mérési terv | Tóth Gergő | 24 óra | belső |
| 8.2 | T0 baseline jegyzőkönyv | Tóth Gergő | 16 óra | belső (kész) |
| 8.3 | Átadott mérési felelősségek | Tóth Gergő | 8 óra | belső |
| | **Összesen** | | **1 260 óra** | |

**Ebből:**

| | Óra | Megjegyzés |
|---|---:|---|
| Belső ráfordítás | 948 óra | 868 óra belső csomag + 80 óra a vegyes csomagokból; kb. 6 fő között, 5 hónapra |
| Külső (Cloudia Solutions) | 312 óra | 240 óra külső csomag + 72 óra a vegyes csomagokból; a 6 500 000 Ft-os bevezetési díj fedezi |

*A négy vegyes csomag (3.3.1, 3.4.2, 3.5, 5.2 — összesen 152 óra) megosztása:
3.3.1: 24 + 24, 3.4.2: 12 + 12, 3.5: 24 + 16, 5.2: 20 + 20 óra (belső + szállító).*

## 3. Amit a workshopon tanultunk

**Három munkacsomag hiányzott az első vázlatból**, és csak a közös átbeszélésen
került elő:

| WBS | Ki vetette fel | Miért maradt ki eredetileg |
|---|---|---|
| 3.3.2 Megőrzés, mentés, visszaállítási teszt | Szabó Márk | „A felhő magától ment" — gyakori tévhit; a megőrzési idő beállítása külön munka |
| 5.3 Felkészített Service Desk | Kiss Réka | A PM a felhasználói oktatásra gondolt, a támogatói oldalra nem |
| 4.2 Üzemi tanácsi véleményezés | Varga Eszter | Az érintettek közül is kimaradt eredetileg |

> **Ezért kell a WBS-t közösen csinálni.** Ha egyedül írod meg, pontosan azok a
> munkacsomagok maradnak ki, amiket nem a te szemszögedből lát valaki.

## 4. Változásnapló

| Dátum | Változás | Verzió |
|---|---|---|
| 2026.02.11. | A workshop eredménye, első teljes lebontás | 1.0 |
| 2026.02.19. | 3.3.2 (visszaállítási teszt) kibontása a kockázati műhely után | 1.1 |
| 2026.03.05. | 3.4.2 kiegészítve a 3 csapat régi fájlszerver-elérésével (A8) | 1.2 |
| 2026.03.13. | Baseline befagyasztva | 1.2 |

---

> **Kapcsolódó dokumentumok:** bemenete a *Hatókör-nyilatkozat*; kimenete a
> *WBS-szótár*, az *Ütemterv*, a *Költségvetés*, az *Erőforrásterv*, a
> *RACI mátrix* és a *Munkacsomag-kiadás*.
