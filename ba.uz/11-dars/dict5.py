number = int(input())

d = {}

for i in range(number):
    data = input().split()
    d[data[0]] = data[1:]

number = int(input())


def getPerm(argument):
    switcher = {
        "read": "R",
        "write": "W",
        "execute": "X",
    }
    return switcher.get(argument, "")


for j in range(number):
    data = input().split()
    if getPerm(data[0]) in d[data[1]]:
        print("OK")
    else:
        print("Access denied")