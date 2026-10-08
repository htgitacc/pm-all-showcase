# Konfigurációs (as-built) dokumentáció

**Dokumentum azonosítója:** XYO-CP-206\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Cloudia Solutions Kft. és Szabó Márk, rendszergazda\
**Ellenőrizte:** Nagy Péter, IT osztályvezető\
**Utolsó frissítés:** 2026. június 19.\
**Verzió:** 1.4

> **Ez azt írja le, hogyan lett ténylegesen kialakítva a környezet** — nem
> hogyan terveztük. Az üzemeltetésbe adás alapja; enélkül minden hibánál a
> projektcsapatot hívják vissza.
>
> **Folyamatosan íródott, nem a végén.** Az utolsó héten már senki nem
> emlékezne, miért állítottak be valamit úgy, ahogy — és pont az az indoklás
> lesz később fontos.

---

## 1. Bérlő (tenant) alapadatok

| | |
|---|---|
| Bérlő neve | xyokft.onmicrosoft.com |
| Egyedi tartomány | xyo.hu (ellenőrizve 2026.04.22.) |
| Régió | Európai Unió — **EU Data Boundary bekapcsolva** |
| Licenc | Microsoft 365 Business Premium × 50 |
| Licenc érvényesség | 2026.05.01 – 2027.04.30. |
| Globális adminisztrátorok | Szabó Márk + 2 break-glass fiók |

> **Az EU Data Boundary beállítást a bérlő szintjén kapcsoltuk be**, nem
> szolgáltatásonként. Ez az L6 korlát és a DPIA feltétele.

## 2. Entra ID

### 2.1 Felhasználók és csoportok

| Csoport | Tagok | Célja |
|---|---:|---|
| `CP-Pilot-Users` | 50 | A pilot teljes köre; ehhez kötődik minden szabály |
| `CP-Pilot-Wave1` | 10 | Első élesítési hullám, egyben az UAT tesztcsoport |
| `CP-Pilot-Wave2` | 20 | Második hullám |
| `CP-Pilot-Wave3` | 20 | Harmadik hullám |
| `CP-Legacy-FileRead` | 14 | A 3 csapat, amely olvasási hozzáférést kap a régi fájlszerverhez (K17) |
| `CP-ServiceDesk` | 3 | Service Desk munkatársak, felhasználó-adminisztrátori joggal |
| `CP-BreakGlass` | 2 | Vészhozzáférési fiókok, MFA-kizárással |

**Szolgáltatásfiókok:** 4 db (`svc-intune-enroll`, `svc-sp-backup`,
`svc-vpn-radius`, `svc-report`) — ezek **nem felhasználók** (lásd Projektszótár).

### 2.2 Hitelesítés

| Beállítás | Érték | Megjegyzés |
|---|---|---|
| MFA | Kötelező a `CP-Pilot-Users` csoportra | 50/50 regisztrálva |
| MFA módszer | Microsoft Authenticator; SMS csak jóváhagyott kivétellel | 2 fő kapott SMS-kivételt (nincs okostelefon) |
| Jelszóhossz | min. 12 karakter | |
| Jelszólejárat | **nincs kényszerített lejárat** | NIST/Microsoft ajánlás |
| Tiltott jelszavak listája | bekapcsolva, magyar szólistával bővítve | |
| Önkiszolgáló jelszó-visszaállítás | bekapcsolva, MFA-val | K27 követelmény |

### 2.3 Feltételes hozzáférési szabályok

| # | Szabály | Állapot | Megjegyzés |
|---|---|---|---|
| CA-01 | MFA megkövetelése minden felhőalkalmazáshoz | **éles** | |
| CA-02 | Belépés csak megfelelő (compliant) eszközről | **éles** | |
| CA-03 | Örökölt hitelesítési protokollok tiltása | **éles** | |
| CA-04 | Kockázatalapú újrahitelesítés | **éles** | |
| CA-05 | **Országkorlátozás — csak Magyarország** | **éles, módosított feltétellel** | lásd alább |

#### CA-05 — az élesítés alatt módosítva

| | |
|---|---|
| **Eredeti beállítás** | Belépés csak magyarországi IP-tartományból |
| **Mi történt** | Az UAT első napján (2026.05.11.) **3 tesztelő nem tudott belépni**. A mobilszolgáltatójuk CGNAT-kimenő IP-je külföldi tartományba sorolt. |
| **Hiba azonosítója** | H-02 (S1, kritikus) — a **R11 kockázat bekövetkezése** |
| **Miért nem szűrte ki a jelentés-mód?** | A jelentés-mód 05.04–05.08. között futott, **irodai hálózaton**. A mobilnetes belépés csak az élesítés napján jelent meg. |
| **Javítás** | A CA-05 szabály feltétele átállítva: országkorlátozás helyett **megbízható eszköz + MFA** kombináció; kockázatos belépésnél kiegészítő ellenőrzés (CA-04) |
| **Javítás dátuma** | 2026.05.12. |
| **Utólagos ellenőrzés** | 2026.05.13–05.22. között további kizárás nem történt |

