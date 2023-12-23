from random import randint


class Person:
    def __init__(self, a, b):
        self.name = a
        self.age = b

    def print_info(self):
        print(f"name: {self.name}, age: {self.age}")

    def __str__(self):
        return f"<name: {self.name}, age: {self.age}>"

    def __repr__(self):
        return f"<name: {self.name}, age: {self.age}>"


lst = []
n = int(input())
for i in range(1, n + 1):
    p = Person(f"name{i}", randint(20, 50))
    lst.append(p)

print(lst)
