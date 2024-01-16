# Recursion theory

# The situation when function calls itself is called recursion, and such function is called recursive

# Recursive function are powerful mechanism in programming. Unfortunately, they are not always effective and often lead
# to mistake. The most common error is infinite recursion, when the chain of function calls never ends (well, actually,it
# ends when you run out of free memory in your computer). An example of infinite recursion

def f(): return f


# The most common reason causing infinite recursion:
# 1. Incorrect stopping condition. For example, if in the factorial-calculating program we forget to put check if n==0,
#     then factorial(0) will call factorial(-1), that will call factorial(-2)... etc.

# 2. Recursive call with incorrect parameters. For example, if the function factorial(n) calls the function factorial(n)
# we will also obtain an infinite chain of calls

# Therefore, when coding a recursive function, it is first necessary to ensure it will reach its stopping conditions
# to think why your recursive will ever end

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def double_factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * double_factorial(n - 2)


print(double_factorial(5))
