# Snowflake
# Statement
# Given an odd number integer n , produce a two-dimensional array of size (n×n) .
# Fill each element with a single character string of "." . Then fill the middle row,
# the middle column and the diagnals with the single character string of "*" (an image of a snow flake).
# Print the array elements in (n×n) rows and columns and separate the characters with a single space.

n = int(input())
a = [['.'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = '*'
        elif i == (n // 2):
            a[i][j] = '*'
        elif i + j == n - 1:
            a[i][j] = '*'
        elif j==(n//2):
            a[i][j] = '*'
for i in a:
    print(*i)
