lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input("Page number: "))


def paginator(lst, number):
    nlst = []
    a = 0

    while len(lst) / number > 0:
        nlst.append(lst[a:number])

        lst = lst[number:]
        a = number
        number += a

    return nlst


print(paginator(lst, n))
# i = 10
# while i > 0:
#     print(i)
#     i -= 1
