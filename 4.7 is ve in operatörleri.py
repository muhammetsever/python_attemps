#İdentity operator is:

# x = y = [1,2,3]
# z = [1,2,3]

# print(x==y)
# print(x==z)
# print(x is y)
# print(x is z)

x = [1,2,3]
y= [2,4]

del x[2]
y[1]=1 
y.reverse()
print(x==y)
print(x is y) # aynı adreste olmadıkları için false aynı adreste olsalardı true çıkardı

print(x is not y)

#Membership opretor in:


x = ['apple','banana']
print ('banana' in x)

name = 'osman'
print('o' in name)
print('c' not in name)