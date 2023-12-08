# Add List Items

# To add an item to the of the list, use the append() method:

# Using the append() method to append an item
thisAppList = [1,2,3,4,5,6]
thisAppList.append(22)
print(thisAppList) #[1, 2, 3, 4, 5, 6, 22]

# Insert Items
# To insert a list item at specified index, use the insert() method.

# The insert() method inserts an item at the specified index:

thisInsertList = [1,2,3,4,5,6]
thisInsertList.insert(1,"250")
print(thisInsertList) #[1, '250', 2, 3, 4, 5, 6]

# Extend List
# To append elements from another list to the current list, use the extend() method.

thisExtendedList1 = [1,2,3,4,5,6]
thisExtendedList2 = [11,12,13,14,15,16]
thisExtendedList1.extend(thisExtendedList2)
print(thisExtendedList1) #[1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16]

# Add Any Iterable
# The extend() method does not  have to append lists, you can add any iterable object(tuples, sets, dictionaries etx)
thisItereableList =[1,2,3,4,5,6,7,8]
thisTuple = ("kive", "banan")
thisItereableList.extend(thisTuple)
print(thisItereableList) #[1, 2, 3, 4, 5, 6, 7, 8, 'kive', 'banan']

