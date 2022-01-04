#Create a list of elements from 200-300, preform the square of list using for and comprehension.

lst= range(200,300)
lst1=[]

for i in lst:
    if i%2==0:
        lst1.append(i**2)
print(lst1)


#using comprehension method
lst1 = [i**2 for i in lst if i%2==0]
print(lst1)