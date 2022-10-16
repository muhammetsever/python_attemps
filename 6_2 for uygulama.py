sayılar = [1,3,5,7,9,12,19,21]

#1- sayılar listesindeki hangi sayılar 3'ün katıdır
'''for x in sayılar:
     if x%3==0:
         print(x)
'''

#2- sayılar listesinde sayıların toplamı kaçtır
'''toplam = 0
for a in sayılar:
     toplam += a  # ya da toplam = toplam + a
print('toplam:',toplam)
'''
# #3- sayılar listesindeki tek sayıların karesini alın
'''kare = 1
for c in sayılar:
   if c%2 != 0:
    print('karesi:',c**2)'''  #kare = c ** 2
    




sehirler = ['kocaeli','ankara','izmir','istanbul','rize']

#4- sehirlerden hangileri en fazla 5 karakterlidir

'''for z in sehirler:
   if len(z) <= 5:
       print(z)'''
        




urunler = [
    {'name' : 'samsung s6' , 'price' : '3000'},
    {'name' : 'samsung s7' , 'price' : '4000'},
    {'name' : 'samsung s8' , 'price' : '5000'},
    {'name' : 'samsung s9' , 'price' : '6000'},
    {'name' : 'samsung s9' , 'price' : '7000'}
]

#5- ürünlerin fiyatının toplamı nedir
'''toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(toplam)   # döngüden çıktıktan sorna yazdır yoksa yanlış sonuç veriyo
'''

#6- ürünlerin fiyatı en fazla 5000 olan ürünleri gösterin

for urun in urunler:
    if int(urun['price']) <= 5000:
        print(urun['name'])