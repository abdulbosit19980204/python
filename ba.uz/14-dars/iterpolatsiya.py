class Car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}"

    # def __repr__(self):
    #     return f"Name: {self.name}, Color: {self}"


class NewCar(Car):
    def __init__(self, name, color, price, year, km):
        super().__init__(name, color, price)
        self.__year = year
        self.__km = km

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Price:{self.price} , Year: {self.__year}, KM: {self.__km}"

    def change_km(self, new_km):
        print()
        if new_km > 0:
            self.__km = self.__km + new_km
            return self.__km
        else:
            self.__km = self.__km
            return "Kamaytirishga urinish"
            # return self.__km


car1 = NewCar("Nexi", "white", 12000, 2020, 25000)
car2 = NewCar("Nexi", "white", 12000, 2020, car1.change_km(-100))
car3 = NewCar("Nexi", "white", 12000, 2020, car1.change_km(100))

print(car1)
print(car2)
print(car3)


