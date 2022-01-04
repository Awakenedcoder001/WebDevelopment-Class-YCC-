lst=range(1,11)
lst1=[]

for i in lst:
    if i%2==0:
        lst1.append(i**2)
    else:
        lst1.append(i**3)
print(lst1)
        

#using Comprehension
lst1 = [i**2 if i%2==0 else i%3==0 for i in lst1]
print(lst1)