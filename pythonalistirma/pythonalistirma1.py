# Örnek 1: Ekrana “Merhaba Dünya” yazdıran python kodu yazınız.
print("Merhaba Dünya")

# Örnek 2: Girilen kullanıcı ismine göre ekrana “Merhaba Kullanıcı” yazdıran python kodunu yazınız.
isim = input("İsim giriniz:")
print("Merhaba" + " " + isim)

#Örnek 3: Klavyeden girilen iki sayıyı toplayan ve sonucu ekranda gösteren python kodunu yazınız.
sayi1= int(input("lütfen bir sayı giriniz:"))
sayi2 = int(input("lütfen bir sayı giriniz:"))
toplam = sayi1+ sayi2
print(toplam)

#Örnek 4: Klavyeden girilen iki sayının ortalamasını bulan ve sonucu ekranda gösteren python kodunu yazınız.
sayi1= int(input("lütfen bir sayı giriniz:"))
sayi2 = int(input("lütfen bir sayı giriniz:"))
ortalama = (sayi1+sayi2)/2
print(ortalama)

#Örnek 5: Klavyeden girilen vize ve final notuna göre vizenin %40 ve finalin %60’ını alan ve sonucu ekranda gösteren python kodunu yazınız.
vizeNotu = int(input("vize notunu giriniz:"))
finalNotu = int(input("final notunu giriniz:"))
sonuc = (vizeNotu * 0.4) + (finalNotu * 0.6)
print(sonuc)

#Örnek 6: Klavyeden girilen üç yazılı notunun ortalamasını bulan ekranda gösteren python kodunu yazınız.
sinav1 = int(input("sınav notunu giriniz:"))
sinav2 = int(input("sınav notunu giriniz:"))
sinav3 = int(input("sınav notunu giriniz:"))
ortalama = (sinav1 + sinav2 + sinav3)/3
print(ortalama)

#Örnek 7: Bir dersin ortalaması girilen öğrencinin o dersten geçip geçmediğini gösteren python kodunu yazınız. (50’den büyükse geçti değilse kaldı yazdıran örnek python kodu)
dersNotu = int(input("öğrenci notunu giriniz:"))
if dersNotu > 50:
    print("geçtiniz.")
else:
    print("kaldınız.")
    
#Örnek 8:  Klavyeden girilen sayının tek mi çift mi olduğunu yazdıran python kod örneğini yapınız.
sayi = int(input("sayi giriniz:"))
if sayi % 2 == 0:
    print("girdiğiniz sayı çifttir.")
else:
    print("girdiğiniz sayı tektir.")
    
#Örnek 9:  Klavyeden girilen sayının pozitif mi negatif mi yoksa sıfır mı olduğunu bulan python kodunu yazınız.
sayi = int(input("sayı giriniz:"))
if sayi > 0:
    print("girdiğiniz sayı pozitiftir.")
elif sayi == 0:
    print("girdiğiniz sayı 0 a eşittir.")
else:
    print("girdiğiniz sayı negatiftir.")
    
#Örnek 10:  Klavyeden girilen yaşa göre ehliyet alıp alamayacağını bulan python kodunu yazınız.
yas = int(input("yaşınızı giriniz:"))
if yas >= 18:
    print("ehliyet alabilirsiniz.")
else:
    print("ehliyet alamazsınız.")
    
#Örnek 11:  1 den 10 a kadar olan sayıları alt alta yazdıran python kodunu yazınız.
for i in range(1,11):
    print(i)

#Örnek 12:  1 den 20’ye kadar olan çift sayıları alt alta yazdıran python kodunu yazınız.
for i in range(1,21):
    if i%2==0:
        print(i)
        
#Örnek 13:  1 den 20’ye kadar olan tek sayıları alt alta yazdıran python kodunu yazınız.
for i in range(1,20):
    if i%2!=0:
        print(i)
#Örnek 14:  1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
        
#Örnek 15:  Klavyeden girilen sayıya kadar olan sayıları alt alta yazdıran python kodunu yazınız.
sayi = int(input("lütfen bir sayı giriniz:"))
for i in range(1,sayi+1):
    print(i)
#Örnek 16:  Klavyeden kısa kenar uzunluğu ve uzun kenar uzunluğu girilen dikdörtgenin alan ve çevresini hesaplayan python kodunu yazınız.
kısaKenar = int(input("uzunluk giriniz:"))
uzunKenar = int(input("uzunluk giriniz:"))
alan= kısaKenar * uzunKenar
print(alan)

cevre= (kısaKenar + uzunKenar)*2
print(cevre)

#Örnek 17:  Klavyeden girilen bir metnin harflerini alt alta yazdıran python kodunu yazınız.
metin = input("lütfen bir kelime giriniz:")
for i in range(len (metin)):
    print(metin[i])

#Örnek 18:  Klavyeden girilen iki sayı arasındaki sayıları toplayan python kodunu yazınız.
sayi1 = int(input("bir sayı giriniz:"))
sayi2 = int(input("bir sayı giriniz:"))
toplam = 0
for i in range(sayi1,sayi2+1):
    toplam = toplam + i
print(toplam)


#Örnek 19:  Klavyeden girilen sayının asal sayı olup olmadığını bulan python kodunu yazınız.    
sayi=int(input("Sayıyı Girin : "))
asalSayi = True
if sayi ==1:
    asalSayi = False
for i in range(2,sayi):
    if (sayi % i) == 0:
        asalSayi = False
        break
    
if asalSayi == True:
    print(sayi, "asal sayıdır.")
else:
   print(sayi," Asal Sayı Değildir.")
        

#örnek 20:  Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
sayi = int(input("bir sayı giriniz:"))
cifttoplam = 0
tektoplam= 0
for i in range(0, sayi+1):
    if i % 2==0:
        cifttoplam = cifttoplam + i  
    else:
        tektoplam =tektoplam + i
   
print("çift sayıların toplamı:" ,cifttoplam)     
print("tek sayıların toplaı:", tektoplam)


  
    
        
