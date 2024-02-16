class Car:
    def __init__(self, name, price, model, year):
        self.name = name
        self.price = price
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car name: {self.name} model: {self.model} year: {self.year} "

    def get_price(self):
        return f"Car name: {self.name} price: {self.price}"


car1 = Car("Ford", 20000, "Mercedes", 2023)

print(car1)
print(car1.get_price())
