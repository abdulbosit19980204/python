# The right way
# Thus, a two-dimensional list cannot be created simply by repeating a string. What to do..?

# A possible way: you can create a list of n elements (say, of n zeros) and then make each of the elements a link to another
# one-dimensional list of m elements
n = 3
m = 3
a = [[0] * n] * m
print(a)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 5
print(a)  # [[5, 0, 0], [5, 0, 0], [5, 0, 0]]

# or

n = 3
m = 3
a = [0] * n
for i in range(n):
    a[i] = [0] * m
a[0][0] = 5
print(a)  # [[5, 0, 0], [0, 0, 0], [0, 0, 0]]

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a[0][0] = 5
print(a)
