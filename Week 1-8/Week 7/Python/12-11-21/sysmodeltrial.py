import sys
lst= []
print(sys.getsizeof(lst))
#No of elements = 0
#size of list =  56
print(lst)

lst.append(10)
print(lst)
print(sys.getsizeof(lst))
#No of elements= 1
#size of lst= 88

lst.extend([20,30,40])
print(lst)
print(sys.getsizeof(lst))
#No of elements : 1+3 = 4
#Size of list = 88

lst.extend([50,60,70,80])
print(lst)
print(sys.getsizeof(lst))
#no of elements = 4+ 4 = 8
#size of element= 152

lst.append(99)
print(lst)
print(sys.getsizeof(lst))
#no of elements : 8 +1 = 9
#size of element= 152
lst.append(100)
print(lst)
print(sys.getsizeof(lst))
