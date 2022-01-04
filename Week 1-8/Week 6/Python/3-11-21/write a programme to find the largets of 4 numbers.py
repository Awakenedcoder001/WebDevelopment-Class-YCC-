a = 88
b = 27
c = 44
d = 0

if a > b and a > c and a > d :
    print("IN the IF SECTION PART 1")
    print(a,"is the largest number from",a,b,c,d)
elif b > a and b > c and b > d:
    print("INSIDE THE ELIF SECTION")
    print(b,"is the larger number amongst the",a,b,c,d)
elif c > a and c > b and c > d:
    print("Inside the ELIF part2 SECTION")
    print(c,"is the largest number amongst the rest",a,b,c,d)
else:
    print("LAST BLOCK OF ELSE")
    print(d,"is Smallest number",a,b,c,d)

