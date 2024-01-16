# Local and Global variables: What happens in realty

# One fact may seem strange: if you initialize some variable inside of the function, you won't be able to use this
# variable outside of it

def f():
    a = 1
    print(a)


f()
a = 0
print(a)
f()

