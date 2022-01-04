Thinley Tobgay, [03.11.21 14:47]
#user-defined
def adding(num1,num2):
 return num1+num2
res=adding(3,4)
print(res)

#using lambda
res=(lambda num1,num2:num1+num2)(3,4)
print(res)

Thinley Tobgay, [03.11.21 15:00]
#using lambda
res=(lambda num1,num2:num1+num2)
print(res)

res_2=res(3,4)
print(res_2)

res_2=res(4,4)
print(res_2)