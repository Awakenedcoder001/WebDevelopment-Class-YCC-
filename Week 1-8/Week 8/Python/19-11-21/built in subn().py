
import re 
pattern=input("Enter the pattern to be match:") 
string="Karma Is Small !His Age is 90! His Number is 77292950" 
replament_string="@" 
result=re.subn(pattern,replament_string,string) 
print(result)


Enter the pattern to be match:\d 
('Karma Is Small !His Age is @@! His Number is @@@@@@@@', 10) 
 

Enter the pattern to be match:[a-z] 
('K@@@@ I@ S@@@@ !H@@ A@@ @@ 90! H@@ N@@@@@ @@ 77292950', 24)