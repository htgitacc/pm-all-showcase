# Felelősségi mátrix (RACI Matrix)

**Dokumentum azonosítója:** XYO-CP-109\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Jóváhagyta:** Projekt Irányító Bizottság — 2026.03.13.\
**Verzió:** 1.1

> **Verziójegyzet:** a nyertes szállító neve (Cloudia Solutions Kft.) a szerződéskötés után, 2026.04.20-án került a dokumentumba. A korábbi változatban a beszerzési tételek (B1–B4) szerepeltek; a baseline tartalma — hatókör, ütem, költség — ezzel nem változott.

---

## Jelölések

| Betű | Jelentés | Magyarázat |
|---|---|---|
| **R** | Responsible — végrehajtó | Ő csinálja meg a munkát. Több is lehet. |
| **A** | Accountable — számonkérhető felelős | Ő felel az eredményért, ő hagyja jóvá. **Soronként pontosan egy.** |
| **A/R** | mindkettő | Ha a számonkérhető felelős maga végzi a munkát. **Minden sorban kell végrehajtó** (R vagy A/R) — különben senki nem csinálja meg. |
| **C** | Consulted — véleményezett | Meg kell kérdezni **a döntés előtt**. Kétirányú. |
| **I** | Informed — tájékoztatott | Értesíteni kell **a döntés után**. Egyirányú. |

> **A leggyakoribb hiba:** két „A" egy sorban. Az nem kettős felelősség, hanem
> nulla — vita esetén egymásra mutatnak. Ez a mátrix ezért soronként ellenőrizve
> van.

---

## 1. Projektirányítás és tervezés

| Feladat | Kovács A.<br>*szponzor* | Tóth G.<br>*PM* | Nagy P.<br>*IT vez.* | Szabó M.<br>*rendszerg.* | Molnár K.<br>*beszerzés* | Balogh T.<br>*kontroller* | Varga E.<br>*HR* | Kiss R.<br>*Service Desk* | dr. Fekete Zs.<br>*DPO* | Cloudia<br>*szállító* |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Projektterv és baseline | **A** | R | C | I | C | C | C | C | I | I |
| Hatókör-nyilatkozat | **A** | R | C | | | | I | I | | |
| WBS és WBS-szótár | | **A** | R | R | R | | C | R | | C |
| Ütemterv | | **A** | R | C | R | | C | C | | C |
| Költségvetés | **A** | R | C | | C | R | | | | |
| Kockázatnyilvántartás | I | **A** | R | R | R | | R | R | C | C |
| Változáskérelem elbírálása (≤1 M Ft) | I | **A/R** | C | | C | C | | | | |
| Változáskérelem elbírálása (>1 M Ft) | **A** | R | C | | C | C | | | | I |
| Heti státuszriport | I | **A/R** | C | C | C | C | I | I | | |
| Steering riport | I | **A/R** | C | | | C | I | | | |

## 2. Beszerzés

| Feladat | Kovács A. | Tóth G. | Nagy P. | Szabó M. | Molnár K. | Balogh T. | Varga E. | Kiss R. | dr. Fekete Zs. | Cloudia |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Beszerzési terv | I | R | C | | **A** | C | | | | |
| Ajánlatkérési dokumentáció — műszaki tartalom | | C | **A** | R | R | | | | C | |
| Ajánlatkérési dokumentáció — kiadás | I | C | C | | **A/R** | | | | | |
| Szállítóértékelési szempontrendszer | **A** | R | C | | R | C | | | | |
| Ajánlatbontás és értékelés | I | R | R | | **A** | C | | | | |
| Szerződéskötés | **A** | C | C | | R | C | | | C | I |
| Teljesítésigazolás | I | R | **A** | R | C | I | | | | I |

> **Figyeld meg:** a beszerzési eljárás „A" felelőse **Molnár Katalin**, nem a
> projektmenedzser. A folyamat gazdája a beszerzés — a PM az ütemért felel, nem
> az eljárás szabályosságáért. Ezt a különbséget sok junior PM összekeveri, és
> vagy fölösleges felelősséget vállal, vagy hatáskört sért.

## 3. Felhőkörnyezet kialakítása

| Feladat | Kovács A. | Tóth G. | Nagy P. | Szabó M. | Molnár K. | Balogh T. | Varga E. | Kiss R. | dr. Fekete Zs. | Cloudia |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Entra ID konfiguráció | | I | **A** | C | | | | | | R |
| MFA és feltételes hozzáférés | | I | **A** | C | | | | I | C | R |
| Intune eszközprofilok | | I | **A** | C | | | | I | C | R |
| SharePoint struktúra és jogosultságok | | I | **A** | C | | | C | | C | R |
| Mentés, megőrzés, visszaállítási teszt | | I | C | **A** | | | | | C | R |
| Azure VPN | | I | **A** | C | | | | | | R |
| Biztonsági alapkonfiguráció | | I | C | **A** | | | | C | C | R |
| As-built dokumentáció | | C | **A** | R | | | | C | | R |

