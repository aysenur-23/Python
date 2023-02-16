

print("19","05","1993", sep = "/") #sep ile yazdırılan değerler arasına ekleme yapılır

print("Ayşe\nNur\nAslan") # \n ile alt satıra geçilir

print("{} + {} = {}".format(2,3,2 + 3 )) # .format  ile {} yerine yazılacak değerler eklenir

print ( "--------------------------------------------------")


a = 3 # a değişkenine 3 değeri atandı, int değer(tam sayı)
b = 3.14 # b değişkenine 3.14 değeri atandı, float tipi (noktalı sayı)
c = "Python" # c değişkenine Python yazısı atandı, string veri tipi (yazı)
d = [1,2,3,4,5,"Python"] # d değişkenine değerler atandı, liste veri tipi
e = (1,2,3,4,5, "Python") # e değişkenine değerler atandı, tuple veri tipi
f = {"Elma":3, "Armut":4, "Kiraz":5} # değerlere karşılık atamalar yapılıyor, sözlük veri tipi
g = False # True veya False değeri alabilir, boolean veri tipi

print(type(a)) # type ile a değişkeninin içeriğinin türünü sorguluyoruz
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

print(a,b,c)

print(3+4) #toplama
print(10-3) #çıkarma
print(10*8) #çarpma
print(10/2) #bölme
print(7//2) #kalan kısmını atıp sadece bölümü verir
print(18%4) #18 mod 4 ün sonucunu verir

print ( "--------------------------------------------------")


a = 5
b = 12
c = a + 2 * b
print(c) # değişkeni yazdırarak içeriğini ekranda görebiliriz

print ( "--------------------------------------------------")


a = "Python"
b = "Programlama"
c = "Dili"

print(a + " "+  b + " " + c) 
#değişkenlere atanmış string verileri + operatörüyle yan yana yazdırır

print ( "--------------------------------------------------")


a = "Python"
b = [1,2,3,4,5,6,7,0,12]
print(a[0]) # a'nın 0. indisindeki değeri yazdır
print(len(a)) # a stringinin boyutunu yazdırır
print(len(b)) # b dizisinin boyutunu yazdırır

print(b[len(b)-1])

print ( "--------------------------------------------------")


a = input("a: ") # değerler default olarak string alınır
b = input("b: ")
c = input("c: ")
print("Toplam: ", a+b+c) # string değerler olduğu için yan yana yazar 

print ( "--------------------------------------------------")


a = int(input("a: ")) #değeri int'e çevirerek tutabiliriz
b = int(input("b: "))
c = int(input("c: "))
print("Toplam: ", a+b+c)

print ( "--------------------------------------------------")


# Python'da koşul durumları

yas = int(input("Yaşınız : "))

if(yas < 18): #yaş 18'den küçükse
        print("Giriş yapamazsınız! ") #bu satır çalısır
else: #değilse
    print("Hoş Geldiniz!") # bu satır çalısır

print ( "--------------------------------------------------")


a = 23
b = 44

if a == 23 and b == 44: # iki kontrol de doğruysa
    print("evet")
    
else:
    print("Hayır")

print ( "--------------------------------------------------")


if a == 23 or b == 32: # iki kontrolden biri doğruysa
    print("evet")
    
else:
    print("Hayır")

print ( "--------------------------------------------------")

i = 0 
while i < 10:
    print("i:",i)
    i = i + 1
    
print ( "--------------------------------------------------")

i = 0

while(i<10):
    if i == 3 or i == 5:
        continue # if döngüsüne girildiğinde yani 3 ve 5 değerlerinde işlem yapılmadan devam edilir
        #break bu komutla döngü kırılır
    
    print("i:",i)
    i += 1

print ( "--------------------------------------------------")

a = [1,2,3,4,5,6]
b = "Python"

for karakter in b:
    print(karakter)

print ( "--------------------------------------------------")

for sayi in range(10,100,2): # 10dan 100e kadar 2şer
    print(sayi)

print ( "--------------------------------------------------")

def selamla(isim): # fonksiyon tanımlama, parametre olarak isim değişkenini alır
    print("Merhaba", isim)
    print("Nasılsın?")

selamla("Aysenur")
selamla("Burçak")

print ( "--------------------------------------------------")

def toplam (a,b,c):
    return a+b+c
# fonksiyon çağırılmadığı sürece çalışmaz

toplam = toplam(3,4,5) 
print(toplam)

print ( "--------------------------------------------------")

liste = [1,2,3,4,5,6]
a = "araba"

print(a.startswith("a"))
 # a stringi a ile başlıyor mu
 
a = a.replace("a","e")
 # a ile e'nin yeri değiştirilir
 
print(a)

liste.append("Python") 
#listeye Python stringi eklenir

print(liste)

liste.pop() 
# listenin son elemanını çıkarır, parametre eklenirse belirtilen indisteki elemanı çıkarır

print(liste)

print ( "--------------------------------------------------")

file = open("dosya.txt","w")
 # dosya.txt isimli dosyayı write modunda aç
 
file.seek(10)
# 

file.write("Naber Python")
# dosyaya yazı yazıyoruz

veri = file.read(10)
print(veri)

file.close()
# dosyayı kapatır

print ("--------------------------------------------------")

# object oriented
class Account: # Account classı                                                                                                                          
    def __init__(self,isim,numara,bakiye): 
    # objenin özellikleri
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
        
    def hesapBilgileri(self):
        print("İsim :", self.isim)
        print ("Numara :", self.numara)
        print("Bakiye :", self.bakiye)
        
    def paraCek(self,miktar):
        if(self.bakiye - miktar < 0):
            print("Bakiyeniz yeterli değil..")
            
        else:
            self.bakiye -= miktar
            print("Yeni bakiye:",self.bakiye)
    def paraYatir(self,miktar):
        self.bakiye += miktar
        print("Yeni bakiye:", self.bakiye)
        
account = Account("Ayşe Nur Aslan",123456,1000)
account.hesapBilgileri()

account.paraCek(800)
account.hesapBilgileri()

print ( "--------------------------------------------------")



































