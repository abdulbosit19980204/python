class Car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self._price = price

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}"

    # def __repr__(self):
    #     return f"Name: {self.name}, Color: {self}"


class NewCar(Car):
    def __init__(self, name, color, price, year, km):
        super().__init__(name, color, price)
        self.__year = year
        self._km = km
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Price:{self._price} , Year: {self.__year}, KM: {self._km}"


car1 = NewCar("Nexi", "white", 11000, 2000, 200000)
print(car1)
car1.year = 2022
car1.km = 1000
car1.price = 41000
print(car1)

lst = [car1, car1, car1, car1]
print(*lst)
