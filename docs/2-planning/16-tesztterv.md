# Tesztterv (Test Plan / UAT Plan)

**Dokumentum azonosítója:** XYO-CP-116\
**Projekt:** Xyo Cloud Pilot\
**Koordinálta:** Tóth Gergő, projektmenedzser\
**Készítette:** Nagy Péter (szakmai vezető), Fodor Gábor (felhasználói képviselő)\
**Verzió:** 1.1

> **Verziójegyzet:** v1.1 (2026.03.12.): a T-09 felvéve a 03.11-én hozzáadott
> K09 követelményhez (L7, üzemi tanács); a tesztesetek azonosítói a
> Követelmény-nyomonkövetési mátrix baseline-számozását követik.

> **Az UAT-t valós felhasználók végzik, valós feladatokkal.** Ha a rendszergazda
> teszteli, csak azt tudod meg, hogy a rendszergazda tud vele dolgozni.

---

## 1. A teszt hatóköre és szakaszai

| Szakasz | Mit vizsgál | Ki végzi | Mikor |
|---|---|---|---|
| **1. Technikai teszt** | Működik-e a konfiguráció műszakilag | Szabó Márk, 10 gépen | 2026.05.06–05.08. (a 10 tesztgép 05.06-ig érkezik) |
| **2. UAT — felhasználói átvételi teszt** | Alkalmas-e a **valós napi munkára** | 10 fős tesztcsoport, élesben | 2026.05.11–05.22. |
| **3. Újratesztelés** | A javított hibák rendben vannak-e | A hibát bejelentő tesztelő | 2026.05.25–06.02. |

**Nem része a tesztnek:** terheléses teszt (50 fő nem indokolja),
behatolásteszt (a biztonsági alapkonfiguráció külön ellenőrzés alatt áll).

## 2. Belépési feltételek

Az UAT **nem indulhat**, amíg ezek nem teljesülnek:

| # | Feltétel | Ki igazolja |
|---|---|---|
| BE-1 | A technikai teszt lezárult, nincs nyitott S1 hiba | Szabó Márk |
| BE-2 | A 10 tesztgép kiosztva, beüzemelve | Szabó Márk |
| BE-3 | A 10 tesztelő részt vett oktatáson | Varga Eszter |
| BE-4 | A tesztesetek elkészültek és jóváhagyva | Nagy Péter |
| BE-5 | A hibabejelentés csatornája működik és ismert | Kiss Réka |
| BE-6 | A Service Desk felkészítve | Kiss Réka |

## 3. Kilépési feltételek

Az UAT akkor zárható le:

| # | Feltétel |
|---|---|
| KI-1 | Minden K prioritású követelmény tesztesete lefutott |
| KI-2 | A tesztesetek **≥ 95%-a** megfelelt |
| KI-3 | **Nincs nyitott S1 (kritikus) hiba** |
| KI-4 | Minden nyitott S2 hibához elfogadott javítási határidő tartozik |
| KI-5 | A tesztjegyzőkönyv elkészült és aláírva |

## 4. A tesztcsoport

| # | Szempont | Létszám |
|---|---|---:|
| Pénzügy (Szilágyi Anna területe) | | 3 fő |
| Értékesítés (Fodor Gábor területe) | | 4 fő |
| Logisztika (Papp Zsófia területe) | | 3 fő |
| **Ebből: kevésbé IT-affin munkatárs** | | **2 fő** |
| **Ebből: rendszeresen otthonról dolgozna** | | **3 fő** |

> **A 2 kevésbé IT-affin tesztelő bevonása szándékos.** Ha csak a magabiztos
> kollégák tesztelnek, a teszt nem mutatja meg, hol akad el a többség — pedig
> pont ők adják majd a helpdesk ticketek nagy részét.

**Ráfordítás:** fejenként 8 óra tesztelési többletmunka 2 hét alatt.
A területvezetők írásban jóváhagyták (2026.03.09.).

## 5. Tesztesetek

A tesztesetek a Követelmény-nyomonkövetési mátrix mind a 27 elfogadott
tételéhez (K, F és H) kapcsolódnak. Minden esethez tartozik: előfeltétel, lépések, elvárt eredmény.

