#adding , removing and modifying of Tuple elements: 
tup_5=2,3,7,11,12,19,25 
 
#AttributeError 
tup_5.pop() #'tuple' object has no attribute 'pop' 
tup_5.remove(5) #'tuple' object has no attribute 'remove' 
tup_5.insert(2,3) #'tuple' object has no attribute 'insert' 
tup_5.append(5) #'tuple' object has no attribute 'append' 
 
#TypeError 
tup_5[3]=55 #'tuple' object does not support item assignment 
tup_5[3:5]=55,44 #'tuple' object does not support item assignment