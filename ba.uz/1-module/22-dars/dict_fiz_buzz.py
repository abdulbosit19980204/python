d = {
    3: 'UCH',
    5: "BESH",
    7: "YETTI",
    11: "ONBIR",
    19: "ONTOQQIZ"
}
lst = [12, 15, 18, 25, 50, 28, 77, 35, 105, 2, 3 * 7 * 11, 5 * 3 * 19, 19, 45, 7, 8, 9, 112, 13]

for i in range(len(lst)):
    num = lst[i]
    res = ""
    for j in d.keys():
        if num % j == 0:
            res += d[j] + "/"
            lst[i] = res
        if num % j != 0:
            lst[i] = lst[i]

print(lst)
