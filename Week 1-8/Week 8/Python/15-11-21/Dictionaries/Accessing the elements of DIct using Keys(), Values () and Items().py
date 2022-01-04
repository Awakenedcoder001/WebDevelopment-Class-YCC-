person_details={"name":"Pemba", 
    "age":25, 
    "gender":"female", 
    "job":"Business", 
    "status":"complicated"} 
 
print(person_details) 
 
#keys() 
#variablename.keys() 
print(person_details.keys()) #dict_keys([]) 
print(type(person_details.keys())) 
 
for i in person_details.keys(): 
    print(i) 
 
#Using For Loop 
for i in person_details: 
    print(i) 
 
#values: 
#variablename.values() 
print(person_details.values()) 
print(type(person_details.values())) 
 
for i in person_details.values(): 
    print(i) 
 
#Using For Loop 
for i in person_details: 
    print(person_details[i]) 
 
#items() 
#varibalename.items() 
print(person_details.items()) 
print(type(person_details.items())) 
 
for i,j in person_details.items(): 
    print(i,":",j) 
 
#Using For Loop 
for i in person_details: 
    print(i,":",person_details[i])