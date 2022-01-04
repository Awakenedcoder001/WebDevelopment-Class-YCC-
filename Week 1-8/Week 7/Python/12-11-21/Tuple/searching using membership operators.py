#Searching: 
print(timeit.timeit(stmt="5 in lst",setup="lst=[1,2,3,4,5,6,7,8,9,10]",number=100000)) 
print(timeit.timeit(stmt="5 in tup",setup="tup=(1,2,3,4,5,6,7,8,9,10)",number=100000)) 
print(timeit.timeit(stmt="5 in s",setup="s={1,2,3,4,5,6,7,8,9,10}",number=100000))