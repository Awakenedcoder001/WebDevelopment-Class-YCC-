#Creating a copy of tuple: 
#Shallow copy 
tup_5=2,3,7,11,12,19,25 
print(tup_5) 
print(id(tup_5)) 
 
tup_6=tuple(tup_5) 
print(tup_6) 
print(id(tup_6)) 
 
#Deepcopy: 
import copy 
tup_5=2,3,7,11,12,19,25 
print(tup_5) 
print(id(tup_5)) 
 
tup_6=copy.deepcopy(tup_5) 
print(tup_6) 
print(id(tup_6))