filename = 'talaba.txt'
lst = []
with open(filename) as file:
    talabalar = file.readline()
    for talaba in file:
        print(talaba)
        lst.append(talaba)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)

print(lst)
