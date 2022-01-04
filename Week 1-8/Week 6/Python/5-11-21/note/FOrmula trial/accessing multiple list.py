lst=[1,66,88,4,14,24,6] 
 
#Accessing 88,4,14 from list 
lst_1=lst[2:-2] 
print(lst_1) 
 
lst_1=lst[2:5] 
print(lst_1) 
 
lst_1=lst[-5:-2] 
print(lst_1) 
 
#Accessing 6,14,88,1 from list 
print(lst[6: :-2]) 
print(lst[-1: :-2]) 
 
#Accessing all the element from the list 
#lst_3=lst[0::1] 
lst_3=lst[::] 
print(lst_3)