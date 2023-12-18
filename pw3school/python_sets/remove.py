# Remove Set Items

# To remove an item in a set, use the remove(), or the discard() method

# Remove "banana" by using the remove() method.
thisSet = {"apple", "banana", "cherry"}
thisSet.remove("banana")
print(thisSet)  # {'apple', 'cherry'}

# Note: If the item to remove does not exist, remove() will raise an error
# Remove "banana" by using the discard() method:

thisSet = {"apple", "banana", "cherry"}
thisSet.discard("banana")
print(thisSet)  # {'apple', 'cherry'}

# Note: If the item to remove does not exsist, discard Not raise an error
# You can also use the pop() method to remove an item, but this  method will remove a random item, so you cannot be sure what item that gets removed

# The return value of the pop() method is the removed item.
thisSet = {"apple", "banana", "cherry"}
thisSet.pop()
print(thisSet)
# {'apple', 'banana'}
# {'banana', 'cherry'}
# Note: Sets are unordered, so when using the pop() method, you don't know which item that gets removed.

# The clear() method  empties the set
thisSet.clear()
print(thisSet) #set()

# The del keyword will delete the set completely
del thisSet
print(thisSet) #NameError: name 'thisSet' is not defined
