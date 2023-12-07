text = "1 2 3 4 664 112 89 43 -12"
lst = text.split()

lst = [int(i) for i in lst]
print(lst)
print(sum(lst))