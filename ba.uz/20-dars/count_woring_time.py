import time


class MyIter:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            return None

        result = self.data[self.index]
        self.index += 1
        return result

    def kvadrat(self):
        print(self.data[self.index] ** 2)

    def __enter__(self):
        self.start = time.time()
        print("Start: ", self.start)
        return self

    def __exit__(self, *args, **kwargs):
        print("Exit:", time.time() - self.start, end=" ")


lst = [1, 2, 3, 4, 5, 7, 9]
with MyIter(lst) as inter:
    print(next(inter))
    print(next(inter))
    time.sleep(5)
    print(next(inter))
    time.sleep(10)
    print(inter.kvadrat())
    print(next(inter))
    print(inter.kvadrat())
