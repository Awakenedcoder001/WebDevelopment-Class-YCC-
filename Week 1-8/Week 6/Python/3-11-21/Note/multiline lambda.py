#user-defined
def adding(num1,num2):
 print("SUM IS : ",end=" ")
 return num1+num2
res=adding(3,4)
print(res)

#using lambda
res=(lambda num1,num2: num1+num2)
print(res(3,4))

res=(lambda num1,num2: print("SUM IS:"), num1+num2)
print(res)