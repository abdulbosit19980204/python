# You can go global

# If you want a function to be able to change some global variable, you must declare this variable as a global  inside
# the function using the keyword global()

def f():
    global a
    a = 1
    print(a)


a = 0
print(a)  # 0
f()  # 1
print(a)  # 1

# This example will print the output of 0 1 1, because the variable a is declared as global,
# and changing it inside the function causes the change of it globally.

# However, it is better not to modify values of global variables inside a function.
# If your function must change some variable, let it return this value and call the function with
# passing that variable as an input. If you follow these rules, the functions' logic works
# independent of the outer code logic, and thus such functions can be easily copied from one program to another,
# saving your time.

