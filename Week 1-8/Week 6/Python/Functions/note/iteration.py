#iterating the list object using for loop
lst=[1,2,3]
for i in lst:
 print(i)

#iterating over the range object using forloop
for i in range(1,5):
 print(i)


#iterating over the tuple object using forloop
for i in tuple(range(1,5)):
 print(i)



#iterating over the set object using forloop
for i in set(range(1,5)):
 print(i)

dict_1={'name':'pema','age':35,'weight':100}
for i in dict_1:
 print(i,':',dict_1[i])