#Inserting: 
#list and set 
print(timeit.timeit(stmt="lst.append(7)",setup="lst=[1,2,3,4,5,6]",number=100000)) 
print(timeit.timeit(stmt="s.add(7)",setup="s={1,2,3,4,5,6}",number=100000))