list_1=[]
print(type(list_1))
print(list_1)

list_2=list()
print(type(list_2))
print(list_2)

list_3 =[20, 11, 6, 17, 34]
print(list_3)
print(type(list_3))

list_4=[13,19.3, 3+2j, 'pema', True]
print(list_4)
print(type(list_4))
print(id(list_4))

#adding elements to the list
list_4.append(False)
print(id(list_4))
print(list_4)


#accessing individual elements 
print(list_4[3])
print(list_4[3][1])

#Removing individual elements from the list
list_4.remove('pema')
print(id(list_4))