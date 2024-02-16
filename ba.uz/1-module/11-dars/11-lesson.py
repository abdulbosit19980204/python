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

#
# word_list = ["apple", "banana", "nasjdn", "sndjknsdjfn","hi", "ojdjna asdjnajosnd aksdias", "jdjnja asskmas"]
#
#
# def cmp(x):
#     # txt = x.split()
#     # return len(txt)
#     return x.count(" ")+1
#
# word_list.sort(key=cmp)
# print(word_list)
#


# *************************************

import random
def cmp(x):
    print(x["avg"])
    return x["avg"]
d = {
    "students": [
        {
            "name": "Abbb",
            "email": "sdjknjsd@sdf.asd",
            "avg": random.randint(1, 100)
        },
        {
            "name": "Sfff",
            "email": "sdjknjsd@sdf.asd",
            "avg": random.randint(1, 100)
        },
        {
            "name": "Bsss",
            "email": "sdjknjsd@sdf.asd",
            "avg": random.randint(1, 100)
        },
    ]
}

answer = input("Studentlarni avg bo'yicha o'sish tartibida chiqarmoqchimisiz(ha/yo'q): ")
if answer == "ha":
        d["students"].sort(key=cmp)
print(d["students"])

# ************************************


import random

d = {
    "students": []
}

n = int(input("Nechta student kiritmoqchisiz: "))

for i in range(1, n + 1):
    print(f"Student {i}")
    # name = input("Student name: ")
    # email = input("Student email: ")
    # avg = float(input("Student average mark: "))
    d_s = {
        "name": f"name{i}",
        "email": f"email{i}",
        "avg": random.randint(1, 100)
    }
    d["students"].append(d_s)

answer = input("Studentlarni avg bo'yicha o'sish tartibida chiqarmoqchimisiz(ha/yo'q): ")

if answer == "ha":
    d["students"].sort(key=lambda x: x["avg"])
else:
    d["students"].sort(key=lambda x: -x["avg"])

for student in d["students"]:
    print(student["name"], student["email"], student["avg"])


