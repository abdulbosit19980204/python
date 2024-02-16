# # For and Range
# a=int(input())
# b=int(input())
# c=int(input())
# s=0
# for i in range(a,b,c):
#     s+=i
# print(s)

#
# a=int(input())
# narx = 5
# for i in range(a//narx):
#     print("Hello")


# lst = [1, 2, 3, "4", "5", 6, 7]
# s = 0
# try:
#     for i in lst:
#         s += i
#         print(i, s)
#
#     # except TypeError:
#     #     print("Hatolik sodir boldi! ", "Na to'g'ri type ishlatildi => ", type(i))
#     #     break
# except Exception as e:
#         print(e)


lst = [2, 5, 7, 20, 90, 21, -5, 24]

len = len(lst)
sum = 0
for i in lst:
    sum += i

avg = sum / len
print("avg => ", avg)
for i in lst:
    if i > avg:
        print(i, end=" ")
