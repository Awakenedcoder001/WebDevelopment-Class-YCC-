lst_filter=list(range(1,11))
#stores the out put in the form of filter objects
filter_result=filter(lambda i: i%2==0,lst_filter)
print(filter_result)
print(type(filter))

filter_result=set(filter(lambda i: i%2==0,lst_filter))
print(filter_result)
print(type(filter))

filter_result=tuple(filter(lambda i: i%2==0,lst_filter))
print(filter_result)
print(type(filter))

#converting the filter object in to list objects
filter_lst=list(filter_result)
print(filter_lst)