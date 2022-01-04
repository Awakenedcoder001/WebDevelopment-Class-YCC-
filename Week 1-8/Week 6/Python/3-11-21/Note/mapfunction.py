lst=[2,4,7,5,9]
map_func=map(lambda X: X**2,lst)
print(map_func)
print(type(map))

#converting map objects into tuple objects
map_tup=tuple(map(lambda X: X**2,lst))
print(map_tup)

#converting the map object into set objects
map_set=set(map(lambda X: X**2,lst))
print(map_set)

#converting the map object into list objecta
map2=list(map_func)
print(map2)