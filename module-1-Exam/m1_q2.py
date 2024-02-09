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
