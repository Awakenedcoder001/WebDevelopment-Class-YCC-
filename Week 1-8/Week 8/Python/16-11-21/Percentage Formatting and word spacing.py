#Percentage Formatting and Word Spacing
#percentage Formating:

a=25.45
b=00.25
print("{:%} {:%}".format(a,b))
print("{:.2%} {:.2%}".format(a,b))


#Word spacing
a="Hello"
print("|{:^10}|".format(a))
print("|{:>10}|".format(a))
print("|{:<10}|".format(a))