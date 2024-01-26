from functools import partial


def power(a, b):
    return a ** b


def add(a, b):
    return a + b


def multiplication(a, b):
    return a * b


adding1 = partial(add, 5)
print(adding1(3))
print(multiplication(adding1(5), 3))

# partial functions
# pow2 = partial(power, b=2)
# pow4 = partial(power, b=4)
# power_of_5 = partial(power, 5)
#
# print(power(2, 3))
# print(pow2(4))
# print(pow4(3))
# print(power_of_5(2))
#
# print('Function used in partial function pow2 :', pow2.func)
# print('Default keywords for pow2 :', pow2.keywords)
# print('Default arguments for power_of_5 :', power_of_5.args)
