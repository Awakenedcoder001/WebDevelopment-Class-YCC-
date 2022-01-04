x=10 
print(f"Value of x before changing is : {x} ") 
 
def func(): 
    global x 
 # x=x+1 
    x+=10 #x=10+10 
    print(f"Value of x After changing is : {x} Inside the Function") 
 
func() 
print(f"Value of x After changing is : {x} Outside the Function")