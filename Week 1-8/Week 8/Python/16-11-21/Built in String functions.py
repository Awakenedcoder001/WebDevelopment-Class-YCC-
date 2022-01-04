pemba="Pemba is Very Smart and Intelligent"
print(pemba.upper())
print(pemba.lower())
print(pemba.capitalize())
print(pemba.swapcase())
print(pemba.casefold())
print(pemba.title())
print(pemba.replace("Smart","Tall"))
print(pemba.index('i'))
print(pemba[::-1])

s=pemba.maketrans("a,e,i,o,u","@,#,*,&,^")
print(pemba.translate(s))
#String Methods which return True Or False:
print(pemba.isupper())
print(pemba.islower())
print(pemba.isalpha())
print(pemba.isalnum())
print(pemba.isdigit())

