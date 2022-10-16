# def sayHello(name='user'):
#     print('hello '+ name)


# sayHello("osman")
# sayHello()


from re import S


def sayHello(name='user'):
    return 'hello '+ name

msg = sayHello("Muh")

print(msg)

def total(num1,num2):
    return num1 + num2

resoult = total(10,20)

print(resoult)

def yashesapla(dogum):
    return 2022 - dogum

# yas = yashesapla()
# print(yas)

def emekliligekacyilkaldi(dogumyili , isim):
    '''
    DOCSTRİNG: Bu uygulama emeklilik yasini tahmin etmek icin yazildi.
    INPUT:Dogum yiliniz , isim.
    OUTPUT:Emeklilik yasiniza kac yil kaldığı.
    '''
    yas = yashesapla(dogumyili)
    emeklilik = 65-yas
    if emeklilik > 0:
        print(f'emekliliğe {emeklilik} yıl kaldı.')
    else:
        print('zaten emekli oldunuz.')
    return
print(help(emekliligekacyilkaldi))
yıl=int(input("doğum yılı: "))

emekli = emekliligekacyilkaldi(yıl,'muh')
# print(emekli)