> **Tanulság:** a jelentés-módot **abban a hálózati környezetben** kell
> lefuttatni, ahol a felhasználók ténylegesen dolgozni fognak. Irodából
> tesztelni egy otthoni munkavégzésre szánt szabályt nem elég.
> → Átvezetve a Tanulságok naplójába.

### 2.4 Break-glass fiókok

| | |
|---|---|
| Darabszám | 2 |
| Névkonvenció | `bg-admin-01@xyo.hu`, `bg-admin-02@xyo.hu` |
| Kizárva | Minden feltételes hozzáférési szabály alól |
| Jelszó tárolása | Lezárt boríték, a pénzügyi széfben; hozzáférés: Nagy Péter, Kovács Anita |
| Riasztás | Bejelentkezéskor azonnali e-mail Nagy Péternek és Szabó Márknak |
| Tesztelve | 2026.05.06. és 2026.06.18. |

## 3. Intune eszközfelügyelet

### 3.1 Eszközprofilok

| Profil | Hatóköre | Fő beállítások |
|---|---|---|
| `CP-Compliance` | CP-Pilot-Users | BitLocker kötelező, tűzfal be, Defender valós idejű védelem be, min. OS build |
| `CP-Config-Win11` | CP-Pilot-Users | Képernyőzár 10 perc, USB-tároló írás korlátozva, energiagazdálkodás |
| `CP-Update-Ring` | CP-Pilot-Users | Biztonsági frissítés max. 7 nap halasztás, funkciófrissítés 30 nap |
| `CP-Autopilot` | Az 50 regisztrált eszköz | Felhasználóvezérelt beüzemelés, automatikus csoportbesorolás |

### 3.2 Amit tudatosan NEM állítottunk be

| Beállítás | Miért nem |
|---|---|
| Böngészési előzmény gyűjtése | **L7 korlát** — üzemi tanácsi kikötés |
| Alkalmazáshasználati napló felhasználónként | **L7 korlát** |
| Képernyőkép- vagy billentyűnaplózás | **L7 korlát** |
| Helymeghatározás | Nincs rá üzleti indok |

> **dr. Fekete Zsolt (DPO) az Intune profil beállításait tételesen átnézte
> 2026.05.07-én**, és írásban igazolta, hogy nem tartalmaz magánhasználati
> adatgyűjtést (AK-10, Sz-9 szerződéses feltétel).

### 3.3 Alkalmazáscsomagok

| Alkalmazás | Telepítés módja | Megjegyzés |
|---|---|---|
| Microsoft 365 Apps | kötelező, automatikus | |
| Microsoft Edge | kötelező, automatikus | alapértelmezett böngésző |
| Azure VPN Client | kötelező, automatikus | előre konfigurált profillal |
| Céges alkalmazásportál | kötelező | opcionális szoftverek önkiszolgáló telepítéséhez |
| Ügyviteli rendszer kliens | opcionális, portálról | csak 14 főnek szükséges |

### 3.4 Autopilot beüzemelési idő — mért értékek

| Mérés | Gép | Idő |
|---|---|---|
| 1. mérés (05.06.) | tesztgép 1 | 2 óra 06 perc |
| 2. mérés (05.06.) | tesztgép 2 | 2 óra 11 perc |
| **Javítás után** (05.20.) | tesztgép 3 | 1 óra 22 perc |
| **Javítás után** (05.20.) | tesztgép 4 | 1 óra 18 perc |
| **Javítás után** (05.21.) | tesztgép 5 | 1 óra 25 perc |
| **Javítás után** (05.21.) | tesztgép 1, újra beüzemelve | 1 óra 20 perc |
| **Javítás után** (05.21.) | tesztgép 2, újra beüzemelve | 1 óra 25 perc |
| **Átlag (javítás utáni 5 mérés, 5 gépen)** | | **1 óra 22 perc** ✔ (célérték ≤1,5 óra) |

A Minőségterv 5 gépen mért átlagot ír elő (AK-06). A javítás előtti két mérés
egy másik konfigurációt mért, ezért nem számít bele — helyette az 1. és 2.
tesztgépet a javítás után újra beüzemeltük.

**Mi volt a hiba (H-05, S2):** az összes alkalmazáscsomag **kötelező,
telepítés-blokkoló** módban volt beállítva, így a beüzemelés megvárta az
ügyviteli rendszer kliensének telepítését is. **Javítás:** az ügyviteli
kliens átállítva opcionálisra, a portálról telepíthetőre.

## 4. SharePoint és OneDrive

### 4.1 Csapatoldalak

