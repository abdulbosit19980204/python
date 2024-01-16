# How do you input two dimensional array?
# But the easiest way is to use generator, creating a list of n elements, each of which is a list of m zeros

n = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
print(a)

