
#using for loop
s1={1,2,3,4,5,6}
s2={1,2,3}
for i in s2:
    s1.remove(i)
print(s1)


or

#using for loop
s1={1,2,3,4,5,6}

for i in {1,2,3}:
    s1.remove(i)
print(s1)