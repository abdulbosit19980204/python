"""
6. Item classini yozing, undan voris olib Book classini yarating. Har bir classda kamida
4 tadan attribute va kamida 2 tadan method bo’lsin. Magic method qo’shilsa afzalroq
"""


class Item:
    def __init__(self, iid, name, number, itype):
        self.iid = iid
        self.name = name
        self.number = number
        self.itype = itype

    def get_info(self):
        print(f"{self.iid} {self.name} {self.number}")

    # def __str__(self):
    #     print(f"{self.itype} =>{self.name}: {self.number}")


class Book(Item):
    def __init__(self, iid, name, number, itype, sold, price):
        super().__init__(iid, name, number, itype)
        self.sold = sold
        self.price = price

    def tax(self):
        print(f"Siz {(self.price * self.sold) * 0.12} so'm soliq to'lashingiz kerak")

    def __add__(self, other):
        print(
            f"Jami sotildi: {self.sold + other.sold} \nUmumiy narxi: {self.sold * self.price + other.sold * other.price}")

    def __repr__(self):
        return f"{self.number}:{self.name} {self.sold * self.price}"


book1 = Book(1, "O'tkan kunlar", 25, "Roman", 250, 50000)
book1.get_info()
book1.tax()
print(book1)
