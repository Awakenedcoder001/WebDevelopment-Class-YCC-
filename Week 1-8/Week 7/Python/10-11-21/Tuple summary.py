#Craetion of a tuple: 
#Empty: 
tup=() 
print(tup) 
print(type(tup)) 
 
tup_1=tuple() 
print(tup_1) 
print(type(tup_1)) 
 
#Homogenous: 
tup_3=4,8,16,24,22 
print(tup_3) 
print(type(tup_3)) 
 
#Heterogenous 
tup_2=(69,2+3j,"abc",True,35.5) 
print(tup_2) 
print(type(tup_2)) 
 
#Advance Type 
#Nested tuple 
tup_4=((10,20),(30,40)) 
print(tup_4) 
print(type(tup_4)) 
 
tup_5=([10,20],(30,40),{50,60},{"name":"Pema","gender":"Male"}) 
print(tup_5) 
print(type(tup_5))