def multiLab(n,a,fn):
    if fn(a):
        return n*a
    else:
        return n


kv = lambda a:a%2==0
kv1 = lambda a:a%2!=0


print(multiLab(5,5,kv))
print(multiLab(2,5,kv1))