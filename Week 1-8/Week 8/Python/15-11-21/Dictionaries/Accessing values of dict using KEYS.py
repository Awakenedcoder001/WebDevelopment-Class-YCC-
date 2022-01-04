#cannot access Dict values using index values
d={1: {},  
'name': 'Dell',  
'age': 1, 
'one': [1, 2, 3],  
'person_details': {'name': 'Pemba', 'gender': 'Male', 'age': 37}, 'person1': [{'name': 'T2', 'gender': 'Male', 'age': 90}],  
'person2': [{'name': 'Zangpo', 'gender': 'Male', 'age': 99}] 
} 
 
#print(d) 
print(d["name"]) 
 
#Accessing the entire list  
print(d["one"]) 
 
#Accessing the individual value of the list  
print(d["one"][1]) 
 
#Accessing dictionary value 
print(d["person_details"]) 
 
print(d["person_details"]["gender"]) 
 
print(d["person2"]) 
 
 
print(d["person2"][0]) 
 
 
print(d["person2"][0]["age"])