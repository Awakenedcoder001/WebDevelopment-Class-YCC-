

lst=[[1,2],[3,4]] 
print(lst) 
print(id(lst)) 
 
lst_1=copy.deepcopy(lst) 
print(lst_1) 
print(id(lst_1)) 
 
lst_1.append([5,6]) 
print(lst) 
print(lst_1) 
 
lst_1[1][0]=33 
print(lst_1) 
print(lst) 
 
print(id(lst[0][0])) 
print(id(lst_1[0][0]))