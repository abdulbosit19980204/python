lst = input().split()


def x_power(n):
    if  int(n) == 0:
        return 'Null'
    elif int(n) % 2 == 0:
        return 'J'
    else:
        return "T"


newLst = list(map(x_power, lst))
print(newLst)
