# 1. N ta son kiritilsin. Birorta son 2 va undan ortiq marta qatnashgan bolsa, "Takrorlanish mavjut" xabarini bersin

n = int(input())
lst = [int(input()) for _ in range(n)]
for i in range(len(lst)):
    if lst[i] in lst[i+1:]:
        print("Takrorlanish")
