"""
input

1 2 3 4
5 6 7 8
4 3 2 1

"""
"""
output
1 5 4
2 6 3
3 7 2
4 8 1
"""

n = int(input())
a = [input().split() for _ in range(n)]


def rotate_matrix(matrix):
    rotated = list(zip(*matrix))
    print(rotated)
    for row in rotated:
        print(" ".join(map(str, row)))


rotate_matrix(a)
