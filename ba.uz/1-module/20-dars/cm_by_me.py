class CM:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __enter__(self):
        print("Starting")
        return self

    def __exit__(self, *args, **kwargs):
        print("Exit")

    def display(self):
        print(f"Name:{self.name}, Age:{self.age}")


with CM("Abdulbosit", 25) as student:
    student.display()
