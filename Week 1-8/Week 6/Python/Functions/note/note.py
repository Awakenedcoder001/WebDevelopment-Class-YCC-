Thinley Tobgay, [01.11.21 15:50]
def power_of(num1,num2):
    res_1=num1**num2
 print(res_1)
power_of(2,5)
power_of(5,2)

Thinley Tobgay, [01.11.21 15:51]
def power_of(num1=1,num2=1):
 res_1=num1**num2
 print(res_1)
#zero numbers of arguments
power_of()
#passing one arguments
power_of(5)
#passing two arguments
power_of(2,3)

def power_of(num1,num2=1):
 res_1=num1**num2
 print(res_1)

#passing one arguments
power_of(5)
#passing two arguments
power_of(2,3)

#non default argument should never follow default 
#argument. if you does not follow it will result 
#into an error

def power_of(num1=1,num2):
 res_1=num1**num2
 print(res_1)

#passing one arguments
power_of(5)
#passing two arguments
power_of(2,3)