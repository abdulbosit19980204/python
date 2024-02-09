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
