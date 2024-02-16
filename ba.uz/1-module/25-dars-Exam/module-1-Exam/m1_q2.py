"""
2. n butun soni kiritiladi, shu son 2 ning darajasi yoki yo’qligini aniqlovchi funktsiya
yozing (recursion bilan ishlansa afzalroq)
Input: n = 16
Output: true
"""

n = int(input("Input the checking number: n="))


def is_power(n, s=0):
    if n != 1 and n % 2 == 0:
        n //= 2
        s += 1
    elif n == 1:
        print(s)
        return
    elif n % 2 != 0:
        print("2 ni darajasi emas")
        return

    is_power(n, s)


is_power(n)
