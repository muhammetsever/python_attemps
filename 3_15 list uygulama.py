names = ["Ali" , "Yağmur" , "Hakan" , "Deniz"]
years = [1998 , 2000 , 1998 , 1997]

# 1- "Cenk" ismini listenin sonuna ekle
names.append("Cenk")
print(names)
# 2- "Sena" değerini listenin başına ekle
names.insert(0,"Sena")
print(names)
#names.insert(len(names),"ehmet") #len biligisini alıp en sona ekler
#print(names)
# 3- "Deniz" ismini lsiteden sil 
# burada batırdım hayır batımadın
#del names[4]   
#names.pop()
# names.remove("Deniz")
#print(names)
# 4- "Deniz" isminin değeri nedir?
# index = names.index("Deniz") denizin indesini bulur
# names.pop(index) denizi siler
#print(index)
# 5- "Ali" listenin bir elemanı mıdır
resoult = "Ali" in names
#resuolt1 = names.index("Ali") -1 den büyük değer veriyorsa vardır
print(resoult)
# 6- liste elemanlarını ters çevir
names.reverse()
print(names)
# 7- elemanları alfabetik olarak sırala
names.sort()
print(names)
# 8- years listesini rakamsal büyüklüğe göre sıralayın
years.sort()
print(years)
# 9- str = "Chevrolet,Dacia" liste çevir
str = "Chevrolet , Dacia"
reso = str.split(",") # splitle listeye çevirdik
print(reso)
# # 10- years dizisinin en büyük en küçük elemanı nedir?
print(max(years))
print(min(years))
# 11-  years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))
# 12- years dizisinin tüm elemanlarını sil
years.clear()
print(years)
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini listede sakla
a = input("Marka Giriniz: ")
print(a.split(" ")) # bu sıkıntı olabilir



# a =[]
# an = input("Markalar: ") bu tek bir bilgiyi sakladığı için 3 defa yapmamız gerekiyor
# a.append(an)
# print(a)
