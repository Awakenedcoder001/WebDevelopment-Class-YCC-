def outer(): 
    x=10 
    def inner(): 
    print(x) 
    inner() 
  outer() 
 
def outer(): #2 
    x=10 #3 --> local variable for outer function 
    def inner(): #5 
    x=20 #6 
    print(x) #7 --> local variable for inner function 
    inner() #4 #8 
    print(x) #9 
outer() #1 #10