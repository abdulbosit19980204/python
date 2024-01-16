# Explanations

# def is the key word for declare function
# factorial is name of the function
# n is the argument to function
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(factorial(3))
print(factorial(5))

