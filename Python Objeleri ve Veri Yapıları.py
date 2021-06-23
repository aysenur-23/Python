#!/usr/bin/env python
# coding: utf-8

# In[1]:


number1 = 10
print(number1)

number1 =20
print(number1)

number1 += 30
print(number1)


# In[6]:


yaş = 20


# In[5]:


a = '20'
b= '   30 '
print(a+b)


# In[ ]:


x, y, name, isStudent = (1,2.3,"Çınar", True)


# In[ ]:





# In[8]:


isim ="Burcu"
soyİsim = " Aslan"
musteri = isim+soyİsim
print(musteri)
cinsiyet = 'kız'
tcNo=1111164614
dogumTrh= 2002
adres="cad sokak"
yas = 21


# In[17]:


x = input('1.say')
y = input('2.say')

print(type(x))
print(type(y))

toplam= int(x)+int(y)

print(toplam)


# In[23]:


yarıcap = input("yarıcap :")
pi=3.14 
yarıcap = int(yarıcap)

cevre = 2 * pi * yarıcap 

alan = pi * (yarıcap ** 2)

print("Çevre:" + str(cevre) + "  Alan: " + str(alan))


# In[42]:


name = 'Sadık'

surname = 'Turan'

age = 36

greeting = 'My name is ' + name + ' ' + surname + ' and \n I am ' + str(age) + 'years old.'
print(greeting)

print(greeting[0])
print(greeting[3])

length = len(greeting)

print(greeting[length-1]) #son karakter
print(greeting[-1]) #son karakter

print(greeting[3:7]) # 3'den 7'ye kadar olan karakterler
print(greeting[3:]) #3den sona kadar karakterleri alır

print(greeting[:16]) #baştan 7'ye kadar karakterleri alır
print(greeting[2:40:2]) #2'den 40'a kadar 2şer gider 1 alır 1 almaz


# In[47]:


name =  'Aysenur'
surname = 'Aslan'

print ('My name is {} {}'.format(name, surname))

print ('My name is {1} {0}'.format(name, surname))

print ('My name is {n} {s}'.format(s=surname, n=name))

print ('My name is {} {} and I am {} years old.'.format(name, surname, '19'))

print ('My name is {} {} and I am {} years old.'.format(name, name, name))

print (f'My name is {name} {surname} and I am {age} years old.')


# In[ ]:


result = 200/700

print('the result is {r:1.3}'.format(r=result))

# tam sayı olarak kaç rakamın belirtileceği .´dan önce belirtilir 1.
# .'dan sonra kaç basamağın yazılacağını .´dan sonra belirtilir .3


# In[96]:


website = "http:\\www.sadikturan.com"
course = 'Python Kursu: Baştan Sona Programlama Rehberiniz(40 saat)'

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?

length = len(course)

print(length)
  
# 2- 'website' içinden www karakterlerini alın

print(website[6:9])
  
# 3- 'website' içinden com karakterlerini alın
print(website[21:24])
  
# 4- 'course' içinden ilk 15 ve son 15 karakterleri alın
 
print(course[0:15])
print(course[42:57])   
  
# 5- 'course' ifadesindeki karakterleri tersten yazdırın
print(course[::-1])
  
# 6- Aşağıda verilen değişkenler ile ekrana anlamlı bir cümle yazdırınız
name, surname, age, job = 'Bora','Yılmaz',32,'mühendis'
 
print(f'Benim adım {name} {surname} ben {age} yaşındayım ve mesleğim {job}')
 
# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
  
s = 'Hello world'

s= s[0:6] + 'W'+ s[-4:]
 
print(s)
  
# 8- 'abc' ifadesini yan yana 3 defa yazdırın

result = 'abc ' * 3 
print(result)
 


# In[110]:


message = 'Hello There. My name is Sadık Turan'

message = message.upper() #tüm metni büyük harfe çevirir

message = message.lower() #tüm metni küçük harfe çevirir
   
message = message.title() #metindeki kelimelerin baş harflerini büyük harfe dönüştürür
 
message = message.capitalize() #ilk harfi büyük harf yapar

message = message.strip() # baş ve sondaki boşlukları atar
 # l eklersek soldan r eklersek sağdan siler  lstrip rstrip
message = message.split() # metni boşluklardan ayırıp dizi oluşturur
   
message = message.split('.') #metni noktalardan ayırır

message = '*'.join(message) #kelimeleri araya tırnağın içindeki karakteri koyarak birleştiriyo  

print(message)

index = message.find('Sadık') #aranan kelimenin kaçıncı indexten başladığını indexe atar

print(index)     # -1 dönerse bulunmamıştır

isFound = message.startswith('H') #kelime h la mı başlıyor

isFound = message.endswith('H') #kelime h la mı bitiyor

message = message.replace('Sadık','Çınar') #sadık yerine çınar yazar

message = message.center(50)  # mesajı 50 karakterin tam ortasına yerleştirir

message = message.center(50,'*') #50 karakterin içine mesajı ortalar ve mesajın denk gelmediği yerlere * koyar


# In[128]:



website = "http:\\www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberniz (40 saat)"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin

text = "  Hello World   "

text = text.strip()

print(text)

# 2- website içindeki sadikturan hariç her şeyi silin

index = website.find('sadikturan')

print(website[10:20])

# 3- "course" karakter dizisindeki tüm harfleri küçük yapın

print(course.lower())

# 4- 'website' içinde kaç tane 'a' karakteri vardır

print(website.count('a'))

# 5- website www ile başlayıp com la bitiyor mu
 
print(website.startswith('www'))

print(website.endswith('com'))

# 6- websitede .com var mı

print(website.find('com'))

# 7-course içindeki karakterlerin hepsi alfabetik mi? 

print(course.isalpha()) #hepsi harf mi
print(course.isdigit()) #hepsi rakam mı

# 50 karakter içine contents yazdırıp sağına veya soluna * koyunuz
print('contents'.center(50,'*')
print('contents'.ljust(50,'*') 
print('contents'.rjust(50,'*')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




