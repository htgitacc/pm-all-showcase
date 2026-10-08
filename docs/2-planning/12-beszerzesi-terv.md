# Beszerzési terv (Procurement Plan)

**Dokumentum azonosítója:** XYO-CP-112\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Molnár Katalin (beszerzési vezető) és Tóth Gergő (PM)\
**A folyamat gazdája:** Molnár Katalin\
**Verzió:** 1.1

> **IT projektben a beszerzés a leggyakoribb csúszásforrás** — és nem a munka
> miatt, hanem a **várakozás** miatt. A 32 napos beszerzési szakaszból
> mindössze 11 nap tényleges munka; a többi ajánlati határidő és belső
> jóváhagyás.

---

## 1. Beszerzési tételek

| # | Tétel | Becsült érték | Eljárás | Szállító típusa |
|---|---|---:|---|---|
| B1 | Laptop, dokkoló, monitor, headset | 27 750 000 Ft | **3 ajánlat, zárt eljárás** | hardver-viszonteladó |
| B2 | Microsoft 365 licenc + Azure előfizetés (12 hó) | 8 280 000 Ft | 3 ajánlat, CSP partnerektől | Microsoft CSP |
| B3 | Bevezetési szolgáltatás | 6 500 000 Ft | 3 ajánlat | rendszerintegrátor |
| B4 | Oktatás és változáskezelés | 1 200 000 Ft | 2 ajánlat (értékhatár alatt) | oktatási partner |
| B5 | Mobilinternet-hozzájárulás | 2 400 000 Ft | **meglévő keretszerződés** | mobilszolgáltatók |

> **B2 és B3 összevonva kerül kiírásra**, mert ugyanaz a CSP partner végzi a
> licencforgalmazást és a bevezetést. Így 14 780 000 Ft-os tételként egy
> eljárásban kezelhető, és a felelősség sem oszlik meg.

## 2. Az alkalmazandó eljárás

A cég beszerzési szabályzata (4.2 §) szerint:

| Értékhatár | Eljárás | Jóváhagyó | Átfutási idő |
|---|---|---|---|
| < 2 M Ft | 1 ajánlat elég | beszerzési vezető | 3 munkanap |
| 2–10 M Ft | 2 ajánlat | gazdasági igazgató | 5 munkanap |
| 10–25 M Ft | 3 ajánlat | gazdasági igazgató | 8 munkanap |
| **> 25 M Ft** | **3 ajánlat + értékelő bizottság** | **ügyvezető** | **8 munkanap** |

**A B1 tétel (27,75 M Ft) a legszigorúbb kategóriába esik:** értékelő bizottság
és ügyvezetői jóváhagyás kell.

## 3. Ütemezés — visszafelé számolva

**A kemény pont:** 10 tesztgépnek 2026.05.06-ig meg kell érkeznie, hogy az első
hullám 05.11-én indulhasson.

```
2026.05.06.  10 tesztgép a helyszínen        ← ez a kemény határidő
   ← 6 hét szállítási idő (részszállítás)
2026.04.17.  Szerződéskötés (M4)
   ← 8 munkanap belső jóváhagyási kör
2026.04.08.  Értékelés lezárva, javaslat kész
   ← 3 munkanap bontás, értékelés + bizottsági ülés (közte húsvét)
2026.04.02.  Ajánlati határidő lejár (a 04.03. Nagypéntek, munkaszüneti nap)
   ← 13 nap ajánlati szakasz (szabályzati minimum: 10 nap)
2026.03.20.  Ajánlatkérés kiadva
   ← 5 nap dokumentáció véglegesítése
2026.03.16.  Beszerzés indul (a Planning-kapu után)
```

| Lépés | Kezdés | Befejezés | Munkanap | Felelős |
|---|---|---|---:|---|
| Ajánlatkérési dokumentáció véglegesítése | 03.16. | 03.20. | 5 | Molnár Katalin, Nagy Péter |
| Ajánlatkérés kiadása | 03.20. | 03.20. | — | Molnár Katalin |
| Ajánlati szakasz | 03.23. | 04.02. | 9 | ajánlattevők |
| Ajánlatbontás és formai ellenőrzés | 04.02. | 04.02. | 1 | Molnár Katalin |
| Szakmai és pénzügyi értékelés | 04.07. | 04.07. | 1 | értékelő bizottság |
| Bizottsági ülés, javaslattétel | 04.08. | 04.08. | 1 | értékelő bizottság |
| Belső jóváhagyási kör | 04.09. | 04.16. | 6 | Kovács Anita → Horváth Júlia |
| Szerződéskötés | 04.17. | 04.17. | 1 | Molnár Katalin |

**Puffer a beszerzési szakaszban: 0 nap.** Ez a kritikus úton van.

