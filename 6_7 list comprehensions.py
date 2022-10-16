# # for x in range(10):
# #     print(x)
# # alternatif olarak:
# numbers = []
# for x in range(10):
#     numbers.append(x)
# print(numbers)

# numbers = [x for x in range(10)]
# print(numbers)

# for x in range(10):
#     print(x**2)

# kareler = [x**2 for x in range(10)]
# print(kareler)

# kübüsüler= [x*x for x in range(10) if x%3==0]  # sadece üçe bölünenler
# print(kübüsüler)

mystring = "hello"
mylist = []

for letter in mystring:
    mylist.append(letter)
print(mylist)

years = [1999,1956,1939,1881,1923]

year = [2021-year for year in years]
print(year)

resoults = [x if x%2==0 else "tek" for x in range(1,10)]
print(resoults)

resoult = []

for x in range(3):
    for y in range(3):    # ilk once x yazar sonra y döngüsü bitene kadar devam eder başa döner; tekrar aynısını yapar
        resoult.append((x,y))
print(resoult)
# alternatifi

numbers= [(x,y) for x in range(3) for y in range(3)]  # üsteki ile aynı işlevi görür
print(numbers)
