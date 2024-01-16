# Global variables

# Inside the function, you can use variables declared somewhere outside of it

def f():
    print(a)


a = 1
f()

# Here the variable a is set to 1, and the function f() prints this value, despite the fact that when we decalre the function
# f this variable is not initialized. The reason is, at the time of calling the function f() (the last string) the
# variable "a" already has a value. That's why the function f() can display it
# Such variables (declared outside the function but available inside the function) are called global
