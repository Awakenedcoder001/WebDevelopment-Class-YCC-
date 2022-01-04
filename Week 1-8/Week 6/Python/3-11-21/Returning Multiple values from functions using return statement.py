def add_func(num1,num2):
 return num1+num2
 print(num1+num2) #unreachable statement

res=add_func(10,20)
print(res)

def mathematical_oper(num1,num2):
    sum=num1+num2
    diff=num1-num2
    product=num1*num2
    quotient=5/5
    remainder=num1%num2
    floor_div=5//5 #(floor division)
    expo=num1**num2
    return sum,diff,product,quotient,floor_div,remainder,expo
res=mathematical_oper(10,5)
print(res)