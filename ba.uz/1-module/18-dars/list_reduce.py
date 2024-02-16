from functools import reduce


def func(x, y):
    return x * y


lst = [int(i) for i in input().split()]  # 1 2 3 5

print(reduce(func, lst))
