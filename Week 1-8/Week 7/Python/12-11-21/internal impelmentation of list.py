#list data structure 
import sys 
lst=[] 
print(sys.getsizeof(lst)) 
#No. of elements : 0 
#Size of the list is : 56(o.s) 
#It is the size allocated for the list data structure 
#to store the values(It is dependent on the o.s) 
 
lst.append(20) 
print(lst) 
print(sys.getsizeof(lst)) 
#No. of elements : 1 
#Size of the list is : 88 
 
lst.append(30) 
print(lst) 
print(sys.getsizeof(lst)) 
#No. of elements : 2 
#Size of the list is : 88 
 
lst.extend([40,50]) 
print(lst) 
print(sys.getsizeof(lst)) 
#No. of elements : 4 
#Size of the list is : 88 
 
lst.append(60) 
print(lst) 
print(sys.getsizeof(lst)) 
#No. of elements : 5 
#Size of the list is : 120 
 
lst.extend([70,80,90]) 
print(lst) 
print(sys.getsizeof(lst)) 
#No. of elements : 8 
#Size of the list is : 120 
 
lst.append(100) 
print(lst) 
print(sys.getsizeof(lst)) 
#No. of elements : 9 
#Size of the list is : 184 
 
lst.extend([110,120,130,140,150,160,170]) 
print(lst) 
print(sys.getsizeof(lst)) 
#No. of elements : 16 
#Size of the list is : 184 
 
lst.append(180) 
print(lst) 
print(sys.getsizeof(lst)) 
#No. of elements : 17 
#Size of the list is : 248