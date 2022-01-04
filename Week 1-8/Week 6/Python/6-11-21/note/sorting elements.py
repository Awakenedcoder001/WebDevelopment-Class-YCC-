Chedup Wangchuk, [06.11.21 12:13]
lst=[1,2,3,4,5] 
print(lst) 
lst[2]=33 
print(lst) 
 
#Modifying Multiple elements in a list 
lst[1:-1]=[22,333,44] 
print(lst) 
print(id(lst)) 
 
lst[1:-1]=[222,3333] 
print(lst) 
print(id(lst)) 
 
lst[1:-1]=[222,3333,44,55] 
print(lst) 
print(id(lst)) 
 
#Sorting the list elements in ascending and descending 
lst=[3,22,7,54,49,17,13] 
print(lst) 
 
#Ascending order 
print(sorted(lst)) 
 
#Descending Order 
lst_1=sorted(lst) 
print(lst_1) 
print(lst_1[::-1]) 
 
#Using sorted and reverse=True 
print(sorted(lst,reverse=True))

Chedup Wangchuk, [06.11.21 12:13]
#Removing the element based on index value 
#pop() --> optional parameter 
 
print(lst.pop()) 
print(id(lst)) 
print(lst) 
 
print(lst.pop(0)) 
print(id(lst)) 
print(lst) 
 
#IndexError:  
# print(lst.pop(17)) 
# print(id(lst)) 
# print(lst) 
 
#Using del keyword 
del lst[-3] 
print(lst) 
print(id(lst)) 
 
#Deleting multiple elements from the list 
lst_2=list(range(1,21)) 
print(lst_2) 
 
#10-15 
del lst_2[9:15] 
print(lst_2)