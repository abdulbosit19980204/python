"""
6. Item classini yozing, undan voris olib Book classini yarating. Har bir classda kamida
4 tadan attribute va kamida 2 tadan method bo’lsin. Magic method qo’shilsa afzalroq
"""


class Item:
    def __init__(self, id, name, number, type):
        self.id = id
        self.name = name
        self.number = number
        self.type = type

    def get_info(self):
        print(f"{self.id} {self.name} {self.number}")

    def __str__(self):
        print(f"{self.type} =>{self.name}: {self.number}")


class Book(Item):
    def __init__(self, id, name, number, type, sold, price):
        super.__init__(self, id, name, number, type)
        self.sold = sold
        self.price = price

    def tax(self):
        print(f"Siz {(self.price * self.sold) * 0.12} so'm soliq to'lashingiz kerak")

    def __add__(self, other):
        print(
            f"Jami sotildi: {self.sold + other.sold} \nUmumiy narxi: {self.sold * self.price + other.sold * other.price}")

    def __repr__(self):
        return f"{self.number}: {self.sold * self.price}"


book1 = Book(1, "O'tkan kunlar", 25, "Roman", 250, 50000)
book1.get_info()
book1.tax()
print(book1)
