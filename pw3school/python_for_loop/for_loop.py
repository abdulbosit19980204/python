# Python for Loops

# A for loop is used for iterating over a squence
# (that is either a list, a tuple, a dictionary, a set, or a string )

# Print each fruit in a fruit list
fruits=["olma","behi","gilos","mandarin"]
for x in fruits:
    print(x, end=" ") #olma behi gilos mandarin

# The for loop does not require an indexing variable to set beforehand

# Looping Through a String
# Even string are iterable objects, they contain a sequence of characters
# Loop through the letters in the word "banana"

for x in "banana":
    print(x, end=" ") #b a n a n a

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
numbers = [ 1,2,3,4,5,6,7,8,9]
for i in numbers:
    print(i, end=" ") #1 2 3 4 5
    if i==5:
        break

# Exit the loop when x is 5, but this time the break comes before the print:
for i in numbers:
    if i==5:
        break
    print(i, end=" ") #1 2 3 4

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
for i in numbers:
    if i==5:
        continue
    print(i, end=" ") #1 2 3 4 6 7 8 9

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function.
for x in range(10):
    print(x, end=" ") #0 1 2 3 4 5 6 7 8 9

# Else if For loop

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for x in range(6):
    print(x, end=" ")
else:
    print("It is end of loop") # 0 1 2 3 4 5 It is end of loop
