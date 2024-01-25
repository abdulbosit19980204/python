def summing(*args):
    if len(args) == 0:
        return 0
    lst = list(args)
    del lst[0]
    return args[0] + sum(lst)


x = summing(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(x)
