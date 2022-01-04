#Performance analysis of a list
lst=[1,2,3,4,5]
print(lst)
lst.append(6)
print(lst)
#Number of elements added: 1
#Number of the shifts: 0

lst=[1,2,3,4,5]
print(lst)
lst.insert(2,6)
print(lst)
#Number of elements added: 1
#Number of the shifts: 3

lst=[1,2,3,4,5]
print(lst)
lst.insert(0,6)
print(lst)
#Number of elements added: 1
#Number of the shifts: 5