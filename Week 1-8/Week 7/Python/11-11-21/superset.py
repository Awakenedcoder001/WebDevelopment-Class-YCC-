#Superset

s1={1,2,3,4,5} 
s2={4,5,6,7} 
print(s1.issuperset(s2)) 
print(s2.issuperset(s1)) 
 
print(s1 >= s2) 
print(s2 >= s1) 
 
s1={1,2,3,4,5} 
s2={3,4,5} 
print(s1.issuperset(s2)) 
print(s2.issuperset(s1)) 
 
print(s1 >= s2) 
print(s2 >= s1) 
 
s1={1,2,3,4,5} 
s2={1,2,3,4,5} 
print(s1.issuperset(s2)) 
print(s2.issuperset(s1)) 
 
print(s1 >= s2) 
print(s2 >= s1)