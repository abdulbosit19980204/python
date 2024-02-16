def input_num():
    n = int(input())
    if n == 0:
        return
    input_num()
    print(n)


input_num()
