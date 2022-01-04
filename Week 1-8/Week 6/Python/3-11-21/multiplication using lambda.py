#multiplication table of 18 using lambda
def square(n):
 return lambda x:x**n
res=square(2)
sq=res(4)
print(sq)