numbers = [1,2,3,4,5]

for num in numbers:
    print(num)

names = ['osman','kerim','muhammet']

for name in names:
    print(f'my name is {name}')

name = 'Muhammet S.'
for n in name:
    print(n)

tuple = [(1,2),(1,3),(1,4),(3,5)]

for t in tuple:  # her bi tupleyi yazdırır
    print(t)


for a,b in tuple:  # her bi tupledaki elemanı yazar
    print(a)    # sadece 1. elemanı yazdırdı b yi alırsak 1 ve 2 yi yazdırır


d = {'k1':1, 'k2':2,'k3':3}

for item in d:
    print(item)    # sadece k1 k2 k3 gelir

for item in d.items():
    print(item)

for key,vaule in d.items():    # sadece vauleler yazarız yada ikisini de yazdırabiliriz
    print(vaule)