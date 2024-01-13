numbers_line = "1 2 30 0 10 11 4 5 0 1 25 4"
z1 = numbers_line.find(' 0')
z2 = numbers_line.rfind(' 0')
newNumbers = numbers_line[z1 + 1:z2].split()
s = 0
for i in newNumbers:
    s += int(i)
print(s)

