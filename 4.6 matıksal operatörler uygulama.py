# 1- girilen bir sayının 0-100 arasında oldup olmadığını kontrol edin

sıfıryüz=int(input("Bir sayı girin: "))
sayı_kont = (sıfıryüz > 0) and (sıfıryüz < 100 )

# print(f'sayı 0-100 arasında mı:{sayı_kont}')

if sayı_kont == True:
    print("Girdiğiniz sayı 0-100 arasında.")
if sayı_kont == False:
    print("Girdiğiniz sayı 0-100 arasında değil.")
# 2- girilen bir sayını pozitif çift olup olmadığını kontrol edin
poziçift = int(input("Bİr sayı girin: "))

kont = (poziçift%2==0) and (poziçift > 0)

# print(f'girilen sayı pozitif ve çift mi? {kont}')

if kont == True:
    print("Girdiğiniz sayı hem pozitif hemde çift!")
if kont == False:
    print("Girdiğinz sayı Çift ya da pozitif değil.")
    if poziçift%2==0:
        print("Girdiğiniz sayı çift! Pozitif değil.")
    if poziçift > 0:
        print("Girdiğinz sayı pozitif. Çift değil.")

# 3- e-mail ve parola bilgileri giriç kontrolu yapın
e_mail = "mmtreves@gmail.com"
password = "abc123"

epos= input("E-postanızı girin: ")
passw = input("Şifrenizi Gİrin: ")

kotn2 = (epos == e_mail) and (password == passw)
print(f'uygulamaya giriş başarılı mı? {kotn2}')

if kotn2 == True:
    print("Kullanıcı bilgileriniz doğru.")
if kotn2 != True:
    print("Kullanıcı bilgileriniz yanlış.")

# 4- girilen 3 sayıyı buyukluk olarak karşılaştırınız
sayı1 = int(input("1. sayı "))
sayı2 = int(input("2.sayı "))
sayı3 = int(input("3.sayı "))
'''
reso = (sayı1 > sayı2) and (sayı1 > sayı3)
print(f'1. sayı en büyüktür.{reso}')

reso = (sayı2 > sayı1) and (sayı2 > sayı3)
print(f'2. sayı en büyük {reso}')
.
.
.   gibi devam edebilir böyle de yapılabilir if else kullanılmayan hali
'''

if sayı1 > sayı2:
    print("Birinci sayı ",sayı1," ikinciden ",sayı2," büyük.")
else:
    print("Birinci sayı ",sayı1," ikinci sayıdan ",sayı2," küçük.")
if sayı1 > sayı3:
    print("Birinci sayı ",sayı1," üçüncüden ",sayı3," büyük.")
else:
    print("Birinci sayı ",sayı1," üçüncüden ",sayı3," küçük.")
if sayı2 > sayı3:
    print("2. sayı ",sayı2," 3.'den ",sayı3," büyük.")
else:
    print("2. sayı ",sayı2," 3.'den ",sayı3," küçük.")
# 5- kullanıcıdan 2 vize (%60) final (%40) notu alın ortama hesaplayın
vize1 = float(input("1. Vize: "))
vize2 = float(input("2. Vize: "))
final = float(input("final: "))

ortalama = ((((vize1+vize2) / 2) * 0.6) + (final * 0.4))

print(ortalama)

#   eğer ortalam 50 nin üzerindeyse geçti altındaysa kaldı yazdırın

belkıran= (ortalama >= 50) and (final>=50)
'''
if ortalama >= 50:
    print("Geçtiniz.")
else:
    print("Kaldınız.")
'''

if final >= 70:
    print("Geçtiniz")
else:
    if belkıran == True:
        print("geçtiniz")
    else:
        print("Kaldınız")
        
 
# if ortalama >= 50:
#     print("Geçtiniz.")
# else:
#     print("Kaldınız.")


#   a-) ortalama 50 olsa bile final notu en az 50 olmalıdır

# belkıran= (ortalama >= 50) and (final>=50)

# if belkıran == True:
#     print("geçtiniz")
# else:
#     print("Kaldınız")

#   B-) finalde 70 aldıysa ortalamnın onemi olmasın
#yukarıda

# 6- kişinin ad kilo ve boy bilgilerini alıp kilo indexlerini hesaplayın
# (kilo /boyun karesi)
# aşağıdaki tabloya göre kişi hangi gruba girmektedir

name = input("Adınız: ")
kilo = float(input("Kilonuzu Girin: "))
boy = float(input("Boyunuzu girin: "))

endex_boy_kilo = (kilo / (boy ** 2))

# zayif = (endex_boy_kilo >= 0) and (endex_boy_kilo <= 18.4)
# normal = endex_boy_kilo > 18.4 and endex_boy_kilo <= 24.9
# kilolu = endex_boy_kilo > 24.9 and endex_boy_kilo <= 29.9  böyle de ölabilirdi
# obez = endex_boy_kilo > 29.9 and endex_boy_kilo <= 34.9
#  print(f'{name} kilo endexin: {endex_boy_kilo} ve kilo değerlendirmen zayıf {zayıf}')
#  print(f'{name} kilo endexin: {endex_boy_kilo} ve kilo değerlendirmen normal {normal}')
#  print(f'{name} kilo endexin: {endex_boy_kilo} ve kilo değerlendirmen kilolu {killu}')
#  print(f'{name} kilo endexin: {endex_boy_kilo} ve kilo değerlendirmen obez {obez}')


if (endex_boy_kilo <= 18.4):
    print(f"{name} Zayıfsınız. ")
else:
    if (endex_boy_kilo <= 24.9):
        print(f"{name} Normal kilodasınız.")
    else:
        if (endex_boy_kilo <= 29.9):
            print(f"{name} Kılolusunuz.")
        else:
            if (endex_boy_kilo <= 34.9):
                print(f"{name} şişmansınız -obez-")


#   0-18.4 => zayıf
#   18.5 24.9 => normal
#   25.0 29.9 => fazla kilolu
#   30.0 34.9 => şişman (obez)