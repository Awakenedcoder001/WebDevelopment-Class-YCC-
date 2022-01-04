#create a list of elements from 100-112 and 112 should be included. Preform the cube operation on the list using for loop and comprehension.

lst=range(100,113)
lst_1=[]

for i in lst:
    lst_1.append(i**3)
print(lst_1)


lst_2= [i**3 for i in lst]
print(lst_2)
