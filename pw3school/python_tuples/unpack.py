# Python - Unpack Tuples
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple
fruitsTuple = ("apple", "banana", "cherry", "orange")

# But in Python we are also allowed to extract the values back into variables. This is called "unpacking"
(green, yellow, red, orange) = fruitsTuple
print(green)  # apple
print(yellow)  # banana
print(red)  # cherry
print(orange)  # orange

# The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the
# remaining values as a list

# Using Asterisk *

fruitsTuple = ("apple", "banana", "cherry", "orange", "apple", "banana", "cherry", "orange")
(green, yellow, red, *orange) = fruitsTuple
print(green) # apple
print(yellow) #banana
print(red) #cherry
print(orange) #['orange', 'apple', 'banana', 'cherry', 'orange']
(green, *tropic, red) = fruitsTuple
print(green) #apple
print(tropic) #['banana', 'cherry', 'orange', 'apple', 'banana', 'cherry']
print(red) #orange
