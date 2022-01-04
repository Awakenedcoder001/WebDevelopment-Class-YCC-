import re 
pattern=input("Enter the pattern to be match:") 
string="Karma Is Small !His Age is 90! His Number is 77292950" 
replament_string="@" 
result=re.sub(pattern,replament_string,string) 
print(result) 
 
 
# Output 
# D:\Python>python sub.py 
# Enter the pattern to be match:[0-9] 
# Karma Is Small !His Age is @@! His Number is @@@@@@@@ 
 
# D:\Python>python sub.py 
# Enter the pattern to be match:\d 
# Karma Is Small !His Age is @@! His Number is @@@@@@@@ 
 
# D:\Python>python sub.py 
# Enter the pattern to be match:[a-zA-Z] 
# @@@@@ @@ @@@@@ !@@@ @@@ @@ 90! @@@ @@@@@@ @@ 77292950 
 
# D:\Python>python sub.py 
# Enter the pattern to be match:\w 
# @@@@@ @@ @@@@@ !@@@ @@@ @@ @@! @@@ @@@@@@ @@ @@@@@@@@ 
 
# D:\Python>python sub.py 
# Enter the pattern to be match:. 
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@