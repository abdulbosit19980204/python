# 3.Kiritilgan sonni polindromga tekshiring: polindrom son 121 232 353

n = input()
#
# pol = False
# for i in range(len(n)):
#
#     if len(n) == 1:
#         print("Bir xonali son kiritildi")
#
#     if n[i] == n[-i] or i != len(n) // 2:
#         print(n[i], "&", n[-i])
#         pol = True
# if pol == True:
#     print("Polindrom son")
# else:
#     print("Polindrom emas")


l = []
for i in n:
    l.append(i)
l.reverse()
s = ""
for j in l:
    s += j

if int(n) == int(s):
    print("Polindrom")
else:
    print("Polindrom emas")
