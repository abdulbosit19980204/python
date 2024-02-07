"""
1. N ta qatorda string’lar kiritiladi, anagrammlarni birga guruhlang. Javobni istalgan
tartibda qaytarishingiz mumkin. Anagramm - bu boshqa so'z yoki iboraning harflarini
o’rnini o'zgartirish orqali hosil bo'lgan so'z yoki ibora, odatda barcha asl harflarni bir
marta ishlatadi.
File Input: strs = ["eat","tea","tan","ate","nat","bat"]
File Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

with open("text.txt", "r") as file:
    strs = file.readlines()

for i in range(len(strs)):
    strs[i] = strs[i].replace("\n", "")

d = []
for i in range(len(strs)):
    k = {}
    for j in strs[i]:
        k[j] = k.get(j, 0) + 1
    d.append(k)

print(d)


"""
Xullas shuni davom ettirib qoyish kerak qiyin yolbolsa keragu Shuni dictionary lar boyicha aylanib chiqib dictionaryni 
xamma keyi va valuesini qiymatlarini solishtirib chiqib qoyish kerak. Agar dic elementlari bir xil va qiymatlari xam
bir xil bolsa buni bitta listga yig'ib natijani chiqarib qoyish kerak. 
"""