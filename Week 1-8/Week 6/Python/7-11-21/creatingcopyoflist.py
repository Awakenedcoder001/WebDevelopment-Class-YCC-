lst=[1,2,3,4,5] 
print(lst) 
print(id(lst)) 
 
lst_1=list(lst) 
print(lst_1) 
print(id(lst_1)) 
 
lst_1.append(6) 
print(lst_1) 
print(lst_1) 
 
lst_1=lst[::] 
print(lst_1) 
print(id(lst_1))