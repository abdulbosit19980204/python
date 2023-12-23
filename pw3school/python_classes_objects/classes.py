# Python Classes/ Objects

# Python is an object oriented programming language
# A Class is like an object constructor, or "blueprint" for creating objects

# Create a Class
# To create a class, use the keyword class
class Person:
    name = "Abdulbosit"


# Create Object
# Now we can use the class named MyClass to create objects
# create an object named user1, and print the vaule of name
user1 = Person()
print(user1.name)  # Abdulbosit


# The __init__() Function
# The examples above are calsses and objects in their simplest form, and are not really useful in real life applications
# To understand the meaning of calsses we have to understand the built-in __init__() function
# All classes have a function called __init__(), which is always executed when the class is being initiated
# Use the __init__ () function to assign values to object properties, or other operations that are necessary to do when
# the objects is being created

# Create a class named Person, use the __init__ () function to assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user2 = Person("Abdusomad", 23)
print(f"{user2.name} is {user2.age}")  # Abdusomad is 23

# Note: The __init__ () function is called automatically every time the class is being used to create a new object

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string
# If the __str__() function is not set, the string representation of the object is returned

# The string  representation of an object Wihtout the __str__() function
print(user2)  # <__main__.Person object at 0x00000199AD9A1130>


# The string representation of an object With the __str__() function
class Person2:
    def __init__(self, name, age):
        self.name = name,
        self.age = age,

    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}"


user3 = Person2("Abdusomad", 23)
print(user3)  # My name is ('Abdusomad',) and my age is (23,)


# print(f"{user3.name} is {user3.age}")  # ('Abdusomad',) is (23,)


# Object Methods
# Objects can also contain methods. Methods in object  are function that belong to the object
# Let's create a method in the Person class
class Person3:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def mySoliq(self):
        return 0.12 * self.salary

    def __str__(self):
        return f"My name is {self.name} and my age is{self.age} and my salary{self.salary} and I need to pay {self.mySoliq()}$"


user4 = Person3("Abdulbosit", 25, 2500)
soliq = user4.mySoliq()
print(soliq)
print(user4)  # My name is Abdulbosit and my age is25 and my salary2500 and I need to pay 300.0$


# Note: The self parametr is a reference to the current instance of the class, and is used to access variables that
# belong to the class.

# The self Parametr
# It doesn't have to be named self, you can call it whatever you like, but it has to be the first parameter of any
# function  in the class
class Person4:
    def __init__(mySelf, name, age):
        mySelf.name = name
        mySelf.age = age

    def __str__(selfInfo):
        return f"My name is {selfInfo.name} and my age is {selfInfo.age} "


user5 = Person4("Abdulbosit", 25)
print(user5)  # My name is Abdulbosit and my age is 25

# Modify Object Properties
# You can modify properties on objects like this
# set the age of user5 to 40
user5.age = 40
print(user5)  # My name is Abdulbosit and my age is 40

# Delete object Porperties
del user5.age
# print(user5.age)  # AttributeError: 'Person4' object has no attribute 'age'

# Delete Objects
# You can delete objects by using the del keyword
# Delete user5 object
del user5
print(user5)  # NameError: name 'user5' is not defined. Did you mean: 'user1'?

# The pass Statement
# class definitions cannot be empty but if you for some reason have a class definition with no content, put in the pass
# statement to avoid getting  an error
class Person5():
    pass

