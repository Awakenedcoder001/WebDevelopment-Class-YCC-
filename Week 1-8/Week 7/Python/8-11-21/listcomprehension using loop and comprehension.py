lst = [1,2,3,4,5]
lst_1=[]


for i in lst:
    lst_1.append(i**2)
    print(lst_1)


lst2= [i**2 for i in lst]
print(lst2)