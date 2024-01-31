# 2. berilgan Text(string)da eng kop  ishlatilgan ikkinchi belgi ni toping  va
# nechi marta qatnashganini belgi bilan birga chiqaring

txt = input()
d = {}

for j in txt:
    d[j] = d.get(j, 0) + 1

items = list(d.items())
items.sort(key=lambda x: (-x[1], x[0]))
print(items[1][0])
