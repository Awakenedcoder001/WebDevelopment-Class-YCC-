d={1: {},  
'name': 'Dell',  
'age': 1, 
'one': [1, 2, 3],  
'person_details': {'name': 'Pemba', 'gender': 'Male', 'age': 37}, 'person1': [{'name': 'T2', 'gender': 'Male', 'age': 90}],  
'person2': [{'name': 'Zangpo', 'gender': 'Male', 'age': 99}], 
'weight':24.5 
} 
 
print(d) 
print(id(d)) 
 
#Deleting using pop() 
#print(d.pop()) --> TypeError 
 
print(d.pop('age')) 
print(d) 
print(id(d)) 
 
#deleting using popitem() 
d.popitem() 
print(d) 
print(id(d)) 
 
# d.popitem('name') --> 0 parameters  
# print(d) 
# print(id(d)) 
 
#Deleting the values using del keyword 
del d['person_details']['name'] 
print(d) 
print(id(d)) 
 
del d['person_details'] 
print(d) 
print(id(d)) 
 
#Updating the values 
d['person1'][0]['name'] = "Tandin Tshewang" 
print(d) 
print(id(d))