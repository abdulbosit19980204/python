# I fill you -1
# Instruction
# Write such a loop that would fill the diagonal elements( the elements a[i][j]) with 1

n = int(input())
a = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

for row in a:
    print(*row)
print('*' * 50)

a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][i] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))
