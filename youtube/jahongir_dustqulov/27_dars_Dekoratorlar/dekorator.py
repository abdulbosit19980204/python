def decor(func):
    def wrapper(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")

    return wrapper


@decor
def p(x, n=2):
    print(x ** n)


p(5)
p(3, 4)
p(4)
