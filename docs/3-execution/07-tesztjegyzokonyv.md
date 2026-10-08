# Tesztjegyzőkönyv (Test Report)

**Dokumentum azonosítója:** XYO-CP-207\
**Projekt:** Xyo Cloud Pilot\
**Összeállította:** Tóth Gergő, projektmenedzser\
**Szakmai felelős:** Nagy Péter, IT osztályvezető\
**Tesztidőszak:** 2026.05.06 – 2026.06.16.\
**Verzió:** 1.2 (az újratesztelés után)

---

## 1. A teszt szakaszai

| Szakasz | Időszak | Ki végezte | Eredmény |
|---|---|---|---|
| Technikai teszt (10 gép) | 05.06 – 05.08. | Szabó Márk | lezárva, 2 S2 hibával |
| **UAT — 1. kör** | **05.11 – 05.22.** | 10 fős tesztcsoport | 22/27 teszteset megfelelt (81,5%) |
| Hibajavítás | 05.25 – 06.02. | Cloudia Solutions, Szabó Márk | 4 hiba javítva (H-03, H-04, H-07, H-11); további 5 már az 1. kör alatt, 1 utána — összesen 10 |
| **UAT — újratesztelés** | 06.03 – 06.16. | a bejelentő tesztelők | **26/27 megfelelt (96,3%)** |

## 2. Végeredmény

| Mutató | Érték | Kilépési feltétel | Teljesült? |
|---|---:|---|:-:|
| Lefutott tesztesetek | 27 / 27 | minden K prioritású | ✔ |
| Megfelelt | **26 / 27 = 96,3%** | ≥ 95% | ✔ |
| Nyitott S1 (kritikus) hiba | **0** | 0 | ✔ |
| Nyitott S2 hiba elfogadott határidővel | 1 | mindegyikhez határidő | ✔ |
| Nyitott S3–S4 hiba | 3 | — | ✔ |

**Következtetés: a megoldás átvehető.**

## 3. Tesztesetek eredménye

| # | Teszteset | Köv. | 1. kör | Újrateszt | Végeredmény |
|---|---|---|:-:|:-:|:-:|
| T-01 | Belépés Entra ID azonosítóval | K01 | ✖ | ✔ | ✔ |
| T-02 | MFA második lépés | K02 | ✖ | ✔ | ✔ |
| T-03 | Elveszett eszköz hozzáférés-visszavonása | K03 | ✔ | — | ✔ |
| T-04 | Break-glass fiók használata | K04 | ✔ | — | ✔ |
| T-05 | Belépés külföldi hálózatról (tiltott) | K05 | ✔ | ✔ *(regressziós)* | ✔ |
| T-06 | SSO az Office alkalmazásokba | K06 | ✔ | — | ✔ |
| T-07 | Autopilot beüzemelés időmérése | K07 | ✖ | ✔ | ✔ |
| T-08 | Lemeztitkosítás ellenőrzése | K08 | ✔ | — | ✔ |
| T-09 | Eszközfelügyeleti profil átnézése | K09 | ✔ | — | ✔ |
| T-10 | Alapszoftverek megléte | K10 | ✔ | — | ✔ |
| T-11 | Biztonsági frissítés telepítése | K11 | ✔ | — | ✔ |
| T-12 | Monitor csatlakoztatása | K12 | ✔ | — | ✔ |
| T-13 | OneDrive elérése, fájlmentés | K13 | ✔ | — | ✔ |
| T-14 | SharePoint csapatoldal, jogosultság | K14 | ✔ | — | ✔ |
| T-15 | Törölt fájl visszaállítása | K15 | ✔ | — | ✔ |
| T-16 | Teljes könyvtár visszaállítása | K16 | ✔ | — | ✔ |
| T-17 | Régi fájlszerver olvasása VPN-en | K17 | ✔ | — | ✔ |
| T-18 | Egyidejű dokumentumszerkesztés | K18 | ✔ | — | ✔ |
| T-19 | Külső megosztási link lejárattal | K19 | ✔ | — | ✔ |
| T-20 | VPN otthoni mobilnetről | K20 | ✔ | — | ✔ |
| T-21 | Bérszámfejtő és ügyviteli rendszer VPN-en | K21 | ✖ | ✔ | ✔ |
| T-22 | VPN belépés Entra ID-val | K22 | ✔ | — | ✔ |
| T-23 | 30 perces videóhívás mobilneten | K23 | ✖ | ✖ | **✖ nem felelt meg** |
| T-24 | Oktatáson való részvétel | K24 | ✔ | — | ✔ |
| T-25 | A gyorssegédlet használhatósága | K25 | ✔ | — | ✔ |
| T-26 | Service Desk útmutató átvétele | K26 | ✔ | — | ✔ |
| T-27 | Önkiszolgáló jelszó-visszaállítás | K27 | ✔ | — | ✔ |

