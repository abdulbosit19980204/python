"""
7. Kitirilgan N butun sonining ichida 5 raqami qatnashgan yoki qatnashmaganligini
aniqlang
"""

n = int(input())

while n > 10:
    if n % 10 == 5:
        print("True")
        break
    n //= 10
else:
    print("Flase")
