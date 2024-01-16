# Looping by elements
# Naturally, to output a single line you can use method join()

a = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 2, 5]]
for i in a:
    print(''.join([str(elem) for elem in i]))

