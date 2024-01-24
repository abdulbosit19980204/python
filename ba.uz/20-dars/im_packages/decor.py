import time as t


def my_decor(func):
    start = t.time()

    def wrapper():
        print("start:", start)
        t.sleep(2)
        func()
        print("end:", t.time() - start)

    return wrapper
