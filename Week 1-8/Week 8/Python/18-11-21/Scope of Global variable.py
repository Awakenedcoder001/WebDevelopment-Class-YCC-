#Scope of Global Variable 
x=10 
def dorji(): 
 print(x) 
dorji() 
print(x) 
 
#Scope of local and global Variables 
x=10 
def dorji(): 
 x=20 
 print(x) 
dorji() 
print(x)