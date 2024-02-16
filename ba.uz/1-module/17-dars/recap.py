a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(' '.join(str(i) for i in a))

lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
for i in lst:
    for j in i:
        print(j, end=' ')
    print()
