# Problémanapló (Issue Log)

**Dokumentum azonosítója:** XYO-CP-210\
**Projekt:** Xyo Cloud Pilot\
**Vezeti:** Tóth Gergő, projektmenedzser\
**Utolsó frissítés:** 2026. június 19.\
**Verzió:** 1.9 — **élő dokumentum**, naponta frissítve

> **A már bekövetkezett problémák nyilvántartása** — szemben a kockázattal,
> ami még csak fenyegetés. Megmutatja, hogy a problémát észrevetted, kezelted,
> és mikor zártad le.
>
> **Ha egy probléma korábban azonosított kockázatból lett, hivatkozz rá.**
> Ez bizonyítja, hogy előre láttad és jelezted.

---

## 1. Lezárt problémák

### P-01 — A jelszóházirend ütközik a meglévő AD-házirenddel

| | |
|---|---|
| Felmerült | 2026.04.21. |
| Bejelentette | Szabó Márk (a 4.3 munkacsomag visszaigazolásában) |
| Leírás | A tervezett 12 karakteres, lejárat nélküli jelszóházirend ütközik a cég helyi AD-házirendjével, ami 8 karaktert és 90 napos lejáratot ír elő |
| Hatás | Hatókör: nincs. Ütem: 2 nap. Költség: nincs. |
| Kezelés | A pilot köre **csak felhő** azonosítást használ, nincs hibrid szinkronizáció — a helyi AD-házirend nem érvényes rájuk. Nagy Péter írásban megerősítette. |
| Felelős | Szabó Márk |
| Lezárva | 2026.04.23. |

> Ez a probléma a **munkacsomag-visszaigazolás** miatt derült ki, még mielőtt
> bárki elkezdett volna dolgozni rajta. Jó példa arra, miért kell visszaigazolást kérni.

### P-02 — Egy CSP-konzultáns kiesett

| | |
|---|---|
| Felmerült | 2026.04.24. |
| Bejelentette | Cloudia Solutions Kft. |
| Leírás | A két nevesített konzultáns egyike tartós betegállományba került |
| Hatás | Ütem: 3.1.2 és 3.2.1 munkacsomag veszélyben |
| **Kapcsolódó kockázat** | **R14 — „A CSP partner kulcsembere kiesik"** (alacsony besorolás, bekövetkezett) |
| Kezelés | A szerződés **helyettesítési kötelezettséget** ír elő azonos vagy magasabb minősítésű szakemberrel, a Megrendelő jóváhagyásával. A szállító 2 munkanapon belül helyettest állított, Nagy Péter jóváhagyta. |
| Felelős | Molnár Katalin |
| Lezárva | 2026.04.28., csúszás nélkül |

> **A szerződéses kikötés itt térült meg.** A helyettesítési kötelezettség
> nélkül a szállító azt mondhatta volna, hogy „majd ha visszajön".

### P-03 — Az önkiszolgáló jelszó-visszaállítás nem működött MFA nélkül

| | |
|---|---|
| Felmerült | 2026.05.06. |
| Bejelentette | Szabó Márk (technikai teszt) |
| Leírás | A funkció csak regisztrált MFA-módszerrel működik; az első belépés előtt álló felhasználónál nem használható |
| Hatás | Minőség: a K27 követelmény részben nem teljesül |
| Kezelés | Elfogadott működés: az MFA regisztrációja az oktatáson megtörténik, tehát az első belépés előtti helyzet nem áll elő. Az oktatási tematika 2. blokkja emiatt 30 percre bővült. |
| Felelős | Varga Eszter |
| Lezárva | 2026.05.07. |

### P-04 — A bérszámfejtő rendszer nem érhető el VPN-en

| | |
|---|---|
| Felmerült | **2026.05.11. — az élesítés első napján** |
| Bejelentette | 2 tesztelő (Pénzügy) |
| Leírás | A VPN felépül, de a bérszámfejtő rendszer nem töltődik be (H-01, S1 hiba) |
| Hatás | 2 tesztelő nem tudja a napi munkáját végezni |
| Kezelés | A VPN-profil útvonaltáblájából hiányzott a 10.10.5.20 cím. Kiegészítve. |
| Felelős | Szabó Márk |
| Lezárva | 2026.05.13. |

