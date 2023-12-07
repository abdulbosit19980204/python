text = "1 2 3 4 664 112 89 43 -12"
lst = text.split()

newLst = [int(i) for i in lst]
print(newLst)
print(sum(newLst))