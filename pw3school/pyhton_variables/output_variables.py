#Output varibales
# The python print() function is often used to output variables

x="I am printing"
print(x)

# In the print() function, you output multipel variables, sperated by a comma:
x="Python"
y="is"
z="awesome"
print(x,y,z)

# we can use the + operator to output multiple variables

x="I am "
y="using"
z=" + operator"

print(x+y+z)

# For numbers, the + charcater works as a mathematical operator
x=5
y=3
print(x+y) # the result will be 8

# In the pyhton print() function, when you try to combine  a string and  a number with the + operator,
# at this situation we will get an error
#Example
x=5
y="5"
# print(x+y) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# to do this we can use type casting
print(x+int(y)) # 10 is printed