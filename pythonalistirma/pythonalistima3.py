#Örnek 38:  Klavyeden başlangıç değeri, bitiş değeri ve artış miktarı girilen sayıları alt alta yazdıran python kodunu yazınız.
baslangic = int(input("ilk sayıyı giriniz."))
bitis=int(input("son sayıyı giriniz."))
artis=int(input("artış miktarını giriniz."))
for i in range(baslangic,bitis+1,artis):
    print(i)
    
#Örnek 39:  0 dan 100 e kadar olan çift sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
toplam=0
for i in range(0,101):
    if i%2==0:
        toplam+=i
print("çift sayıların toplamı:",toplam)

#or

sayi=0
toplam=0
while sayi<101:
    if sayi%2==0:
        toplam+=sayi
    sayi+=1
print("çift sayıların toplamı:",toplam)
        
##Örnek 40:  0 dan 100 e kadar olan tek sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
toplam=0
for i in range(0,101):
    if i %2!=0:
        toplam+=i
print("tek sayıların toplamı:", toplam)
        
    #OR
    
sayi=0
toplam=0
while sayi<101:
    if sayi%2!=0:
        toplam+=sayi
    sayi+=1
print("tek sayıların toplamı:", toplam)
 
    
print("tek sayıların toplamı:",toplam)
#Örnek 41:  Klavyeden girilen sayıya kadar olan sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
sayi = int(input("sayı giriniz:"))
sayac=0
toplam=0
while sayac<sayi:
    toplam+=sayac
    sayac+=1   
print("girilen sayıya kadar olan sayıların toplamı:",toplam)
    
#Örnek 42:  Klavyeden girilen sayıya kadar olan tek sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
sayi = int(input("sayı giriniz:"))
sayac=0
toplam=0
while sayac<sayi:
    if sayac%2!=0:
        toplam+=sayac
    sayac+=1   
print("girilen sayıya kadar olan tek sayıların toplamı:",toplam)

#Örnek 43:  Klavyeden girilen sayıya kadar olan çift sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
sayi = int(input("sayı giriniz:"))
sayac=0
toplam=0
while sayac<sayi:
    if sayac%2==0:
        toplam+=sayac
    sayac+=1   
print("girilen sayıya kadar olan çift sayıların toplamı:",toplam)

#Örnek 44:  Klavyeden girilen bir metni harflerine ayıran python programını while döngüsü ile yazdıran kodunu yazınız.
metin = input("bir metin giriniz:")
index=0
while index<len(metin):
    harf=metin[index]
    print(harf)
    index+=1
    

#Örnek 45:  0 ile 100 arasında 10 tane rastgele tam sayı üreten ve bu sayılardan en büyüğü ile en küçüğünü bulan ve ekranda gösteren python kodunu yazınız.
import random
liste = []
for i in range(0,101):
  liste.append(i)
  
print("rastgele sayıların en büyüğü:",max(random.sample(liste,10)),"rastgele sayıların en küçüğü:",min(random.sample(liste,10)))
   
##Örnek 46:  Kullanıcının klavyeden kilo bilgisi alınarak kilo 50 ve altında ise zayıfsın, 50-80 arası fitsin, 80 ve üstü ise kilo almışsın şeklinde ekranda yazdıran python kodunu yazınız.
##Örnek 47:  Kullanıcının klavyeden yaş bilgisi alınıp 18 yaşından küçükse çocuk 18-40 yaş arası ise genç, 40-60 yaş arası ise orta yaşlı 60 yaştan büyükse yaşlı şeklinde ekrana yazdıran programın python kodlarını yazınız.
##Örnek 48:  Klavyeden girilen iki sayının yine klavyeden girilen aritmetik operatör işaretlerine göre (toplama, çıkarma, çarpma bölme) dört işlem yapan ve sonucu ekranda gösteren python kodunu yazınız.
##Örnek 49:  Klavyeden girilen iki sayının yine klavyeden girilen aritmetik operatör işaretlerine göre (toplama, çıkarma, çarpma bölme) dört işlem yapan ve sonucu ekranda gösteren python kodunu yazınız.
##Örnek 50: Program çalıştırıldığı anda o anın tarih ve saat bilgilerini ekrana yazdıran python kodunu yazınız.
##Örnek 51: Şu anki sistemin tarihini ekrana yazdıran python kodunu yazınız.
##Örnek 52:  Klavyeden Fahrenheit cinsinden girilen sıcaklığı Dereceye çeviren python kodunu yazınız.
##Örnek 53:  Klavyeden bir kenar uzunluğu girilen karenin alanını ve çevresini bulan ve ekrana yazdıran python kodunu yazınız.
##Örnek 54:  Klavyeden girilen saniye değerinin kaç saat kaç dakika ve kaç saniye olduğunu bulan python kodunu yazınız.
##Örnek 55:  Klavyeden boy ve kilo bilgileri girilen kişinin beden kitle endeksini hesaplayan python kodunu yazınız.
##Örnek 56:  Klavyeden girilen iki sayıdan büyük olanı bulan ve ekranda gösteren python kodunu yazınız.
##Örnek 57:  Klavyeden girilen not ortalamasına göre kişinin takdir teşekkür normal geçme yada sınıf tekrarı yapması gerektiğini gösteren python kodunu yazınız.
