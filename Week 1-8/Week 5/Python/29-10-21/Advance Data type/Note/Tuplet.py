#creating two empty tuple
tup=()
print(type(tup))
print(tup)
tup_1=tuple()
print(tup_1)
print(type(tup_1))
#homogenous type
tup_2=19, 49, 59, 69, 79
print(type(tup_2))
print(tup_2)
#Hetrogenous type
tup_3=('Tandin',30,66.6,False,'B+ve')
print(tup_3)
print(type(tup_3))
#Accessing Single elements
print(tup_3[3]) #using +ve indexing
print(tup_3[-2]) #using -ve indexing
#removing the elements
tup_3.remove(30)
#adding the elements 
tup_3.append(50)
#AttributeError: 'tuple' object has no attribute 'append'