# I fill you -3
# Here's another solution, which repeats lists to build the next rows of the list. The i -th line of
# the list consists of "i" numbers 2, followed by one integer 1, followed by n-i-1 zeros

# Instructions
# Combine this code and the code from the previous step to obtain the code filling the whole array


n = 7
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = 2
    a[i][i] = 1
    for j in range(i + 1, n):
        a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))