| # | Teszteset | Követelmény | Prioritás | Ki teszteli |
|---|---|---|:-:|---|
| T-01 | Belépés Entra ID azonosítóval | K01 | K | mind a 10 |
| T-02 | MFA második lépés végrehajtása | K02 | K | mind a 10 |
| T-03 | Elveszett eszköz hozzáférés-visszavonása | K03 | K | Szabó Márk (technikai) |
| T-04 | Break-glass fiók használata | K04 | K | Szabó Márk (technikai) |
| T-05 | Belépési kísérlet külföldi hálózatról (tiltott) | K05 | F | Szabó Márk (technikai) |
| T-06 | Belépés Office alkalmazásokba újbóli jelszó nélkül | K06 | F | mind a 10 |
| T-07 | Új gép beüzemelése Autopilottal, időméréssel | K07 | K | Szabó Márk (technikai) |
| T-08 | Lemeztitkosítás állapotának ellenőrzése | K08 | K | Szabó Márk (technikai) |
| T-09 | Az eszközfelügyeleti profil átnézése | K09 | K | dr. Fekete Zsolt |
| T-10 | Alapszoftverek megléte és indítása | K10 | K | mind a 10 |
| T-11 | Biztonsági frissítés telepítésének ellenőrzése | K11 | K | Szabó Márk (technikai) |
| T-12 | Monitor csatlakoztatása dokkolón / adapteren | K12 | K | mind a 10 |
| T-13 | OneDrive elérése, fájl mentése és megnyitása | K13 | K | mind a 10 |
| T-14 | SharePoint csapatoldal elérése; más csapaté nem | K14 | K | mind a 10 |
| T-15 | Törölt fájl visszaállítása a lomtárból | K15 | K | 3 tesztelő |
| T-16 | Teljes könyvtár visszaállítása | K16 | K | Szabó Márk (technikai) |
| T-17 | Régi fájlszerver olvasása VPN-en | K17 | F | 3 tesztelő (az érintett csapatokból) |
| T-18 | Dokumentum egyidejű szerkesztése két felhasználóval | K18 | F | 4 tesztelő |
| T-19 | Külső megosztási link lejárati idővel | K19 | H | 2 tesztelő |
| T-20 | VPN-kapcsolat felépítése otthoni mobilnetről | K20 | K | mind a 10, otthonról |
| T-21 | Bérszámfejtő és ügyviteli rendszer elérése VPN-en | K21 | K | mind a 10, otthonról |
| T-22 | VPN belépés Entra ID azonosítóval | K22 | F | mind a 10 |
| T-23 | 30 perces videóhívás mobilneten | K23 | F | 5 tesztelő |
| T-24 | Oktatáson való részvétel igazolása | K24 | K | Varga Eszter |
| T-25 | A gyorssegédlet használhatósága | K25 | K | a 2 kevésbé IT-affin tesztelő |
| T-26 | A Service Desk útmutató átvételének igazolása | K26 | K | Kiss Réka |
| T-27 | Önkiszolgáló jelszó-visszaállítás | K27 | F | 5 tesztelő |

**Összesen 27 teszteset**, ebből 19 kötelező (K).

## 6. „Egy napom az új környezetben" — szabad tesztelés

A strukturált tesztesetek mellett minden tesztelő **két teljes munkanapot**
kizárólag az új környezetben dolgozik, a saját valódi feladataival, és
naplózza, hol akadt el.

> **Ez találja meg azokat a hibákat, amikre nem gondoltunk.** A teszteset azt
> ellenőrzi, amit vártunk; a szabad használat azt, amit nem.

Kötelező napló-kérdések a nap végén:

1. Mi volt ma a legbosszantóbb?
2. Mit csináltál volna gyorsabban a régi gépen?
3. Kellett-e segítséget kérned? Mihez?
4. Mit nem találtál meg?

## 7. Hibabejelentés és -kezelés

| Lépés | Hogyan |
|---|---|
| Bejelentés | Service Desk ticket, **„CP-UAT" címkével** |
| Besorolás | Nagy Péter, 1 munkanapon belül (S1–S4) |
| Javítás | S1: 1 munkanap; S2: 5 munkanap; S3-S4: hypercare vagy átadás |
| Újratesztelés | **A hibát bejelentő tesztelő** végzi, nem a javító |
| Lezárás | A bejelentő visszaigazolása után |

> **Az újratesztelést a bejelentő végezze.** Aki javította, az tudja, hogyan
> kell „helyesen" használni — pont azt a lépést fogja kihagyni, ami a hibát
> okozta.

## 8. Napi és heti ritmus az UAT alatt

| Mikor | Mi | Ki |
|---|---|---|
| Naponta 16:00 | 15 perces hibaáttekintés | Nagy Péter, Szabó Márk, Kiss Réka |
| Hetente péntek | Tesztelői visszajelző kör (30 perc) | a 10 tesztelő + Nagy Péter |
| Naponta | Ticketstatisztika a státuszriporthoz | Kiss Réka |

## 9. Kockázatok

| Kockázat | Kezelés |
|---|---|
| A tesztelők nem valós feladattal dolgoznak | A 2 napos szabad tesztelés kötelező; a napló ellenőrizhető |
| A tesztelők nem érnek rá (napi munka mellett) | A területvezetők írásos jóváhagyása; napi 1 óra beépítve |
| Kevés hibát találunk, mert nem mernek bejelenteni | A visszajelző körön külön kérdezzük; a hibabejelentés nem panasz |
| Az újratesztelési ablak (9 nap) kevés | Az UAT az élesítéssel párhuzamosan fut, nem utána |

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Nagy Péter, IT osztályvezető | 2026.03.10. |
| Készítette | Fodor Gábor, felhasználói képviselő | 2026.03.10. |
| Koordinálta | Tóth Gergő, projektmenedzser | 2026.03.10. |
| Jóváhagyta | Projekt Irányító Bizottság | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete a *Követelmény-nyomonkövetési mátrix*
> és a *Minőségterv*; kimenete a *Tesztjegyzőkönyv* és az *UAT-elfogadás*.
