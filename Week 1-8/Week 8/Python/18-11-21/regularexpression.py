#1.Create a regular expression object 
#2.check the regular expression object in string  
#3.If found print it 
 
import re 
re_obj=input("Enter the string for pattern matching") 
pattern=re.compile(re_obj) 
string=input("Enter the string for pattern matching") 
match=re.finditer(pattern,string) 
for matches in match: 
 print(f'{matches.start()} & {matches.end()} and {matches.group()}')