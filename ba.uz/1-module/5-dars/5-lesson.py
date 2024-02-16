# text = "1 2 3 4 664 112 89 43 -12"

# lst = [int(i) for i in text.split()]
# print(lst)
# print(sum(lst))


"""Next"""

# n = int(input())
# toq=[]
# juft = []
# a  =[int(input()) for _ in range(n)]
# for i in a:
#     if i%2==0:
#         juft.append(i)
#     else:
#         toq.append(i)

# print("Juft => ", juft)
# print("Toq => ",toq)


"""Next"""

n = int(input())
print(n, "! = ", sep="", end="")

s = 1
for i in range(1, n + 1):
    s = s * i
    print(i, end=" * ")

print("\b\b=", s)

"""
5! = 1 * 2 * 3 * 4 * 5 = 120
6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
0! = 1
1! = 1
2! = 1 * 2 = 2

"""