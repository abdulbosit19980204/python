# Nested Generators -1
# You can use nested generators to create two-dimensional arrays, placing the generator of the list which is a string inside
# the generator of all the strings. Recall that you can create a list of n rows and m columns using the generator
# which creates a list of n elements, where each element is a list of m zeros

# As usual, you can replace the loop with the generator:
m = 3
n = 8
a = [[0] * m for i in range(n)]
print(a)

