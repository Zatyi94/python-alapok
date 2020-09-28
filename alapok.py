# meghívjuk a print függvényt és átadjuk neki 
# a 'hello world' 
# a kettőskereszttel kezdődő sorokat a python nem értelmezi
# a kettőskereszttel kezdődő sorok a comment-ek

print ('hello world')

# létrehoztunk egy szöveg nevű változót, az értéke pedig a
# 'sziasztok!' karakterlánc
# ha egy darab egyenlőségjelet látunk a kódban, az minden esetben
# értékadást jelent. Az egyenlőségjel jobb oldala bekerül az
# egyenlőségjel bal oldalán lévő változóba.
szoveg = 'sziasztok!'
print(szoveg)
# szekvencia: a program az utasításokat (sorokat) soronként
# és egynás után hajtja végre
# ez a következő sor hibát dobna, mert nem hoztuk még létre a szoveg2 változót
# print(szoveg2)
szoveg2 = "alma"
# meghívjuk a format fgv-t az aposztrofok közötti szövegre
print('a szoveg2 értéke: {}' .format(szoveg2))
# megnézzük a szoveg2 változó típusát
# meghívjuk a type függvényt a print parancsba, ami megmutatja a szoveg2 változó típusát
# ebben az esetben kiírja, hogy 'str' (azaz string)
print(type(szoveg2))

# ha valahol látunk egy sima zárójelet és előtte valami szöveget
# pl.: sdfsdfsdf()
# ez egy függvényhívást jelent, a függvény neve a
# nyitó zárójel előtti rész

# ha beírok egy szöveget '' közé, majd utána ütök egy .-ot, feldob egy lenyíló menüt
# nekem itt épp konfigurációs probléma miatt nem hozta be, ezért hf: utána nézni otthon
# python autocomplete function with help window - erre ráguglizni 
# autocomplete = intellisence = code complete (show it in VScode)
# 'ez itt egy szoveg'.upper
# upper függvény minden karaktert átalakít nagy betűre
# lower: kis betűre

print('a szoveg erteke: {} a szoveg2 erteke {}'.format(szoveg, szoveg2))
# mindig belülről kifelé kell gondolkodni: belső függvény csinál vmt, és bekerül a másikba
# majd azok is bekerülnek a legkülsőbe
# ezek lefutnak és ebből lesz egy nagy eredményem

# létrehozzuk a szam nevű változót, és az érték, amit kap ez a változó
# az egy szám lesz (nincs körülötte aposztrof, vagy idézőjel - innen tudni, h szám)
# szám típusa az 'int'
# ha ''-t rakok köré, automatikusnak szövegnek értelmezi
# ha szövegesen írom be hogy három, aposztrof nélkül -> változónak hiszi
# és hibát dob, hogy undifined
# dinamically typed programming language: a változók típusát
# létrehozáskor (deklaráláskor) automatikusan megpróbálja kitalálni a futtató környezet
# (jelen esetben a python, de a JavaScript és a php is így működik)
# python dinamikus programozási nyelv (megrpóbálja kitalálni)
# string, int stb -> ezt be kell írni pl. C-ben, Csharpban - mert ezek statikus nyelvek
szam = 34
print(type(szam))
szam1 = 10
print(szam+szam1)
# szám típusú változókkal lehet matematikai műveleteket végezni (pl. +, -, *, /)

# ezzel növeljük 1-gyel a szám voltozó értékét
# ezt követően a szam változó értéke felülíródik (eddig 34 volt, most már 35)
szam = szam + 1
# az előző sor rövidebben (vagyis ugyanazt jelenti):
szam += 1
print(szam)

# string = szöveg
# int (integer) = szám

# boolean típusú változónak két értéke lehet: True vagy False
# ezeket a pythonban mindig nagy betűvel kell írni, míg pl. JavaScriptben kicsivel
# True-t nem adhatom változó névnek, lefoglalt szó a pythonban, nem használhatom másra
# a True a boolean változó 1-es értéke
# kisbetűvel, pl. false létre tudnám hozni, de összezavarja azt, aki olvassa
kapcsolo = True
print(type(kapcsolo))

# az elágazás egy olyan kód blokk, ami egy adott feltétel alapján
# vagy lefut vagy nem...
# ezt az dönti el, hogy mi a feltételem
# if alatt lévő sor mindig egy tabbal beljebb van, csak akkor fut le

if kapcsolo is True:
    print('A kapcsoló fel van kapcsolva')
# pythonban úgy mondod meg, meddig van egy parancs, amíg beljebb van egy kód
print ('ez már az if blokkon kívül, így ez mindenképp lefut...')

a = 3
b = 4

if a > b:
    print('az a nagyobb, mint b')
else:
    print('a nem nagyobb, mint b')
# relációt szám típusú változóknál lehet értelemszerűen megcsinálni
# python valszeg errort dobna, ha szövegnél tennénk próbát

# ciklus: egy adott kódrész többször fut le
# egy adott feltétel szerint
# addig futtatja le a while, amg igaz a feltétel, aztán megáll

szam = 10
while szam > 0:
    print('a szám változóból levonunk 1-et: {}'.format(szam))
    # szam = szam -1
    szam -= 1
    # ha nem csökkentenénk és a szam 10 maradna, az egy végtelen ciklus lenne
    # vételen ciklus nem mindig hiba, lehet rá szükség

# a kapcsos zárójel a pythonban a lista típusú változót jelenti
# a kapcsos zárójelen belülre írjuk a lista elemeit
# a listába több elemet is el lehet tárolni
# itt most 3db string van, de lehetne bele tenni pl. számot, booleant, másik listát stb
nevsor = ['Pista', 'Kata', 'Tibor']

# "it's a great day", double quotes-ot érdemes használni ha pl. angolul írok, és
# aposztrof s van a szövegben
# amúgy érdemes inkább a single-t
# de mindegy, csak azzal is kell lezárni, amivel megnyitottuk

# a for ciklust legtöbbször arra hasznháljuk, hogy
# végig menjünk egy lista összes elemén, és az elemeken vmilyen művelettel végezzünk
for nev in nevsor:
    print('a névsorban szerepel: {} '.format(nev))

for index, nev in enumerate(nevsor):
    print('{} : {} '.format(index, nev))

# nev lehetne n is, vagy az index i, csak akkor a zárójelen belül is úgy kell rájuk hivatkozni

print('a nevsor nulladik eleme: {} '.format(nevsor[0]))