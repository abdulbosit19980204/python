def fil_num(x):
    if str(x).isnumeric():
        return True
    return False


def fil_let(x):
    if str(x).isalpha():
        return True
    return False


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'ds', 'sdf', '4']
lts_let = list(filter(fil_let, lst))
lts_num = list(filter(fil_num, lst))
print(lts_let)
print(lts_num)
