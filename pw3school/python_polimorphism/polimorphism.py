# Python Polymorphism

# The word "polymorphism" means "many forms", and in programming it refers to methods/function/operators with the same
# name that can be executed on many objects or classes

# Function Polymorphism
# An example of a Python function  that can be used on different objects is the len() function

# String
# For string len() returns the number of characters

x = "hello world"
print(len(x))  # 11

# Tuple
# For tuples len() returns the number of items in the tuple
tuple = ("hello world", "apple", "banan", "peach")
print(len(tuple))  # 4

# Dictionary
# For dictionaries len() function returns the number of key/value pairs in the dictironary

thisDict = {
    "x": "Exec",
    "W": "Write",
    "R": "Read"
}
print(len(thisDict))  # 3


# Class Polimorphism

# Polimorphism is often used in Class methods, where we can have multiple classes with the same method name
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car = Car("BMW", "Mercedes")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "777")

for x in (car, boat, plane):
    x.move()


# Look at the for loop at the end. Because of polymorphisms we can execute the same method for all three classes

# Inheritance Class Polymorphism
# What about classes with child classes with the same name? Can we use ploymorphism there?
# Yes, if we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane
# child classes of Vehicle the child classes  inherits the Vehicle methods, but can override them

# Create a class called Vehicle and make Car, Boat, Plane childs classes of Vehicle
class Vehicle:
    def __init__(self, brend, model, color):
        self.brend = brend
        self.model = model
        self.color = color

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Boat Sail!")


class Plane(Vehicle):
    def move(self):
        print("Plane Fly!")


car1 = Car("Ford", "Mustang", "balck")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20", "white")  # Create a Boat object
plane1 = Plane("Boeing", "747", "uzb flag")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brend, x.model, x.color)
    x.move()


