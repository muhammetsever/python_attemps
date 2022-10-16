meyveler={"portakal", "elma","muz"}

# print(meyveler[0]) indexlenemez

for x in meyveler:
    print(x)

meyveler.add('cilek')
print(meyveler)

meyveler.update(["mango","greyfurt","elma"])
print(meyveler)

# mylist = [1,1,2,3,4,5]
# print(set(mylist))

meyveler.remove("greyfurt")
print(meyveler)