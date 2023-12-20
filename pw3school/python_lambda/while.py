# n = int(input())
# a, b = 0, 1
# i = 2
# ind = -1
# while b < n + 1:
#     print(a,b)
#     a, b = b, a + b
#     if b == n:
#         ind = i
#         break
#     i += 1
#
# print(ind)


n = int(input())
dict = {
    "words": []
}

for i in range(n):
    txt = input().split()
    m_word = txt[0]
    synonm = txt[1]
    word = {
        "word": m_word,
        "synonm": synonm,
    }
    dict["words"].append(word)
newTxt = input()
for i in range(len(dict["words"])):
    if dict["words"][i]["word"] == newTxt:
        print(dict["words"][i]["synonm"])
    elif dict["words"][i]["synonm"] == newTxt:
        print(dict["words"][i]["word"])
    else:
        continue
