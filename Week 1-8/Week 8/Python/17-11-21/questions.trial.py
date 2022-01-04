#Write a Python program to create a set.
#fruits= {"mango","apple","juice"}
#print(fruits)
#print(type(fruits))

#Write a Python program to iteration over sets.
#magicmake= {"mango","apple","juice"}
#print(magicmake)
#print(type(magicmake))
#for i in magicmake :
 #   print(i)

#Write a Python program to add member(s) in a set
#team1 = {"Nado", "Kado", "Shado"}
#team1.add("Dodo")
#print(team1)

#team2 = {"Nado", "Kado", "Shado"}
#team2.update(["Boto", "Seto"])
#print(team2)

#Write a Python program to remove item(s) from a given set.
#set3 = {"Momo", "Chillichop", "Shado"}
#set3.remove("Momo")
#print(set3)

#set4 = {"Momo", "Chillichop", "Burger"}
#print(set4)
#set4.discard("Momo")
#print(set4)

#set4 = {"Momo", "Chillichop", "Burger"}
#print(set4)
#set4.remove("Momo")
#print(set4)

#set4 = {"Momo", "Chillichop", "Burger", 1,2}
#print(set4)
#set4.pop()
#print(set4)

# set4 = {"Momo", "Chillichop", "Burger", 1,2}
# print(set4)
# for i in {"Momo", "Chillichop", "Burger", 1,2}:
#     set4.remove(i)
#     break
# print(set4)

# set4 = {"Momo", "Chillichop", "Burger", 1,2}
# print(set4)
# for i in set4:
#     if i == 2:
#         set4.remove(i)
#         break
# print(set4)


# set4 = {"Momo", "Chillichop", "Burger", 1,2}
# print(set4)
# if "Momo" in set4:
#     set4.remove("Momo")
# print(set4)

# set4 = {"Momo", "Chillichop", "Burger", 1,2}
# print(set4)
# if "Burger" in set4:
#     set4.discard("Burger") 
# print(set4)

# set4 = {"Momo", "Chillichop", "Burger", 1,2}
# print(set4)
# if "Burger" in set4:
#     set4.pop() 
# print(set4)

#5 Write a Python program to remove an item from a set if it is present in the set.
# set4 = {"Momo", "Chillichop", "Burger", 1,2}
# if 1 in set4:
#     set4.remove(1)
# print(set4)

# set4 = {"Momo", "Chillichop", "Burger", 1,2}
# if "Burger" in set4:
#     set4.discard("Burger")
# print(set4)

#6Write a Python program to create an intersection of sets.
# s5 = {1,2,3,4,5}
# s6 = {5,7,8,9,10}
# print(s5 & s6)
# print(s6 & s5)
# print(s5.intersection(s6))
# print(s6.intersection(s5))

#7 Write a Python program to create a union of sets
# s1 = {2,3,4,5}
# s2 = {4,5,6,7}
# print(s1|s2)
# print(s2|s1)
# print(s1.union(s2))
# print(s2.union(s1))

#Write a Python program to create set difference.
# s1 = {2,3,4,5}
# s2 = {4,5,6,7}
# print(s1.difference(s2))
# print(s2.difference(s1))

# print(s1-s2)
# print(s2-s1)

#Write a Python program to create a symmetric difference.

# s1 = {2,3,4,5}
# s2 = {4,5,6,7}
# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1))

# print(s1^s2)
# print(s2^s1)

#Write a Python program to check if a set is a subset of another set.
# s1 = {1,2,3,4,5,6,7,8}
# s2 = {4,5,6,7,8}
# print(s1.issubset(s2))
# print(s1.issubset(s1))

# print(s1<=s2)
# print(s2<=s1)

#Python program to check if a set is a superset of another set.
# s1= {1,2,3,4,5,6,7,8,9}
# s2= {4,5,6,7,8,9}
# print(s1.issuperset(s2))
# print(s2.issuperset(s1))


#Write a Python program to create a shallow copy of sets
# lst={1, 2.3 ,2+3j ,"Tandin",True}
# print(lst)
# print(id(lst))
# lost=set(lst)
# print(lost)
# print(id(lost))

# lost.add(7)
# print(lost)
# print(id(lost))

 #Q12 Write a Python program to remove all elements from a given set
# lst={1, 2.3 ,2+3j ,"Tandin",True}
# lst.clear()
# print(lst)

#Write a Python program to use of frozensets
# so= frozenset({1,2,3,4,5})
# print(so)
# print(id(so))
# print(type(so))

#Write a Python program to find maximum and the minimum value in a set.
# seto = {30,60,20,15,45,90}
# print(seto)
# print(len(seto))
# print(max(seto))
# print(min(seto))

# seto = list({30,60,20,15,45,90})
# for i in seto:
#     seto.sort()
# print(seto[0],"Minimum")
# print(seto[-1], "Maximum")


# seto = list({30,60,20,15,45,90})
# for i in seto:
#     seto.sort(reverse=True)
# print(seto[-1], "Minumum")
# print(seto[0],"Maximum")

#Write a Python program to find the length of a set
# podu= {10,90,50,30,20,60,80}
# print(podu)
# print(len(podu))

#Write a Python program to check if a given value is present in a set or not. 
# gongdo = {"Tandin", 2+3j, 30, 40.5, False}
# print("Tandin" in gongdo)
# print(2+3j in gongdo)
# print(30 in gongdo)
# print(40.5 in gongdo)
# print(False in gongdo)

#Write a Python program to check if two given sets have no elements in common
#ango = {1,2,3,4,5}
#tango = {"Tandin", 2+3j, 2, 40.5, False}
#print(ango!=tango)

#print(ango.isdisjoint(tango))

#print(ango in tango)
#print(tango in ango)

#print(tango not in ango)
#print(ango not in tango)


#Write a Python program to check if a given set is superset of itself and superset of another given set
# a = {10,20,30,40,90,15,100,120,130,140}
# b = {100,120,130,140}
# print(a.issuperset(a))
# print(a.issuperset(b))
# print(b.issuperset(a))
# print(a >= b)
# print(b >= a)

#Write a Python program to find the elements in a given set that are not in another set.
# a = {10,20,30,40,90,15,100,120,130,140}
# b = {100,120,130,140}

# print(a-b)
# print(b-a)
# print(a.difference(b))
# print(b.difference(a))

#Write a Python program to remove the intersection of a 2nd set from the 1st set.
# a = {10,20,30,40,60,70,80,90}
# b = {60,70,80,100}
# print(a.intersection(b))
# print(a & b)
# print(a.difference(b))