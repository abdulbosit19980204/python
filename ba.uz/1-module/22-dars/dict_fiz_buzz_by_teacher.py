lst = [3, 5, 7, 11, 13, 3 * 5, 3 * 5 * 7, 3 * 5 * 7 * 11 * 13, 8]
# lst = map(int, input().split())
d = {
    3: "Fizz",
    5: "Buzz",
    7: "Fuzz",
    11: "Tuzz",
    13: "Luzz"
}

for i in range(len(lst)):
    s = ""
    for key, value in d.items():
        if lst[i] % key == 0:
            s += value
    if len(s) > 0:
        lst[i] = s

print(lst)

"""
12 -> 3 -> Fizz
18 -> 3 -> Fizz
15 -> 3 * 5 -> FizzBuzz
28 -> X -> ''
50 -> 5 -> Buzz

"""
