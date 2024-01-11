# Strings and Dictionaries

# Working with strings and dictionaries, two fundamental Python data types

# Strings
# One place where the Python language really shines is in the manipulation of strings. String manipulation patterns
# come up often in the context of data science work

# String syntax
# You've already seen plenty of strings in examples during the previous lessons, but just to recap, strings in Python can
# be defined using either single or double quotations. They are functionally equivalent
x = 'Pluto is a planet'
y = "Pluto is a planet"
x == y

# Double cuotes are convenient if you  string contains a single quote character.
# Similarly, it's easy to create a string that contains double-quotes if you wrap single quotes around
print("Pluto's a planet!")
print('My dog is named "Pluto"')

# String are squences
# Strings can be thought of as squences of characters. Almost  everything we've seen that we can do to a list, we can also
# do to a string
# Indexing
planet = 'Pluto'
planet[0]

# Slicing
planet[-3:]

# How long is this string?
len(planet)

# Yes, we can even loop over them
[char + '! ' for char in planet]

# But a major way in which they differ from lists is that they are immutable. We can't change them
# planet[0] = 'B'

# String methods
Like list, the type str has lots of very useful methods. 