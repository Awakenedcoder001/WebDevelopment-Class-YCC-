#create a list of number of elemnts from 1-15, while 15 is inclusinve.preform square operation if number is greater than 5
lst = range(1,16)
lst1=[]

for i in lst:
    if i>5:
        if i%2==0:
            lst1.append(i**2)
print(lst1)

lst_2=[i**2 for i in lst if i>5 if i%2==0] 
print(lst_2)
