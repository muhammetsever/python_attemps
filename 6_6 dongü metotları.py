# list = [1,2,3]

# for item in list:
#     print(item)  eğer list listesi yoksa;

# for item in range(1,50,2):   # sıfırdan başlar ve 50' ye kadar gider 
#     print(item)             # 1 den başla 50' e kadar git 2 şer olarak art

#enumerate

index = 0 
greeting = 'hello world'
for letter in greeting:    #enumerate olmadan bu şekilde yapılabilir.
    print(f'index: {index} letter: {letter}')  #letter yerine {greeting[index]} yazılabilir
    index += 1 

# greeting = 'hello'
# for index,letter in enumerate(greeting):
#     print(f'index {index} letter {letter}')

list1 = [1,2,3]
list2 =['a','b','c']

# print(list(zip(list1,list2)))

for item in zip(list1,list2):
    print(item)

for a,b in zip(list1,list2):
    print(a,b)