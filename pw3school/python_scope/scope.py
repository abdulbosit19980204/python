# Python Scope
# A variable is only available from inside the region it is created. This is called scope

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function

def myfunc():
    x = 30
    print(x)


myfunc()  # 30


# Function inside Function

# As explained in the example above, the variable x is not available outside the function, but it is available for any
# function inside the function

# The local variable can be accessed from a function within the function
def myfunction():
    x = 300

    def myfunction2():
        print(x)

    myfunction2()


# myfunction2()  # NameError: name 'myfunction2' is not defined. Did you mean: 'myfunction'?
myfunction()  # 300

# Global Scope

# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local

# A variable creted outside of a function is global and can be used by anyone
x = 500


def myfunc():
    print(x)


myfunc()

# Naming Variables

# If you operate with the same variable name inside and outside of a function, Python will treat them as
# two separate variables, one available in the global scope(outside the function)
# and the local scope(inside the function)

# The function will print the local x, and then the code will print the global x
x = 500


def myfunction2():
    x = 100
    print(100)


myfunction2()  # 100
print(x)  # 500


# Global Keyword

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword
# The global keyword makes the variable global

def myfunction2():
    global x
    x = 300


myfunction2()
print(x)

# Also, use the global keyword if you want to make a change to a global variable inside the function

x = 500


def myfunction3():
    global x
    x = 100
    print(x)


myfunction3()  # 100
print(x)  # 100


