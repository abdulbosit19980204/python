# Nested lists: the creation
# Suppose that two numbers are given: the number of rows of n and the number of columns m. You must create a list of
# size nxm, filled with, say zero

# The obvious solution appears to be wrong
# This can be easily seen if you set the value of a[0][0] to 5, and then print  the value of a[1][0] - it will also be equal
# to 5. The reason is, [0]*m returns just a reference to a list of m zeros, but not a list. The subsequent repeating
# of this element creates a list of n items that all reference to the same list , so all rows in the the resulting list are
# actually the same string

# Using our visualizer, keep track of the id of lists. If two lists have the same id number, it's actually the same list memory

m = 3
n = 3
a = [[0] * m] * n
print(a)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 5
print(a)  # [[5, 0, 0], [5, 0, 0], [5, 0, 0]]

