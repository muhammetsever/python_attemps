x = 6

hak = 5
devam = 'e'
# resoult = 5< x <10

# print(resoult)      # her zaman böyle yapamacağımız için:

#and

# --> True ve True => True
# --> True ve False => False    mantıkta ve bağlacı

resoult = (x > 6) and (x < 10)
oyunşısi=(hak > 0) and (devam == 'e')
print(resoult)
print(oyunşısi)


#or

# --> True veya True => True
# --> True veya False => True    mantıkta ki veya bağlacı 
# --> False veya False => False

resoult= (x > 0) or (x%2 == 0)

print(resoult)

#not    tam tersini alır


resoult= not(x>0)
print(resoult)