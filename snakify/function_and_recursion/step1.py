# Enter the function

# Recall that in mathematics the factorial of a number n is defined as n!=1*2*...*n
# It is clear that factorial is easy to calculate, using a for loop.
# Imagine that we need in our program to calculate the factorial of various numbers several times.

# compute 4!
fac = 1
for i in range(1, 5):
    fac *= i
print(fac)

# compute 7!
fac = 1
for i in range(1, 8):
    fac *= i
print(fac)

# However, if we make a mistake in the initial code, this erroneous code will appear in all the place where we've copied
# the computation of factorial. Moreover,the code is longer than it could be. To avoid re-writing the same logic in
# programming languages the functions were invented

