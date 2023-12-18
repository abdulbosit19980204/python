# Python Sets


# Set
# Set are used to store multiple items in a single variable.
# A set is a collections which is unordred, unchangable*, and unindexed
# * Set items are unchangable, but you can remove items and add new items

# Sets are written with curly brackets
myset = {"apple", "banana", "pear", "orange"}
print(myset)  # {'banana', 'pear', 'apple', 'orange'}

# Set Items
# Set items are unordred, unchangable, and do not allow duplicate values

# Unordred
# Unordered means that the items in a set do not have s defined order
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key

# Duplicates Not Allowed
# Sets cannot have two items with the same valu

thisSet = {"apple", "banana", "apple", "orange", "banana"}
print("thisSet =>", thisSet)  # thisSet => {'banana', 'apple', 'orange'}

# Note values True and 1 are considred the same value in sets, and are treated as duplicates

# Ture and 1 is considred the same value
# False and 0 is considered the same value:
thisMultiset = {"apple", "banana", True, False, 0, 1, 2, 3}
print(thisMultiset)  # {False, True, 2, 3, 'apple', 'banana'}

# Get the length of a Set
# To determine how many items a set has, use the len() function
thisSets = {"apple", "banana", "apple", "banana", "orange", "banana", 1, True}
print(len(thisSets))  # 4

# Set Items - Data types

# Set items can be of any data type
# String, int and boolean data types

set1 = {"apple", "banana", "apple"}
set2 = {1, 2, 3}
set3 = {True, False, True}
print(type(set1))

# A set can contain different data types
setMix = {"apple", "banana", 1, 2, 3, False}

# The set constructor
# It is also possible to use the set() constructor to make a set
madeSet = set(("apple", "banana", "apple", "list"))
print(madeSet)
print(type(madeSet))
"""
{'list', 'banana', 'apple'}
<class 'set'>
"""
