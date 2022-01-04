s1=frozenset({1,2,3,4,5}) 
print(s1) 
print(type(s1)) 
 
# s1.add(99) AttributeError: 'frozenset' object has no attribute 'add' 
# print(s1) 
# print(id(s1)) 
 
# s1.remove(3) AttributeError: 'frozenset' object has no attribute 'remove' 
# print(s1) 
 
#Accessing the elements: 
for i in s1: 
 print(i)