# Local variables
# But if you initialize some variable inside of the function, you won't be able to use this variable outside of it

def f():
    a = 1


f()
# print(a)
# NameError: name 'a' is not defined
# We receive error NameError. Such variables declared within a function are called "local". They become unaviable after you
# exit the function

