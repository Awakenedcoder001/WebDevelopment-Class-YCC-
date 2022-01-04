a = 10
b = 20
c = 30
#Default
print("The Value of a is:",a,"The Value of b is:",b,"The Value of c is:",c)

#Using {}
print("The value of a is : {} b is : {} c is : {}".format(a,b,c))

#Positional Formatting
a = "Tandin"
b = "Tshewang"
c = "Code with"
print("{fname} {lname} {initil}".format(fname=a,lname=b,initil=c))


#Other Positional Formatting
b = "Tandin"
a = "Tshewang"
c = "Code with"
d = "30$"
e = "at"
f = "in a month"
print("{title} {fname} {lanme} {initil} {salary} {vllage} ".format(fname=b,lanme=a,title=c,initil=e,salary=d,vllage=f,))


#Simple positional formattings
b = "Tandin"
a = "Tshewang"
c = "Code with"
d = "30$"
e = "at"
f = "in a month"
print("{2} {1} {0} {4} {3} {5}".format(a,b,c,d,e,f))