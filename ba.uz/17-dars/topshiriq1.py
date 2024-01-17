"""
1 2 3
4 5 6
7 8 9
"""
# l1 = [int(i) for i in input().split()]
# l2 = [int(i) for i in input().split()]
# l3 = [int(i) for i in input().split()]
# lst = [l1, l2, l3]
# Horizontal
lst = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
for ind, row in enumerate(lst):
    print(ind + 1, "- qator s =", sum(row))

# Vertical
for i in range(len(lst)):
    s = 0
    for j in range(len(lst)):
        s += lst[j][i]
    print(i + 1, "-satr s =", s)
s = 0
rs = 0
for i in range(len(lst)):
    # s = 0
    for j in range(len(lst)):
        if i == j:
            s += lst[i][j]
        if i + j == len(lst) - 1:
            rs += lst[i][j]
print("s=", s, "rs = ", rs)

