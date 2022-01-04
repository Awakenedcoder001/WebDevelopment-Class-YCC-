def outer(): 
    x=10 
    y=20 
    def inner(): 
        nonlocal x,y 
        x+=10 
        y+=10 
        print(x)    
        print(y) 
    inner() 
outer()