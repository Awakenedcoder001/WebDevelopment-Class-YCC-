import re 
re_obj=input("Enter the string for pattern matching") 
#pattern=re.compile(re_obj) 
string=input("Enter the string for pattern matching") 
match=re.finditer(re_obj,string) 
for matches in match: 
 print(f'{matches.start()} & {matches.end()} and {matches.group()}')