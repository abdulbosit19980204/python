# Creating Variables

# Python has no command for declaring a variable
# A variable is created the moment you first assign a value to it 
x=5 
y="Name"

print(x)
print(y)

# Variables do not need to be declared wiht any type, and can even change type after they have been set

x=4
print(type(x))
x="Hello"
print(type(x))

# CASTING

#  If you want to specify the data type of variable, this can be done with casting
x="4"
print(type(x))
y=int(x)
print(type(y))

# examples
x=str(3) # x will be '3'
y=int(3) # y will be 3
z=float(3) # z will be 3.0

# GET THE TYPE

x=3
y="Kim Min"

print(type(x))
print((type(y)))

# SINGLE OR Double QUOTES

# String variables can be declared either by using single or double quotes

x="John"
y='Jakhon'

print(type(x)) # type str
print(type(y)) # type str

# CASE-SENSITIVE
# variable names are case-sensitive
a=5
A=3
# A will not overwrite a. They are all alone variabel
