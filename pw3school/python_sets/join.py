# Join Sets

# Join two sets
# There are several ways to join two or more sets in Python
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that
# inserts all     the items from one set into another

# The union() method returns a new set with all items from both sets
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {'a', 'b', 'c', 'f'}
set3 = set1.union(set2)
print(set3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 'b', 'c', 'f', 'a'}

# The update() method inserts the items in set2  into set1
set1.update(set2)
print(set1)#{1, 2, 3, 4, 5, 6, 7, 8, 9, 'f', 'b', 'c', 'a'}

# Note: Both union() and update() will exclude any duplicate items