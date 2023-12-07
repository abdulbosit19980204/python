text = "1 2 3 4 664 112 89 43 -12"

lst = [int(i) for i in text.split()]
print(lst)
print(sum(lst))