liste = ['a','b','c','d','e']
print(liste)

liste = liste + ['f', 23]
liste

liste[3:5]

liste.append('g')    #geri atamadık ama listeye g'yi ekleyip liste ye atar
liste

liste = ['a','b','c','d','e','f','g']
liste.pop(5)   #listenin 5. elemanını atar
print(liste)

liste.pop() #listenin son elemanını atar

sayilar= [123,251,23,154,123556,1,2]
sayilar.sort()   #sıralama yapar
sayilar

sayilar.reverse()   #diziyi ters çevirir
print(sayilar)

set(sayilar)    #tekrar eden sayıları 1 kere yazar, sayıları sıralar ve {} arasında yazar set biçimine çevirir

list=['Elazığ','Eskişehir','Erzurum','Edirne','Erzincan','Elazığ']
print(list)

tup=('Elazığ','Eskişehir','Erzurum','Edirne','Erzincan','Elazığ')
print(tup)

list[0] = 1223
list

 # tup[0] = 1223 tup'un özelliği sebsebiyle herhangi bir elemanını değiştiremeyiz
 
 print(tup.count('Eskişehir')) #elemanını kaç kere olduğunu sorgulama
print(tup.count('Elazığ'))

tup.count('b') # 0 tane olduğunu söyler

tup.index('Eskişehir') #aradığım ifadenin yerini soruyorum 
tup.index('Elazığ') #ifadeden iki tane varsa ilkinin indexini verir
 
#for

yorum_birakanlar = ["İremnur Aydemir", "Ali Veli","Melike Sena Elitok", "Çağla Nur Teker","Esma İlbak","Eren Salık"]
kullanici_say = 0

for kullanici in yorum_birakanlar:
    ad = kullanici.split()[0]
    soyad = kullanici.split()[1]
    kullanici_say += 1
    print('{0}. kullanıcının adı {1} soyadı {2} '.format(kullanici_say,ad, soyad))


liste = [[1,2],[3,4],[5,6]]

for x,y in liste: #listelerdeki ilk elemanlar x'e 2. elemanlar y'ye atanır
    print(x ,y,"=", x*y)
[09:08, 06.09.2021] Ayşe Nur: #range
print(range(10)) # 0'dan 10 a kadar tüm sayılar

print(list(range(10))) # sayıları liste olarak listeye atar

print (  *range(10) ) # sayıları daha profesyonel şekilde listeye atar

print(*range(2,7)) # 2'den 7'ye kadar lsiteler

# enumerate

harfler = ['a','b','c','d','e']
for harf in enumerate(harfler):
    print(harf) #indexlerini ve değeri yazdırır
 for index, harf in enumerate(harfler):
    print("{}. harf: {}".format(index+1, harf)) #indexi ve değer
    
    
    # zip

ulkeler = ['TR','FR','DE']
siralamalar = range(1,4)

for ulke in zip(ulkeler, siralamalar): # aynı boyuttaki 2 listeyi birleştirir
    print(ulke)

# break
harfler = ['a', 'b', 'c', 'd', 'e'] *100
for index,harf in enumerate(harfler):
    if harf == 'c':
        print('{} harfi {}. indextedir.'.format(harf,index))
        break #sonucu bulur bulmaz çık demektir

#continue
for sayi in range(1,6):
    if sayi%2==0:
        continue # hiçbir şey yapma devam et
    print(sayi)

# pass
for sayi in range(1,6):
    if sayi%2==0:
        pass # geç
    else:
        print(sayi)


if say<5:
    pass
else:
    print("hey"
