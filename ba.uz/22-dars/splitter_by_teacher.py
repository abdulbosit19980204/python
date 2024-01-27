def my_split(word, sep=" "):
    lst = []
    s = ""
    for i in range(len(word)):
        if word[i] == sep:
            lst.append(s)
            s = ""
            continue
        s += word[i]
    lst.append(s)
    return lst


text = "1.22.35.47.225.-6.444"
print(my_split(text, "."))
