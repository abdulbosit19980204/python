# The diagonal parallel to the main
# Statement
# Given an integer n , produce a two-dimensional array of size (n×n)
# and complete it according to the following rules, and print with a single space between characters:

# *On the main diagonal write 0 .
# *On the diagonals adjacent to the main, write 1 .
# *On the next adjacent diagonals write 2 and so forth.

# Print the elements of the resulting array.

# n = int(input())
# a = [[j for j in range(n)] for i in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             a[i][j] = 0
#
# for i in a:
#     print(i)


# ***************************************************************************
def generate_array(n):
    array = [[abs(i - j) for j in range(n)] for i in range(n)]
    for row in array:
        # print(" ".join(map(str, row)))
        print(' '.join([str(i) for i in row]))


generate_array(int(input()))
# ******************************************************************************
n = 5
array = [[abs(i - j) for j in range(n)] for i in range(n)]
print(array)
for row in array:
    # print(" ".join(map(str, row)))
    print(' '.join([str(i) for i in row]))
