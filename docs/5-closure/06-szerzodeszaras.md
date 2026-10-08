# Szerződészárás (Contract Closure)

**Dokumentum azonosítója:** XYO-CP-406\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Molnár Katalin, beszerzési vezető\
**Szakmai teljesülést igazolta:** Tóth Gergő (PM) és Nagy Péter (szakmai vezető)\
**Dátum:** **2026. június 30.**

> A nyitva maradt szerződés később **jogi és pénzügyi kockázat**. A zárás
> akkor teljes, ha minden teljesült, minden számla rendezve, és a
> **garanciális feltételek írásban rögzítve** vannak — mert azokat a projekt
> után az üzemeltetés fogja használni.

---

## 1. Lezárt szerződések

| # | Szállító | Tárgy | Nettó érték | Teljesítés | Zárás |
|---|---|---|---:|---|---|
| 1 | **TechLine Zrt.** | 50 munkaállomás-készlet | 26 890 000 Ft | 2026.06.02. | ✔ lezárva |
| 2 | **Cloudia Solutions Kft.** | M365 licenc + felhőkörnyezet bevezetése | 14 200 000 Ft | 2026.06.19. | ✔ lezárva |
| 3 | Cloudia Solutions Kft. | Oktatás és változáskezelés (B4) | 1 150 000 Ft | 2026.06.10. | ✔ lezárva |
| — | Mobilszolgáltatók | Mobilinternet-hozzájárulás | keretszerződés | folyamatos | **nem zárul** — átadva az üzemeltetésnek |

---

## 2. TechLine Zrt. — teljesülés igazolása

| Szerződéses vállalás | Teljesült? | Bizonyíték |
|---|:-:|---|
| 1. részszállítás, 10 készlet, 2026.05.06-ig | ✔ | 1. sz. átvételi jkv., **2026.05.05.** (1 nappal korábban) |
| 2. részszállítás, 40 készlet, 2026.05.29-ig | ✔ | 2. sz. átvételi jkv., **2026.05.28.** (1 nappal korábban) |
| Sz-2: Autopilot-regisztráció | ✔ | Intune eszközlista: 50/50 |
| Sz-3: monitor HDMI/DP csatlakozóval | ✔ | 50/50 ellenőrizve |
| Sz-4: dokkoló töltés és 2 kijelző | ✔ | mintavételes teszt |
| Sz-5: gyári specifikáció | ✔ | mintavételes ellenőrzés |
| Hiánypótlás (12 db tápkábel) | ✔ | 3. sz. jkv., **2026.06.02.** (1 nappal a vállalt határidő előtt) |

### Hibás teljesítés és kötbér

| | |
|---|---|
| **Feltárt hiány** | 12 db dokkoló tápkábel a 2. részszállításnál |
| **Kezelés** | Fenntartással történő átvétel, tételes hiánylistával; a 80%-os fizetési részlet visszatartva |
| **Pótlás** | 2026.06.02., a vállalt határidőn belül |
| **Kötbér** | **Késedelmi kötbér nem keletkezett.** Mindkét részszállítás a határidő előtt érkezett (05.05., 05.28.); a 12 tápkábel hiánya mennyiségi hiány, vagyis hibás teljesítés, nem késedelem — ezt a szállító a vállalt határidőn belül pótolta. Viszonyításként: ha a 2. részszállítás késett volna, a kötbér napi 107 560 Ft (21 512 000 Ft × 0,5%) lett volna, legfeljebb 2 689 000 Ft (a szerződéses érték 10%-a). |
| **Vitatott tétel** | Nincs |

### Garanciális feltételek — az üzemeltetésnek átadva

| | |
|---|---|
| **Garancia** | 3 év, **helyszíni szerviz, következő munkanapi kiszállással** |
| **Kezdete** | 2026.05.29. (a teljes szállítás átvétele) |
| **Vége** | **2029.05.29.** |
| **Bejelentés módja** | A szerződés 4. sz. mellékletében rögzített szervizcsatorna |
| **Kire terjed ki** | Mind az 50 laptop, dokkoló, monitor, headset |

