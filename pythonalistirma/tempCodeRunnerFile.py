
girilen_saniye = int(input("Saniye değerini girin: "))

saat = girilen_saniye // 3600
kalan_saniye = girilen_saniye % 3600
dakika = kalan_saniye // 60
saniye = kalan_saniye % 60

print("girilen saniye:",saat, "sa " ,dakika, "dk ", saniye, "sn ")