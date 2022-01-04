import re 
pattern=input("Enter the pattern to be match:") 
string="Code with Keshav Murthy" 
result=re.match(pattern,string) 
if result is not None: 
 print("pattern matched") 
 print(f'{result.start()} ..{result.end()} ..{result.group()}') 
else: 
 print('pattern not matched') 
#output 
# D:\Python>python "builtin(method).py" 
# Enter the pattern to be match:Code 
# pattern matched 
# 0 ..4 ..Code 
 
# D:\Python>python "builtin(method).py" 
# Enter the pattern to be match:code 
# pattern not matched