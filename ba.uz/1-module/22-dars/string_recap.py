lst = ["apple", "banan", "peach", "app"]

prefix = input()
for word in lst:
    if prefix in word.lower()[:len(prefix)]:
        print(word, end=" ")

print("*" * 50)
for item in lst:
    if item.startswith(prefix):
        print(item)

print("*" * 50)
for word in lst:
    s = 0
    for i in range(len(prefix)):
        if prefix[i] == word[i]:
            s += 1
        else:
            break

    if s == len(prefix):
        print(word)
