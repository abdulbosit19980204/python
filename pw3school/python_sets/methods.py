# Set Methods

# Python has a set of built-in methods that you can use on sets

# add()
# clear()
# copy()
# difference()
# difference_update()
# discard()
# intersection() - Return a set, that  is the intersection of two other sets
# intersection_update()
# isdisjoint() - Return whether two sets have a intersection or not
x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
y = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99}
print(y.intersection(x))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# issubset() -  Returns whether another set contains this set or not
z = y.intersection(x)
print(z)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(z.issubset(x))  # True

# issupperset() - Returns whether this set contains another set or not
# pop() - Removes an element from the set
# remove() - Removes the specified element
# symmetric_difference() -Returns a set with the symmetric difference of two sets
# symmetric_difference_update()  - insert the symmetric difference from this set and another
# union() - Return a set containing the union of sets
# update() - Update the set with the union of this set and others