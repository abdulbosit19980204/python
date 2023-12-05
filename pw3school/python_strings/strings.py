#Strings

# Strings in python are surrounded by either single or double quotation marks.
a='hello'
b="World"
print(type(a))
print(type(b))

# Multiline Strings

# We can assign a multiline string to a variable by using three quotes

c = """Hello I am 
Abdulbosit, I am from Uzbekistan 
I am a student at TUIT university"""

print(c)

# or three single quotes

c='''
this 
is multiline 
variable
'''

print(c)

# Strings are Arrays
# Square brackets can be used to access elements of the string

a= "Hello world"
print(a[1]) # "e" is printed

# Looping through a String
# Since strings are arrays, we can loop thorugh  the characters in a strings, with a for loop

for x in "Hello world":
    print(x) # vertically printed

# String Length
# To get the length of a string, use the "len()" function

a="Hello strings"
print(len(a)) # 13 is printed

# CHeck String
# To check if a certain phrase or character is present in a string, we can use the keyword "in"

txt = "I am Abdulbosit. I am 27 years old"
print("years old" in txt)

# use it in an if statement
if '25' in txt:
    print("Yes")
else:
    print("Check your old")

# Check if NOT
# To check if a certain phrase or character is Not present in a string, we can use the keyword "not in"

print("Tuychiev" not in txt) # True

if "Tuychiev" not in txt:
    print("Enter your surname")
else:
    print("Welcome")

