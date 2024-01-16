# Nested loops
# To process 2-dimensional array, you typically use nested loops. The first loop iterates through the row number,
# the second loop runs through the elements inside of a row. For example, that's how you display two-dimensional
# numerical list on the screen line by line, separating the numbers with space

a = [[1, 2, 3], [4, 5, 6]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
print()
for i in a:
    for j in i:
        print(j, end=' ')

