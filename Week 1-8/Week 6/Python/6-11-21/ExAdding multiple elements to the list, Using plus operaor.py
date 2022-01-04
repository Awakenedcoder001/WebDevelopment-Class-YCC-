# + operator 
lst_3=[1,2,3] 
print(id(lst_3)) 
#print(lst_3) 
 
lst_2=[4,5] 
#print(lst_2) 
#print(id(lst_2)) 
 
#Creates a new lsit and assigns it to lst_3 variable 
#lst_3=lst_3+lst_2 
#print(id(lst_3)) 
 
#Adds the list of elements to the same list. 
lst_3+=lst_2 
print(id(lst_3)) 
print(lst_3) 
print(lst_2)