# Getting Help
# You saw the abs function in the pervious tutorial, but what if you've forgotten what it does?
# The help() function is possibly the most important Python function you can learn. If you can remember how to use help()
# you hold the key to understanding most other functions

help(round)
"""
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.

    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
"""

# help() displays two things:
# 1. The header of that function round(number, ndigits=None). In this case, this tells us that round() takes an argument
# we can describe as number. Additionaly, we can optionally give a separate argument which could be described as ndigits
# 2. A brief English description of what the function does

# Common pitfall: when you're looking up a function, remember to pass in the name of the function itself, and not the
# result of calling that function

# what happens if we invoke help on a call to the function round()? Unhide the output of the cell below to see
help(round(-2.01))

# round is a very simple function with a short docstring. help shines even more when dealing with more complex, configurable
# functions like print. Don't worry if the following output looks inscrutable... for now, just see if you can pick
# anything new out from this help

help(print)
"""
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

"""


# Defining functions
# Built in functions are great, but we can only get so far with them before we need to start defining our own functions
# Below is a simple example

def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),  # Python allows trailing commas in argument lists. How nice is that?
)

# help() function can tell us something about it
help(least_difference)
"""
Help on function least_difference in module __main__:

least_difference(a, b, c)
"""


# Python isn't smarter enough to read my code and turn it into a nice English description. However, when I write a function
# I can provide a description in what's called the docstring

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.

    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


# The docstring is a triple-quoted string (which may span multiple lines) that comes immediately after the header of a function
# When we call help() on a function, it shows the docstring

help(least_difference)

# Function that don't return
# What would happen if we didn't include the return keyword in our function?
# We only call them for their side effects
help(help)

# Default arguments
# When we called help(print),  we saw that the print function has several optional arguments. For example, we can specify
# a value for sep to put some special string in between our printed arguments
print(1, 2, 3, sep=' < ')  # 1 < 2 < 3


# Adding optional arguments with default values to the functions we define turns out to pretty easy
def greet(who="Colin"):
    print("Hello,", who)


greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")


# Functions Applied to Functions
# Here's something that's powerful, thought it can feel very abstract at first
# You can supply function as arguments to other functions. Some example may make this clearer
def mult_by_five(x):
    return x * 5


def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))


print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n',  # '\n' is the newline character - it starts a new line
)


# Functions that operate on other functions are called "higher-order functions" You probably won't write your
# own for a little while. But ther are  higher-order functions built into Python that you might find usefull to call
# Here's an interesting example using the max function
# By default max returns the largest of its arguments. But if we pass in a function using the optional key argument, it
# returns the argument x that maximizes key(x) (aka the 'argmax')

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5


print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

