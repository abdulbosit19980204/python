# Python Modules

# What is a Module
# Consider a module to be the same as a code library
# A file containing  a set of functions you want to include in your application

# Create Module
# To create a module just save the code you want in a file withe file extension .py

# Use a Module
# Now we can use the module we just created, by using the import statement

# Import the module named mymodule, and call the xisobla function
import mymodule

mymodule.xisobla(5, 3)  # 8

# Note: When using a function from a module, use the syntax. module_name.function_name
# Variables in Module

# The module can contain functions, as already described, but also variables of all types(arrays,dictionaries, objects)
print(mymodule.person1["name"])  # Abdulbosit

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Renaming a Module
# You can create an alias when you import a module, by using the as keyword
# Create an alias for mymodule called mym
import mymodule as mym

print(mym.person1["name"], mym.person1["birthday"])  # Abdulbosit 1970-01-01

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like

# Import and use the platform module
import platform

print(platform.system())  # Windows
print(platform.machine(), platform.release(), platform.processor())
# AMD64 11 AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD

# Using the dir() function
# There is a built in function to all the function names (or variable names) in a module. The dir() function

# List all the defined names belonging to the platform module
# print(dir(platform))
print(dir(mymodule))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'person1', 'xisobla']
# Note: The dir() function can be used on all modules, also the ones you create yourself

# Import from module
# You can choose to import only parts from a module, by using the from keyword

# The module named mymodule has one function and one dictionary
# Import only the person1 dictionary from the module
from mymodule import person1

print(person1["name"], person1["surname"], person1["birthday"])  # Abdulbosit Tuychiev 1970-01-01

# Note: When importing using the from keyword, do not use the module name when referring to elements, in the module.
# Example: person1["name"] , not mymodule.person1["name"]