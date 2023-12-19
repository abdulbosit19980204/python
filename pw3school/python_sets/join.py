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
print(set1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 'f', 'b', 'c', 'a'}

# Note: Both union() and update() will exclude any duplicate items

# Keep Only the Duplicates
# The intersection_update() method will keep only the items that are present in both sets

# Keep the items that exist in both set x, and set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)  # {'apple'}

# The intersection() method will return a new set, that only contains the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)  # {'apple'}

# Keep all, But Not the Duplicates

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)  # {'banana', 'microsoft', 'google', 'cherry'}

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)  # {'banana', 'google', 'cherry', 'microsoft'}

