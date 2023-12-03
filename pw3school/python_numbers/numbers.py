# Python Numbers

# There are three numeric types in Python

# int, float, complex

x=1         #int
y=1.001     #float
z=1j        #complex

# Int

# int or integer is a whole number, positive or negative, without decimals,of unlimited length
x=1
y=11111111111111444444444444444447777777777777777755555555
z=-5555555555555554444444444

print(type(y))

#Float

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x=1.0024
y=-1.45454
z=1.0

print(type(x), type(y), type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10

x=35e3
y=12E4
z=-87.7e100

print(z)

# Complex

# Complex numbers are written with s "j" as the imaginary part:

x=3+5j
y=5j
z=-5j

print(x)

# Type conversion
# We can convert from one type to another with the int(), float(), and complex() methods:

x=1
y=2.8
z=1j

#convert from int to float:
a=float(x)
print(a)

# convert from float to int:
b=int(y)

#convert from int to complex:
c=complex(x)

print(a)
print(b)
print(c)


# Random number

# Python doesn't have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random
print(random.randrange(1, 10))
