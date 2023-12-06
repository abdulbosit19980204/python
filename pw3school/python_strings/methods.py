# Python - String Methods

# Python has a set of built-in methods that you can use on strings.

# capitalize()

a = "text"
print(a.capitalize())  # Text

# casefold()
a = "Text"
print(a.casefold())  # text

# center()
a = "Text"
print(a.center(20))  # "        Text  "

# Count()
a = "I am Abdulbosit"
print(a.count("b"))  # 2

# endswith()
a = "I am Abdulbosit"
print(a.endswith("it"))  # True

# index()- Searches the string for a specified value and returns the position of where it was found
print(a.index("A"))  # 5
print(a.index("I"))  # 0

# isalnum - returns True if all characters in the string are alphanumeric
a = "121545487"
print(a.isalnum())  # True
a="I am years old 25"
print(a.isalnum()) # False

# isalpha() - returns true if all characters in the string are alphabet
a="I am Abdulbosit"
print(a.isalpha()) #False - because of there are two whitespace
a="441 I am Uzbek"
print(a.isalpha()) #False - in addition, number and whitespace
a="Abdulbosit"
print(a.isalpha()) #True - this is only alphabetic

