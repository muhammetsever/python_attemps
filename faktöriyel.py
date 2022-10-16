# fsayı = int(input('bir sayı girin: '))

# if fsayı == 0:
#     print(1)
# elif fsayı == 1:
#     print(1)
# elif fsayı == 2:
#     print('2!=',2*1)
# elif fsayı == 3:
#     print('3!=',3*2*1)
# elif fsayı == 4:
#     print('4!=',4*3*2*1)
# elif fsayı == 5:
#     print('5!=',5*4*3*2*1)
# elif fsayı == 6:
#     print('6!=',6*5*4*3*2*1)
# elif fsayı == 7:
#     print('7!=',7*6*5*4*3*2*1)
# elif fsayı == 8:
#     print('8!=',8*7*6*5*4*3*2*1)
# elif fsayı == 9:
#     print('9!=',9*8*7*6*5*4*3*2*1)
# elif fsayı == 10:
#     print('10!=',10*9*8*7*6*5*4*3*2*1)
# elif fsayı == 11:
#     print('11!=',11*10*9*8*7*6*5*4*3*2*1)
# elif fsayı == 12:
#     print('12!=',12*11*10*9*8*7*6*5*4*3*2*1)
# elif fsayı == 13:
#     print('13!=',13*12*11*10*9*8*7*6*5*4*3*2*1)
# elif fsayı == 14:
#     print('14!=',14*13*12*11*10*9*8*7*6*5*4*3*2*1)
# elif fsayı == 15:
#     print('15!=',15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)
# elif fsayı == 16:
#     print('16!=',16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)
# elif fsayı == 17:
#     print('17!=',17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)
# elif fsayı == 18:
#     print('18!=',18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)
# elif fsayı == 19:
#     print('19!=',19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)
# elif fsayı == 20:
#     print('20! =',20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)
# else:
#     print('gerisini hesaplayamıyorum sorry :(')    döngüsüz hal


sayı = int(input('bir sayı girin: '))
a = 1
for faktoriyel in range(sayı):    
    a = a * (faktoriyel+1)
print(a)

