# Remove Specified Item

# The remove() method removes the specified item

thisRemoveList = [1,2,3,4,5,6,7,8,9]
thisRemoveList.remove(1)
print(thisRemoveList) #[2, 3, 4, 5, 6, 7, 8, 9]

# If there are more than one item with the specified value, the remove() method removes the first occurance

thisMultiRemList = [1,2,3,4,5,7,8,9,1,2,1,2]
thisMultiRemList.remove(1)
print(thisMultiRemList) #[2, 3, 4, 5, 7, 8, 9, 1, 2, 1, 2]

# Remove Specified Index

# The pop() method removes the specified index

thisPopList = [1,2,3,4,5,6]
thisPopList.pop(3)
print(thisPopList) #[1, 2, 3, 5, 6]

# if you do not specified the index, the pop() method removes the last item.
thisNotSpecPopList = [1,2,3,4,5,6,7,8]
thisNotSpecPopList.pop()
print(thisNotSpecPopList) #[1, 2, 3, 4, 5, 6, 7]

# The del keyword also remove the specified index

thisDelList = [1,2,3,4,5,6,7,8]
del thisDelList[1]
print(thisDelList) #[1, 3, 4, 5, 6, 7, 8]

# The del keyword can also delete the list completly
thisCompletlyDelList = [1,2,3,4,5,6,7,8]
del thisCompletlyDelList
# print(thisCompletlyDelList) #NameError: name 'thisCompletlyDelList' is not defined

# Clear the List
# The clear() method empties the list.
# The list still  remains, but it has no content

thisClearList = [1,2,3,4,5,6,7,8]
thisClearList.clear()
print(thisClearList) #[]

