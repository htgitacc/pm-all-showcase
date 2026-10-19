# Incidens → probléma → ismert hiba: esetkövetés és nyilvántartás

**Dokumentum azonosítója:** XYO-ITIL-004\
**Szolgáltatás:** Felhőalapú munkahely (XYO-ITIL-001)\
**Készítette:** Szabó Márk, problémagazda, Kiss Rékával\
**Jóváhagyta:** Nagy Péter, szolgáltatásgazda\
**Dátum:** **2026. október 14.** — a PIR után, az SLA 1.1 verziójával együtt\
**Verzió:** 1.0

> ⚠ **ITIL 4-kiegészítés.** A Xyo-projekt minden hibát gondosan nyilvántartott — csak három
> különböző helyen, három különböző azonosítóval: a tesztjegyzőkönyvben (H-xx), a
> problémanaplóban (P-xx) és a Run-book hibakezelési részében (esetszám). Ez a dokumentum
> **összeköti őket**, és megmutatja, mi lesz belőlük az üzemeltetésben.
>
> **A lényege:** az incidenskezelés a szolgáltatást állítja helyre, a problémakezelés az okot
> szünteti meg. Az ismert hiba a kettő közötti híd: **ismerjük az okot, van kerülőmegoldás, de a
> végleges javítás még nincs meg.**

---

## 1. Három fogalom — és egy névütközés

| ITIL-fogalom | Angolul | Jelentés | A Xyo-nál |
|---|---|---|---|
| **Incidens** | *Incident* | A szolgáltatás nem tervezett megszakadása vagy minőségének romlása | Egy felhasználó bejelentése: „nem jön az MFA-értesítés” |
| **Probléma** | *Problem* | Egy vagy több incidens **oka** — tényleges vagy lehetséges | Miért késik az értesítés, és miért ismétlődik? |
| **Ismert hiba** | *Known error* | Olyan probléma, amelynek okát elemezték, de még nem szüntették meg | „Szolgáltatói oldali késés; kerülőmegoldás: kódos belépés” |

> **Vigyázat, névütközés.** A Xyo **Problémanaplója** (XYO-CP-210) a PMI *issue log*-ja: a
> projekt akadályainak nyilvántartása. A 13 bejegyzés ITIL-szemmel vegyes: a P-04 és a P-05
> incidens volt (az élesítés első napján nem tudtak dolgozni), a P-09 probléma (ugyanaz az ok
> minden gépnél, 5. pont), a P-02 (kiesett konzultáns) pedig egyik sem — tiszta projektakadály.
> **Egy ITIL-t ismerő csapatban ezt a
> naplót „Issue-napló” vagy „Akadálynapló” névre kell keresztelni**, különben a
> problémakezelés bevezetésekor mindenki mást ért a szón.

## 2. Az azonosítók láncai

A projekt átadáskor nyitva hagyott hibái négy helyen szerepelnek. ITIL-szemmel mindegyikből
**ismerthiba-rekord** lesz (KE-xx), egy esetben **problémarekord** is (PR-01).

| Hiba (Tesztjegyzőkönyv) | Projektakadály (Problémanapló) | Run-book eset | Ismert hiba | Problémarekord |
|---|---|---|---|---|
| H-06 — videóhívás mobilneten | P-11 | 14. | KE-01 | — |
| H-08 — alkalmazásportál magyar felirata | P-12 | 15. | KE-02 | — |
| H-09 — Authenticator-értesítés késése | P-13 | 1. | KE-03 | **PR-01** |
| H-13 — alkalmazásportál ikonja | — | — | KE-04 | — |

> **Mire jó ez a táblázat?** Amikor a Service Desk egy hívásnál az 1. esetet látja a
> Run-bookban, innen tudja meg, hogy az KE-03, és hogy van mögötte egy nyitott probléma — vagyis a
> bejelentést **hozzá kell kötni**, nem csak lezárni. Ezen az egy mezőn múlik, hogy a PIR
> később meg tudja-e mondani, hány ticketet okozott a hiba.

## 3. Ismerthiba-nyilvántartás

