#Membership operator: 
#in , not in 
 
d2={1:1,2:2,3:3} 
print(3 in d2.keys()) 
print(3 not in d2.keys()) 
 
print(4 in d2.values()) 
print(1 in d2.values()) 
print(4 not in d2.values()) 
print(1 not in d2.values()) 
 
print((1,1) in d2.items()) 
print((1,2) in d2.items())
print((1,1) not in d2.items()) 
print((1,2) not in d2.items())