# Maximum
# Statement
# Given two integers representing the rows and columns (m×n) , and subsequent m  rows of n
# elements, find the index position of the maximum element and print two numbers representing the index (i×j)
# or the row number and the column number. If there exist multiple such elements
# in different rows, print the one with smaller row number.
# If there multiple such elements occur on the same row, output the smallest column number.
m = 5
n = 3
max = 0
from random import randint

a = [[randint(1, 100) for i in range(m)] for j in range(n)]
for i in a:
    print(i)
for row in a:
    for i in row:
        if i > max: max = i
print(max)
# ******************************************************************************

max = 0
i = 0
j = 0
for k in range(len(a)):
    for g in range(len(a[k])):
        if int(a[k][g]) > max:
            i = k
            j = g
            max = a[k][g]

print(n, m, max)
# *****************************************************************************

n, m = input("m= , n =").split()

a = [input().split() for i in range(int(n))]
for i in a:
    print(i)
max = int(a[0][0])
i = 0
j = 0
for k in range(len(a)):
    for g in range(len(a[k])):

        if int(a[k][g]) > max:
            max = int(a[k][g])
            i = k
            j = g
print(i, j)