> **Regressziós újrateszt (T-05).** A T-05 az 1. körben megfelelt: a külföldi
> belépést a CA-05 valóban tiltotta. A H-02 javítása azonban **ugyanezt a
> szabályt** módosította, ezért a T-05-öt is újra kellett futtatni. Amit egy
> javítás érint, azt akkor is újrateszteljük, ha korábban megfelelt.

## 4. Feltárt hibák

### S1 — kritikus (2 db, mindkettő javítva)

#### H-01 — A bérszámfejtő rendszer nem érhető el VPN-en

| | |
|---|---|
| Bejelentette | Szilágyi Anna területéről 2 tesztelő, 2026.05.11. |
| Teszteset | T-21 |
| Tünet | A VPN felépül, de a bérszámfejtő rendszer webes felülete nem töltődik be |
| Ok | A VPN útvonalválasztás csak a 10.10.5.35 (ügyviteli) címet tartalmazta, a 10.10.5.20 (bérszámfejtés) kimaradt a konfigurációból |
| Javítás | Útvonal hozzáadása a VPN-profilhoz | 
| Javítva | 2026.05.13. |
| Újratesztelve | 2026.06.03., ✔ megfelelt |

#### H-02 — Három tesztelő nem tud belépni (feltételes hozzáférés)

| | |
|---|---|
| Bejelentette | 3 tesztelő, 2026.05.11. — **az élesítés első napján** |
| Teszteset | T-01, T-02 (a CA-05 módosítása miatt a T-05 regressziós újratesztje is) |
| Tünet | Otthonról, mobilneten a belépés elutasítva |
| Ok | A **CA-05 országkorlátozási szabály** kizárta őket: a mobilszolgáltató CGNAT-kimenő IP-je külföldi tartományba sorolt |
| **Kapcsolódó kockázat** | **R11 — „A feltételes hozzáférési szabály kizárja a felhasználókat"** (bekövetkezett) |
| Miért nem szűrte ki a jelentés-mód? | A jelentés-mód **irodai hálózaton** futott 05.04–05.08. között; a mobilnetes belépés csak élesben jelent meg |
| Javítás | A CA-05 átállítva: országkorlátozás helyett megbízható eszköz + MFA |
| Javítva | 2026.05.12. (a bejelentés utáni napon) |
| Újratesztelve | 2026.06.03., ✔ megfelelt |
| Tanulság | A jelentés-módot **abban a hálózati környezetben** kell futtatni, ahol a felhasználók dolgozni fognak → Tanulságok naplója |

### S2 — súlyos (4 db)

| # | Hiba | Teszteset | Állapot |
|---|---|---|---|
| H-03 | A SharePoint keresés lassú (12–18 mp) nagy könyvtárakban | — | **javítva** 05.27. (indexelés újraépítve) |
| H-04 | 12 dokkoló nem tölti a laptopot | — | **javítva** 06.02. (hiányzó tápkábelek pótolva, P-08) |
| H-05 | Az Autopilot beüzemelés 2,1 óra, nem ≤1,5 óra | T-07 | **javítva** 05.19. (az ügyviteli kliens opcionálisra állítva) |
| H-06 | A videóhívás mobilneten 30 perc alatt megszakad | T-23 | **nyitva**, lásd alább |

### S3 — zavaró (5 db)

| # | Hiba | Állapot |
|---|---|---|
| H-07 | A OneDrive szinkronizálás első indításkor 40+ percig tart | javítva 05.26. (előszinkronizálás a kiosztás előtt) |
| H-08 | A céges alkalmazásportál magyar felirata hiányos | **nyitva**, átadva az üzemeltetésnek |
| H-09 | Az Authenticator értesítés néha 30+ mp késéssel érkezik | **nyitva**, szolgáltatói oldal, figyelés alatt |
| H-10 | A `CP-Kozos` csapatoldal hiányzott a struktúrából | javítva 05.20. (létrehozva az UAT visszajelzés alapján) |
| H-11 | A VPN-kliens nem indul automatikusan bejelentkezéskor | javítva 05.28. |

