import re
Gojay=input("Enter the Data to be searched for : ")
Changzay=input("Enter the string : ")
gojay_Changzay=re.finditer(Gojay,Changzay)
print (gojay_Changzay)
for lagar in gojay_Changzay:
    print(f'{lagar.start()} & {lagar.end()} and {lagar.group()}')
