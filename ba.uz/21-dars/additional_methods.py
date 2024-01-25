"""
eval,
iter,
zfill,
expandtabs,
startswith, endswith,
issubclass, isinstance
callable, functools
frozenset, set
"""
print("*" * 50)
eval("print(5**3)")
# *************************************

print("*" * 50)

a = "25"
print(a.zfill(4))
print("*" * 50)
# ******************************************

txt = "hello\tmy\tbudget    very expensive"
print(txt.expandtabs(8))
print("*" * 50)
# ********************************************

lst = ["Hello", "My", "Name", "Abdullo"]
for i in lst:
    if i.endswith("o") or i.startswith("H"):
        print(i)

print("*" * 50)


# ******************************************

class B:
    pass


class C:
    pass


class A(B, C):
    pass


print(issubclass(A, B))
print(issubclass(A, C))
print(issubclass(B, C))

print(isinstance(3.025, float))

print("*" * 50)


# ************************************************

def add(a, b):
    return a + b


print(callable(add))
print("*" * 50)
# *************************************************
from functools import reduce

lst = [1, 2, 3, 4]
print(reduce(add, lst))
print("*" * 50)
# ***********************************************

a = [5, 3, 6, 7]
b = [1, 2, 3, 8, 7, 9, 1, 2, 3]
lset = set(a + b)
print(lset)
frozenset(lset)
print(lset)
lset = list(lset)
lset[0] = "a"
lset = set(lset)
print(lset)
print("*" * 50)