### P-05 — Három tesztelő nem tud belépni (feltételes hozzáférés)

| | |
|---|---|
| Felmerült | **2026.05.11. — az élesítés első napján** |
| Bejelentette | 3 tesztelő |
| Leírás | Otthonról, mobilneten a belépés elutasítva (H-02, S1 hiba) |
| **Kapcsolódó kockázat** | **R11 — „A feltételes hozzáférési szabály kizárja a felhasználókat"** (közepes besorolás, **bekövetkezett**) |
| Ok | A CA-05 országkorlátozás kizárta őket: a mobilszolgáltatói CGNAT-kimenő IP külföldi tartományba sorolt. A jelentés-mód irodai hálózaton futott, így ez nem derült ki. |
| Hatás | 3 tesztelő nem tud belépni; az UAT első napja csúszik |
| Kezelés | A CA-05 szabály átállítva: országkorlátozás helyett megbízható eszköz + MFA |
| Felelős | Szabó Márk |
| Lezárva | 2026.05.12. (a bejelentés utáni napon) |
| Eszkalálva | Nagy Péterhez, 2026.05.11. 10:40 |

> **A kockázatnyilvántartás itt igazolta magát.** Az R11 kockázat azonosítva
> volt, a válaszlépés (5 napos jelentés-mód) meg is történt — mégis
> bekövetkezett, mert a jelentés-mód rossz hálózatban futott. **Ez nem a
> kockázatkezelés kudarca, hanem a tanulság forrása**, és a Tanulságok
> naplójába átvezetve.

### P-06 — Az Autopilot beüzemelés 2,1 óra a célzott 1,5 helyett

| | |
|---|---|
| Felmerült | 2026.05.06. |
| Bejelentette | Szabó Márk |
| Leírás | Az AK-06 átvételi kritérium (≤1,5 óra) nem teljesül (H-05, S2 hiba) |
| Hatás | Minőség: átvételi kritérium veszélyben; a C-cél (gyors beüzemelés) is |
| Kezelés | Az összes alkalmazáscsomag kötelező, telepítés-blokkoló módban volt. Az ügyviteli rendszer kliense (14 főnek szükséges) opcionálisra állítva (05.19.). Újramérés 5 gépen (05.20–21.): **1 óra 22 perc**. |
| Felelős | Cloudia Solutions |
| Lezárva | 2026.05.21. |

### P-07 — A SharePoint keresés lassú

| | |
|---|---|
| Felmerült | 2026.05.14. |
| Bejelentette | 4 tesztelő |
| Leírás | Nagy könyvtárakban a keresés 12–18 mp (H-03, S2 hiba) |
| Hatás | Használhatóság; nem blokkoló |
| Kezelés | A keresési index újraépítése a csapatoldalak feltöltése után |
| Felelős | Cloudia Solutions |
| Lezárva | 2026.05.27. |

### P-08 — 12 dokkoló tápkábel hiányzik

| | |
|---|---|
| Felmerült | **2026.05.28.** (2. részszállítás átvétele) |
| Bejelentette | Szabó Márk |
| Leírás | A 40 dokkolóból 12 doboza nem tartalmazta a tápkábelt (H-04, S2 hiba) |
| Hatás | 12 munkatárs dokkolója nem használható; a 3. élesítési hullám (06.10.) veszélyben |
| Kezelés | Az átvétel **fenntartással**, tételes hiánylistával. A szállító a helyszínen elismerte, pótlást vállalt 06.03-ig. A 80%-os fizetési részlet a pótlásig visszatartva. |
| Felelős | Molnár Katalin |
| Lezárva | 2026.06.02. (a pótlás megérkezett, 1 nappal a vállalt határidő előtt) |

### P-09 — Az első OneDrive szinkronizálás 40+ percig tart

| | |
|---|---|
| Felmerült | 2026.05.15. |
| Bejelentette | 4 tesztelő (szabad tesztelés) |
| Leírás | Az első bejelentkezésnél a szinkronizálás miatt a gép hosszan használhatatlan (H-07, S3 hiba) |
| Kezelés | **Előszinkronizálás a kiosztás előtt**, a raktárban, céges hálózaton. A 2. és 3. hullámnál már így ment. |
| Felelős | Szabó Márk |
| Lezárva | 2026.05.26. |

