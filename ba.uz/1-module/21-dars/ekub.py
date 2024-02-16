# ekub: 12: 2, 3 || 14: 2,7

def ekub(n, b=1):

    if b > n:
        return
    if n % b == 0:
        print(b, end=" ")
    ekub(n, b + 1)


ekub(8)
