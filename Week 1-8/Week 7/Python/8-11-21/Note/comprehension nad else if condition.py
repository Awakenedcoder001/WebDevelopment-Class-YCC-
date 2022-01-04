lst=range(1,11) 
lst1=[] 
for i in lst: 
 if i%2==0: 
  lst1.append(i**2) 
 else: 
  lst1.append(i**3) 
print(lst1) 
 
#comprehension: 
lst2=[i**2 if i%2==0 else i**3 for i in lst] 
print(lst2)