### P-10 — Hiányzik egy közös csapatoldal

| | |
|---|---|
| Felmerült | 2026.05.15. |
| Bejelentette | 4 tesztelő (szabad tesztelés) |
| Leírás | Nincs hely a csapatok közötti, megosztott anyagoknak (H-10, S3 hiba) |
| Kezelés | `CP-Kozos` csapatoldal létrehozva, mind az 50 fő hozzáféréssel |
| Felelős | Nagy Péter |
| Lezárva | 2026.05.20. |

## 2. Nyitott problémák

### P-11 — Videóhívás megszakadása mobilneten (2 fő)

| | |
|---|---|
| Felmerült | 2026.05.19. |
| Leírás | 2 tesztelőnél a 30 perces videóhívás megszakad (H-06, S2 hiba; AK-19 nem teljesült) |
| Ok | A lakóhelyükön gyenge a mobilszolgáltatói lefedettség — **nem a megoldás hibája** |
| Hatás | 2 fő korlátozottan tud otthonról videóhívást tartani |
| Kezelés | 1) Egyeztetés a mobilszolgáltatóval. 2) Ha nem javul: fix internet-hozzájárulás a tartalékból (becsült 240 000 Ft) |
| Felelős | Nagy Péter |
| Határidő | 2026.07.31. |
| Státusz | **nyitva**, az UAT-elfogadásban rögzítve és elfogadva |

### P-12 — Az alkalmazásportál magyar felirata hiányos

| | |
|---|---|
| Felmerült | 2026.05.22. |
| Leírás | A céges alkalmazásportál felületén angol feliratok maradtak (H-08, S3) |
| Kezelés | A szállító a következő szolgáltatásfrissítéssel javítja |
| Felelős | Cloudia Solutions |
| Határidő | 2026.09.30. |
| Státusz | **nyitva**, átadva az üzemeltetésnek |

### P-13 — Az Authenticator értesítés késése

| | |
|---|---|
| Felmerült | 2026.06.04. |
| Leírás | Az MFA-értesítés néha 30+ mp késéssel érkezik (H-09, S3) |
| Ok | Szolgáltatói oldali jelenség, nem konfigurációs hiba |
| Kezelés | Figyelés a hypercare alatt; ha rendszeressé válik, szolgáltatói bejelentés |
| Felelős | Szabó Márk |
| Státusz | **nyitva**, figyelés alatt |

---

## 3. Összesítés

| Kategória | Darab |
|---|---:|
| Összes problémabejegyzés | 13 |
| Lezárva | 10 |
| Nyitva, elfogadott kezeléssel | 3 |
| Ebből korábban azonosított kockázatból lett | **2** (P-02 ← R14, P-05 ← R11) |
| Az élesítés első napján felmerült | 2 (P-04, P-05) |
| A szabad tesztelésből származó | 2 (P-09, P-10) |
| Eszkalált | 1 (P-05) |

## 4. Amit a problémanaplóból megtanultunk

| Megfigyelés | Következmény |
|---|---|
| **A 13 problémából 2 korábban azonosított kockázatból lett.** A kockázatnyilvántartás tehát működött — de a válaszlépés nem mindig elég (P-05). | A válaszlépéseket ugyanolyan gondosan kell megtervezni, mint a kockázat azonosítását |
| **Az élesítés első napján 2 kritikus hiba jött elő**, mindkettő olyan, amit irodai teszteléssel nem lehetett megtalálni | A tesztelést a valós használati környezetben kell végezni |
| **A szabad tesztelés 2 problémát talált**, amit egyik teszteset sem fedett le | A strukturált teszt mellett kell szabad használat is |
| A P-01 a **munkacsomag-visszaigazolásból** derült ki, munkakezdés előtt | A visszaigazolás nem formalitás |

---

> **Kapcsolódó dokumentumok:** bemenete a *Kockázatnyilvántartás*, a
> *Munkacsomag-kiadás*, a *Teljesítésigazolás* és a *Tesztjegyzőkönyv*;
> kimenete a *Státuszriport*, az *Eszkalációs napló* és a
> *Tanulságok naplója*.
