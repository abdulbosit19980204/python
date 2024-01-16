# Nested generators -2
# But the internal list can also be created using, for example, such genrator [0 for j in range(m)] Nesting one
# generator into another, we obtain the code as we wrote

# What's the point of using the longer syntax? At the moment, there is no point
# but the number 0 can be replaced by some expression that depends on i (the line number) and j (the column number),
# so with this longer syntax it is possible to get the matrix filled according to some formula

m = 3
n = 8
a = [[0 for j in range(m)] for i in range(n)]
print(a)