## 3. Cloudia Solutions Kft. — teljesülés igazolása

| Szerződéses vállalás | Teljesült? | Bizonyíték |
|---|:-:|---|
| M5: környezet tesztelésre kész, 2026.05.08-ig | ✔ | 4. sz. teljesítésigazolás, 2026.05.08. |
| Oktatási anyag és gyorssegédlet, 2026.05.15-ig | ✔ | Oktatási anyag, XYO-CP-209 |
| 5 oktatási csoport, 2026.06.10-ig | ✔ | Jelenléti ívek, 50/50 fő |
| M8: UAT elfogadva, 2026.06.19-ig | ✔ | UAT-elfogadás, XYO-CP-208 |
| Sz-6: átvételi kritériumok (AK-01 – AK-23) | ✔ | 22/23 megfelelt (a teljes listán 25/26); az AK-19 nem a szállító hibája |
| **Sz-7: as-built és Run-book átadva, elfogadva** | ✔ | Nagy Péter írásos elfogadása, 2026.06.19. (UAT-elfogadás, AK-23); megerősítve az átadás-átvételkor, 06.26. |
| **Sz-8: rendszergazdai tudásátadás** | ✔ | 3 napos oktatás + közös munkavégzés, dokumentálva |
| Sz-9: DPO-igazolás az Intune profilról | ✔ | dr. Fekete Zsolt, 2026.05.07. |
| Sz-10: EU Data Boundary konfiguráció | ✔ | As-built 1. pont, ellenőrizve |
| V8: helyettesítési kötelezettség | ✔ | 2026.04.24-i kiesés, 2 munkanapon belül helyettes |

### Az AK-19 kritérium és a szállítói felelősség

| | |
|---|---|
| **Mi nem teljesült** | AK-19 — 30 perces videóhívás mobilneten, 3/5 sikeres |
| **Ok** | Két tesztelő lakóhelyén gyenge a mobilszolgáltatói lefedettség |
| **Szállítói felelősség** | **Nincs.** Az ok a szolgáltatói lefedettség, nem a Cloudia által kialakított konfiguráció. A bizonyítást a sávszélesség-mérés adja. |
| **Következmény** | A teljesítést nem érinti; a hiba kezelése a Xyo Kft. hatáskörében marad (VK-04) |

> **Fontos megkülönböztetés:** az, hogy egy átvételi kritérium nem teljesült,
> **nem jelenti automatikusan a szállító hibás teljesítését.** Az okot meg
> kell vizsgálni, és a jegyzőkönyvben rögzíteni.

### Adminisztrátori hozzáférés megszűnése

| | |
|---|---|
| Szerződéses kikötés | A Vállalkozó Intune-adminisztrátori jogosultsága az UAT-elfogadással megszűnik |
| Esedékesség | 2026.06.19. |
| **Ellenőrizve** | **2026.06.26., Szabó Márk** — a hozzáférés megszűnt |

### Szavatosság — az üzemeltetésnek átadva

| | |
|---|---|
| **Szavatosság** | 6 hónap a bevezetésre (konfigurációs hibák) |
| **Kezdete** | 2026.06.19. |
| **Vége** | **2026.12.19.** |
| **Mire terjed ki** | A Vállalkozó által kialakított konfiguráció hibáinak díjmentes javítása |
| **Nyitott, szavatosság alatti hiba** | **H-08** — az alkalmazásportál hiányos magyar felirata, javítás 2026.09.30-ig |

## 4. Szállítói teljesítményértékelés

*(Belső használatra. A szállítónak a szerződéses teljesítésről adunk
visszajelzést, nem a belső pontszámokról.)*

