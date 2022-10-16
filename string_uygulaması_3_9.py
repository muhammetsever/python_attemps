website = "http://www.sadikturan.com"
course = "Python kursu: Baştan sona python proglamlama rehberiniz (40 saat)" 


#1: course karakterinin içinde kaç karakter var
result =len(course)
print(len(course))
lenght = len(website)

#2: website içinden www karakterlerini alın
result = website[7:10]
print(website[7:10])

#3: webside içinden com karakterlerini alın
result = website[22:25]
result = website[lenght-3:lenght] # alternatif
print(website[-3:])

#4: course nin içinden ilk 15 ve son 15 karakteri alın
result = course[:15]
result = course[-15:]
print(course[:15],course[-15:])

#5: course ifadesindeki karakterleri tersten yazdırın
print(course[::-1])
result = course[::-1]
#6: Verilen değişikenler ile şunu yazdırın
#   Benim adım bora yılmaz, yaşım 32 ve mesleğim mühendis

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"
print(f"Benim adım {name } {surname} , yaşım {age} ve mesleğim {job}.")
result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"
#7: Hello world ifadesinin w hafini W ile değiştirin.
a = "Hello world"
a = a[0:6] + "W" + a[-4:]
print(a)
#8: abc ifadesini 3 defa yan yana yazdırın.
result = "abc" * 3
print(result)



#9 course karakteri dizisindeki tüm karakterleri - ile yer değiştirin

course=course.replace(" ","-")
print(course)
