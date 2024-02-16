# 4. Bir nechta son berilgan Agar ularning hammasini toq son bo'lsa "ROST" aks xolda "Yolg'on" chiqaring

# nums = '1 2 3 4 5 6 7 8 9 10'
# nums = '2 4 6 8'
nums = '1 3 5 7'
nums = nums.split()
s = True
for num in nums:
    if int(num) % 2 == 0:
        s = False

if s:
    print("Rost")
else:
    print("Yolg'on")
