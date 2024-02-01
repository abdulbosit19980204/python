# Modules

# Modules refer to a file containing Python statements and definitions.
# modules provide reusability of code.


# Import modules in Python

# We use the "import" keyword to do this.

# Python import with Renaming
# In Python, we can also import a module by renaming it. For example,
# import module by renaming it
import math as m

print(m.pi)

# Output: 3.141592653589793

# We have renamed the "math" module as "m".

# Python from...import statement
# We can import specific names from a module without importing the module as a whole.
# import only pi from math module
from math import pi

print(pi)

# Output: 3.141592653589793

# Import all names
# we can import all names(definitions) from a module using the following construct:
# import all names from the standard module math
from math import *

print("The value of pi is", pi)


# The dir() built-in function
#  we can use the dir() function to list all the function names in a module.


