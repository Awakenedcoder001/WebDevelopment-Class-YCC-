#creating empty 
dict_1={}
print(dict_1)
print(type(dict_1))
dict_2=dict()
print(dict_2)
print(type(dict_2))
#creating elements
dict_3={
 'name':'Riana',
 'run':14000,
 'avg':28.5
}
print(dict_3)
print(type(dict_3))
print(id(dict_3))
#accessing the key values
print(dict_3['name'])
#accessing base on index values
# print(dict_3[0])
#adding the elements
dict_3['Age']=36
print(id(dict_3))
print(dict_3)
#remove the key values pair
del dict_3['avg']
print(dict_3)
print(id(dict_3))