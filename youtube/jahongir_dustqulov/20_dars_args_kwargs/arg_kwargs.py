def summing(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(summing(1, 2, 3, 4, 5, 6))
