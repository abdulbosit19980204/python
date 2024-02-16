lst = [int(i) for i in input().split()]

new_lst = [i ** 2 for i in lst]
print(new_lst)

# ***********************************************

for i in range(len(lst)):
    lst[i] = lst[i] ** 2

print(lst)

# ***********************************************

