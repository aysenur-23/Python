print(3+2)

print(5*4)

print(5%4)

print(type(2.3 + 4.7))

strvar = 'Ayse Nur Aslan'
strvar[10]

strvar.index('ü')

strvar.upper().lower()

strvar.split("a")

a = True 
b = False
c = 'True'
print(a == b)
print(a == c)
print(a!=b)

liste = [1,'a',2,3, True, 4, 5, 'True', '1']
len(liste)
print(liste[-1]) #listenin son değerini getirir
print(liste[8])

liste[2::4] #2:6:3 = 2,4

liste.reverse() # [::-1] listeyi tersten sıralar
liste



ic_ice_liste = [1,2,3,[4,5]]
a = ic_ice_liste[3]
a[1]

ic_ice_liste = [1,2,3,[4,5]]
a = ic_ice_liste.pop()
a

ic_ice_liste = [1,2,3,[4,5]]

yeni_liste= ic_ice_liste[:2] + [ic_ice_liste[-1]]
yeni_liste

ic_ice_liste = [1,2,3,[4,5]]

print(ic_ice_liste[-1][-1])
print(ic_ice_liste[3][1])
print(ic_ice_liste[-1][1])

ic_ice_liste = [1,2,3,[4,5]]
ic_ice_liste.remove(3)
ic_ice_liste

my_dict = {'isim': 'Mesut', 'yas':32, 'lokasyon': {'yasadigi':'Berlin', 'dogdugu': 'Istanbul'}}

print(my_dict['yas'])

print(my_dict.get
     
     ('yas'))
     
     
my_dict = {'isim': 'Mesut', 'yas':32, 'lokasyon': {'yasadigi':'Berlin', 'dogdugu': 'Istanbul'}}

my_dict['isim'] ='Ayşenur'

my_dict.values()


print(my_dict['lokasyon']['dogdugu'])
print(my_dict.get('lokasyon').get('dogdugu'))

my_dict.keys()
