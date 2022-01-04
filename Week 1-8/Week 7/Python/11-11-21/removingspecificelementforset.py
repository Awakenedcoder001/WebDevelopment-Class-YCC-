#removing sepecific elememnts from the set 
s1={2,4,6,8,7,11} 
for i in s1: 
 if i==6: 
  s1.remove(i) 
  break; 
print(s1)