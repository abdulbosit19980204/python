# Python Math
# Python has a set of built-in math function, including an extensive  math module , that allows you to perform mathematical
# tast to numbers

# Built-in Math Functions
# The min() and max() function can be used to find the lowest or highest value in an iterable
x = max(1, 18, 22, 15, -14, 154)
y = min(1, 15, 22, 8, 14, -7, -5, -11)
print(x, y)  # 154 -11

# The abs() function returns the absolute (positve) value of the specified number
x = -784
print(abs(x))  # 784

# The pow(x,y) function returns the value of x to the power of y. (x**y)

x = 5
y = 3
print(pow(x, y))  # 125

# The Math module
# Python has also a built-in module called math, which extends the list of mathematical functions
# To use it, you must import the math module

import math

# When you have imported the math module, you can start using methods and constants of the module
# The math.sqrt() method for example, returns the square root of a number
x = math.sqrt(64)
print(x)  # 8.0

# The math.ceil() method rounds a number upwards to its nearest integr, and the math.floor() method rounds a number
# downwards to its nearest integer, and returns the result
x = math.ceil(1.4)
y = math.floor(1.4)
print(x, y)  # 2  1

# The math.pi constant, returns the value of PI(3.141592653589793)
x = math.pi
print(x)  # 3.141592653589793

