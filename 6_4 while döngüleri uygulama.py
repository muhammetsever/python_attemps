from typing_extensions import runtime


sayılar = [1,3,5,7,9,12,19,21]

#1- sayıları while ile ekrana yazdır
'''i = 0
while (i < len(sayılar)):
    print(sayılar[i])
    i+=1'''

# 2- başlangıç ve bitiş değerlerini kullanıcıdan alıp tek sayıları yazdır
'''a = int(input('başlangıç:' ))
b = int(input('bitiş: '))

while a < b:
     a+=1
     if a % 2 ==1:
        print(a)'''

#3- 1-100 arasındaki sayıları azalan biçimde yazdırın

# x = 100   
# while x > 0:    
#     x-=1
#     print(x)

# 4- kullanıcıdan alacağınız 5 sayıyı sıralı bir biçimde yazdırın
'''
numbers = []

c = 0

while c < 5:
    sayi = int(input('sayı: '))
    numbers.append(sayi)
    c+=1
numbers.sort()
print(numbers)
'''



# 5 kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayın
#  -ürün sayısını kullanıcıya sorun
#  -dictionary listesi şeklinde (name, price) olsun
#  -ürün ekleme işlemi bittiğinde ekrana while ile listeleyin

ürünler = []
c = 0 
ürün_sayısı = int(input('Ürün sayısı: '))

while c < ürün_sayısı:
     item=input("Bir ürün adı girin: ")
     price=input('fiyatı')
     ürünler.append({
         'name' : item,
         'price': price
         })
     c+=1

for urun in ürünler:
     print(urun)


# urunler = []

# adet = int(input('kaç ürün eklemek istiyorsunuz: '))
# i = 0

# while(i<adet):
#     name = input('ürün ismi: ')
#     price = input('ürün fiyatı: ')
#     urunler.append({
#         'name': name,
#         'price': price
#     })
#     i += 1

# for urun in urunler:
#     print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')