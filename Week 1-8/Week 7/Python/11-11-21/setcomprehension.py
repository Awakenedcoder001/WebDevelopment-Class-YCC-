Tshering Yangden DS(40)20-11063, [11.11.21 14:21]
#using for loop
set1={1,2,3,4,5}
set2={}
set3=set(set1)
set4=set(set2)
#using for loop
for i in set3:
  set4.add(i**2)
print(set4)
#using set comprehension
set4={i**2 for i in set3}
print(set4)