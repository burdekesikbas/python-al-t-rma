#Örnek 21:  Klavyeden maaşı ve zam oranı girilen kişinin zamlı maaşını hesaplayan python kodunu yazınız.
maas = int(input("maaşınızı giriniz:"))
zamOrani = int(input("zam oranınızı giriniz(%):"))
zamliMaas = (maas*zamOrani/100)+ maas
print("zamlı maaş:" , zamliMaas)

#Örnek 22:  Klavyeden yarıçapı girilen dairenin çevresini ve alanını hesaplayan python kodunu yazınız.
yaricap = int(input("yarıçapı giriniz:"))
cevre = 2*3.14*yaricap
alan=3.14*yaricap*yaricap
print("dairenin çevresi:" ,cevre)
print("dairenin alanı:", alan)

#Örnek 23:  Klavyeden kısa kenar ve uzun kenar uzunluğu girilen dikdörtgenin alanını fonksiyon kullanarak hesaplayan python kodunu yazınız.
k= int(input("kısa kenar uzunluğunu giriniz:"))
u= int(input("uzun kenar uzunluğunu giriniz:"))

def dikdortgenAlan(k,u):
    
     alan = k * u
     print(alan)
dikdortgenAlan(k, u)

     
#Örnek 24:  Önceden belirlenen bir liste içerisinde bulunan sayılardan kaç tanesinin 5’in katı olduğunu bulan python kodunu yazınız.
sayilar =[5,10,18,22,25,32,38,43]
sayac=0
for i in sayilar:
     if i % 5==0:
          sayac+=1
print("5in katı olan sayıların adedi:",sayac)

#Örnek 25:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan çift sayıların ortalamasını bulan python kodunu yazınız.
sayi1= int(input("sayı giriniz:"))
sayi2= int(input("sayı giriniz:"))
toplam=0
adet=0
for i in range(sayi1, sayi2+1):
     if i%2==0:
          toplam+=i
          adet+=1
if adet>0:
     ortalama = toplam/adet
     print("çift sayıların ortalaması:",ortalama)
    

#Örnek 26:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan tek sayıların ortalamasını bulan python kodunu yazınız.
sayi1= int(input("sayı giriniz:"))
sayi2= int(input("sayı giriniz:"))
toplam =0
adet=0
for i in range(sayi1, sayi2+1):
     if i %2!=0:
          toplam+=i
          adet+=1
if adet>0:
     ortalama = toplam/adet
     print("tek sayıların ortalaması:",ortalama)

#Örnek 27:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan sayıların ortalamasını bulan python kodunu yazınız.
sayi1= int(input("sayı giriniz:"))
sayi2= int(input("sayı giriniz:"))
toplam=0
adet=0
for i in range(sayi1,sayi2+1):
     toplam+=i
     adet+=1
if adet>0:
     ortalama = toplam/adet
     print(ortalama)
     
##Örnek 28:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan sayıların toplamını bulan python kodunu yazınız.
sayi1= int(input("sayı giriniz:"))
sayi2= int(input("sayı giriniz:"))
toplam=0
for i in range(sayi1,sayi2+1):
     toplam+=i
print(toplam)

##Örnek 29:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan çift sayıların toplamını bulan python kodunu yazınız.
sayi1= int(input("sayı giriniz:"))
sayi2= int(input("sayı giriniz:"))
toplam=0
for i in range(sayi1,sayi2+1):
     if i%2==0:
          toplam+=i
print("çift sayıların toplamı:",toplam)

##Örnek 30:  Klavyeden girilen başlangıç ve bitiş sayıları arasında bulunan tek sayıların toplamını bulan python kodunu yazınız.
sayi1= int(input("sayı giriniz:"))
sayi2= int(input("sayı giriniz:"))
toplam=0
for i in range(sayi1,sayi2+1):
     if i%2!=0:
          toplam+=i
print("tek sayıların toplamı:", toplam)


#Örnek 31:  Klavyeden girilen üç yazılı notunun ortalamasını bulan python kodunu yazınız.
sayi1= int(input("1.notunuzu giriniz:"))
sayi2= int(input("2.notunuzu giriniz:"))
sayi3= int(input("3.notunuzu giriniz:"))
ortalama = (sayi1+sayi2+sayi3)/3
print("3 sınavın ortalaması:",ortalama)

#Örnek 32:  Klavyeden girilen sayının tek sayı mı çift sayı mı olduğunu bulan ve sonucu ekranda gösteren python kodunu yazınız.
sayi= int(input("sayı giriniz:"))
if sayi % 2==0:
     print("sayı çift sayıdır.")
else:
     print("sayı tek sayıdır.")
     
#Örnek 33:  Örnek :Bir otoparkın ücret tarifesi aşağıdaki gibidir:
     #1 saate kadar: 10 TL
#1-5 saat arası: Saat başı 8 TL
#5 saatten fazla: Saat başı 6 TL
#Buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana yazdırınız.
saat= int(input("Otoparkta kaç saat kaldığınızı giriniz:"))
if saat<=1:
     print("10TL ödeyiniz")
elif saat>1 and saat<=5:
     odeme1= (10+ (saat-1)*8)
     print(odeme1,": TL ödeme yapınız.")
else:
     odeme2=(10+ ((saat-1)*8)+ (saat-5)*6)
     print(odeme2,"TL ödeme yapınız.")
     
#Örnek 34:  Klavyeden girilen bir ifadeyi ekrana 10 defa yazdıran python kodunu yazınız.
ifade = input ("bir ifade giriniz:")
for i in range(10):
     print(ifade)


#Örnek 35:  Klavyeden girilen bir ifadeyi klavyeden girilen bir sayı kadar ekrana yazdıran python kodunu yazınız.
ifade = input ("bir ifade giriniz:")
sayi =int(input("bir sayı giriniz:"))
for i in range(sayi):
     print(ifade )

#Örnek 36:  Klavyeden aralarına virgül konularak yazılan tüm sayıları toplayan python kodunu yazınız.
sayilar =input("arasına virgül koyarak istediğiniz kadar sayı giriniz:")
sayilar_liste=[int(sayi) for sayi in sayilar.split(",")]
toplam= sum(sayilar_liste)
print("sayıların toplamı:",toplam)

#Örnek 37:  Klavyeden aralarına virgül konularak yazılan tüm sayıların ortalamasını hesaplayan python kodunu yazınız.
sayilar =input("arasına virgül koyarak istediğiniz kadar sayı giriniz:")
adet=0
sayilar_liste=[int(sayi) for sayi in sayilar.split(",")]
for i in sayilar_liste:
     adet+=1
toplam= sum(sayilar_liste)
ortalama =toplam/adet
print("sayıların ortalaması:",ortalama)