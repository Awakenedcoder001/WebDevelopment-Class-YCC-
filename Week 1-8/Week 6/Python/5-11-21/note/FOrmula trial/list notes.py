#Creation of empty list
a=[]
b=list()
print(a,b)
print(type(a),type(b))

#Hemogenous LIST
lst=[1,2,3,4,5]
print(lst)

#Heterogenous
lst_1=[1,2.2,3+2j,"Hello"]
print(lst_1)

#Nested List:
lst_3=[[1,2],[3,4]]
print(lst_3)

#Advanced Data Types In list:
lst_4=[[1,2],(3,4),{4,5},{"name":"Pema Choda","gender":"Male"}]
print(lst_4)
print(lst_4[3]["gender"])