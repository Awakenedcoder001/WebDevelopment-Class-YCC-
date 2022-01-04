passwordlocker= {10,30,40,50,70,"tenzin"}
s1 = input("Enter your pasword : ") #string type

#covert string to integer and check the datatype
if type(int(s1)) == int or s1==str:
    if s1 in passwordlocker:
        print("Welcome")

    elif int(s1) in passwordlocker:
        print("Welcome")
    else:
        print("Get Lost")
else:
    print("Get Lost")



