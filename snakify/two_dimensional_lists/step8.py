# Another right way
# Another (but  similar) way: create an empty list and then append a new element to it n times
# this element should be a list of length m

n = 3
m = 3
a = []
for i in range(n):
    a.append([0] * m)
print(a)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 5
print(a)  # [[5, 0, 0], [0, 0, 0], [0, 0, 0]]


