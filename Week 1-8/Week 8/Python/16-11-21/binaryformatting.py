#binary Formatting

a=1600
b=2361
c=30
d=5000

  # 2- 1600
  # 2- 800 - 0
  # 2- 400 - 0
  # 2- 200 - 0
  # 2- 100 - 0
  # 2- 50  - 0
  # 2- 25  - 0
  # 2- 12  - 1
  # 2- 6   - 0
  # 2- 3   - 0
  #    1   - 1

#Binary Notation
print("{0:b} {1:b}".format(a,b,c,d))

#Ocatal Notation
print("{:o} {:o}".format(a,b))

#Hexadecimal Notation
print("{:x} {:x}".format(a,b))

#Floating-Point Notation
from math import pi
value=pi
print(value)
print("{:.6f}".format(value))
print("{:.2f}".format(value))
print("{:.0f}".format(value))

#Exponential Notation
a=168.1234567890213456754567865
print("{:e}".format(a))

a=-169676869.1234567890213456754567865234567892345678234567823456783456783456
print("{:e}".format(a))