class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def __enter__(self):
        print("start")
        return self

    def __exit__(self, *args, **kwargs):
        print("exit")


with Student("John", 54) as s:
    s.display()
