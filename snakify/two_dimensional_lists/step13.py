# Processing a two-dimensional array: an example
# Suppose you are given a square  array (an array of n rows and n columns ) And suppose you have to set elements of the
# main diagonal equal to 1 (that is, those elements a[i][j] for which i==j), to set elements above than that diagonal
# equal to 0, and to set elements below that diagonal equla to 2. That is, you need to produce the array like that
# the array you can see on the code side

# You can produce such an array manually by setting a[0][0] =1, a[0][1]=0 and so on, but you won't do it manually for arrays
# of 10000 rows and 10 columns, which are often the case
#   This is example for <code>n==4</code>.
#
#   1 0 0 0
#   2 1 0 0
#   2 2 1 0
#   2 2 2 1

n = int(input())

a = [[0 for j in range(n)] for i in range(n)]
# for row in a:
#     # print(row)

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 1
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 0
    print(a[i])
