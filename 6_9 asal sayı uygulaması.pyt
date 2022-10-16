#bir sayının asal olup olmadığını bul
'''
    girilen sayı 1'e ve kendisine bölünüyorsa asaldır.
'''

sayi= int(input('Bir sayı girin:'))

if sayi==1:
    print('1 sayısı asal değildir')

asalmi= True

# for a in range(2, sayi):
    
#     if  sayi%a!=0:        #eğer ==0 yaparsam if else yerleri değişir
#        print(f'girdiğiniz sayı {sayi} asal bir sayıdır')
#        break    
#     else:
#         print('girdiğiniz sayı asal değildir')
#         break

for a in range(2, sayi):
    if  (sayi%a==0):
        asalmi= False
        break
if asalmi == True:
    print("sayı asal")
else:
    print("sayı asal değil")