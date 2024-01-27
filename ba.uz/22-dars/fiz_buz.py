lst = [12, 18, 15, 28]
for i in range(len(lst)):
    num = lst[i]
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)
    lst[i] = string

print(lst)
