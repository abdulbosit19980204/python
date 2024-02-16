# 5. Gaplardan iborat list berilgan. Shu listdagi gaplarning  qaysi birida eg kop so'zlar qatnashgan va ular nechtaligini
# hisoblovchi funksiya yozing

lst = ["Hello I am Abdulbosit", "I am from Uzbekist and I live in Andijan", "I am studying at univeristy"]
word_count = []
for text in lst:
    word_count.append(len(text.split()))

ind = word_count.index(max(word_count))
print(lst[ind])
