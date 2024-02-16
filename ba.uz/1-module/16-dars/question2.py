n = 5
lst = []
s = 0
for i in range(n):
    a = int(input())
    lst.append(a)

for i in range(len(lst)):
    if lst[i] == 0:
        for j in range(i + 1, len(lst)):
            if lst[j] == 0:
                break
            s += lst[j]
        break

print(s)
