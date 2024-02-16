# 3. N ta son o'qib oling. o'qib olingan olingan sonlar ichidan ikki xonali sonlarning yig'indisini toping

n = int(input("Enter n"))
lst = [int(input()) for i in range(n)]
s = 0
for num in lst:
    if num // 10>0:
        s += num
print(s)
