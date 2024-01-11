# 6. Berilgan String ichida har bir berlgi nechi marta takrolanganini  hisoblovchi funktsiya yoizng
txt = "The quick brown fox jumps over the"

chars = {}


def word_counter(txt):
    for i in range(len(txt)):
        chars[txt[i]] = txt.count(txt[i])


word_counter(txt)
print(chars)
