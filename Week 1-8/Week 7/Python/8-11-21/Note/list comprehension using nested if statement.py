lst=range(1,16) 
lst_1=[] 
for i in lst: 
 if i>5: 
  if i%2==0: 
   lst_1.append(i**2) 
 
print(lst_1) 
 
lst_2=[i**2 for i in lst if i>5 if i%2==0] 
print(lst_2)