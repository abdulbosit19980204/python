class Private_iter:
    def __init__(self, data, skip_num):
        self.data = data
        self.skip_num = skip_num
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            return None

        result = self.data[self.index]
        self.index += self.skip_num
        return result


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mylst = Private_iter(lst, 2)
print(next(mylst))
print(next(mylst))
print(next(mylst))
print(next(mylst))
print(next(mylst))
print(next(mylst))

