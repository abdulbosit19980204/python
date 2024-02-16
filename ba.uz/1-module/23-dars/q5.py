# 5. Ikki ro'yxatni quyidagi tartibda birlashtiring
from functools import reduce

list1 = ["1", "2"]
list2 = ["3", "4"]
# output = ["13", "24"]
lst = [list(a) for a in zip(list1, list2)]


def func(x, y):
    return x + y


a = []
for i in lst:
    a.append(reduce(func, i))
print(a)

l = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if i == j:
            l.append(list1[i] + list2[j])
print(l)
