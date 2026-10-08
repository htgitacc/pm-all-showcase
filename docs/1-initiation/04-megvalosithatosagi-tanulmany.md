# Megvalósíthatósági tanulmány (Feasibility Study)

**Dokumentum azonosítója:** XYO-CP-004\
**Projekt:** Xyo Cloud Pilot\
**Készült:** 2026. január 16.\
**Koordinálta:** Tóth Gergő, projektmenedzser\
**Szakmai tartalom:** Nagy Péter, IT osztályvezető; Szabó Márk, rendszergazda\
**Külső szakértő:** Cloudia Solutions Kft., előzetes felmérés (2026.01.08-09.)\
**Verzió:** 1.0

> Azért készült, mert a felhőalapú munkakörnyezet **teljesen új terület** a Xyo
> Kft.-nél. A tanulmány azt vizsgálja, hogy a megoldás technikailag, szervezetileg,
> jogilag és pénzügyileg megvalósítható-e — és milyen feltételekkel.

---

## 1. Technikai megvalósíthatóság

### 1.1 Hálózat és sávszélesség

**A vizsgált kérdés:** elegendő-e a mobilinternetes kapcsolat a napi munkához?

**Mérés:** 2026.01.12-13-án 6 munkatárs otthoni környezetében mértük a
mobilinternetes kapcsolatot, három szolgáltatónál, munkaidőben.

| Helyszín | Letöltés | Feltöltés | Késleltetés | Értékelés |
|---|---:|---:|---:|---|
| Budapest, belváros | 78 Mbit/s | 24 Mbit/s | 28 ms | megfelelő |
| Budapest, agglomeráció | 54 Mbit/s | 18 Mbit/s | 34 ms | megfelelő |
| Vidéki nagyváros | 61 Mbit/s | 21 Mbit/s | 31 ms | megfelelő |
| Vidéki kisváros | 22 Mbit/s | 6 Mbit/s | 52 ms | határeset |
| Külterület (2 mérés) | 8–11 Mbit/s | 2–3 Mbit/s | 88 ms | **nem megfelelő** |

**Következtetés:** a mért helyszínek többségén a kapcsolat megfelelő. **Két
külterületi helyszínen nem.** A pilot résztvevőinek kijelölésekor a lakóhelyet
figyelembe kell venni, vagy fix internet-hozzájárulást kell biztosítani.

> **Feltétel (F-1):** a HR a résztvevők kijelölésekor jelezze, ha valaki
> külterületen lakik; ezekben az esetekben egyedi vizsgálat szükséges.

### 1.2 Azonosítás és eszközfelügyelet

| Kérdés | Megállapítás |
|---|---|
| Van-e a cégnek Entra ID bérlője? | Igen, alapszintű, e-mail szolgáltatáshoz. Kiterjeszthető. |
| Alkalmas-e a jelenlegi Active Directory a hibrid azonosításra? | Nem szükséges hibrid: a pilot gépei **csak felhő** azonosítást használnak. |
| Van-e eszközfelügyelet? | Nincs. Az Intune a Business Premium licenc része, külön beszerzést nem igényel. |
| Automatizált beüzemelés lehetséges? | Igen, Windows Autopilot, a szállítóval előre regisztrált eszközökkel. |

> **Feltétel (F-2):** a laptopokat a szállítónak **Autopilot-regisztrációval**
> kell szállítania. Ezt az ajánlatkérésbe be kell írni, különben marad a manuális
> beüzemelés.

### 1.3 VPN

A cégnek **nincs** jelenleg használható vállalati VPN-megoldása. A pilot körben
csak néhány belső rendszer (bérszámfejtés, ügyviteli rendszer webes felülete)
igényel VPN-hozzáférést.

| Lehetőség | Éves költség | Értékelés |
|---|---:|---|
| Azure VPN Gateway (VpnGw1) | kb. 1 400 000 Ft | Illeszkedik a platformhoz, Entra ID azonosítással |
| Külön gyártói VPN-eszköz | 2 800 000 Ft + eszköz | Külön üzemeltetés, külön azonosítás |
| Nincs VPN, csak felhős alkalmazások | 0 Ft | Nem járható: 2 belső rendszer így elérhetetlen |

**Javaslat:** Azure VPN Gateway. A költségvetésben az Azure infrastruktúra
tételen belül szerepel.

### 1.4 Fájlkezelés

| Kérdés | Megállapítás |
|---|---|
| Mekkora adatmennyiség érintett? | A pilot kör kb. 1,8 TB adatot tart a fájlszerveren |
| Kell-e átköltöztetni? | **Nem** — a projekt migráció nélküli. Az új munka SharePointon indul; a régi adat a fájlszerveren marad, olvasható maradhat. |
| Elegendő-e a tárhely? | Igen: Business Premium licencenként 1 TB OneDrive + 25 TB SharePoint alapterület |
| Mentés? | A megőrzési szabályokat be kell állítani; a felhő önmagában **nem** mentés |

> **Feltétel (F-3):** a mentési és megőrzési szabályokat a Biztonsági
> alapkonfigurációban rögzíteni kell, és visszaállítási tesztet kell végezni.

### 1.5 Kompetencia

