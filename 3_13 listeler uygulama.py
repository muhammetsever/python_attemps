#"Bmw, Mercedes, Opel, Mazda" elemanları olan bir liste yapın
cars =["Bmw", "Mercedes", "Opel", "Mazda"]
#kaç eleman var?
print(len(cars))
#listenin ilke ve son elemanı nedir?
print(cars[0],cars[-1])
#Mazda değerini Toyota ile değiştirin
cars[-1]="Toyota"   #listelerde replace çalışmıyor onun yerine indexini yazarak değiştirdik
print(cars)

#Mecedes listenin bir elemanı mıdır?
cvp = "Mercedes" in cars  #in içindemi diye bakar
print(cvp)
#listenin -2. indesindeki değeri nedir?
print(cars[-2])
#listenin ilk üç elemanını alın
print(cars[0:3]) # bir yerden bir yere kadar alınacaksa : kulanılır
print(cars[:3])
print(cars[:-1])
#listenin son 2 elemanı yerine toyota ve renault ekleyin
cars[-2:] = ["Toyota","Renault"]
print(cars)
#cars[-2:] de kullanılabilir
#listenin üzerine audi ve nissan değerlerini ekleyin
cars2 = ["Audi","Nissan"]
C = cars + cars2
print(C) #ya da
a = cars + ["Audi","Nİssan"]
print(a)
#listenin son elemanını silin
del cars[-1]
print(cars)
#liste elemanlarını tersten yazdırın
print(cars[::-1])
#aşağıdaki verilen bir liste içinde saklayın

        # studentA Yiğit Bilgili 2010 (70,60,70)
        # studentB Sena Turan    1999 (80,80,70)
        # studentC Ahmet Turan   1998 (80,70,90)

studentA = ["Yiğit","Bilgili",2010, (70,60,70)] # stA = ["yiğit","bilgili",2010,[70,60,70]] olarak da saklanabilir
studentB = ["Sena", "Turan",1999,(80,70,90)]
studentC = ["Ahmet", "Turan",1998,(80,70,90)]
#liste elemanlarını ekrana yazdırın
print(studentA)
print(studentB)
print(studentC)
print(studentA[0])
print(studentB[2])
print(studentC[3][1])
resoult =f'{studentA[0]} {studentA[1]} {2021-studentA[2]} yaşında ve not oratalaması {int((studentA[3][0] + studentA[3][1] + studentA[3][2])/3)}'
print(resoult)