| Csapatoldal | Tagok | Tárhely-korlát |
|---|---:|---|
| `CP-Penzugy` | 12 | 100 GB |
| `CP-Ertekesites` | 18 | 150 GB |
| `CP-Logisztika` | 14 | 100 GB |
| `CP-Vezetoseg` | 6 | 50 GB |
| `CP-IT` | 4 | 50 GB |
| `CP-Kozos` | 50 | 200 GB |

### 4.2 Jogosultsági modell

| Szint | Ki | Jog |
|---|---|---|
| Oldalgazda | csapatonként 1 fő | Tagok kezelése, mappaszerkezet |
| Tag | a csapat tagjai | Olvasás, írás, megosztás a szervezeten belül |
| Látogató | — | Nem használjuk |
| Külső megosztás | nevesített külső címzett, **30 napos lejárattal** | K19 követelmény |

### 4.3 Megőrzés és visszaállítás

| Beállítás | Érték |
|---|---|
| OneDrive lomtár | 30 nap |
| Másodlagos lomtár | további 30 nap |
| SharePoint verziókövetés | 50 verzió |
| Megőrzési szabály | Munkaviszony vége + 30 nap, majd törlés |

**Visszaállítási teszt (2026.05.08.):**

| Teszt | Eredmény | Időigény |
|---|---|---|
| 1 törölt fájl visszaállítása lomtárból | ✔ sikeres | 2 perc |
| Teljes könyvtár (1 240 fájl, 4,2 GB) visszaállítása | ✔ sikeres | **42 perc** |

> A 42 perces időigényt **dokumentáltuk**, mert üzemeltetési szempontból ez a
> lényeges információ: incidens esetén ennyivel kell számolni.

## 5. Azure VPN

| | |
|---|---|
| Gateway típusa | VpnGw1, aktív-passzív |
| Régió | West Europe |
| Kliens | Azure VPN Client, előre konfigurált profillal |
| Hitelesítés | **Entra ID, MFA-val** (K22) |
| Címtartomány | 10.42.0.0/24 (VPN-kliensek) |
| **Elérhető erőforrások** | **Csak az alábbi 3 cél — nem teljes hálózati hozzáférés** |

| Cél | Cím | Ki éri el |
|---|---|---|
| Bérszámfejtő rendszer (webes) | 10.10.5.20:443 | CP-Pilot-Users |
| Ügyviteli rendszer (webes) | 10.10.5.35:443 | CP-Pilot-Users |
| Régi fájlszerver (**csak olvasás**) | 10.10.2.10 | **CP-Legacy-FileRead** (14 fő) |

> A legkisebb jogosultság elve: a VPN nem ad teljes belső hálózati
> hozzáférést, csak a három nevesített célt. A régi fájlszerverhez tartozó
> hozzáférés **olvasásra korlátozott**, és csak a 3 érintett csapat 14 tagja
> kapja meg (K17, A8 feltevés).

## 6. Naplózás és riasztás

| Mit naplózunk | Megőrzés | Miért |
|---|---|---|
| Entra ID bejelentkezések | 30 nap (licenc szerinti) | Incidenskezelés |
| VPN-kapcsolódások (időpont, forrás-IP) | 90 nap | Incidenskezelés |
| Intune megfelelőségi állapot | folyamatos | Üzemeltetés |
| Break-glass fiók használata | riasztás + napló | Biztonság |

## 7. Eltérések a tervezett konfigurációtól

| # | Amit terveztünk | Ami megvalósult | Miért |
|---|---|---|---|
| 1 | CA-05 országkorlátozás IP alapján | Megbízható eszköz + MFA kombináció | H-02: mobilszolgáltatói CGNAT külföldi IP-t adott |
| 2 | Minden alkalmazás kötelező telepítés | Az ügyviteli kliens opcionális | H-05: a beüzemelési idő 2,1 óra volt a célzott 1,5 helyett |
| 3 | 50 fő egységes SMS/Authenticator MFA | 48 fő Authenticator, 2 fő SMS | 2 munkatársnak nincs okostelefonja |
| 4 | 6 csapatoldal | 6 csapatoldal + 1 közös | A `CP-Kozos` oldal az UAT visszajelzései alapján jött létre |

> **Az eltérések dokumentálása kötelező.** Az üzemeltetésnek nem az számít, mit
> terveztünk, hanem hogy **mi van most a rendszerben, és miért**.

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Cloudia Solutions Kft. | 2026.06.18. |
| Készítette | Szabó Márk, rendszergazda | 2026.06.18. |
| Ellenőrizte és elfogadta | Nagy Péter, IT osztályvezető | 2026.06.19. |

> **Kapcsolódó dokumentumok:** bemenete a *Biztonsági alapkonfiguráció*;
> kimenete az *Üzemeltetésbe adás (Run-book)*, a *Felhasználói gyorssegédlet*
> és az *Archiválási jegyzék*.
