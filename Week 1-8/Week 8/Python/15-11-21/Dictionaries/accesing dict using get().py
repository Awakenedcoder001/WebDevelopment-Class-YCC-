d={1:"one",2:"two",3:"three",4:"four"} 
print(d) 
print(d.get(2)) 
 
print(d.get(5)) #--> None 
print(d[5]) #--> KeyError