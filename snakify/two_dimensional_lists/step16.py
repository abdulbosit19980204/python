# I fill you -2
# Think of the elements above the main diagonal; they must be filled with zeros. To make this, for each row with the number
# i you need to asign a value to a[i][j] for j=i+1,...,n-1. To do that you need nested loops, look at the code section
# By analogy, as you see, for j less than i the elements a[i][j] are set equal to 2

# Instruction
# Combine this code and the code from the previous step to obtain the code filling the whole array

n = 3
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][i] = 1
for i in range(n):
    for j in range(i + 1, n):
        a[i][j] = 0

for i in range(n):
    for j in range(0, i):
        a[i][j] = 2
for row in a:
    print(' '.join([str(elem) for elem in row]))



