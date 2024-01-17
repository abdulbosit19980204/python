# Chess board

# Statement
# Given two numbers n  and m . Create a two-dimensional array of size (n×m)
# and populate it with the characters "." and "*" in a checkerboard pattern.
# The top left corner should have the character "." .

n, m = input().split()
m = int(m)
n = int(n)

a = [['.'] * m for _ in range(n)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if i % 2 == 0:
            if j % 2 == 1:
                a[i][j] = '*'
        else:
            if j % 2 == 0:
                a[i][j] = '*'
for i in a:
    print(*i)
