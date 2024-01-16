# Processing a two-dimensional array: an example
# Note:
#   1. elements that lie above the main diagonal - are elements a[i][j] for which i<j
#   2. for elements below the main diagonal i>j
# Thus, we can compare the values i and j : the result of comparison determines the value of a[i][j]
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))

# This algorithm is slow: it uses two loops and for each pair (i,j) executes one or two if instructions. If we choose
# another algorithm, we will be able to do it without a conditional statement
