# I fill you -4

# Instructions
# Combine this code and the code from the pervious step to obtain the code filling the whole array

n = 3
a = [0] * n
for i in range(n):
    a[i] = [2] * i + [1] + [0] * (n - i - 1)
# or, without for-cycle,
# a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
for row in a:
    print(' '.join([str(elem) for elem in row]))

