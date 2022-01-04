Thinley Tobgay, [04.11.21 11:35]
lst=[12,14,18,24]
def reduce_sum(lst1):
 sum=0
 for i in lst1:
  sum=sum+i
 return sum 
res=reduce_sum(lst)
print(res)


from functools import reduce
lst=[12,14,18,24]
reduce_func=reduce(lambda x,y:x+y,lst)
print(reduce_func)
print(type(reduce))