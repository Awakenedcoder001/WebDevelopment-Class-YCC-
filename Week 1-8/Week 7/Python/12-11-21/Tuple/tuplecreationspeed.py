import timeit
print(timeit.timeit(stmt= "tup=(1,2,3,4,5,6)", number=100000))
print(timeit.timeit(stmt= "lst=[1,2,3,4,5,6]", number=100000))