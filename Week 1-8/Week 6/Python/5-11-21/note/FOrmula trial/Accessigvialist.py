#Accessing Single elements from the list:
lst_4=[[1,2],(3,4),{4,5},{"name":"Pema Choda","gender":"Male"}]

#accessing Tuple from the list:
print(lst_4[1])

#accessing indvidual elements of tuple from the list'
for i in lst_4[1]:
 print(i)

#Accesing list from the list:
print(lst_4[0])

#accessing indvidual elements of list from the list'
for i in lst_4[0]:
 print(i)

#accesing the set from the list:
print(lst_4[2])

#accessing the dictionary from the list:
print(lst_4[-1])

#accesing the individual elements from the dictionary from the list:
for i in lst_4[-1]:
 print(i,":",lst_4[-1][i])