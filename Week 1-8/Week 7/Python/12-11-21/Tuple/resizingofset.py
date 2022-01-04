import sys 
s=set() 
print(sys.getsizeof(s)) 
#No of elements :0 
#size of set:216[Based on OS] 
 
s.add(1) 
print(sys.getsizeof(s)) 
#No of elements:1 
#size of set:216 
 
s.update([2,3,4]) 
print(sys.getsizeof(s)) 
#No of elements:4 
#size of set:216 
 
s.add(5) 
print(sys.getsizeof(s)) 
#No of elements:5 
#size of set:728 
 
#print(728/216) 
 
s.update([6,7,8,9,10,11,12,13,14,15,16,17,18]) 
print(sys.getsizeof(s)) 
#No of elements:14 
#size of set:728 
 
s.add(19) 
print(sys.getsizeof(s)) 
#No of elements:19 
#size of set:2264 
 
lst=list(range(20,77)) 
s.update(lst) 
print(sys.getsizeof(s)) 
#No of elements:76 
#size of set:2264 
 
s.add(77) 
print(sys.getsizeof(s)) 
#No of elements:77 
#size of set:8408