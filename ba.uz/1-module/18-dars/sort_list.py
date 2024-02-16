lst = input().split()


nums = []
strs = []
for i in lst:
    if i.isnumeric():
        nums.append(i)
    elif i.isalpha():
        strs.append(i)

print(nums)
print(strs)
