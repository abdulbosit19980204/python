# Do not hesitate to return a lot

# It is useful to say that function can return more than one value. Here's the example of
# returning a list of two or more values return [a,b]

# You can call the function of such list and use it in multiple assignment: n,m =f(a,b)
a = '5'
b = '7'


def f(a, b):
    return [a + 'th', b + 'th']


n, m = f(a, b)
print(n)  # 5th
print(m)  # 7th
