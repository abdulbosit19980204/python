lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input("Spliting Pages number: "))


#
# def paginator(lst, number):
#     nlst = []
#     a = 0
#
#     while len(lst) / number > 0:
#         nlst.append(lst[a:number])
#
#         lst = lst[number:]
#         a = number
#         number += a
#
#     return nlst
#
#
# print(paginator(lst, n))

def paginator(lst_numbers, n):
    lts = []
    for i in range(0, len(lst_numbers), n):
        lts.append(lst_numbers[i:i + n])
    return lts


lts = paginator(lst, n)
print(lts)

while True:
    a = int(input("Page nnumber: "))
    print(lts[a - 1])
