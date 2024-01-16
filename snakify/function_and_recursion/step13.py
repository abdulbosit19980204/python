# Global
# It is much better to rewrite this example as follows
# the chunk of code that can be copied from program to program
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


# end of the chunk

# n = int(input())
n = 5
f = factorial(n)
print(f)
# doing other stuff with variable f

# This function is now ready to be called from different parts of our program wiht ease. It's also ready to be
# copy-pasted to your other program

