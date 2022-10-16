x, y, z= 2, 5, 10

numbers = 1, 5, 7, 10, 6


#1- kulanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
# a=int(input("Bir sayı girin: "))
# b=int(input("Bir sayı girin: "))

# toplam = x+y+z

# answer= (a*b)-toplam #(a*b)-(x+y+z) de yapılabilir

# print(answer)

#2-y'nin x'e kalansız bölümünü hesapla

ac= y//x
print(ac)

#3-x,y,z toplamının mod-%- 3 ü nedir
bc = (x+y+z)
reso= bc % 3
print(reso)

#4-y'nin x'inci kuvvetini hesaplayın
cd= y**x
print(cd)


#5-x,*y,z = numbers işelmine göre z'nin küpü kaçtır
x,*y,z = numbers

cx=z**3
print(cx)


#6-x,*y,z = numbers işlemine göre y'nin değerlerinin toplamı kaçtır

toplamm= y[0]+y[1]+y[2]
print(toplamm)