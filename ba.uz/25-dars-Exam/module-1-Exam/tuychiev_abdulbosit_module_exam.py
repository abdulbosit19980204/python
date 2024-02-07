"""
2. n butun soni kiritiladi, shu son 2 ning darajasi yoki yo’qligini aniqlovchi funktsiya
yozing (recursion bilan ishlansa afzalroq)
Input: n = 16
Output: true
"""

n = int(input("Input the checking number: n="))
s = 0


def power_2(n):
    if n == 1:
        return 1
    elif n % 2 != 0:
        return 1
    else:
        n //= 2

    power_2(n)


print(power_2(n))

# **************************************************************

"""
4. n x n matritsa berilgan. Shu matritsaning 2 ta diagonalidagi eng katta sonni toping
"""
n = int(input())
lst = []

for i in range(n):
    lst.append(input().split())

d1 = []
d2 = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if i == j:
            d1.append(lst[i][j])
        elif i == j + 2 or i + 2 == j:
            d2.append(lst[i][j])

if max(d1) >= max(d2):
    print(max(d1))
else:
    print(max(d2))

# ************************************************************************
"""
5. Memoizatsiya/keshlash dekoratori. Funktsiya natijalarini keshlaydigan dekorator
yozing. Kesh natijalarni funksiya parametrlari asosida saqlashi kerak, shunda funksiya
yana bir xil parametrlar bilan chaqirilsa, funksiyani qayta bajarish o‘rniga keshlangan
natija qaytariladi.
"""

d = []


def saved_kesh():
    def wrapper(func):
        d.append(func)

    return wrapper


@saved_kesh
def add(a, b):
    return a + b


add(4, 5)
add(3, 5)

print(d)

# *********************************************************************
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

# *******************************************************************
"""
7. Kitirilgan N butun sonining ichida 5 raqami qatnashgan yoki qatnashmaganligini
aniqlang
"""

n = int(input())


def length(n):
    return len(str(n))


l = length(n)

while l > 1:
    l = length(n)
    if n // 10 * l == 5:
        print("True")
    elif l != 0 and n // 10 != 5:
        print("False")
    n //= 10 * l
