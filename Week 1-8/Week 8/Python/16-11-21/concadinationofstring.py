#concatenation of string:

#using + operator

s1="CODE WITH"
s2="Tandin Tshewang"

print(s1+" "+s2)

#using format()
print("{} {}".format(s1,s2))

#using f literal
print(f"{s1} {s2}")
print(f"{s1.lower()} {s2.lower()}")

#join method
print(" ".join([s1,s2]))