class Person:
    def __init__(self, a, b):
        self.name = a
        self.age = b
        self.is_alive = False

    def print_info(self):
        print(f"name: {self.name}, age: {self.age}")

    def __str__(self):
        return f"<name: {self.name}, age: {self.age}>"

    def __add__(self, other):
        return self.name+" "+other.name , self.age+other.age




p = Person("Azam", 12)
p1=Person("Tulkinov",12)
# print(len(p))
print(p1+p)
