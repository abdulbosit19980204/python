# The easiest way
# But the easiest way is to use generator, creating a list on n elements, each of which is a list  of  m zeros
# In this case each element is created independently from the others. The list [0]*m is n times constructed as the new one
# and no copying of references occurs

n = 3
m = 4
a = [[0] * m for i in range(n)]
print(a)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

