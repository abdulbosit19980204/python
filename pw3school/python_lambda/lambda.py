# Python Lambda
from _ast import arguments

# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression

# Syntax
# lambda arguments: expression
# The expression is execude and the result is returned

# Add 10 to argument a, and return the result
x = lambda a: a + 10
print(x(4))  # 14
print(type(x))  # <class 'function'>

# Multiply argument a with argument b and return the result
x = lambda a, b: a * b
print(x(5, 3))  # 15

# Summarize argument a,b and c and return the result
x = lambda a, b, c: a + b + c
print(x(11, 22, 33))  # 66


# Why Use Lambda Function?
# The power of lambda is better shown when you use them as an anonymous function inside another function
# Say you have a function definition that takes one argument, and that arguments will be multiplied with an unknown number
def multiLab(n):
    return lambda a: a * n
# print(multiLab(5))
#<function multiLab.<locals>.<lambda> at 0x000001D170D98900>

# Use that function defination to make a function that always doubles the number you send in
myDoubler = multiLab(2)
print(myDoubler(3)) #6




