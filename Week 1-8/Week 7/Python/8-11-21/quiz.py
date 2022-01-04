#Reverse the given list in Python
aLsit = [100, 200, 300, 400, 500]
aLsit.sort(reverse=True)
print(aLsit)

#Concatenate two lists in Python with +index
lst1= ["M", "na","i","ke"]
lst2=["y","me","s","lly"]
lst3 =(lst1[0]+ lst2[0]) + " " +(lst1[1]+lst2[1]) + " " + (lst1[2]+lst2[2]) + " " + (lst1[3]+lst2[3])
print(lst3)

#Concatenate two lists in Python with -index
lst1= ["M", "na","i","ke"]
lst2=["y","me","s","lly"]
lst3=(lst1[-4]+lst2[-4]) + " " + (lst1[-3]+lst2[-3]) + " " + (lst1[-2]+lst2[-2]) + " " +(lst1[-1]+lst2[-1])
print(lst3)

#Concatenation of list 
list1 = ["M", "na", "i", "Ke"] #4 
list2 = ["y", "me", "s", "lly","Hi","Hello"]#6 
print(len(list2)) 
print(len(list1)) 
lst=[] 
 
for i in range(len(list2)):#(0,6) 
 if i<len(list1): 
  lst.append(list1[i]+list2[i]) 
 else: 
  lst.append(list2[i]) 
print(lst)

#Given a Python list of numbers. Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]
aList2=[]

for i in aList:
  aList2.append(i**2)
print(aList2)


#Concatenate two lists in the following order
#list1 = ["Hello ", "take "]
#list2 = ["Dear", "Sir"]
#lst3= [a+b for a in list1 for b in list2]
#print(lst3)

list1 = ["Hello ", "Take "]
list2 = ["Imba", "Chigga"]
list3= [a+b for a in list1 for b in list2]
print(list3)

#Other methods
list1 = ["Yo ", "Give "]
list2 = ["Chigga", "Bigga"]
list3=[]

for i in list1:
  for j in list2:
    list3.append(i+j)
print(list3)


#Given the two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

print(sorted(list1,reverse=False))
print(sorted(list2,reverse=True))

#Exercise 5: Given a two Python list.  
#Iterate both lists simultaneously such that list  
#should display item in original order and list2 in reverse order 
 
list1 = [10, 20, 30, 40] 
list2 = [100, 200, 300, 400] 
 
list2.sort(reverse=True) 