### S4 — kozmetikai (3 db)

| # | Hiba | Állapot |
|---|---|---|
| H-12 | A gyorssegédlet 3. képernyőképe elavult | javítva 06.05. |
| H-13 | Az alkalmazásportál ikonja nem céges | **nyitva**, átadva |
| H-14 | Elírás az oktatási diasor 12. diáján | javítva 05.17. |

## 5. Nyitva maradt hibák — elfogadott kezeléssel

| # | Hiba | Szint | Kezelés | Határidő | Felelős |
|---|---|:-:|---|---|---|
| H-06 | Videóhívás megszakadása mobilneten | S2 | A 2 érintett tesztelőnél a szolgáltatói lefedettség a probléma, nem a megoldás. Egyeztetés a mobilszolgáltatóval; ha nem javul, fix internet-hozzájárulás a tartalékból | 2026.07.31. | Nagy Péter |
| H-08 | Alkalmazásportál hiányos magyar felirat | S3 | A szállító a következő szolgáltatásfrissítéssel javítja | 2026.09.30. | Cloudia Solutions |
| H-09 | Authenticator értesítés késése | S3 | Szolgáltatói oldali jelenség; figyelés a hypercare alatt | folyamatos | Szabó Márk |
| H-13 | Alkalmazásportál ikon | S4 | Üzemeltetési feladat, ráérős | — | Szabó Márk |

**A T-23 teszteset (videóhívás) nem felelt meg.** Ez a 27-ből az egyetlen
bukott eset, és **F prioritású** (fontos, de nem kötelező) követelményhez
tartozik. A kilépési feltétel (≥95% és nincs nyitott S1) így is teljesül.

> **A nyitva maradt hibákat nem söpörjük a szőnyeg alá.** Ha írásban van, hogy
> tudunk róluk, mikor javítjuk és ki a felelős, az **védelem**; ha nincs, az
> elhallgatás — és az átvétel után derül ki.

## 6. A szabad tesztelés („egy napom az új környezetben") eredménye

A 10 tesztelő fejenként 2 teljes munkanapot dolgozott kizárólag az új
környezetben. A naplókból a leggyakrabban visszatérő megállapítások:

| Megállapítás | Hányan említették | Következmény |
|---|---:|---|
| „Nem tudtam, hova mentsem: OneDrive vagy SharePoint?" | 6 | A gyorssegédlet kiegészítve egy döntési ábrával |
| „Hiányzott egy közös hely a csapatok közötti anyagoknak" | 4 | `CP-Kozos` csapatoldal létrehozva (H-10) |
| „Az első szinkronizálás nagyon lassú volt" | 4 | Előszinkronizálás a kiosztás előtt (H-07) |
| „A VPN-t mindig kézzel kellett indítani" | 3 | Automatikus indítás beállítva (H-11) |
| „Otthonról gyorsabb, mint az irodában" | 3 | — (pozitív visszajelzés) |

> **A 27 teszteset egyike sem találta volna meg ezeket.** A tesztesetek azt
> ellenőrzik, amit vártunk; a szabad használat azt, amire nem gondoltunk.
> A `CP-Kozos` csapatoldal és az előszinkronizálás mindkettő innen jött.

## 7. Statisztika

| | |
|---|---:|
| Tesztesetek száma | 27 |
| Tesztelők | 10 fő |
| Tesztelési ráfordítás | 84 óra (tervezett: 80) |
| Feltárt hibák összesen | 14 |
| Ebből javítva | 10 |
| Ebből nyitva, elfogadott kezeléssel | 4 (H-06, H-08, H-09, H-13) |
| Az 1. kör hibáiból az élesítés napján derült ki | 2 (H-01, H-02) |

---

| Szerep | Név | Aláírás | Dátum |
|---|---|---|---|
| Összeállította | Tóth Gergő, projektmenedzser | | 2026.06.17. |
| Szakmai felelős | Nagy Péter, IT osztályvezető | | 2026.06.17. |

> **Kapcsolódó dokumentumok:** bemenete a *Tesztterv*; kimenete az
> *UAT-elfogadás*, a *Minőségellenőrzési jegyzőkönyv* és a *Problémanapló*.
