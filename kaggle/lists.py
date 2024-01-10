# Lists

# Lists in Python represents order sequences of values. Here is an example of  how to create them
primes = [1, 2, 5, 45]

# We can put other types of things in list or make a list of list
hands = [[1, 2, 5, 4], ['A', 'B', 'C'], ['5', 'A', True, '@', 7]]

# A list can contain a mix of different types of variables

# Indexing
# You can access individual list elements with square brackets
print(primes[0])

# Slicing

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# What are the first three planets? We can answer this question using slicing
print(planets[0:3])  # ['Mercury', 'Venus', 'Earth']
# planets[0:3] is our way of asking for the elements of planets
# starting from index 0 and continuing up to but not including index 3

# If I leave out the index, it's assumed to be the length of the list
planets[3:]  # ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# the expression above means "give me all the planets from index 3s onward"
# We can also use negative indices when slicing

print(planets[1:-1])  # ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
print(planets[-3:])  # ['Saturn', 'Uranus', 'Neptune']

# Changing list
# Lists are "mutable", meaning they can be modified "in place"
# One way to modify a list is to assign to an index or slice expression
# For example. let's say we want to rename Mars
planets[3] = "Malacandra"
print(planets)  # ['Mercury', 'Venus', 'Earth', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Hm, that's quite a mouthful. Let's compensate by shortening the names of the first 3 planets
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)  # ['Mur', 'Vee', 'Ur', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# List functions

# Python has several useful functions for working with lists
# len gives the length of list

print(len(planets))  # 8

# sorted - returns a sorted version of a list
sorted(planets)
print(sorted(planets))  # ['Jupiter', 'Malacandra', 'Mur', 'Neptune', 'Saturn', 'Ur', 'Uranus', 'Vee']

# sum does what you might expect
print(sum(primes))  # 53

# Interlude object
# I've used the term 'object' a lot so far - you may have even read that everything in Python is an object.  What does that mean?
# In short, objects carry some things around with them. You access that stuff using Python's dot syntax
# For example, number in python carry around an associated variable called imag representating their imaginary part.
x = 12
# x is a real number, so its imaginary part is 0
print(x.imag)  # 0
# Here's how to make a complex number, in case you have ever been curious
c = 12 + 3j
print(c.imag)  # 3.0
# The things an object carries around can also include functions. A function attached to an object is called a method
# Non function things attached to an object, such as imag, are called attributes
# For example, numbers have a method called bit_length. Again, we access it using dot syntax
print(x.bit_length)  # <built-in method bit_length of int object at 0x00007FFF028FCB18>
# To actually call it, we add parentheses:
print(x.bit_length())  # 4
# help(x.bit_length)

# List methods
# list.append() modifies a list by adding an item to the end
# Pluto is a planet darn it!
planets.append('Pluto')

# list.pop() removes and returns the last element of a list
planets.pop()

# Searching list
# Where does Earth fall in the order of planets? We can get its index using the list.index method
print(planets.index('Mur'))
# If argument doesn't occure on the list we can get an error ValueError: 'Pluto' is not in list
# To avoid unpleasant surprises like this, we can use the in operator to determine whether a list contains a particular value

# Is Earth a planet?
print("Earth" in planets)  # False

# Tuples

# Tuples are almost exactly the same as list. They differ in just two ways
# 1. The syntax for creating them uses parentheses instead of square brackets
# t = (1, 2, 3)
t = 1, 2, 3
print(type(t))
print(t)

# 2. They cannot be modified (They are immutable)
# t[0] = 100
# TypeError: 'tuple' object does not support item assignment

# Tuples are often used for functions that have multiple return values
# For example, the as_integer_ratio() method of float objects returns a numerator and a denominator in the form of a tuple
x = 0.125
print(x.as_integer_ratio())  # (1, 8)
# These multiple return values can be individually assigned as follows
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)  # 0.125

# Finally we have some insight into the classic Stupid Python Trick for swapping two variables
a = 1
b = 0
a, b = b, a
print("a=", a, "b=", b)  # a= 0 b= 1