### 3.1 Az átadáskor (2026.06.26.) — a Run-book 7. pontjából

| # | Ismert hiba | Kiváltó ok | Kerülőmegoldás a Service Desknek | Gazda | Határidő |
|---|---|---|---|---|---|
| KE-01 | Videóhívás megszakad mobilneten (2 felhasználó) | Gyenge mobilszolgáltatói lefedettség a lakóhelyükön — nem a megoldás hibája | Sávszélesség-mérés; ha tartósan gyenge, jelentés Nagy Péternek | Nagy Péter | 2026.07.31. |
| KE-02 | Angol feliratok az alkalmazásportálon | Szállítói hiba | „Nem hiba, javítás folyamatban a szállítónál” | Cloudia Solutions | 2026.09.30. |
| KE-03 | Késik az Authenticator-értesítés | Szolgáltatói oldali jelenség, nem konfigurációs hiba | Authenticator kézi megnyitása; ha 1 percen túl sem jön, jelszó + kódos belépés | Szabó Márk | folyamatos |
| KE-04 | Az alkalmazásportál ikonja nem céges | Beállítás hiányzik | Nincs rá szükség — kozmetikai | Szabó Márk | — |

### 3.2 A PIR után (2026.10.14.)

| # | Állapot | Mi történt | Forrás |
|---|---|---|---|
| KE-01 | **lezárva** | A szolgáltatói egyeztetés eredményt hozott; a 240 000 Ft-os feltételes keret nem került felhasználásra | PIR 7. pont |
| KE-02 | **lezárva** | Javítva a szállítói frissítéssel | PIR 7. pont |
| KE-03 | **nyitva** | „Szolgáltatói oldal, figyelés alatt” — négy hónapja | PIR 7. pont |
| KE-04 | **lezárva** | Javítva | PIR 7. pont |

**Négy ismert hibából három lezárva, egy nyitva.** A nyitott egy (KE-03) az, amelyiknek nincs
végleges javítási útja — ezért kap problémarekordot.

> **Tipikus hiba:** az ismert hibát a projekt végén „átadja” a projekt, és onnantól senki nem
> nézi meg. A KE-01, KE-02 és KE-04 azért zárult le, mert **volt határideje és gazdája**. A
> KE-03-nak gazdája volt, határideje nem.

## 4. Problémarekord: PR-01 — késő MFA-értesítés

| | |
|---|---|
| **Felvéve** | 2026.10.14. (visszamenőleg; a jelenség 2026.06.04. óta ismert, P-13) |
| **Kapcsolódó ismert hiba** | KE-03 |
| **Kapcsolódó incidensek** | Run-book 1. eset; a ticketrendszerben eddig nem volt összekötve |
| **Hatás** | A PIR szerint az M1 mutató (ticket/hó) elmaradásának egyik oka; a kérdőívben a 44 válaszadóból 12 említette; a sebességre vonatkozó K4 kérdés lett a leggyengébb (3,8) |
| **Prioritás** | Közepes — egyenként P3 incidensek (van kerülőmegoldás), de sok felhasználót érint, és rontja az elégedettséget |
| **Problémagazda** | Szabó Márk |

### 4.1 A problémakezelés három szakasza a PR-01-en

| Szakasz | ITIL-név | Mi a kérdés | PR-01 |
|---|---|---|---|
| **Azonosítás** | *Problem identification* | Ismétlődik-e? Mekkora a hatása? | A projekt már a tesztelésnél észlelte (H-09); a hatás mértékét a kérdőív és a PIR mutatta meg |
| **Kontroll** | *Problem control* | Mi az oka? Van-e kerülőmegoldás? | Szolgáltatói oldali jelenség; a kerülőmegoldás a Run-bookban — **ez a szakasz kész** |
| **Hibakontroll** | *Error control* | Megszüntethető-e, és megéri-e? | **Itt akadt el:** a „figyelés alatt” nem döntés |

### 4.2 Döntés (2026.10.14.)

