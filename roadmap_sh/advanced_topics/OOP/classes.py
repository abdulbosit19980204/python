# 1. class
# To create a class use the class keyword and after keyword write class  Name with Title case
class Add:
    pass


# 2. Object
# To create an Object use the classname
a = Add()


# here "a" is the object

# 3. __init__()
# to initialization variable on Class use the __init__() func
# and self.variable_name = variable_name
class Add:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def xisobla(self):
        return self.num1 + self.num2


ex1 = Add(5, 3)
print(ex1.xisobla())


# 4. __str__()  function controls what should be returned when the class object is represented as a string.
class Add:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def xisobla(self):
        return self.num1 + self.num2

    def __str__(self):
        return (f"Yig'indi {self.num1} va {self.num2} a+b={self.num2 + self.num1}")


ex2 = Add(2, 3)
print(ex2)  # Yig'indi 2 va 3 a+b=5

# 4. Object Method
# In our Add class, xisobla is Object Method

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to
# the class

