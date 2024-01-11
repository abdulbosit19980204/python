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
# Like list, the type str has lots of very useful methods. I'll show just a few examples here

# ALL CAPS
claim = "Pluto is a planet!"
claim.upper()

# all lowercase
claim.lower()

# Searching for the first index of a substring
claim.index('plan')

print(claim.startswith(planet))

# false because of missing exclamation mark
claim.endswith('planet')

txt = "Pluto is a planet! My dog is named. Pluto is a planet!"

# Going between strings and lists: .split() and .join()
# str.split() turns a string into a list of smaller strings, breaking on whitespace by default. This is super useful for
# taking you from one big string to a list of words
words = claim.split()
print(words)  # ['Pluto', 'is', 'a', 'planet!']

# Occasionaly you'll want to split on something other than whitespace
datestr = '1956-01-31'
year, month, day = datestr.split('-')

# str.join() takes us in the other direction, sewing a list of sitrings up into one long string, using the string it was
# called on as a separator
print('/'.join([month, day, year]))

# Yes, we can put unicode characters right in our string literals :)
print(' 👏 '.join([word.upper() for word in words]))

# Building strings with .format()

# Python lets us concatenate strings with the + operator
planet + ', we miss you'
# position = 9
# "{}, you'll always be the {}th planet to me.".format(planet, position)
# So much cleaner! We call .format() on a "format string ", where the Python values we want to insert are represented with
# {} placeholders

# Notice how we didn't even have to call str() to convert from an int. format() takes care of that for us
# If that was all that format() dit, it would still be incredibly useful. But as it turns out, it can do a lot more. Here's
# just a taste

pluto_mass = 1.303 * 10 ** 22
earth_mass = 5.9722 * 10 ** 24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

# Dictionaries

# Dictionaries are builtin Python data structure for mapping keys to values
numbers = {'one': 1, 'two': 2, 'three': 3}

# In this case "one", "two", and "three" are the keys, and 1, 2 and 3 are their corresponding values.
# Values are accessed via square bracket syntax similar to indexing into lists and strings
print(numbers['one'])  # 1

# We can use the same syntax to add another key, value pair
numbers["four"] = 4
print(numbers)  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# Or to change the value associated with an existing key

numbers['four'] = "4"
print(numbers)  # {'one': 1, 'two': 2, 'three': 3, 'four': '4'}

# Python has dictionary comprehension with a syntax similar to the list comprehension we saw in the pervious tutorial
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)
# {'Mercury': 'M', 'Venus': 'V', 'Earth': 'E', 'Mars': 'M', 'Jupiter': 'J', 'Saturn': 'S', 'Uranus': 'U', 'Neptune': 'N'}

# The in operator tells us whether something is a key in the dictionary
'Saturn' in planet_to_initial  # True

# A for loop over a dictionary will loop over its keys
for k in numbers:
    print("{} = {}".format(k, numbers[k]))

"""
one = 1
two = 2
three = 3
four = 4
"""

# We can access a collection of all the keys or all the values with dict.keys() and dict.values() respectively
# Get all the initials, sort them alphabetically, and put them in a space-separated string.
' '.join(sorted(planet_to_initial.values()))

# They very useful dict.items() method lets us iterate over the keys and values of a dictionary siultaneously.
# In Python jargon, an item refers to a key, value pair

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(8), initial))
