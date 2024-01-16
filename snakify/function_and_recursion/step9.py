# Local and global variables: hey
# If you haven't understood the last explanation, take a look at the following code and think about how it worked,
# if the function could change the value  of the global loop variable i

def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    return fac


for i in range(1, 6):
    print(i, '!', ' = ', factorial(i), sep='')

# so if some variable is modified inside a function, that variable becomes a local variable, and its modification will not
# change a global variable with the same name

