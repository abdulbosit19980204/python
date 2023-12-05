# Escape character

# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert

# An example of an illegal character is a double quote inside a string  that is surrounded by double quotes:

txt = "We are the so-called \"Vikings\" from the north"  # We are the so-called "Vikings" from the north
print(txt)

# Escape characters
# Other escape characters used in Python

# "\'" - single quote
name = "Abdulbosit"
text = "Hello \'{}\'"
print(text.format(name))  # Hello 'Abdulbosit'

# Back slash - \\
print("a\\2")  # a\2
print("sin\\cos")
# New line - \n
# Carrige Return - \r
print("Hello\rWorld")
