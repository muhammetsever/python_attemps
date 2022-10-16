# x = 5
# y = 10
# z = 20

# x,y,z = 5,10,20

# x, y = y, x

# x = x+5
# x += 5  #x=x+5
# x -= 5  #x=x-5

# x*=5
# x/=5
# x//=5
# x%=5
# x**=5

# print(x ,y ,z)


values = 1, 2, 3, 4, 5


x,y,*z = values      #valuesdeki 1 2 ve 3 x y z ye geçti  yıldız bir küme oluştrdu ve 4 5'i aldı

print(x,y,z)
print(type(values))