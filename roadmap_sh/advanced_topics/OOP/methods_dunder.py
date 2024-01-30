# Methods and Dunder

# Methods in python are very similar to functions except for two major differences.
#   *The method is implicitly used for an object for which it is called.
#   *The method is accessible to data that is contained within the class.

# Dunder or magic methods in Python are the methods having
# two prefix and suffix underscores in the method name.
# Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading.
# Few examples for magic methods are: init, add, len, repr etc.


# Python Magic methods are the methods starting and ending with double underscore'__method_name__()' They are defined
# by built in classes in Python and commonly used for operator overloading

# Python Magic methods

# Built in classes define many magic methods, dir() function can show you magic methods inherited by a class
print(dir(int))


# or we can try cmd/terminal to get the list of magic functions in Python, open  cmd or terminal, type python3 to go  to the
# Python console, and type

# dir(init)

# 1. __init__() method
# The __init__ method for initialization is invoked without any call when an instance of a class is created, like construction
# in certain other programming languages such as C++, Java ...

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


# 2. __repr__ method
# __repr__ method in python defines how an object is presented as a string

# The below snippet of code prints only the memory address of the string object. Let's add a __repr__ method to represent

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Name: {self.fname}\nSurname:{self.lname}"


odam1 = Person("Abdulbosit", "Tuychiev")
print(odam1)


# 3. __add__ method
# This method defines how will be the objects of a class added togther. It is also known as overload addition operator
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Name: {self.fname}\nSurname:{self.lname}"

    def __add__(self, other):
        return self.fname + " " + other.lname


bobo = Person("Oribjon", "Pozilov")
nevara = Person("Abdulloh", "Tuychiev")
print(bobo + nevara)  # Oribjon Tuychiev


