# def cmp(x):
#     if x % 2 == 0:
#         return -x
#     else:
#         return x
#
#
# lst = [5, 12, 85, 23, 34, 78]
# lst.sort(key=cmp)
# print(lst)


# def cmp(n):
#     s = 0
#     for j in range(1, n + 1):
#         if n % j == 0:
#             s += 1
#     return s
#
#
# lst = [5, 12, 85, 23, 34, 78]
# lst.sort(key=cmp)
# print(lst)

# for n in lst:
#     s=0
#     for j in range(1, n+1):
#         if n % j == 0:
#             s += 1
#     print(n, s)


word_list = ["apple", "banana", "nasjdn", "sndjknsdjfn","hi", "ojdjna asdjnajosnd aksdias", "jdjnja asskmas"]


def cmp(x):
    # txt = x.split()
    # return len(txt)
    return x.count(" ")+1

word_list.sort(key=cmp)
print(word_list)

