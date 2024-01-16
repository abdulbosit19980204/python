# Looping by elements
# We have already tried to explain that a for-loop variable in Python can iterate not only over a range()
# but generally over all the elements of any sequence. Sequence in Python are list and strings (and some other objects)
# Look how you can print a two-dimensional array, using this handy feature of loop for:
a = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

