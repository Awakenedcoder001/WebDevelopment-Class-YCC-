import timeit 
 
print(timeit.timeit(stmt="lst.append(6)",setup="lst=[1,2,3,4,5]",number=100000)) 
print(timeit.timeit(stmt="lst.insert(2,6)",setup="lst=[1,2,3,4,5]",number=100000)) 
print(timeit.timeit(stmt="lst.insert(0,6)",setup="lst=[1,2,3,4,5]",number=100000))