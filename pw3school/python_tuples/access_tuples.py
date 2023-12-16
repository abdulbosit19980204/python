# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets

thisTuple = (1, 2, 3, 4, 5)
print(thisTuple[2])#3

# Negative indexing
# Negative indexing means start from the end.

# -1 refers to the last item, -2 refers to the second lst item etc.
print(thisTuple[-1]) #5

# Range of Index
# When specifying a range, the return value will be a new tuple with the specified items
thisFruitsTuple = ('apple', 'banana', 'orange','kiwi','cherry')
print(thisFruitsTuple[2:5]) #('orange', 'kiwi', 'cherry')

# By leaving out the start value, the range will start at the first item
print(thisFruitsTuple[:2])#('apple', 'banana')

# By leaving out the end value, the range will go on to the end of the tuple
print(thisFruitsTuple[2:]) #('orange', 'kiwi', 'cherry')

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple

print(thisFruitsTuple[-4:-1]) #('banana', 'orange', 'kiwi')

# Check IF item Exists
# To detirmaine if a specified item is present in a tuple use the in keyword
if "apple" in thisFruitsTuple:
    print("Yes")
else:
    print("No")

