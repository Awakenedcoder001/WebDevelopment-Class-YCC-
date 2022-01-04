import re 
gojay=input("Enter the pattern to be match:") 
changzay=input("Enter the string:") 
gojay_changzay=re.finditer(gojay,changzay) 
print(gojay_changzay) 
for i in gojay_changzay: 
 print(f'{i.start()} & {i.end()} and {i.group()}') 
 
#output 
 
# D:\Python>python quantifiers.py 
# Enter the pattern to be match:a+ 
# Enter the string:abababbaaaabbb 
# <callable_iterator object at 0x0000024743427CA0> 
# 0 & 1 and a 
# 2 & 3 and a 
# 4 & 5 and a 
# 7 & 11 and aaaa 
 
# D:\Python>python quantifiers.py 
# Enter the pattern to be match:a* 
# Enter the string:abababbaccaaddacbbdb 
# <callable_iterator object at 0x000001EBF6147CA0> 
# 0 & 1 and a 
# 1 & 1 and 
# 2 & 3 and a 
# 3 & 3 and 
# 4 & 5 and a 
# 5 & 5 and 
# 6 & 6 and 
# 7 & 8 and a 
# 8 & 8 and 
# 9 & 9 and 
# 10 & 12 and aa 
# 12 & 12 and 
# 13 & 13 and 
# 14 & 15 and a 
# 15 & 15 and 
# 16 & 16 and 
# 17 & 17 and 
# 18 & 18 and 
# 19 & 19 and 
# 20 & 20 and 
 
# D:\Python>python quantifiers.py 
# Enter the pattern to be match:a? 
# Enter the string:abababbaccaaddacbbdb 
# <callable_iterator object at 0x000001E72AD07CA0> 
# 0 & 1 and a 
# 1 & 1 and 
# 2 & 3 and a 
# 3 & 3 and 
# 4 & 5 and a 
# 5 & 5 and 
# 6 & 6 and 
# 7 & 8 and a 
# 8 & 8 and 
# 9 & 9 and 
# 10 & 11 and a 
# 11 & 12 and a 
# 12 & 12 and 
# 13 & 13 and 
# 14 & 15 and a 
# 15 & 15 and 
# 16 & 16 and 
# 17 & 17 and 
# 18 & 18 and 
# 19 & 19 and 
# 20 & 20 and 
 
# D:\Python>python quantifiers.py 
# Enter the pattern to be match:a{2} 
# Enter the string:abababbaccaaddacbbdb 
# <callable_iterator object at 0x000001F09B4E7CA0> 
# 10 & 12 and aa 
 
# D:\Python>python quantifiers.py 
# Enter the pattern to be match:a{2} 
# Enter the string:abaababbaaaaddaaabbdb 
# <callable_iterator object at 0x000002F9855E7CA0> 
# 2 & 4 and aa 
# 8 & 10 and aa 
# 10 & 12 and aa 
# 14 & 16 and aa 
 
# D:\Python>python quantifiers.py 
# Enter the pattern to be match:a{1,3} 
# Enter the string:abaababbaaaaddaaabbdb 
# <callable_iterator object at 0x000001FFBB397CA0> 
# 0 & 1 and a 
# 2 & 4 and aa 
# 5 & 6 and a 
# 8 & 11 and aaa 
# 11 & 12 and a 
# 14 & 17 and aaa