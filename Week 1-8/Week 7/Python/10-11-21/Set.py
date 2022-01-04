#Creation of sets: 
#empty set 
set_1=set() 
print(type(set_1)) 
print(set_1) 
 
#Homogenous  
set_2={10,20,30,40} 
print(set_2) 
 
#Heterogenous 
set_3={"ABC",True,4,36.5,2+3j,69} 
print(set_3) 
 
 
#Advance Data type: TypeError: unhashable type: first mutable datatype 
set_5={10,(20,30,40),([10,20,30],)} 
print(set_5) 
 
#Advance data types --> TypeError: unhashable type: first mutable datatype 
set_5={10,(20,30,40),{1:1,2:2},[10,20,30]} 
print(set_5) 
 
#Nested Sets: 
set_4={{1,2,3},{4,5,6}} 
print(set_4)