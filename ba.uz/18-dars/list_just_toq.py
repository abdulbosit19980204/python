lst = input().split()

nums = []
strs = []
for i in lst:
    if i.isnumeric():
        nums.append(i)
    elif i.isalpha():
        strs.append(i)

toq = []
juft = []
for i in nums:
    if int(i) % 2 == 0:
        juft.append(i)
    else:
        toq.append(i)

print(toq)
print(juft)

