"""
5. Memoizatsiya/keshlash dekoratori. Funktsiya natijalarini keshlaydigan dekorator
yozing. Kesh natijalarni funksiya parametrlari asosida saqlashi kerak, shunda funksiya
yana bir xil parametrlar bilan chaqirilsa, funksiyani qayta bajarish o‘rniga keshlangan
natija qaytariladi.
"""

d = []


def saved_kesh(func):
    def wrapper(a, b):
        c = func(a, b)
        d.append(c)

    return wrapper


@saved_kesh
def add(a, b):
    return a + b


add(4, 5)
add(3, 5)

print(d)
