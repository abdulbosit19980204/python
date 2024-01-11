# Loops and List Comprehensions
# For and while loops, and a much-loved Python feature: list comprehension
from unittest import case

# Loops

# Loops are way to repeatedly execute some code. Here's an example
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ')

# The for loop specifies
#     * the variable name to use (in this case, planet)
#     * the set of values to loop over (in this case, planets)

# You use the word "in" to link them together
# The object to the right of the "in" can be any object that supports iteration. Basically, if it can be thought of as
# a group of things, you can probably loop over it. In addition to list, we can iterate over the elements of a tuple

multiplicands = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
product = 1
for multiplicand in multiplicands:
    product *= multiplicand

print(product)

# You can even loop through each character in a string
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
mas = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')

# range()

# range() is a function that returns a sequence of numbers it turns out to be very useful for writing loops
# For example, if we want to repeat some action 5 times
for i in range(5):
    print("Printed i=", i)

# while Loops
# The other type of loop in Python is a while loop, which iterates until some condition is met

i = 0
while i < 10:
    print(i, end=' ')
    i += 1
# 0 1 2 3 4 5 6 7 8 9

# The argument of the while loop is evaulated as a boolean statement, and the loop is executed until the
# statement evaluates to False

# List comprehensions

# List comprehensions are one of Python's most beloved and unique features. The easiest way
# to understand them is probably to just look at a few examples
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Here's how we would do the same thing without a list comprehension
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# We can also add an if condition:
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)  # ['Venus', 'Earth', 'Mars']

# (If you're familiar with SQL, you might think of this as being like a "WHERE" clause)
# Here's an example of filtering with an if condition and applying some transformation to the loop variable
# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)  # ['VENUS!', 'EARTH!', 'MARS!']

# People usually write these on a single line, but you might find the structure clearer when it's split up over 3 lines
loud_short_planets = [
    planet.upper() + '!'
    for planet in planets
    if len(planet) < 6
]
print(loud_short_planets)  # ['VENUS!', 'EARTH!', 'MARS!']

# List comprehensions combined with function like min, max and sum can lead to impressive one-line solutions for problems
# that would otherwise require several lines of code
# For example, compare the following two cells of code that do the same thing
nums = [5, -1, -2, 0, 3]


def count_negatives(nums):
    """Return the number of negative numbers in the given list.

        >>> count_negatives([5, -1, -2, 0, 3])
        2
        """
    n_negatives = 0
    for num in nums:
        if num < 0:
            n_negatives += 1
    return n_negatives


print(count_negatives(nums))  # 2


# Here's a solution using a list comprehension:
def count_positives(nums):
    return len([num for num in nums if num > 0])


print(count_positives(nums))


# Much better, right?
# Well if all we care about is minimizing the length of our code, the third solution is better still!

def count_negatives(nums):
    return sum([num < 0 for num in nums])  # this line count the negatives on the list


print(count_negatives(nums))  # 2


def sum_negatives(nums):
    return sum([num for num in nums if num < 0])


print(sum_negatives(nums))

