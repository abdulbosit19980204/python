# Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class

# Parent class is the class being inherited from, also called base class
# Child class is the class that inherits from another class, also called derived class

# Create a parent class
# Any class can be a parent class, so the syntax is the same as creating any other class

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


x = Person("Abdulbosit", "Tuychiev")
x.printname()


# Create a Child class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when
# creating the child class:

class Student(Person):
    pass


s = Student("Abdusomad", "Tuychiev")
s.printname()


# Add the __init__() Function
class Teacher(Person):
    def __init__(self, fname, lname, salary, experience):
        Person.__init__(self, fname, lname)
        self.salary = salary
        self.experience = experience


# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent

class User(Person):
    def __init__(self, fname, lname, items):
        super().__init__(fname, lname)
        self.items = items

    def __repr__(self):
        return f"{self.lname} {self.fname}: {self.items}"


u = User("Abdulbosit", "Tuychiev", ["MacBook", "iPhone 15 Pro", "Monitor 15"])
print(u)  # Tuychiev Abdulbosit: ['MacBook', 'iPhone 15 Pro', 'Monitor 15']
u.printname()

