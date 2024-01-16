# You can make me global
# For example, suppose your program should calculate the factorial of the given number that you want to save in the
# variable f
def factorial(n):
    global f
    res = 1
    for i in range(1, n + 1):
        res *= i
    f = res


factorial(5)
print(f)  # 120

# This is the example of bad code, because it's hard to reuse the function factorial().
# If tomorrow you need another program to use the function "factorial", you will not be able to just copy
# this function from here and paste in your new program. You will have to ensure that that program doesn't contain
# the variable f.

# Even worse, whenever you make other calls to factorial() from your program,
# you need to make sure that there's no variable called f defined for other needs and storing the valuable data.

