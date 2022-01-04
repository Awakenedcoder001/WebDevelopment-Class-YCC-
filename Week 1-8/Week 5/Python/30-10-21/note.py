Thinley Tobgay, [30.10.21 10:47]
num1=20
#create different objects (use same address in memory segments)
num2=49
num3=49
print(num1)
print(id(num1))
print(num2)
print(id(num2))
print(num3)
print(id(num3))

Thinley Tobgay, [30.10.21 10:47]
#create same objects (use different address in the memory segments)
num1=20
print(num1)
print(id(num1))
num1=30
print(num1)
print(id(num1))