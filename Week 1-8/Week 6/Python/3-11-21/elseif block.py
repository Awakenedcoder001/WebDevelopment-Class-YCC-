#program to find the largest of three numbers

a=10
b=45
c=18

if a>b and a>c:
 print("INSIDE IF BLOCK")
 print(a,"is the largest number among",a,b,c)

elif b>c:
 print("INSIDE elif BLOCK")
 print(b,"is the largest number among",a,b,c)

else:
 print("INSIDE ELSE BLOCK")
 print(c,"is the largest number among",a,b,c)