| Szempont | TechLine Zrt. | Cloudia Solutions Kft. |
|---|:-:|:-:|
| Határidő-tartás | **5/5** — mindhárom határidőt 1 nappal korábban | **5/5** — minden mérföldkő pontosan |
| Minőség | 4/5 — 12 hiányzó tápkábel | **5/5** — eltérés nélkül |
| Dokumentáció | 4/5 | **5/5** — a Run-book kiemelkedő |
| Együttműködés, kommunikáció | 4/5 | **5/5** |
| Problémakezelés | **5/5** — a hiányt a helyszínen elismerte, korábban pótolta | **5/5** — a konzultáns-kiesést proaktívan kezelte |
| Ár-érték arány | **5/5** | 4/5 — nem a legolcsóbb ajánlat volt |
| **Átlag** | **4,5** | **4,8** |

### Javaslat a jövőbeli beszerzésekhez

| Szállító | Javaslat |
|---|---|
| **TechLine Zrt.** | **Ajánlott.** A kiterjesztési projektnél újra megszólítandó. Figyelem: a csomagolási hiányra (tápkábelek) az átvételnél tételes ellenőrzés szükséges. |
| **Cloudia Solutions Kft.** | **Kifejezetten ajánlott.** A tudásátadás és a dokumentáció minősége a kiterjesztésnél is döntő szempont lesz. |
| NovaComp Kft. | Kizárva volt (Autopilot-vállalás hiánya). A kiterjesztésnél újra megszólítható, ha a vállalást teljesíti. |
| Azurion Consulting Kft. | Nem ajánlott bevezetési feladatra; a tudásátadási képessége dokumentáltan gyenge. |

> **A szállítói értékelést akkor is el kell készíteni, ha nem kérik.**
> A következő beszerzésnél ez lesz az egyetlen tényalapú információd —
> egyébként az emlékezetre kellene hagyatkozni.

## 5. Amit az üzemeltetés átvesz

| Mit | Meddig | Hol dokumentált |
|---|---|---|
| TechLine hardvergarancia (3 év, helyszíni NBD) | 2029.05.29. | Run-book 6. pont |
| Cloudia bevezetési szavatosság (6 hó) | 2026.12.19. | Run-book 6. pont |
| Microsoft M365 licenc (megújítás!) | 2027.04.30. | Run-book 3. pont |
| Mobilinternet keretszerződés | folyamatos | Pénzügyi zárás 6. pont |
| Nyitott, szavatosság alatti hiba (H-08) | 2026.09.30. | Run-book 7. pont |

## 6. Zárási ellenőrzőlista

| # | Feltétel | TechLine | Cloudia |
|---|---|:-:|:-:|
| 1 | Minden szerződéses vállalás teljesült | ✔ | ✔ |
| 2 | Teljesítésigazolások aláírva | ✔ | ✔ |
| 3 | Minden számla kiegyenlítve | ✔ | ✔ |
| 4 | Nincs vitatott tétel | ✔ | ✔ |
| 5 | Kötbér-, illetve hibás teljesítési igény rendezve | ✔ (kötbér nem keletkezett; a hiánypótlás 06.02-án teljesült) | ✔ (nem merült fel) |
| 6 | Garanciális / szavatossági feltételek rögzítve és átadva | ✔ | ✔ |
| 7 | Szállítói hozzáférések megszűntek | n. a. | ✔ |
| 8 | Teljesítményértékelés elkészült | ✔ | ✔ |

**Mindhárom szerződés 2026.06.30-i hatállyal lezárva.**

---

| Szerep | Név | Aláírás | Dátum |
|---|---|---|---|
| Készítette | Molnár Katalin, beszerzési vezető | | 2026.06.30. |
| Szakmai teljesülést igazolta | Nagy Péter, IT osztályvezető | | 2026.06.30. |
| Szakmai teljesülést igazolta | Tóth Gergő, projektmenedzser | | 2026.06.30. |

> **Kapcsolódó dokumentumok:** bemenete a *Szerződés* és a
> *Teljesítésigazolás*; kimenete a *Pénzügyi zárás* és az
> *Archiválási jegyzék*.
