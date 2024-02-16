# a+aa+aaa+aaaa ifoda natijasini, a ning  qiymati sifatida  berilgan raqam bilan hisoblaydigan dastur tuzing
n = int(input())
s = 0
for i in range(n):
    num = ""
    for j in range(i + 1):
        num += str(n)
    print(num)
    s += int(num)
print(s)
