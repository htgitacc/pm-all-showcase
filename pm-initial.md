# Projektmenedzser tervező mindenes

A cél egy olyan felület, ami a hagyományos waterfall projektek 5 fázisán végigvezeti a projektmenedzsert és hasonlóan egy chekclist-hez minden fázis minden részletén végigmegy.

Ez legyen az első ötlet, tervdokumentum, amire létrejön a projekt. Ezt készítsd el a megfelelő néven és helyezd majd a listában a megfelelő helyre.

Mintacég a Xyo Kft., példaként használandó mintaprojekt.

A cég egy közepes magyarországi vállalat IT részlege, ahol Cloud first megoldásokat kezdenek bevezetni. Nincs migráció, mindent új beszerzéssel. A cél, hogy legyen egy virtuális infrastruktúra, mintegy pilot projekt, ahol elkezdik élesben tesztelni a csak virtuális kiszolgálókkal való működést. A környezet a magyar viszonyokhoz igazodjon, ezért gondolom a Microsoft termékei jöhetnek szóba, de ha Googel-t vagy Amazon-t használsz a példában az is jó, ha van realitása a magyar vállalatoknál. A cél, hogy kb. 50 fő a felhőben dolgozzon. Ehhez az asztali gépparkot laptopokra cserélik, mert a felhő több rugalmasságot ad és a home office lehetőséget mindenkinek megadják, aki a projektben részt vesz. A laptophoz mindenkinek kell egy plusz monitor otthonra, a cégnél ez már megvan és a cég állja az internetet, ez jelenleg mobilneten történne. A cégnek minden mobilszolgáltatóval van szerződése, a dolgozói csomag korlátlan netet tartalmaz. Minden dolgozónak szükséges egy VPN megoldás, ha van a cégnek ezt nem kell beszerezni, ha nincs, akkor ez is plusz költség vagy a Microsoft előfizetésen (Amazon, Google) belül van rá lehetőség. A projektben az EntraID segítségével fognak belépni a gépbe, a korábbi fájlszervert a sharepoint és ondedrive megoldások váltják ki. Röviden ennyi a projekt nem kell túl részletezni, még talán ennyire se. Sima informatikai beszerzés és bevezetés előre tervezhető lépcsőkkel, határidőkkel, költségkerettel. Ez lesz a példa, amiből végig építkezel.

1. Initiation
2. Planning
3. Execution
4. Monitoring and Controlling
5. Closure

+1 Mérések, visszatekintés, a projekt sikeres bevezetése után egy 3 hónapos időszakot is iktassunk be és nézzük meg, hogy milyen mérőszámok alapján igazolható, hogy a projekt tényleg sikeres és fokozatosan bevezethető a cég többi részlegén. Mit, hogy, ki mér?

## Minden fázisra érvényes általános szabályok

Ezeket minden fázisban viszgáld meg és ha releváns, akkor dolgozd ki részletesen.
Ha nem releváns, akkor ne találj ki semmit, akkor egyszerűen hagyd ki.

1. A PM-nek mi a feladata a fázison belül?
2. Milyen meetingeket kell megszerveznie és kiket kell meghívni?
3. Kitől és milyen adatokat, dokumentumokat kell bekérni és kinek és milyen adatot kell szolgáltani. Kinek és mit nem szabad kiadni?
4. Az adott fázisban miért és milyen felelősséggel kell vállalnia?
5. A dokumentumok kapcsolatát végig jelezd.
6. A legfontosabb, hogy milyen dokumentumokat kell elkészíteni az adott fázison belül
    6.1. Mik a jellemzően mindig elkészítendő dokumentumok és mik azok, amik a gyakorlatban nem mindig készülnek el, de számonkérhető a PM-en vagy saját magát védi, ha elkészíti.
    6.2. Melyik dokumentumnak mi a bemenete, milyen dokumentumokból kell összerakni (ha van)
    6.3. Minden dokumentumra készíts egy mintát, amiben a példa projekt adatait használod. Ezek a minták kimásolhatók legyen md formátumban, ha teljes dokumentumról van szó, akkor pedig fájl szinten is készüljenek el, md formátumban.
7. A +1 fázis a mérésekről szól. A projekt indulásakor legyen megfogalmazva, hogy mit várunk a digitális projekttől és a végén ezt tudjuk a mérésekkel igazolni vagy cáfolni. Több ötletet is vázolj föl, amit előre vetítünk és módszereket, amivel a projekt alatt, de leginkább utána, mérni tudunk.

## Kialakítás

Az egész legyen olyan, mint egy bevásárlólista, csak sokkal szakmaibb és bővebb. Mindenre hozz példát, akár csak pár sorban, akár teljes dokumentumot. A példák lehetnek lenyíló ablakban, aki akarja lenyitja és átolvassa, de mellette jól látszódjon az adott fázis sorrendje, a fontos és kötelező lépések kiemelve, alatta altéma, magyarázat, példa stb.

A formátuma minél egyszerűbb legyen, sima md fájlok esetleg astro, de fájl szinten nem szeretnék külön böngészve szerkeszteni. Mindent a felületen érjek el, szerkeszthessek és letölthessek. Lehet python és streamlit is.

Ez a projekt itt ér véget, idág kell eljutni, egy hordozható PM feladatmenedzser.

# Távlati célok

Ezek nem részei a mostani projektnek nem kell megtervezni. Azt jelezheted, hogy a most kialakítandó megoldás alkalmas lesz-e további bővítésre.

A távolabbi cél, hogy a minta dokumentum helyére, ha éles ötletet teszek, akkor AI segítségével generáljon javaslatokat. A feladatokhoz legyen lehetőség határidőt és felelőst tenni. Legyen benne ellenőrző mechanizmus, ha X bemenetet várok és hiányzik, akkor jelezze a PM felé, hogy mit kell pótolni az adott eredményhez.