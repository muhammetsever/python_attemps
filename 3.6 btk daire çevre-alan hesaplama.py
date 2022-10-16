'''
   Daire alanı  :πr²
   Daire cevresi :2πr

   *Yari çapı verilen bir dairenin alanını ve çevresini hesaplayınız. (r=3.14)
'''
r =  float(input("Yarı çap:"))  #flaota çevirmediğim için çalışmadı ve inputu unuttum
pi = 3.14

alan = pi * (r ** 2)    # aralaea boşluk bırak denedim gerek yokmuş
cevre = 2 * pi * r

#print("çevresi: " , cevre) #print le yazdırırken parentezin içine virgül koy eğer başka 
#print("alanı: " , alan)    #kelime varsa

print("çevresi: "+ str(cevre) + " alanı: " + str(alan))   #hepsini tek printe yazabiliriz cevre ve
           # alan float değer olduğu için str ye çevirmek lazım yoksa hata verir