 # support.py is the python file/module
import support
support.print_func('Bhagyashree')



#Another way using aliasing:
# import support as sp
# sp.print_func('Bhagyashree')

#Another example using aliasing:
import math as m
print("The value of pi is ", m.pi)

#A way where we read only pi function to avoid more memory usage
from math import pi
print("The value of pi is ", pi)

#Another way to import all modules from math module using *
from math import *
print("The value of Pi is ", pi)

#Accessing individual elements
import support
a = support.person1['age']
print(a)


import sys
for path in sys.path:
    print(path)