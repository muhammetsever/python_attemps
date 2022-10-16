"""
    öğrenciler= {
        "120":{
            "ad" : "Ali",
            "soyad":"Yılmaz",
            "telefon":"532 000 0001"
        },
        "125":{
            "ad":"Can",
            "soyad":"Korkmaz",
            "telefon":"533 000 0002"
        },
        "128":{
            "ad":"Volkan"
            "soyad":"Yükselen"
            "telefon":"534 000 0003"
        },
    }

1- Bilgileri verilen öğrencileri kulanıcıdan aldığınız veriler ile saklayın

2- Öğrenci numarasını kullanıcıdan alıp kullanıcıya gösterin
"""

# ad1 =input("Öğrencinin ad bilgisini girin 120: ")
# soyad1 = input("Öğrencinin soyad bilgisini girin 120: ")
# tel1 = input("Öğrencinin telefon bilgisini girin 120: ")

# ad2 = input("Öğrencinin ad bilgisini girin 125: ")
# soyad2 = input("Öğrencinin soyad bilgisini girin 125: ")
# tel2 = input("Öğrencinin telefon bilgisini girin 125: ")

# ad3 = input("Öğrencinin ad bilgisini girin 128: ")
# soyad3 = input("Öğrencinin soyad bilgisini girin 128: ")
# tel3 = input("Öğrencinin telefon bilgisini girin 128: ")





# öğrenciler = {
#     120:{
#         "ad":ad1,
#         "soyad":soyad1,
#         "telefon":tel1
#     },
#     125:{
#         "ad":ad2,
#         "soyad":soyad2,
#         "telefon":tel2
#         },

#     128:{
#         "ad" : ad3,
#         "soyad":soyad3,
#         "telefon":tel3
#     }
# }    bunlar benim yaptığım

öğrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

# öğrenciler[number] ={
#     "ad":name,
#     "soyad":surname,
#     "telefon":phone

# }
# print(öğrenciler)

öğrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "tel":phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

öğrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "tel":phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

öğrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "tel":phone
    }
})


# print(öğrenciler)

# ogrNo = input("öğrenci no:")
# öğrenci = öğrenciler[ogrNo]

# print(öğrenci)

print("*"*50)

ogrNo = input("öğrenci no:")
öğrenci = öğrenciler[ogrNo]

print(f"aradığınız {ogrNo} lu öğrencinin adı: {öğrenci['ad']} soyadı: {öğrenci['soyad']} telefon numarası ise: {öğrenci['tel']}")