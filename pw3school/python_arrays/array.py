# Python Arrays
# Python doesn't have built-in support for Arrays, but Python List can be used instead
# To work with arrays in Python you will have to import a library, like the NumPy library

# Arrays are used to store multiple values in one single variable

cars = ['audi', 'bmw', 'subaru', 'damas']

# What is An Array?
# An array is a special variable, which can hold more than one value at a time
# If you have  a list of items, storing the cars in single variables could look like this

car1 = "damas"
car2 = "subaru"
car3 = "audi"
car4 = "subaru"

# However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
# The solution is an array
# An array can hold many values under  a single name, and you can access the values by referring to an index number

# Access the Elements of an Array
# You refer to an array element by refering  to the index number

# Get the value of the first array item
print(cars[0])  # audi

# Modify the value of the first array item
cars[0] = "Malibu"
print(cars)  # ['Malibu', 'bmw', 'subaru', 'damas']

# The Length of an Array
# Use the len() method to return the length of an array
print(len(cars))  # 4

# Looping Array elements
# You can use the for in loop to loop through all the elements of an array

# Print each item in the cars array
for x in cars:
    print(x)

"""
Malibu
bmw
subaru
damas
"""

# Adding Array Elements
# You can use the append() method to add an element to an array
# Add one more element to the cars array
cars.append("Honda")
print(cars)  # ['Malibu', 'bmw', 'subaru', 'damas', 'Honda']

# Removing Array Elements
# You can use the pop() method to remove an element from the array
# Delete the second element of the cars array
cars.pop(2)
print(cars)  # ['Malibu', 'bmw', 'damas', 'Honda']

# You can also use the remove() method to remove an element from the array
# Delete the element that has the value "damas"
cars.remove("damas")
print(cars)  # ['Malibu', 'bmw', 'Honda']
# The list's remove method removes the first occurrence of the specified value