| Terület | Jelenlegi állapot | Szükséges lépés |
|---|---|---|
| Entra ID / feltételes hozzáférés | Alapszintű | Oktatás Szabó Márknak (CSP partner biztosítja) |
| Intune / Autopilot | Nincs tapasztalat | Bevezetést a CSP partner végzi, átadással |
| SharePoint jogosultságkezelés | Alapszintű | Oktatás + dokumentált jogosultsági modell |
| Azure hálózat / VPN | Nincs tapasztalat | A CSP partner alakítja ki, Run-book átadással |

**Következtetés:** a belső kompetencia jelenleg **nem elegendő** az önálló
bevezetéshez. A bevezetést külső partnerrel kell végezni, dokumentált átadással.

> **Feltétel (F-4):** a szerződésben kötelezővé kell tenni a tudásátadást és a
> Run-book átadását, mint teljesítési feltételt.

## 2. Szervezeti megvalósíthatóság

| Kérdés | Megállapítás |
|---|---|
| Van-e kapacitás a projektre? | Az IT részlegről 2 fő, a napi munkája mellett. Ez **szűkös**. |
| Elfogadja-e a szervezet a változást? | Az előzetes érdeklődés kedvező: a home office lehetőség erős motiváció. |
| Van-e home office szabályzat? | Készül, HR-nél, várható elfogadás: 2026. március |
| Van-e üzemi tanács, amivel egyeztetni kell? | Igen, a home office és az eszközhasználat kérdésében véleményezési joga van. |
| Felkészült-e a Service Desk? | Nem. Új hibatípusokra kell felkészíteni, az élesítés előtt. |

> **Feltétel (F-5):** a home office szabályzatnak **az élesítés előtt** hatályba
> kell lépnie, különben a résztvevők jogilag rendezetlen helyzetben dolgoznak otthonról.

> **Feltétel (F-6):** az üzemi tanács véleményezését a tervezési fázisban be kell szerezni.

## 3. Jogi és megfelelőségi megvalósíthatóság

| Kérdés | Megállapítás |
|---|---|
| Hol tárolódnak az adatok? | Microsoft EU-s adatközpontokban (EU Data Boundary) |
| Kell-e adatfeldolgozói szerződés? | Igen, a CSP partnerrel és a Microsofttal (a licencfeltételek része) |
| Kell-e adatvédelmi hatásvizsgálat (DPIA)? | **Valószínűleg igen** — az Intune eszközfelügyelet miatt. A DPO előzetes véleménye szerint vizsgálandó. |
| Van-e ágazati előírás? | A Xyo Kft. nem tartozik különleges ágazati felügyelet alá. |
| Munkajogi kérdés? | A home office feltételeit a szabályzatban kell rendezni (eszköz, internet, munkaidő). |

> **Feltétel (F-7):** a DPO írásos állásfoglalását a tervezési fázisban be kell
> szerezni; ha DPIA szükséges, azt a beszerzés indítása előtt el kell készíteni.

## 4. Pénzügyi megvalósíthatóság

A részletes számítást a *Költség-haszon elemzés* tartalmazza. Megállapítások:

- A tervezett költség **50 743 000 Ft**, a rendelkezésre álló keret 52 000 000 Ft —
  a projekt **belefér**, 1 257 000 Ft mozgástérrel.
- A 2. évtől jelentkező **10 680 000 Ft/év folyó költségnek gazdát kell találni**
  az IT üzemeltetési keretben. Ez a projekt zárásának feltétele.
- A számítás érzékeny a hardverárra: 20%-os áremelkedés esetén a keret nem elegendő.

> **Feltétel (F-8):** a beszerzést a lehető legkorábban el kell indítani, hogy a
> hardverár még a tervezési fázisban ismertté váljon.

## 5. Következtetés

**A projekt megvalósítható**, az alábbi feltételekkel. Ezek a feltételek a
*Feltevés- és korlátnaplóba* átvezetendők, felelőssel és határidővel.

| Az. | Feltétel | Felelős | Határidő |
|---|---|---|---|
| F-1 | A résztvevők kijelölésénél a lakóhely internet-ellátottságát vizsgálni kell | Varga Eszter | 2026.02.27. |
| F-2 | Autopilot-regisztrációt az ajánlatkérésbe kell írni | Tóth Gergő | 2026.03.20. |
| F-3 | Mentési és megőrzési szabály + visszaállítási teszt | Szabó Márk | 2026.05.08. |
| F-4 | Tudásátadás és Run-book a szerződés teljesítési feltétele | Molnár Katalin | 2026.04.17. |
| F-5 | Home office szabályzat hatályba lépése az élesítés előtt | Varga Eszter | 2026.04.30. |
| F-6 | Üzemi tanács véleményezése | Varga Eszter | 2026.03.06. |
| F-7 | DPO állásfoglalás, szükség esetén DPIA | dr. Fekete Zsolt | 2026.03.06. |
| F-8 | Beszerzés korai indítása | Molnár Katalin | 2026.03.16. |

---

| Szerep | Név | Dátum |
|---|---|---|
| Koordinálta | Tóth Gergő, projektmenedzser | 2026.01.16. |
| Szakmai tartalom | Nagy Péter, IT osztályvezető | 2026.01.16. |
| Tudomásul vette | Kovács Anita, szponzor | 2026.01.22. |

> **Kapcsolódó dokumentumok:** bemenete a *Projekt ötlet*; kimenete az
> *Üzleti indoklás*, a *Projektalapító okirat* és az *Adatvédelmi hatásvizsgálat*.
> A 8 feltétel a *Feltevés- és korlátnaplóba* átvezetve.
