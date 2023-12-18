# Add Set items

# Add items
# Once a set is created, you can't change its items, but you can add new items.

# To add one item to a set use the add() method.

thisAddSet = {"appel", "banana", "cherry"}
thisAddSet.add("orange")
print(thisAddSet)  # {'orange', 'appel', 'banana', 'cherry'}

# Add Sets
# To add items from another set into the current set, use the update() method
thisFruitsSet = {"appel", "banana", "orange"}
thisNumbersSet = {1, 2, 3, 4}
thisFruitsSet.update(thisNumbersSet)
print(thisFruitsSet)  # {1, 2, 3, 'banana', 4, 'appel', 'orange'}

# Add any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object(tuples ,list, dictionaries)

thisSet = {"appel", "banana", "orange"}
thisList = [1, 2, 3, 4, 5, 6]
thisSet.update(thisList)
print(thisSet)  # {1, 2, 'orange', 3, 4, 5, 6, 'appel', 'banana'}
