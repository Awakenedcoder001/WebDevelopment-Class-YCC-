#Creation: 
d2={} 
print(d2) 
print(type(d2)) 
 
d=dict() 
print(d) 
 
#Homogenous keys: 
d1={1:10,2:20,3:30} 
print(d1) 
 
#heterogenous Basic Keys: 
d3={"name":"Karma","age":90,"weight":105.9,"gender":"Male",1:40,2.2:25.4} 
print(d3) 
 
#Nested dictionary: 
d5={"person1":{"name":"Karma","age":90,"gender":"male"}, 
"person2":{"name":"Thazay Khandu","age":16,"gender":"Male"}} 
print(d5) 
 
# #Advance Data types as Keys: 
# d4={{24,32}:25,[1,2]:24,} 
# print(d4) 
#cannot have a mutabel type as keys
 
# d4={[1,2]:24,{24,32}:25} 
# print(d4) 
#
 
#list of tuples 
d5=dict([(1,1),(2,2),(3,3),(4,5)]) 
print(d5) 
 
d6=dict([("person1",["Karma","Male",90]),("person2",["Sonam","Others",69])]) 
print(d6) 
 
d7=dict([("person1",["Karma","Male",90]),("person2",{"Sonam","Others",69}),("person3",("Jimmy","Others",16))]) 
print(d7)