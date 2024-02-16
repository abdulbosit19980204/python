# Birinchi va ikkinchi qatorda bo'sh joy  bilan ajratilgan butun sonlar kiritildi.
# Ushbu 2 ta qatordagi sonlarning  umumiylarini ekranga chiqaring

set1 = set([i for i in input().split()])
set2 = set([i for i in input().split()])
set1.intersection_update(set2)
print(set1)
