# Recursion Example

# As we saw above, a function can call another function. But a function can also call itself!

# To illustrate it, consider the example of the factorial-computing function.
# It is well known that 0!=1, 1!=1. How to calculate the value of n! for large n?
# If we were able to calculate the value of (n-1)!, then we easily compute n!, since n!=n⋅(n-1)!.
# But how to compute (n-1)!? If we have calculated (n-2)!, then (n-1)!=(n-1)⋅(n-2)!. How to calculate (n-2)!?
# If... In the end, we get to 0!, which is equal to 1.
# Thus, to calculate the factorial we can use the value of the factorial for a smaller integer. Look at the code.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # 5

