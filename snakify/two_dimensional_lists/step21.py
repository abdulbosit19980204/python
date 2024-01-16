# Initialization: an example

# For example, suppose you need to initialize the following  array (for convenience, extra space are added between items)

# In this array there are n=5 rows, m=6 columnsm, and the element with row index i and column index j is calculated by
# the formula

# a[i][j] = i * j

# And as always, you could use generator to create such an array
# [[i * j for j in range(m)] for i in range(n)]

n = 5
m = 6
a = [[i * j for j in range(m)] for i in range(n)]
for i in a:
    print(*i)
