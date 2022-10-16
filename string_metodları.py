message = "Hello there. My name is Muhammet."

# message = message.upper() tüm harfleri büyütür
# message = message.lower() tüm harfleri küçültür
# message = message.title() kelimelerin baş harfini büyütür
# message = message.capitalize() ilk harfbüyük olur
# message = message.strip() baştaki boşluğu siler
# message = message.split()  #boşlıuklardan bölünür
# # message = message.split(".") noktadan ayırır
# message =" ".join(message) bölünmüşse toparlar
# index =message.find("Muhammet") cümlede kelime aramaya yarar
isFound = message.startswith("H") #belirtilen harf ile mi başladığını sorgular

# isfound = message.endswith(".") belirtilen hafle bittiğini sorgular
# message = message.replace("Muhammet","Osman") yelerine geçer
# message = message.center(50) belirtilen sayıya göre ortalar

print(isFound)
