#creating empty set
set_1=set()
print(set_1)
print(type(set_1))
#set elements
#homogeneous data type
set_2={10,20,30,40,50}
print(set_2)
print(type(set_2))
#Hetrogeneous data type
set_3=set({40,True,2+3j,'Tandin',90.4})
print(set_3)
print(type(set_3))
#
set_4={19,False,0,19,True}
print(set_4)
print(type(set_4))
print(id(set_4))
#adding the elements
set_4.add(4)
print(set_4)
print(id(set_4))
#removing the elements
set_4.remove(19)
print(set_4)
print(id(set_4