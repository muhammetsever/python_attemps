# 1- kullanıcıdan isim yaş ve ğitim durumu bilgilerini iste. ehliyet alıp alamadığını
#    kontrol et. ehliyet alma koşulu en az 18 yaşında eğitim durumu lise yada üni olmalı
'''
ad = input('adınız: ')
age = int(input('yaşınız: '))
education = input('eğitim durumunuz: ')

#if (age >= 18) and (education =='lise' or aducation=='üni') diğer yol detasız olan
#    print('ehliyet alabilirsiniz')
#else:
#    print('ehliyet alamazsınız')
if age >= 18:
    if education == 'lise' or education == 'üniversite':
        print(f'{ad} Araba ehliyeti almaya uygunsunuz')
    else:
        print(f'{ad} öğrenim durumunuz yeterli olmadığı için ehliyet alamazsınız')
else:
    print(f'{ad} yaşınız küçük olduğu için ehliyet alamazsınız.')
'''

# 2- bir öğrencinin 2 yazılı bir sözlü notunu alın ve ortalamaya göre aşağıdaki not 
#    versin.
#   0-24=0 , 25-44=1 , 45-54=2 , 55-69=3 , 70-84=4 , 85-100=5 
'''
yazili1 = float(input('1.yazılı: '))
yazili2 = float(input('2.yazılı: '))
sozlu = float(input('sözlü notu: '))

ortalama = (yazili1 + yazili2 + sozlu) / 3

if ortalama >= 0 and ortalama <= 24:  f string ile ortalamsı da yazılabilir
    print('notunuz:0')
elif ortalama >= 25 and ortalama <= 44:
    print('notunuz:1')
elif ortalama >= 45 and ortalama <= 54:
    print('notunuz:2')
elif ortalama >= 55 and ortalama <= 69:
    print('notunuz:3')
elif ortalama >= 70 and ortalama <= 84:
    print('notunuz:4')
elif ortalama >= 85 and ortalama <= 100:
    print('notunuz:5')
else:
    print('yalış bilgi girdiniz')

'''
# 3- trafiğe çıkış tarihi alınan bir aracı servis zamanını aşağıdaki bilgilere göre 
#   hesaplayın
#   1.bakım=> 1.yıl
#   2.bakım=> 2.yıl
#   3.bakım=> 3.yıl
'''
days = int(input('aracınız kaç gündür trafikte? '))

if days<= 365:
    print('aracın bakımı daha gelmemiş')
elif days >= 365 and days <= 365*2:
    print('aracın 1. bakımı gelmiş')
elif days >= 365*2 and days <= 365*3:
    print('aracın 2. bakımı gelmiş')
elif  days >= 365*3 and days <= 365*4:
    print('aracın 3. bakımı gelmiş.')
else:
    print('yanlış bilgi girdiniz')
'''
import datetime
tarih = (input('aracınız hangi tarihte trafiğe çıktı (2019/1/15):'))
tarih = tarih.split("/")

trafiğeçıkış = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

now = datetime.datetime.now()

fark = now - trafiğeçıkış

days=fark.days

if days <= 365:
    print('aracın 1. bakımı gelmiş')
elif days >= 365 and days <= 365*2:
    print('aracın 2. bakımı gelmiş')
elif days >= 365*2 and days <= 365*3:
    print('aracın 3. bakımı gelmiş')
else:
   print('yanlış bilgi girdiniz')