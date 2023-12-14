# Python If...Else

# Python conditions and If statements
# Python supports the usual logical conditions from mathematics:

# An if statement is written by using the if keyword

a=33
b=55
if b>a:
    print("b katta") #b katta

# Indentation
# Python relies on indentation (whitespace at the beggining of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose.

# ELIF

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a,b = 33,33
if b>a:
    print("b katta")
elif a==b:
    print("a teng b ga") #a teng b ga

# ELSE
# The else keyword cathes anything which isn't caught by the preceding conditions

a,b = 23,55
if a%2==0 and b%2==0:
    print("Ikkalasi xam juft")
elif a%2==0 or b%2==0:
    print("ularni biri juft")
else:
    print("Toq sonlar kiritilgan") #Toq sonlar kiritilgan

# Short hand if
# If you have only one statement to execute, you can put it on the same line as the if statement

# One line if statement:
a=33
b=11
if a>b: print("a is katta") #a is katta

# Short hand if ELSE
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
# One line if else statement

a=2
b=330
print("A") if a>b else print("B") #B
# This technique is known as Ternary Operators , or Conditional Expressions.

# You can also have multiple else statements on the same line:

# One line if else statement, with 3 conditions:
a,b =330,330
print("A") if a>b else print("=") if a==b else print("B") #=

# And
# The and keyword is a logical operator, and is used to combine conditional statements:
a=220
b=22
c=500
if a>b and c>a:
    print("Both condition are true") #Both condition are true

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:

# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement

# The Pass Statement
"""
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statemetn to
avoid getting an error
"""
a=30
b=200
if b>a:
    pass
