# 7. Kamayish tartibida bolmagan sonlar ketmaketligi berilgan, eng yaxshi usul orqali bu sonlar ketma-ketligi
# ichidan necha xil son borligini aniqlang

a = [int(i) for i in input().split()]
d = {}

for i in a:
    d[i] = d.get(i, 0) + 1
print(len(d.keys()))
s = 0
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        s += 1
print(s + 1)
