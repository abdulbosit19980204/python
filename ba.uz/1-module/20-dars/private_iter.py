class MyIter:
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

        return result


lst = [1, 2, 3, 4]

myiter = MyIter(lst)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

