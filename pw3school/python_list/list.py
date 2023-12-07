# Python List

# List are used to store multiple items in a single variable

# Lists are creted using """square brackets""":

thisList = ['a','b',1,2]
print(thisList) #['a', 'b', 1, 2]

# List Items

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item index [0], the second item has index [1] etc.

# Ordered

# When we say that list are ordred, it means that the items have a difined order, and that order will not change
# If you add new items to a list, the new items will be placed at the end of the list

# Changeable
# The list is changeable, meaning that we can change, add and remove items in a list after it has been created

# Allow duplicates
# Since lists are indexed, list can have items with the same value:

dupList = ["apple","banan","apricot", "sugar","apple","bread"]
print(dupList) #all elements are printed

# List length
# To detirmine how many items a list has, use the len() function.

lenList=["hello",1,2,4,22.122,"Abdulbosit",False]
print(lenList) #['hello', 1, 2, 4, 22.122, 'Abdulbosit', False]
print(len(lenList)) #7

# List Items

# List Items can be of any data type:
# List can contain different data types:

# Type
print(type(lenList)) #<class 'list'>

# List constructor
conList = list(("appel", "banan","shakar"))
print(conList) #['appel', 'banan', 'shakar']


