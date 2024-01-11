# N soni o'qib oling va N ta sonni ham klaviaturadan kiriting. Sonlar Maximumdan Minimumgacha (kamayish tartibida)
# saralab qaytadan ekranga chiqaring

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)

for num in lst:
    print(num)
