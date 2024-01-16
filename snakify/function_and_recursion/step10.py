# Local and global variables: hey
# More formally: Python considers a variable local to the function, if in  the code of this function there is at least
# one instruction that  modifies the value of the variable. Then that variable also cannot be used prior to initialization
# Instructions that modify the value of a variable are operators =, += and usage of the variable  as a loop for  parameter
# Even if the variable-changing statement is never executed, the variable is still local.

def f():
    print(a)
    if False:
        a = 0


a = 1
f()

# UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

# An error occurs: UnboundLocalError. Namely, since the function contains the command which modifies the variable a,
# in the function f() the identifier a becomes a local variable.
# Although the modifying instruction will never be executed, the interpreter has no way to check it.
# Therefore, when you try to print the variable a, you use an uninitialized yet local variable. Python prohibits that.

