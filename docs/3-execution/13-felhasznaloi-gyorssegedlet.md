# Felhasználói gyorssegédlet — Xyo Cloud Pilot

**Dokumentum azonosítója:** XYO-CP-213\
**Kinek szól:** a pilotban részt vevő 50 munkatársnak\
**Készítette:** Cloudia Solutions Kft., lektorálta Kiss Réka (Service Desk)\
**Verzió:** 1.2 (2026. június 5.)

> **Ez az egyetlen dokumentum a projektben, amit nem projektnyelven írunk.**
> Magyarul, szakzsargon nélkül, képernyőképekkel. Mindenki megkapja
> **kinyomtatva is**, a géppel együtt — a SharePointon eldugott PDF-et senki
> nem találja meg.

---

## 1. Az első bejelentkezés

**Amire szükséged lesz:** a laptop, a céges e-mail-címed, és a telefonod.

1. Kapcsold be a gépet, és csatlakozz a wifire vagy a mobilnetre.
2. Írd be a **céges e-mail-címedet** (pl. `kovacs.janos@xyo.hu`).
3. Add meg a jelszavadat.
4. A gép kb. **másfél órán át magától beállítja magát.** Ez alatt nem kell
   csinálnod semmit — nyugodtan hagyd bekapcsolva.

> **Az MFA-t (a telefonos megerősítést) az oktatáson beállítjuk közösen.**
> Ha valamiért lemaradtál róla, hívd a Service Desket, ne próbáld egyedül.

## 2. Belépés minden nap

Amikor bejelentkezel, a telefonodra érkezik egy értesítés. **Koppints rá, és
hagyd jóvá** — ezután belépsz.

| Ha ez történik | Ezt tedd |
|---|---|
| Nem jön az értesítés | Nyisd meg magad az Authenticator alkalmazást a telefonon |
| 30 másodpercnél tovább vársz | Türelem, néha lassabb. Ha 1 percnél tovább tart, próbáld újra a belépést |
| Elfelejtetted a jelszavad | Kattints a **„Elfelejtettem a jelszavam"** linkre — magadtól vissza tudod állítani |

## 3. Hova mentsem a fájljaimat?

Ez volt a leggyakoribb kérdés az oktatásokon. Íme a szabály:

```
                    Ezt a fájlt rajtam kívül
                    más is használja?
                              |
              ┌───────────────┴───────────────┐
             NEM                             IGEN
              │                                │
         ONEDRIVE                    Csak a saját csapatom?
    (a te személyes                          │
     munkamappád)              ┌─────────────┴─────────────┐
                              IGEN                        NEM
                               │                           │
                    A CSAPATOD SHAREPOINT              CP-KOZOS
                        OLDALA                    (közös csapatoldal)
```

| Hely | Mire való | Ki látja |
|---|---|---|
| **OneDrive** | A saját munkamappád: piszkozatok, jegyzetek, amin még dolgozol | csak te (amíg meg nem osztod) |
| **A csapatod SharePoint oldala** | Amin a csapatod közösen dolgozik | a csapatod tagjai |
| **CP-Kozos** | Csapatok közötti anyagok, közös sablonok | mind az 50 pilot résztvevő |

> ⚠️ **Ne mentsd az asztalra vagy a `C:` meghajtóra!** Az nem szinkronizálódik,
> és ha a géppel történik valami, elveszik. Az OneDrive és a SharePoint
> automatikusan menti a munkádat.

## 4. Otthoni munkavégzés

### 4.1 A dokkoló csatlakoztatása

1. Dugd be a dokkoló **tápkábelét** a konnektorba.
2. Csatlakoztasd a **monitort** a dokkolóhoz (HDMI vagy DisplayPort kábellel).
3. Dugd be a dokkoló **USB-C kábelét** a laptopba.

A laptop innentől töltődik is, és a monitor is működik.

> Ha adaptert kaptál a monitorodhoz, azt a monitor és a kábel közé kell tenni.

### 4.2 A VPN

A VPN akkor kell, ha a **bérszámfejtő** vagy az **ügyviteli rendszert** akarod
használni otthonról. Minden más (e-mail, OneDrive, SharePoint, Teams) VPN
nélkül is működik.

**A VPN magától elindul, amikor bejelentkezel.** Ha mégsem:

1. Kattints a tálcán a hálózat ikonra.
2. Válaszd a **„Xyo VPN"** kapcsolatot, és kattints a Csatlakozás gombra.
3. Hagyd jóvá a telefonodon.

## 5. Ha valami nem működik

| Probléma | Mit tegyél először |
|---|---|
| Nem tudsz belépni | Ellenőrizd, hogy a telefonod online van-e. Ha nem megy, hívd a Service Desket. |
| Elfelejtetted a jelszavad | „Elfelejtettem a jelszavam" link a belépő képernyőn |
| Nem találsz egy fájlt | Nézd meg a OneDrive lomtárában — **30 napig** visszaállítható |
| Lassú a gép az első napon | Az első szinkronizálás időigényes. Hagyd bekapcsolva 1 órát. |
| A monitor nem működik | Ellenőrizd, hogy a dokkoló tápkábele be van-e dugva |
| Elveszett vagy ellopták a gépet | **Azonnal** hívd a Service Desket — távolról letiltjuk |

### A Service Desk elérése

| | |
|---|---|
| Telefon | belső 4200 |
| E-mail | `servicedesk@xyo.hu` |
| Nyitvatartás | munkanapokon 7:30 – 17:00 |
| **A bevezetés utáni 3 hétben** | **kiemelt támogatás, 2 órás válaszidővel** |

> Ha a projekthez kapcsolódó a kérdésed, írd az e-mail tárgyába, hogy **„CP"** —
> így előre kerül a sorban.

## 6. Amit jó tudni

**Mit lát a cég a gépeden, és mit nem?**

| Látja | **Nem látja** |
|---|---|
| A gép típusát, az operációs rendszer verzióját | A böngészési előzményeidet |
| Hogy be van-e kapcsolva a titkosítás és a vírusvédelem | Hogy mit gépelsz |
| Hogy telepítve vannak-e a biztonsági frissítések | A képernyődet |
| Hogy melyik céges alkalmazások vannak fent | Hol vagy (nincs helymeghatározás) |

> Az eszközfelügyelet célja a **gép védelme**, nem a munkád figyelése. Ezt az
> üzemi tanács külön kikötötte, és az adatvédelmi tisztviselő tételesen
> ellenőrizte a beállításokat.

**A fájljaid hol vannak?** Az Európai Unión belüli adatközpontokban — ez
szerződéses kikötés.

**Mi történik a pilot után?** A projekt 2026. június végén zárul, de utána
3 hónapig mérjük, hogyan működik a megoldás. Kapni fogsz egy rövid kérdőívet —
kérünk, töltsd ki őszintén, mert ez alapján dől el, hogy a cég többi részlege
is megkapja-e.

---

## Változásnapló

| Verzió | Dátum | Változás |
|---|---|---|
| 1.0 | 2026.05.15. | Első kiadás |
| 1.1 | 2026.05.26. | **„Hova mentsem?" döntési ábra hozzáadva** — az UAT szabad tesztelésén 6 tesztelőből ez volt a leggyakoribb kérdés |
| 1.2 | 2026.06.05. | A 3. képernyőkép frissítve (H-12); a dokkoló-csatlakoztatás képe bekerült |

---

> **Kapcsolódó dokumentumok:** bemenete az *Oktatási anyag* és a
> *Konfigurációs (as-built) dokumentáció*; kimenete az
> *Üzemeltetésbe adás (Run-book)*.
