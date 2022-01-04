
#positional formating
a="Keshav"
b="Murthy"
c="Code With"

#Code with Keshav Murthy
print("{2} {0} {1}".format(a,b,c))

#Keyword Fomratting
a="Keshav"
b="Code with"
c="K"
d="Murthy"

#Code with Keshav Murthy K
#Keyword Formatting
print("{title} {fname} {lname} {initil}".format(fname=a,title=b,initil=c,lname=d)) 

#Error 
print("{a} {b} {c} {d}".format(fname=a,title=b,initil=c,lname=d))

#Error
print("{1} {0} {3} {2}".format(fname=a,title=b,initil=c,lname=d))