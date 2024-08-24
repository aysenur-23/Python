strvar = "HELLO World"
print(strvar)

strvar[2] #2. indexi yazdır

strvar[2:] #2. indexten sona kadar alır

strvar[:3] #baştan 3. değere kadar alır

strvar[2:5] #5 dahil olmadan 2den 5e kadar alır

strvar[::2] # 1 değeri atlayarak 2. değeri  alır

strvar[1:5:3]

strvar= strvar + " Ogren!" #stringleri toplar ve strvar'a atar
print(strvar)

strvar * 5  #5 kez yazdırır

strvar.upper() #harflerin hepsini büyük yazar

strvar= strvar.upper() #tüm harfleri büyük yazıp strvar'a atar
print(strvar)

print(strvar.capitalize()) #ilk karakter büyük gerisi küçük olarak döndürür

print(strvar.casefold())# tüm karakterleri küçük döndürür

strvar.lower() #tüm harfleri küçük yazar

strvar = strvar + "ogren!" 
print(strvar)

print(strvar.split()) #kelimeleri boşluklrdan ayırıp listeye atar
strvar = strvar.split("sep = "o", maxsplit =1 ") #sep nerden ayıracağı, maxspilt en fazla kaç kere ayıracağını belirtir

print(strvar.split('!') #ünlemden itibarren ayırır, sep'e eşitlemesek de ilk parametre ayrılacağı yeri belirtir

len(strvar) #stringin uzunlugunu bulur

print(strvar.split("O")) #o'dan ayır

print(strvar.split(sep="O", maxsplit=1))  #maxsplit ile kaç kere bölebileceğimizi belirtiyoruz


