class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        print(self.name, self.price, self.quantity)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.quantity}'


class Phone(Item):
    def __init__(self, name, price, quantity, ram, color):
        super().__init__(name, price, quantity)
        self.ram = ram
        self.color = color

    def info(self):
        print(
            f"Name: {self.name}, Price: {self.price}$, Quantity: {self.quantity}, Ram: {self.ram}, Color: {self.color}")

    def all_price(self):
        return self.price * self.quantity


class Laptop(Phone):
    def __init__(self, name, price, quantity, ram, color, model, made):
        super().__init__(name, price, quantity, ram, color)
        self.model = model
        self.made = made

    def info(self):
        print(
            f"Name: {self.name}, \nPrice: {self.price}$, \nQuantity: {self.quantity}, \nRam: {self.ram}, \nColor: {self.color}, \nMade: {self.made}, \nModel: {self.model}")


phone1 = Phone("iPhone 15", 1500, 25, 6, "black")
laptop = Laptop("LENOVO", 650, 5, 4, "balck", "core i3", "China")
print("Over all price: ", phone1.all_price())
print("*" * 80)
phone1.info()
print("*" * 80)
laptop.info()
print("*" * 80)
