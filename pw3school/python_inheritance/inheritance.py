# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class

# Parent Class: is the class being inherited from, also called base class
# Child Class: is the class that inherits from another class, also called derived class

# Create a Parent Class

# Any class can be parent class, so the syntax is the same as creating any other class:

# Create a class named Person, with firstname, lastname properties and a printname method:

class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printName(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method

x = Person("Abdulbosit", "Tuychiev")
x.printName()  # Abdulbosit Tuychiev


# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating
# the child class

class Student(Person):
    pass


newStudent = Student("Abdusomad", "Tuychiev")
newStudent.printName()  # Abdusomad Tuychiev


# Now the Student class has the same properties and methods as the Person class

# Add the __init__ () Function
# So far we have created a child class that inherits the properties and methods from its Parent
# We want to add the __init__() function to the child class (instead of the pass keyword)

# Note: The __init__() function is called automatically every time the class is being used to create a new object
class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = fname,
        self.lastname = lname


# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function
# Note: The child's __init__() function overrides the inheritence of the parent's __init__() function

# To keep the inheritance of the Parent's __init__ () funtion, add  a call to the parent's __init__() function

class Student2(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready
# to add functionality in the __init__() function

# Use the super() Function
# Python also has a super() function that will make the child class inherit all methods and properties from it's parent

class Student3(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


# By using the super() function, you don't have to use the name of the parent element, it will automatically inherit the methods
# and properties from its parent

# Add Properties
# Add a property called graduationyear to the Student class
class Student4(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2020


student4 = Student4("Abdulbosit", "Tuychiev")
print(student4.firstname, student4.graduationyear)  # Abdulbosit 2020


# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects
# To do so, add another parameter  in the __init__() function

# Add a year parameter , and pass the correct year when creating objects
class Student5(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


student5 = Student5("Abdulbosit", "Tuychiev", 2025)
print(student5.firstname, student5.graduationyear)  # Abdulbosit 2025


# Add methods
# Add a method called welcome to the student class
class Student6(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(f"Hello {self.firstname}  {self.lastname} welcome to {self.graduationyear} the graduation ceremony")

student6=Student6("Abdulbosit", "Tuychiev" ,2025)
student6.welcome() #Hello Abdulbosit  Tuychiev welcome to 2025 the graduation ceremony


