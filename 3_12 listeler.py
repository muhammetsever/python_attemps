# message = "Hello there. My name is Muhammet!".split() #splitle ayırığımız için 0 index hello olur
# #split le ayırmazsak 0 index H olur
# print(message[0])

# my_list = [1,2,3]
# my_list = ["bir",2,True,5.6]
# print(my_list)

list1 = ['one', 'two' , 'there']
list2 = ["four","five","six"]

t = list1 + list2


print(t[0])

userA = ["Osman",26]
userB = ["Kerim",14]

#users = userA + userB

users = [userA , userB] # liste içinde liste userA=0 userB=1

print(userA)
print(userB)
print(users)

print(users[1][0]) # userA yı bulur ("osman",26) onun içinden 0'ı alır osman a