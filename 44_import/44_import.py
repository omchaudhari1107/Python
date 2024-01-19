# to import math
import math as m

x = m.sqrt(4)
print(x)

print("-------------------------")

# to import only one function from import(using from keyword)
from math import floor, pi

x = floor(4.2423)
pie = pi
print(x, pie)

print("-------------------------")

# to import all function
from math import *

x = floor(2.2423)
pie = 2 * pi
print(x, pie)

print("-------------------------")

# the dir function:use to see the function inside math pack
print(dir(m))

print("-------------------------")

# create custom pack
from four_four_om import welcome, om

welcome()
print(om)
