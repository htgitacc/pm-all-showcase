# Költségvetés és költségbázis (Budget / Cost Baseline)

**Dokumentum azonosítója:** XYO-CP-107\
**Projekt:** Xyo Cloud Pilot\
**Készítette:** Tóth Gergő, projektmenedzser\
**Ellenőrizte:** Balogh Tamás, pénzügyi kontroller\
**Jóváhagyta:** Kovács Anita, szponzor — 2026.03.13.\
**Verzió:** 1.0 — **költségbázis, befagyasztva**\
**Költséghely:** IT-2026-CP (a kontrolling által nyitva)

---

## 1. Költségtételek a WBS szerint

| WBS | Tétel | Menny. | Egységár | Összesen | Típus |
|---|---|---:|---:|---:|---|
| 2.3.1 | Laptop (i5 / 16 GB / 512 GB, üzleti) | 50 | 420 000 Ft | 21 000 000 Ft | CAPEX |
| 2.3.2 | Dokkoló és tápegység | 50 | 45 000 Ft | 2 250 000 Ft | CAPEX |
| 2.3.2 | Monitor otthoni munkavégzéshez (24" FHD) | 50 | 65 000 Ft | 3 250 000 Ft | CAPEX |
| 2.3.2 | Headset | 50 | 25 000 Ft | 1 250 000 Ft | CAPEX |
| 3.1–3.4 | M365 Business Premium (12 hónap) | 50 | 105 600 Ft | 5 280 000 Ft | OPEX |
| 3.4 | Azure infrastruktúra és VPN Gateway (12 hónap) | 1 | 3 000 000 Ft | 3 000 000 Ft | OPEX |
| 7.x | Mobilinternet-hozzájárulás (12 hónap) | 50 | 48 000 Ft | 2 400 000 Ft | OPEX |
| 3.x, 5.1 | Bevezetési szolgáltatás (CSP partner) | 1 | 6 500 000 Ft | 6 500 000 Ft | CAPEX |
| 5.2 | Oktatás és változáskezelés | 1 | 1 200 000 Ft | 1 200 000 Ft | OPEX |
| | **Részösszeg** | | | **46 130 000 Ft** | |
| | Tartalékkeret (10%) | | | 4 613 000 Ft | |
| | **Mindösszesen** | | | **50 743 000 Ft** | |

**Jóváhagyott keret:** 52 000 000 Ft — **mozgástér: 1 257 000 Ft.**

## 2. Egyszeri és folyó bontás

| | Összeg | Megjegyzés |
|---|---:|---|
| **Egyszeri (CAPEX)** | 34 250 000 Ft | Hardver + bevezetési szolgáltatás |
| **Folyó (OPEX), 12 hónap** | 11 880 000 Ft | Licenc + Azure + mobilnet + oktatás |
| Tartalék | 4 613 000 Ft | |
| **Összesen** | **50 743 000 Ft** | |

> ⚠️ **A 2. évtől jelentkező folyó költség: 10 680 000 Ft / év**
> (M365 5 280 000 + Azure/VPN 3 000 000 + mobilnet 2 400 000; az oktatás
> egyszeri). Ennek **nevesített gazdát kell találni az IT üzemeltetési keretben
> a projektzárásig** — ez a zárás feltétele. Felelős: Balogh Tamás.

## 3. Időbeli elosztás (költségbázis)

Az elosztás a lenti **fizetési ütemezésből** következik: egy tétel abban a
hónapban jelenik meg, amikor a hozzá kötött mérföldkő után a számla kifizetése
esedékes. A licenc és az Azure 12 havi díja a felhő-tétel (B2+B3) mérföldkő-
részleteiben fizetődik, a mobilnet-hozzájárulás havonta, 2026.05-től.

| Hónap | Tervezett költés | Halmozott | Mi történik |
|---|---:|---:|---|
| 2026. február | 0 Ft | 0 Ft | Tervezés, nincs kötelezettségvállalás |
| 2026. március | 0 Ft | 0 Ft | Ajánlatkérés kiadva |
| 2026. április | 4 434 000 Ft | 4 434 000 Ft | Szerződéskötés (M4) → a B2+B3 felhő-tétel 30%-a |
| 2026. május | 11 662 000 Ft | 16 096 000 Ft | B2+B3 40% (M5) + hardver 20% (részszállítás) + mobilnet |
| 2026. június | 28 034 000 Ft | 44 130 000 Ft | Hardver 80% (teljes szállítás) + B2+B3 30% (M8) + oktatás + mobilnet |
| 2026. július – 2027. április | 2 000 000 Ft | 46 130 000 Ft | Mobilnet-hozzájárulás, 10 × 200 000 Ft |
| | *tartalék, ha kell* | *50 743 000 Ft* | |

**Fizetési ütemezés a szerződésekben:**

| Beszerzési tétel | Mérföldkőhöz kötve | Arány | Tervezett összeg |
|---|---|---:|---:|
| B2+B3 — licenc, Azure és bevezetés (CSP partner) | M4 szerződéskötés | 30% | 4 434 000 Ft |
| B2+B3 — licenc, Azure és bevezetés (CSP partner) | M5 környezet kész | 40% | 5 912 000 Ft |
| B2+B3 — licenc, Azure és bevezetés (CSP partner) | M8 UAT elfogadva | 30% | 4 434 000 Ft |
| B1 — hardver (hardver-viszonteladó) | Részszállítás (10 gép) átvéve | 20% | 5 550 000 Ft |
| B1 — hardver (hardver-viszonteladó) | Teljes szállítás átvéve | 80% | 22 200 000 Ft |
| B4 — oktatás | Oktatások megtartva | 100% | 1 200 000 Ft |

> **Miért beszerzési tételt írunk, nem szállítónevet?** A költségbázis
> 03.13-án fagyott be, az eredményhirdetés 04.16-án volt. A baseline nem
> nevezheti meg előre a nyertest — ha mégis, az a beszerzés tisztaságát
> kérdőjelezi meg.

> **Miért mérföldkőhöz kötött a fizetés?** Mert így a szállítónak érdeke a
> határidő. Előre kifizetett díjnál elveszted az egyetlen valódi eszközödet.

## 4. Tartalékkeret és felhasználási szabálya

| | |
|---|---:|
| Tartalékkeret | 4 613 000 Ft |
| **Ebből lekötve 2026.03.13-ig** | **182 000 Ft** |
| Szabadon felhasználható | 4 431 000 Ft |

**Felhasználási szabály (a Charter 6. pontja szerint):**

| Összeg | Ki dönt |
|---|---|
| ≤ 1 000 000 Ft / eset | Tóth Gergő, projektmenedzser — utólagos tájékoztatással |
| > 1 000 000 Ft / eset | Kovács Anita, szponzor — előzetes jóváhagyással |
| A teljes tartalék kimerülése esetén | Projekt Irányító Bizottság |

**Már lekötött tétel:**

| Dátum | Tétel | Összeg | Döntés |
|---|---|---:|---|
| 2026.03.03. | 14 db HDMI–VGA adapter (A7 feltevés megdőlt) | 182 000 Ft | Tóth Gergő, PM-hatáskörben (D-07) |

## 5. Amit a költségvetésen kívül tartunk

| Tétel | Miért nincs a projektköltségben |
|---|---|
| Belső munkaidő (948 óra) | A kontrolling nem terheli projektre; a szervezet saját kapacitása |
| A régi fájlszerver további üzemeltetése | Nem a pilot költsége — a nem érintett 190 fő használja |
| Otthoni irodabútor (K10) | Hatókörön kívül, HR-hatáskör |
| Céges mobiltelefon (K9) | Hatókörön kívül, a meglévő dolgozói csomagra épülünk |

## 6. Költségkövetés rendje

| | |
|---|---|
| **Formátum** | A kontrolling havi projektköltés-sablonja (IT-2026-CP költséghely) |
| **Ki szolgáltat adatot** | Balogh Tamás, minden hónap 3. munkanapjáig |
| **Hol jelenik meg** | Havi státuszriport és Steering riport |
| **Előrejelzés** | Havonta újraszámolt várható végösszeg (nem csak az aktuális állás) |
| **Jelzési küszöb** | Ha az előrejelzés meghaladja az 51 000 000 Ft-ot, azonnali szponzori jelzés |

> **Ne csak azt nézd, mennyit költöttél — azt is, mennyi lesz a vége.**
> A pénz elfogyását előre kell jelenteni. Utólag már nincs mit dönteni.

## 7. Érzékenység

| Forgatókönyv | Hatás | Belefér a keretbe? |
|---|---:|---|
| Alapeset | 50 743 000 Ft | ✔ igen |
| Hardver 10%-kal drágább | +2 775 000 Ft | ✔ igen, a tartalékból |
| Hardver 20%-kal drágább | +5 550 000 Ft | ⚠ **csak papíron** — lásd lent |
| Árfolyamhatás a licencen (+8%) | +422 000 Ft | ✔ igen |

**Miért csak papíron fér bele a +20%?** A várható költés 46 130 000 +
5 550 000 + a már lekötött 182 000 = **51 862 000 Ft** lenne. Ez az 52 000 000
Ft-os kereten belül van, de **a teljes tartalékot felemészti**: 138 000 Ft
maradna minden más kockázatra. Tartalék nélkül folytatni nem felelős döntés.

**Ha a hardver 20%-kal drágább:** a Steering elé viendő döntési javaslat a
headset elhagyása (−1 250 000 Ft) és az otthoni monitor 40 főre csökkentése
(−650 000 Ft), vagy a pilot 45 főre szűkítése.

---

| Szerep | Név | Dátum |
|---|---|---|
| Készítette | Tóth Gergő, projektmenedzser | 2026.03.06. |
| Ellenőrizte | Balogh Tamás, pénzügyi kontroller | 2026.03.10. |
| Jóváhagyta | Kovács Anita, szponzor | 2026.03.13. |

> **Kapcsolódó dokumentumok:** bemenete a *WBS*, az *Ütemterv* és a
> *Költség-haszon elemzés*; kimenete a *Beszerzési terv*, a *Státuszriport*,
> az *Ütem- és költségeltérés elemzés* és a *Pénzügyi zárás*.
