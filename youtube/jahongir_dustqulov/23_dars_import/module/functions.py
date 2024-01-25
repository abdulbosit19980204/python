def qoshish(*args):
    s = 0
    for i in args:
        s += i
    return s


def kopaytirish(*args):
    s = 1
    for i in args:
        s *= i
    return s


def factorial(n):
    if n == 1 or n == 0:
        return 1
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s
