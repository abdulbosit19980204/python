# lst = [1, 2, 4, 7, '7', '1', 8]
#
#
# def sorting(s):
#     return str(s)
#
#
# lst.sort(key=sorting)
# print(lst)


def sum(*items):
    if len(items) == 0:
        return 0
    items2 = list(items)
    del items2[0]
    return items[0] + sum(*items2)


print(sum(1, 5, 7, 3))
