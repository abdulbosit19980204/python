from random import randint


class MobileShop():
    def __init__(self, name, phoneMark, price, quantity):
        self.name = name
        self.phoneMark = phoneMark
        self.price = price
        self.quantity = quantity

    def soldPrice(self, number):
        return self.price * number

    def __str__(self):
        # return "Welcome to Mobile shop"
        return f"Mobile shop: name={self.name}, phoneMark={self.phoneMark}, price={self.price}, quantity={self.quantity}"

    def __repr__(self):
        return f"<Mobile shop: name={self.name}, phoneMark={self.phoneMark}, price={self.price}, quantity={self.quantity}>"

    @staticmethod
    def tax(quantity, price):
        return quantity * 0.12 * price


shop1 = MobileShop("Olcha.uz", "iPhone 14 Pro", 14940000, 25)
print(shop1)  # Welcome to Mobile shop
print(f"Mobile shop : {shop1}, phone Mark : {shop1.phoneMark}, price : {shop1.price}")
# Mobile shop : Welcome to Mobile shop, phone Mark : iPhone 14 Pro, price : 14940000
n = int(input("Enter how many buy: "))
buyPrice = shop1.soldPrice(n)
print(f"You are going to buy {n} {shop1.phoneMark}. You need to pay about {buyPrice} UZS")
# I am going to  buy 2 iPhone 14 Pro. I need to pay about 29880000 UZS

lst = []
n = int(input("Enter the number of shops: "))
for i in range(1, n + 1):
    shop = MobileShop(f"Shop{i}", f"iPhone {randint(10, 16)} Pro", randint(10000000, 30000000), randint(10, 100))
    lst.append(shop)
print(lst)

sortType = input("input the sroted type price/phoneMark/name: ")
if sortType not in ["price", "phoneMark", "name"]:
    print("Make sure it is correct, there isn't such field")
    raise ValueError("You need to input one of these price/phoneMark/name: ")

lst.sort(key=lambda x: getattr(x, sortType))
# the getattr() function will be used to dynamically access the attribute specified by sortType.
# lst.sort(key=lambda x: x.price)
print(lst)
print("You have about ", lst[0].tax(lst[0].quantity, lst[0].price), " sum tax")
# You have about  139779603.6  sum tax
