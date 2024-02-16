def power(a, n=2, c=0):
    if a == 1:
        print_power(n, c)
        return
    if a % n == 0:
        c += 1
        a /= n
    else:
        print_power(n, c)
        n += 1
        c = 0
    return power(a, n, c)


def print_power(n, c):
    if c == 1:
        print(n, end=" ")
    elif c > 1:
        print(f"{n} ^ {c}", end=" ")


power(4268880)
