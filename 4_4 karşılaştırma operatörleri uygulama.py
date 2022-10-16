#1- Girilen 2 sayıdan hangisi büyüktür 
"""
a =int(input("bir sayı girin:"))

b = int(input("diğer sayıyı girin: "))

sonuç = a > b

# print(sonuç)
print(f'a: {a} b: {b} den büyüktür: {sonuç}')
"""
# 2-kullanıcıdan iki vize (%60),final(%40) sonucu alıp ortalama hesapma
# 50 nin üzerindeyse geçri değilse kaldı yazdırın

# vize = float(input("Vize 1: "))  # ben int te çevirdim floata çevirmek lazım çünkü küsüratlı sayı girilebilir
# vize2 = float(input("Vize 2: "))

# final= float(input("Final : "))

# ortalama = (((vize + vize2)/2) * 0.6) + (final * 0.4)



# if ortalama>=50:
#     print("geçtiniz")
# if ortalama<50:
#     print("kaldınız")
   

# print(f'ortalamanız {ortalama} dersten geçme durumunuz: {ortalama>=50}')

#3-girilen bir sayının tek mi çift mi olduğunu yazdırın

sayı =int(input("Bir sayı girin: "))

# tekçift = (sayı%2 == 0)

# print(sayı%2)
# print(f'girilen sayının çift olma durumu {tekçift}')

if sayı%2 == 0:
    print("çift")
if sayı%2 != 0:
   print("tek") 

# c = 4%2
# print(c)

#4- girilen bir sayının negatif mi pozitifmi olduğunu yazdırın

# sayi = int(input("Bir sayı girin: "))

# pozitifmi=(sayi>0)

# print(f'sayının pozitif olma durumu {pozitifmi}')

# if sayi>=0:
#     print("pozitif")
# if sayi<0:
#     print("negatif")


#5- parola e-mail bilgisi isteyip doğruluğunu kontrol et
# (eposta-mmtreves@gmail.com şifre-a1b2c3d4)

email =input("E mailinizi girin: ")
passsword = input("Şifrenizi girin: ")

ekont= email == "mmtreves@gmail.com" # sonuna .lower konulursa küçük yapar küçük büyük harf fark etmiyosa

passkont= passsword == "a1b2c3d4"  # sonuna boşlıuk koyarsa false geleceği için strip kullanırız

print(ekont,passkont)

print(f'e mail bilgisi doğru mu {ekont} parola bilgisi doğru mu {passkont}')