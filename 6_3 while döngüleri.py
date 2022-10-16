#1 den 100 e kadar

x = 0
'''
while x < 100:
    print(x)
    x = x + 1  #bunun üstte veya alta olması bir şey değiştirmiyor
print('bitti...')
'''

'''
while x <= 100:
    if x%2 == 0:   # sadece çiflteri yazar 0 yerine 1 yazarsan tekleri yazar
        print(x)
    x+=1
'''
'''
while x <= 100:
    if x%2==0:
        print(f'sayı çift {x}')
    else:
        print(f'sayı tek {x}')
    x+=1
'''

name = ''

while not name:
    name = input('isminizi girin: ')

print(f'Merhaba! {name}')


