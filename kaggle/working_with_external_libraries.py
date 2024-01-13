# Working with external Libraries

# Imports, operator overloading, and survival tips for venturing into the world of external libraries

# Imports
# Either way, we'll access additional codes with imports
# We'll start our example by importing math from the standard library
import math

print("It's math! It has type {}".format(type(math)))
# It's math! It has type <class 'module'>

# math is a module. A module is just a collection of variables (a namespaces, if you like) defined by someone else.
# We can see all the names in math using the built-in function dir()
print(dir(math))

# We can access these variables using dot syntax. Some of them refer to simple values, like math.pi

print("Pi to significant digits: {:.4}".format(math.pi))
# Pi to significant digits: 3.142

# But most of what we'll find in the module are functions, like math.log
print(math.log(32, 2))  # 5.0

# Of course, if we don't know what math.log does, we can call math help() on it

help(math.sqrt)
"""
sqrt(x, /)
    Return the square root of x.
"""

# Other import syntax
# If we know we'll be using functions in math frequently, we can import it under a shorter alias to save some typing
# (though in this case "math" is already pretty short)
import math as mth

print(mth.pi)  # 3.141592653589793
# The as simply renames the imported module. It's equivalent to doing something like
import math

mt = math
print(mt.pi)

# Wouldn't it be great if we could refer to all the variables in the math module by themselves? i.e if we could just refer
# to pi instead of math.pi or mt.pi? Good news we can do that
from math import *

print(pi)
print(sqrt(4))

# import * makes all the module's variables directly accessible to you (without any dotted prefix)
# Bad news: some purists might grumble at you for doing this
# Worse: they kind of have a point
# from math import *
# from numpy import *
# print(pi, log(32, 2))
# TypeError: return arrays must be of ArrayType

# What has happened? It worked before!
# These kind of "star imports" can occasionally lead to weird, difficult-to-debug situations
# The problem in this case is that the math and numpy modules both have functions called log ,but they have
# different semantics. Because we import from numpy second, its log overwrites (or "shadows") the log variable we imported
# from math
# A good compromise is to import only the specific things we'll need from each module
from math import log, pi
from numpy import asarray

# Submodules
# we've seen that modules contain variables which can refer to functions or values. Something to be aware of if that
# they can also have variables referring to other modules

import numpy

print("numpy.random is a", type(numpy.random))
print("it contains names such as ", dir(numpy.random)[-15:])

# so if we import numpy as above, the calling a function in the random "submodule" will require two dots
rols = numpy.random.randint(low=1, high=6, size=10)
arr = numpy.array(rols)
print(rols)
print(arr)

# Operator overloading
# What's the value of the bellow expression?

print(rols + 10)
print(arr + 10)

print(rols <= 3)  # [ True False  True False  True False False False  True  True]
xlist = [[1, 2, 3], [2, 4, 6], ]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

print(x[1, -1])

"""
numpy's ndarray type is specialized for working with multi-dimensional data, 
so it defines its own logic for indexing, allowing us to index by a tuple to specify the index at each dimension.
"""

# When does 1 + 1 not equal 2?
# Things can get weirder than this. You may have heard of (or even used) tensorflow,
# a Python library popularly used for deep learning. It makes extensive use of operator overloading.
# import tensorflow as tf
#
# # Create two constants, each with value 1
# a = tf.constant(1)
# b = tf.constant(1)
# # Add them together to get...
# a + b