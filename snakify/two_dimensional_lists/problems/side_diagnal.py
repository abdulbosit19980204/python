# Side diagonal

# Statement
# Given an integer n , create a two-dimensional array of size (n×n)
#  and populate it as follows, with spaces between each character:

# The positions on the minor diagonal (from the upper right to the lower left corner) receive 1 .
# The positions above this diagonal recieve 0 .
# The positions below the diagonal receive 2 . [[0,0,0,1],[0,0,1,2],[0,1,2,2],[1,2,2,2]]
"""
0 0 0 1
0 0 1 2
0 1 2 2
1 2 2 2

"""


def generate_side_diagonal_array(n):
    array = [[0] * n for _ in range(n)]

    for i in range(n):
        array[i][n - i - 1] = 1  # Minor diagonal
        for j in range(n - i - 1):
            array[i][j] = 0  # Above the diagonal
        for j in range(n - i, n):
            array[i][j] = 2  # Below the diagonal

    for row in array:
        print(" ".join(map(str, row)))


generate_side_diagonal_array(int(input()))
