#GLOBAL VARIABLES

# Variables that are created outside of a  function (as in all of the examples above) are known as global variables
# Global variables can be used by everyone, both inside and outside of the function

x="awesome"
def myFunc():
    print("Python is "+x)

myFunc()

# If we create a variable the same name inside a function, this variable will be local, and can only be used inside the function

def newFunc():
    x="running"
    print("New function is "+x)
newFunc()

# To create a global variable inside a function, you can use the "global" keyword

def globalVarFunc():
    global x
    x="Hello"
    print(x+ " world")

globalVarFunc()
print(x+" dunyo")

