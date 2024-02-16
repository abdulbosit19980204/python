"""
3. s va t o’zgaruvchilarida string berilgan(input), s va t shunday berilganki s ning
belgilari random holda joylari almashtirilganda va bitta harf qo’shilganda t hosil bo’ladi.
Berilgan s va t dan foydalangan holda, qo’shilgan bitta harfni aniqlang
Input: s = "abcd", t = "adebc"
Output: "e"
"""
# s = input()

s = input()
t = input()
d = {}
d1 = {}

for i in s:
    d[i] = d.get(i, 0) + 1

for j in t:
    d1[j] = d1.get(j, 0) + 1

for key, val in d1.items():
    if key not in list(d.keys()):
        print(key)
    elif d[key] != d1[key]:
        print(key)
