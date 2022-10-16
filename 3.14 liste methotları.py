numbers = [1 , 10 , 5 , 16 , 4 , 9 , 10]
letters = ["a" , "g" , "s" , "b" , "y" , "a" , "s"] 

val = max(numbers)
val1 = min(numbers)
print(val)
print(val1)
val2 = max(letters)
val3 = min(letters)
print(val2)
print(val3)
val4 = numbers[3:6]
print(val4)
val5 = numbers[:3]
print(val5)
numbers[4] = 40
print(numbers)

numbers.append(49)
print(numbers)
numbers.insert(5, 78)
print(numbers)

#numbers.pop()
#numbers.pop(3)
#numbers.remove(1)

numbers.sort()
letters.sort()
numbers.reverse()
print(numbers)
print(letters)
print(len(numbers))

print(numbers.count(10))

numbers.clear()
print(numbers)