website= "hptts//www.sadikturan.com"
course="Python Kursu: Baştan Sona Pyhton Proglamlama Rehperiniz (40 Saat)"
a=" Hello World "

#1 " Hello World " karakter dizisinin baştaki ve sondaki boşluğu sil
a=a.strip()
#..lstrip yazarsan soldan
#..rstrip yazarsan sağdan siler
print(a)

#2  "www.sadikturan.com" sadikturan dışındaki tüm karakterleri sil
b = "www.sadikturan.com".strip("w.com") #içine yazılanları siler

print(b)
#3 "course" deki tüm harfleri küçük yap
course = course.lower()
print(course)

#4 "website" kaç tane a karakteri vardır (count("a"))
a_sayisi =  website = website.count('a')
print(a_sayisi)

#5 "website" www ile başlayıp com ile bitiyor mu

# nedense bu olmuyo

#resoult = website.startswith("www")

#print(resoult)





#6  "website" içinde com var mı

#resoult = website.find(".com")

#print(resoult)
#7  "course" içindeki tüm harfler alfabetik mi (isalpha,isdigit)

alfabe = course.isalpha()

print(alfabe)


#8 "contents" ifadesine 50 karakter içine * ekle sağa sola eşit

asd="contents"

#asd = asd.center(50,"*")

asd = asd.ljust(50, '1')
print(asd)



#9 "course " içindeki tüm boşlukları - ile değiştir

#course = course.replace(" ","-")

#print(course)


#10   "Hello world" karakter disinde hello yerine there yaz

hello ="Hello World"

hello = hello.replace("World","there")

print(hello)



#11   "course" karakter dizisini boşluklarında ayırın

course = course.split(" ")

print(course)