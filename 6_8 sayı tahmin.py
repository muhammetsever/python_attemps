'''
    1-100 arasında rasgele üretilecek sayıyıy aşağı yukarı ifadelerle buldurmaya açlışın
    *** random mödülünü kullan
    *** 100 üzerinden puanlama yap her soru 20 puan
    *** can bilgisini kullanıcıdan al ve her soru belirtilen can 
    üzerinden hesaplansın (can=5)
'''

import random

r1 = random.randint(1,10)



can = int(input("kaç can lazım kardeş? "))
sayac=0
while can > 0:
        can-=1
        sayac+=1
        kullanıcı_tahmini=int(input("tahmin: "))
        if kullanıcı_tahmini== r1:
            print(f"tebrikler {sayac}. defada sayıyı buldunuz puanınız {100-20*(sayac-1)}")
            break
        
        elif kullanıcı_tahmini> r1:
            print("girdiğiniz sayı büyük daha küçük sayı yazın.")
        else:
            print('girdiğiniz sayı küçük daha büyük sayı yazın.')

        if can ==0:
            print(f'kaybettiniz tutuğum sayı {r1}')