| # | Döntés | Ki | Határidő |
|---|---|---|---|
| 1 | Szállítói ügy nyitása a Microsoftnál a CSP-partneren (Cloudia Solutions) keresztül, a jelenség leírásával és a bejelentések számával | Szabó Márk | 2026.10.30. |
| 2 | A ticketrendszerben az MFA-késéssel kapcsolatos bejelentések összekötése a PR-01-gyel | Kiss Réka | azonnal |
| 3 | **Kiváltó feltétel** a továbblépéshez: ha egy hónapban legalább öt bejelentés kapcsolódik a PR-01-hez, a probléma prioritása magasra emelkedik, és Nagy Péter a szolgáltatás-felülvizsgálat napirendjére veszi | Nagy Péter | havonta, a szolgáltatásszint-riporttal |
| 4 | Alternatíva vizsgálata a kiterjesztés előtt: más hitelesítési mód (pl. a pilotban tudatosan kihagyott hardveres kulcs újbóli mérlegelése, Run-book 7. pont) | Szabó Márk, dr. Fekete Zsolt | a kiterjesztés tervezési fázisában |

> **A „figyelés alatt” nem állapot, hanem halasztás.** A problémakezelés nem azt kéri, hogy
> minden problémát megoldjunk — van, amit nem éri meg. Azt kéri, hogy **valaki döntsön**, és a
> döntésnek legyen mérhető feltétele. A 3. sor ezt adja meg.

## 5. Egy megoldott probléma a projektből: a lassú első nap

A problémakezelés nem új a Xyo-nak — a projekt egyet már megoldott, csak nem így hívta.

| Lépés | Mi történt | Forrás |
|---|---|---|
| Incidensek | A tesztelők jelezték: az első bejelentkezéskor a gép 40+ percig használhatatlan | H-07, P-09 |
| A probléma | Ugyanaz az ok minden új gépnél: az első OneDrive-szinkronizálás | P-09 |
| Végleges megoldás | **Előszinkronizálás a kiosztás előtt**, a raktárban, céges hálózaton — a 2. és 3. hullámnál már így ment | P-09, D-17 |
| Ami megmaradt | A Run-book 8. esete („Lassú a gép”): ha mégis előfordul, 1 óra türelem, utána eszkaláció | Run-book 4. pont |

> **Ez a minta arra, ahogy a PR-01-nek is végződnie kellene:** ismétlődő incidensek → közös ok →
> végleges javítás → a Run-book már csak a maradék esetet kezeli.

## 6. Kiemelt incidens — ami a Run-bookból hiányzik

A Run-book eszkalációs útja (5. pont) az **adatvédelmi incidenst** külön kezeli: „AZONNAL, a
szinteket átugorva”. A **szolgáltatáskiesésre** — amikor a pilot kör egésze nem tud dolgozni —
nincs külön eljárás. A projekt idején ezt a **Visszaállási terv** fedte le (hullám-szintű
visszaállás, ha a résztvevők több mint 30%-a nem tud belépni); a régi gépek selejtezésével
(2026.07.10.) ez a lehetőség megszűnt.

### 6.1 Mikor kiemelt?

Ha az alábbiak bármelyike igaz (az SLA szerinti **P1**):

| # | Kiváltó esemény | Példa |
|---|---|---|
| K1 | A pilot kör egy teljes csapata vagy egésze nem tud dolgozni | Microsoft 365-kiesés; a feltételes hozzáférés mindenkit kizár |
| K2 | Biztonsági esemény | Elveszett vagy ellopott gép (Run-book 10. eset); gyanús bejelentkezés |
| K3 | Adatvédelmi incidens | Személyes adat jogosulatlan hozzáférése |

### 6.2 Ki mit csinál

| Szerep | Ki | Feladat |
|---|---|---|
| **Incidensfelelős** | Nagy Péter | Dönt, koordinál, tájékoztatja a vezetést |
| Technikai vezető | Szabó Márk | Diagnózis: Microsoft szolgáltatásállapot-jelentés, Entra bejelentkezési napló; szükség esetén break-glass fiók |
| Kommunikáció | Kiss Réka | Tájékoztatja az érintett felhasználókat — a hypercare idején is ő tette (Kommunikációs terv 3. pont) |
| Adatvédelem (K3) | dr. Fekete Zsolt | Azonnal bevonva; NAIH-bejelentés 72 órán belül, ha szükséges |

