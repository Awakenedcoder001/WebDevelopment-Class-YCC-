d={} 
print(d) 
print(id(d)) 
 
#adding single values
#direcly adding method(Only works for empty dicts)
#Adding elements using Key values
#values can be duplicate 
d[1]=[1,2,3] 
print(d) 
print(id(d)) 
 
d[1]=[1,2,3,4] 
print(d) 
print(id(d)) 

#Multiple key:values
#d.update method
#multiple values 
d.update({"name":"Dell","age":1}) 
print(d) 
print(id(d)) 
 
d.update(one=[1,2,3],person_details={"name":"Pemba","gender":"Male","age":37}) 
print(id(d)) 
print(d) 
 
d.update([("person1",[{"name":"T2","gender":"Male","age":90}]),("person2",[{"name":"Zangpo","gender":"Male","age":99}])]) 
print(d) 
print(id(d))