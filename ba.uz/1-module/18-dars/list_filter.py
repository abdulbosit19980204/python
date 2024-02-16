def func(x):
    if x % 2 == 1:
        return True
    return False


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lts = list(filter(func, lst))
print(lst)
