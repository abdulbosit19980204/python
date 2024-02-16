class Even_list:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            return None

        result = self.data[self.index]
        self.index += 1
        if result % 2 == 0 and self.index % 2 == 0:
            return result
        return next(self)


# lst = [1, 3, 2, 3, 4, 8, 12, 7, 7, 5, 6, 7, 8, 9]
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newObj = Even_list(lst)
print(next(newObj))
print(next(newObj))
print(next(newObj))
print(next(newObj))
print(next(newObj))
