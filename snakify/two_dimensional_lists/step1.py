# Nested lists: processing and printing

# In real-world tasks you often have to store rectangular data table. [say more on this!]
# Such tables are called "matrices" or two-dimensional arrays. In Python any table can be represented as a list of lists
# (a list, where each element is in turn a list) For example, here's the program that creates a numerical table with two
# rows and three columns, and then makes some manipulations with it

# The first element of "a" here -a[0] -is a list of numbers [1,2,3]. The first element of this newlist is a[0][0] ==1
# morever, a[0][1] = 2 ...

a = [[1, 2, 3], [4, 5, 6]]
print(a[0])
print(a[1])
print("len a = ", len(a))
print(a[0][0])
print(a[1][0])

