import re 
pattern=input("Enter the pattern to be match:") 
string="Code with Keshav Murthy" 
result=re.search(pattern,string) 
if result is not None: 
 print("pattern matched") 
 print(f'{result.start()} ..{result.end()} ..{result.group()}') 
else: 
 print('pattern not matched') 
 
#output: 
 

# Enter the pattern to be match:with 
# pattern matched 
# 5 ..9 ..with 
 

# Enter the pattern to be match:^with 
# pattern not matched 
 

# Enter the pattern to be match:^Code 
# pattern matched 
# 0 ..4 ..Code 
 

# Enter the pattern to be match:Murthy$ 
# pattern matched 
# 17 ..23 ..Murthy 
 

# Enter the pattern to be match:with$ 
# pattern not matched   