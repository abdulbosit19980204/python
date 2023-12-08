# Change item value

# To change the value of a specific item, refer to the index number:

thisList = ['apple', 1, 2, 2, 4]
thisList[0] = 1
print(thisList)

# Change a Range of Item Values 
"""
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where 
you want yo insert the new values
"""

thisRangeLisit = [1, 2, 3, 4, 5]
thisRangeLisit[1:3] = [1, 1]
print(thisRangeLisit)  # [1, 1, 1, 4, 5]

# If we insert more items than we replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thisList = [1, 2, 5, 7, 8, 9, 11]
thisList[2:5] = [10, 28, 11, 12, 15, 17]
print(thisList)  # [1, 2, 10, 28, 11, 12, 15, 17, 9, 11]

# If we insert less than we replace, the new items will be inserted where you specified, and the remaining items will move accordingly

thisLessList = [1, 2, 3, 4, 5, 6]
thisLessList[1:5] = [11]
print(thisLessList)  # [1, 11, 6]

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:
thisInsertableList = [1, 2, 3, 4, 5]
thisInsertableList.insert(2, 111)
print(thisInsertableList)  # [1, 2, 111, 3, 4, 5]

