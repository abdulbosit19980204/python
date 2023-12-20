# Python Functions
from inspect import Arguments


# A function is a block of code which only runs when it is called
# You can pass data, known as parameters, into a function.
# A function can return data as a result

# Creating a Function
# In Python a function is defined using the def keyword

def firstFunc():
    print("This is the first function")


# Calling a function
# To call a function, use the function name followed by parenthesis
firstFunc()  # This is the first function


# Arguments
# Information can be passed into function as arguments
# Arguments are specified after the function name, inside the parenthesis
# You can add as many arguments as you want, just sperate them with a comma.
def secondFunc(prop):
    print("Hello " + prop)


secondFunc("Abdulbosit")  # Hello Abdulbosit


# Arguments are often shortened to args in Python Documentations

# Parameters or Arguments?
# The terms parameters and arguments can be used for the same thing. information that are pased into a fucntion

# Arbitary Arguments, *args
# If you don't know how many arguments that will be passed into your function, add * before the parameter name in function definition
# This way the function will recive a tuple of arguments, and can access the items accordingly
def thirdFunc(*args):
    for i in args:
        print("Hello", i)


thirdFunc("Jumong", "Sardor")


# Hello Jumong
# Hello Sardor

# Arbitary Arguments are often shortened to *args in Python documentations
# Keyword Arguments
# You can also send arguments with the key=value syntax
# This way the order of the arguments does not matter

def keyVal(car1, car2, car3):
    maxPrice = max(car1, car2, car3)
    print("The most expensive car is", maxPrice)


keyVal(car1=15000, car2=25000, car3=5000)  # The most expensive car is 25000


# The phrase Keyword Arguments are often shortned to kwargs in Python documentations

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the 4
# parameter name in the function definition

# This way the function will recive a dictionary of arguments, and can access the items acordingly
def myChildre(**kids):
    print("My youngest child is", kids["name"], "and he is", kids["age"])


myChildre(name="John", age=20)  # My youngest child is John and he is  20


# Arbitary Kword Arguments are often shortened to **kwargs in Python documentations

# Default Parameter Value
# The following example shows how to use a default parameter value
# If we call the function without argument, it uses the default value

def my_info(name, age, country="Uzbeksitan"):
    print("Hello. My name is", name, "and my age is", age, "and my coutry is", country)


my_info("Abdulbosit", 25)  # Hello. My name is Abdulbosit and my age is 25 and my coutry is Uzbeksitan
my_info(name="Jumong", age=55, country="Korea")  # Hello. My name is Jumong and my age is 55 and my coutry is Korea


# Passing a list as an Argument
# You can send any data types of argument to a function (string, number, list, dictionry etc) and it will be treated
# as the same data type inside the function

def my_food(recipe):
    print("My favorite food is contain: ")
    for i, x in enumerate(recipe):
        print(i + 1, x)


recipe = ["apple", "banana", "cherry"]
my_food(recipe)
"""
My favorite food is contain: 
1 apple
2 banana
3 cherry
"""


# Return Values
# To let a function return  a value, use the return statement

def my_food_price(price, pors):
    return price * pors


print("Your order will be ", my_food_price(5, 30000))  # Your order will be  150000

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in  the pass statemtent to avoid getting an error

def passFunc():
    pass

