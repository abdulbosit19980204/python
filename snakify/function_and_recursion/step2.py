# What is a function?

# Functions are the code sections which are isolated from the rest of the program and executed only when called
# They all have something in common: They take parameters (zero, one, ore several of them) and they can return a value
# (or nothing, None)

# Now we want to show you how to write a function called factorial() which takes a single parameter - the number,
# and returns a value - the factorial of that number

def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


print(factorial(3))
print(factorial(5))

