lst = list(range(1,11))
print(id(range(1,11))
print(lst)


print(lst.pop(0))
print(id(lst))
print(lst.pop(0))

del lst[-3]
print(lst)
print(id(lst))
