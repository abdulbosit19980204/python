lst = [int(i) for i in input().split()]

kopaytma = 1
for i in range(len(lst)):
    kopaytma *= lst[i]
print(kopaytma)