| Lépés | Mikor |
|---|---|
| A felhasználók első tájékoztatása: mi nem működik, mi a kerülőút | 15 percen belül |
| Frissítés a helyzetről | óránként, a helyreállításig |
| Horváth Júlia tájékoztatása | ha a kiesés várhatóan 4 munkaóránál tovább tart |
| **Utólagos értékelés** — mi történt, miért, mit változtatunk; szükség esetén problémarekord | 5 munkanapon belül |

> **Miért nem elég a Microsoft-állapotjelentés?** Mert a felhasználót nem az érdekli, hogy kinek a
> hibája, hanem hogy mikor dolgozhat újra, és mit tegyen addig. A kiemelt incidens lényege
> nem a technika — azt a beszállító javítja —, hanem a **kommunikáció és a döntés**.

## 7. Mit mérünk — célként, nem eredményként

| Mutató | Cél | Miért |
|---|---|---|
| Problémához kötött incidensek aránya | minden ismétlődő tünetnél 100% | Enélkül a hatás nem mérhető (PR-01) |
| Ismert hibák határidővel és gazdával | 100% | A KE-01, KE-02, KE-04 ezért zárult le |
| Nyitott problémák kora | egyik sem 90 napnál régebbi döntés nélkül | A „figyelés alatt” ne legyen végállapot |
| Kiemelt incidens utáni értékelés | minden esetben, 5 munkanapon belül | Tanulás a ritka, nagy hatású esetekből |

*Ezekre még nincs mért adat. Az első értékelés a 2027. januári szolgáltatás-felülvizsgálaton
lesz (XYO-ITIL-002, 2. pont).*

---

## Mi a különbség a projekt hibakezeléséhez képest?

| | Projekt (Tesztjegyzőkönyv + Problémanapló) | **ITIL 4 (incidens, probléma, ismert hiba)** |
|---|---|---|
| Mit kezel | Hibát (H-xx) és projektakadályt (P-xx) | **Szolgáltatásromlást és annak okát** |
| Mi a mérce | Súlyosság (S1–S4): blokkolja-e az átvételt? | **Prioritás (P1–P4):** mennyire érinti a szolgáltatást? |
| Mikor zárul | Javításkor, vagy elfogadott kezeléssel az átvételkor | **Incidens:** helyreállításkor; **probléma:** a megszüntetéskor vagy tudatos döntéskor |
| Ki a gazdája | A projektmenedzser | **A Service Desk (incidens) és a problémagazda** |
| Mi marad meg | A tanulságok naplója | **Ismerthiba-nyilvántartás**, amit a Service Desk naponta használ |

> **A tanulság egy PM-nek:** a projekt által nyitva hagyott hiba nem tűnik el az átadással —
> **ismert hibaként él tovább**, és a projekt minősége azon is mérhető, mennyire jól írta le. A
> Xyo itt jól teljesített: minden nyitott hibának volt kerülőmegoldása és gazdája. Egy dolgot
> kell még hozzátenni: **határidőt vagy kiváltó feltételt** minden nyitott tételhez.

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Szabó Márk, problémagazda; Kiss Réka, Service Desk vezető | 2026.10.14. |
| **Jóváhagyta** | **Nagy Péter**, szolgáltatásgazda | 2026.10.14. |

---

> **Kapcsolódó dokumentumok:** bemenete a *Tesztjegyzőkönyv*, a *Problémanapló*, a *Run-book*
> (4., 5. és 7. pont), a *Visszaállási terv*, az *Átadás-átvételi jegyzőkönyv*, a *Felhasználói
> kérdőív* és a *PIR*; kimenete az *SLA* szolgáltatásszint-riportja (XYO-ITIL-002) és a
> *Folyamatos fejlesztési nyilvántartás* (XYO-ITIL-006).
