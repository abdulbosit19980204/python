n=int(input())
d={}
for i in range(n):
    txt = input().split()
    for word in txt:
        # print(word)
        d[word]=d.get(word,0)+1
items = list(d.items())

items.sort(key=lambda x: (-x[1], x[0]))
print(items[0][0])