## 4. Megfelelőség

| Feladat | Kovács A. | Tóth G. | Nagy P. | Szabó M. | Molnár K. | Balogh T. | Varga E. | Kiss R. | dr. Fekete Zs. | Cloudia |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Adatvédelmi hatásvizsgálat (DPIA) | I | R | C | C | | | C | | **A** | C |
| Üzemi tanácsi véleményezés | I | C | | | | | **A/R** | | C | |
| Home office szabályzat | **A** | I | | | | | R | | C | |
| Adatfeldolgozói megállapodás | I | C | | | R | | | | **A** | C |

## 5. Felkészítés, teszt, élesítés

| Feladat | Kovács A. | Tóth G. | Nagy P. | Szabó M. | Molnár K. | Balogh T. | Varga E. | Kiss R. | dr. Fekete Zs. | Cloudia |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Oktatási és adaptációs terv | | C | C | | | | **A** | C | | R |
| Oktatási anyag és gyorssegédlet | | I | C | C | | | **A** | C | | R |
| Oktatások megtartása | | I | | | | | **A** | I | | R |
| Service Desk felkészítés | | C | C | C | | | I | **A/R** | | C |
| Kommunikáció a pilot körnek | I | **A** | C | | | | R | I | | |
| Tesztterv és tesztesetek | | C | **A** | R | | | C | C | | C |
| Technikai teszt | | I | **A** | R | | | | I | | C |
| Felhasználói átvételi teszt (UAT) — R: a 10 fős tesztcsoport | | C | **A** | C | | | C | C | | I |
| UAT-elfogadás aláírása — társaláíró: Fodor Gábor, felhasználói képviselő (nem elhagyható) | I | R | **A** | | | | C | C | | I |
| Élesítési hullámok | | **A** | C | R | | | C | R | | C |
| Hypercare | | I | C | R | | | I | **A** | | C |

## 6. Zárás és mérés

| Feladat | Kovács A. | Tóth G. | Nagy P. | Szabó M. | Molnár K. | Balogh T. | Varga E. | Kiss R. | dr. Fekete Zs. | Cloudia |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Átadás-átvételi jegyzőkönyv | I | R | **A** | C | | | | C | | C |
| Üzemeltetésbe adás (Run-book) | | R | **A** | C | | | | C | | R |
| Szerződészárás | I | C | C | | **A/R** | C | | | | I |
| Pénzügyi zárás | **A** | C | | | C | R | | | | |
| Tanulságok workshop | I | **A** | R | R | R | R | R | R | | C |
| Projektzáró jelentés | **A** | R | C | | | C | C | C | | I |
| KPI-adatlapok és mérési terv | I | **A** | C | R | | C | R | R | C | |
| Mérési felelősségek átadása | I | R | **A** | C | | C | C | C | | |
| A hasznok realizálása (mérési szakasz) | I | R | **A** | R | | R | R | R | | |

---

## Ellenőrzés: minden sorban pontosan egy „A", és van végrehajtó

| Blokk | Sorok száma | Egy „A" és legalább egy „R" mindenhol? |
|---|---:|---|
| 1. Projektirányítás | 10 | ✔ |
| 2. Beszerzés | 7 | ✔ |
| 3. Felhőkörnyezet | 8 | ✔ |
| 4. Megfelelőség | 4 | ✔ |
| 5. Felkészítés, teszt, élesítés | 11 | ✔ |
| 6. Zárás és mérés | 9 | ✔ |
| **Összesen** | **49** | **✔** |

## Amit a mátrix készítésekor tisztáztunk

**Három vitás pont került elő, mindhárom hasznos:**

| Vitás sor | Az eredeti javaslat | Amit eldöntöttünk | Miért |
|---|---|---|---|
| Mentés és visszaállítási teszt | „A" = Nagy Péter | **„A" = Szabó Márk** | Ő az egyetlen, aki tényleg meg tudja mondani, működik-e a visszaállítás |
| Hypercare | „A" = Tóth Gergő | **„A" = Kiss Réka** | A támogatás a Service Desk folyamata; a PM nem tud napi szinten hibát kezelni |
| A hasznok realizálása | „A" = Tóth Gergő | **„A" = Nagy Péter** | A projekt lezárul, a PM elmegy — a hasznok gazdája az üzemeltetés vezetője marad |

> **A harmadik a legfontosabb.** Ha a hasznok „A" felelőse a projektmenedzser
> marad, akkor a projekt zárása után gazdátlanná válik a mérés. Ezért kellett
> már a tervezéskor átadni Nagy Péternek.

---

> **Kapcsolódó dokumentumok:** bemenete a *WBS*, az *Érintettek nyilvántartása*
> és az *Erőforrásterv*; kimenete a *Kommunikációs terv*, a
> *Munkacsomag-kiadás* és az *Eszkalációs napló*.
