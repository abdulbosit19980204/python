"""
4. n x n matritsa berilgan. Shu matritsaning 2 ta diagonalidagi eng katta sonni toping
"""
n = int(input())
lst = []

for i in range(n):
    lst.append(input().split())

d1 = []
d2 = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if i == j:
            d1.append(lst[i][j])
        elif i + j == n - 1:
            d2.append(lst[i][j])

if max(d1) >= max(d2):
    print(max(d1))
else:
    print(max(d2))
