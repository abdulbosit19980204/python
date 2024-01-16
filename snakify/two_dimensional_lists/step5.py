# Problem: sum all the elements
# This is how you can use 2 nested loops to calculate the sum of all the numbers in the 2-dimensional list
# Or the same with iterating by elements, not by the variables i and j

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print("s=", s)

s = 0
for row in a:
    for elem in row:
        s += elem
print("elem s = ", s)

