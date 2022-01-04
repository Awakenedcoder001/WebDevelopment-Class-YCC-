import re 
pattern=input("Enter the pattern to be match:") 
string="Code with Keshav Murthy ! Code is Important" 
result=re.findall(pattern,string) 
 
print(result) 
print(len(result))