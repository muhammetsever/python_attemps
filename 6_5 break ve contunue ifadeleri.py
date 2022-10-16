name = 'muhammet'
'''
for let in name:
    if let == 'e':
        break
    print(let)     # break e ye gelince durdurdu
'''
'''for let in name:
    if let == 'e':
        continue   # sadece e yi yazmaz
    print(let) '''

x = 0
'''
while x < 5:
    if x == 2:
       break     # 2 den sonra yazmadı
    print(x)
    x+=1
'''
'''
while x < 5:
    x+=1
    if x == 2:
        continue    # x+1 aşağıda olduğu için sürekli takılı kalır o yüzden x i yukarı yazarız
    print(x)
'''  
# 1 den 100 e kadar çift sayıların toplamı
sayı = 0
resoult =1

while sayı <= 100:
    sayı+=1
    if sayı % 2 == 1:         # sadece çift sayıları alır
        continue
    resoult += sayı
    
print(f'toplam {resoult}')