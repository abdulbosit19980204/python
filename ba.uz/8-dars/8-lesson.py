# def func(a,b,c):
#     return a*b-c
#
# # def add(a, b):
# #     return a + b
# #
#
# add = lambda x, y: x + y
# print(add(int(input()), 2))

# Lambda function
#
# equal = lambda a, b, c: a * b - c
# print(equal(1, 2, 3))


# Reqursiya

# def pr_numbers(n):
#     if n >= 1:
#         pr_numbers(n - 1)
#
#     print(n)
#
#
# pr_numbers(10)
#
# # recursion, lambda, date, f string

# def even_numbers(n):
#    if n%2==0:
#        # print(n, end=" ")
#        if n >= 2:
#            even_numbers(n - 2)
#        print(n, end=" ")
#    else:
#        # print(n, end=" ")
#        if n >= 2:
#            even_numbers(n - 1)
#        print(n, end=" ")

def even_numbers(n):
    if n > 1:
        if n % 2 == 0:
            print(n, end=" ")
        even_numbers(n - 1)


even_numbers(int(input()))

# def odd_numbers(n):
#     print(n)
#     if n >= 1:
#         odd_numbers(n - 1)
#     print(n)
#
# odd_numbers(10)