> **Amit a tervezéskor megtanultunk:** eredetileg 03.30-ra terveztük az
> ajánlatkérés kiadását. Amikor Molnár Katalin megmutatta a szabályzat 10 napos
> ajánlati minimumát és a 8 munkanapos jóváhagyási kört, kiderült, hogy
> **2 hetet csúsztunk volna** — mielőtt egyetlen ajánlat is beérkezett volna.

## 4. Az ajánlatkérés kötelező elemei

A műszaki tartalmat Nagy Péter és Szabó Márk adja; a PM feladata, hogy az
alábbiak **biztosan benne legyenek**:

| # | Elem | Miért kritikus |
|---|---|---|
| P1 | **Autopilot-regisztráció** a szállítótól, gyári szinten | F-2 feltétel. Enélkül 50 gép × 6,5 óra = 325 óra kézi beüzemelés |
| P2 | **Részszállítás:** 10 gép 05.06-ig, 40 gép 05.29-ig | R1 kockázat válaszlépése; a kritikus úton nincs puffer |
| P3 | **Készlethelyzet igazolása** az ajánlatban | R1 korai jelzés |
| P4 | Kötbér a késedelemre: napi 0,5%, max. 10% | R1 következmény |
| P5 | **Adatfeldolgozói megállapodás** (B2, B3 tételnél) | GDPR-kötelezettség; szerződéskötéskor már nem alkudható |
| P6 | **EU-s adattárolás** kikötése | L6 korlát, DPO állásfoglalás |
| P7 | **Tudásátadás és Run-book** teljesítési feltételként | F-4 feltétel; enélkül nincs önálló üzemeltetés |
| P8 | Helyettesítési kötelezettség a nevesített konzultánsra | R14 kockázat |
| P9 | Fizetés mérföldkövekhez kötve | A határidő betartásának egyetlen valódi eszköze |
| P10 | A monitorok csatlakozótípusa: HDMI vagy DisplayPort | A7 tanulság |

> **P1 a legfontosabb tétel az egész dokumentumban.** Ha kimarad az
> ajánlatkérésből, utólag csak felárral vagy sehogy nem szerezhető meg — és a
> C-cél (1,5 óra/gép beüzemelés) teljesíthetetlenné válik.

## 5. Szerződéstípusok

| Tétel | Szerződéstípus | Miért |
|---|---|---|
| B1 hardver | Adásvételi, fix áras | Jól definiált termék, nincs bizonytalanság |
| B2 licenc | Előfizetéses, 12 hónapos | A Microsoft licencelési modellje ezt adja |
| B3 bevezetés | **Átalánydíjas (fix price)**, mérföldkövekhez kötött fizetéssel | Az óradíjas konstrukciónál a szállítónak érdeke a csúszás |
| B4 oktatás | Átalánydíjas | Fix tartalom, fix csoportszám |
| B5 mobilnet | Meglévő keretszerződés lehívása | Nincs új beszerzés |

> **Miért átalánydíjas a bevezetés?** Óradíjas szerződésnél a szállító a
> ráfordított órát számlázza — minél tovább tart, annál többet keres. Fix áras
> szerződésnél a késés az ő kockázata. Cserébe pontosabb specifikációt kell
> adnod, ezért fontos a részletes ajánlatkérés.

## 6. A beszerzés kockázatai

| # | Kockázat | Kezelés |
|---|---|---|
| R1 | Szállítás csúszik | P2 részszállítás, P3 készletigazolás, P4 kötbér |
| R8 | A belső jóváhagyási kör hosszabb 8 napnál | Molnár Katalin 03.16-án előre értesíti a pénzügyet és az ügyvezetői titkárságot a várható időpontról |
| — | Kevesebb mint 3 érvényes ajánlat érkezik | Előzetes piaci tájékozódás 02.24–26-án megtörtént: 5 potenciális ajánlattevő azonosítva |
| — | Az ajánlatok meghaladják a keretet | A Költségvetés 7. pontja szerinti hatókörcsökkentési javaslat készen áll |

## 7. Amit a beszerzésnek NEM adunk ki

| Mit | Miért |
|---|---|
| A jóváhagyott keretösszeg (52 M Ft) | Az ajánlatok ahhoz igazodnának |
| A belső költségbecslés | Ugyanez, és a szabályzat is tiltja |
| A másik ajánlattevő ára | Üzleti titok |
| A jelenlegi üzemeltetési költségek bontása | Visszaszámolható a fizetési hajlandóság |

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Molnár Katalin, beszerzési vezető | 2026.03.06. |
| Készítette | Tóth Gergő, projektmenedzser | 2026.03.06. |
| Jóváhagyta | Kovács Anita, szponzor | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete a *Költségvetés* és az *Ütemterv*;
> kimenete a *Szállítóértékelési szempontrendszer*, az *Ajánlatkérési
> dokumentáció* és a *Szerződés*.
