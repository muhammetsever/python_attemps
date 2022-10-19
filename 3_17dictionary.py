# # key to vaule çalışır

# #dictionary olmadan nasıl yapılır?

# plakalar = [16,34]
# sehirler = ["Bursa","İstanbul"]

# print(plakalar[sehirler.index("Bursa")]) #şehirleden aldığı indesi plakalrdan da alır

# #print(plakalar["bursa"]) => 16 dictionariy bu işe yarıyor

# plaka ={"Bursa" : 16 , "İstanbul" : 34}
# print(plaka["Bursa"])

# plaka["Ankara"] = 6
# plaka["Adana"] = 1
# print(plaka)

kullanıcılar = {
   "osman": { "age":26,
              "adres":"Bursa",
              "e-posta":"m",
              "telefon":123213213,
              "roles":["admin","user"]
               } ,
    "kerim":{
            "age": 14,
            "adres":"Mudanya",
            "roles":["user"],
            "eposta":"",
            "tel":21321321
    }              
              
}
print(kullanıcılar["osman"])
print(kullanıcılar["kerim"]["adres"])
print(kullanıcılar["osman"]["roles"][0])
