# List Comprehension

numbers =[22,55,33,77,88,99,222,2222,]
newNumber = []

for x in numbers:
    if x%2==0:
        newNumber.append(x)

print(newNumber) #[22, 88, 222, 2222]

# With list comprehension you can do all that with only one line of code

numbers = ["2121","5454","8787","9898","454"]
newNumber = [x for x in numbers if "5" in x]
print(newNumber) #['5454', '454']

newWFiveList = [x for x in numbers if "5" not in x]
print(newWFiveList) #['2121', '8787', '9898']

# ITERABLE

# The iterable can be any iterable object, like a list, tuple, set, etc
# You can use the range() function to create an iterable
iterableList = [x for x in range(8)]
print(iterableList) #[0, 1, 2, 3, 4, 5, 6, 7]
# Itterable with a condition
conIterList = [x for x in range(15) if x%2==0]
print(conIterList) #[0, 2, 4, 6, 8, 10, 12, 14]

# EXPRESSION
"""
The expression is the current item in iteration, but it is also the outcom, which you can manipulate before it ends up
like a list item in the new list

"""
fruitsList =["olma", "shaftoli","persik"]
newExList = [x.upper() for x in fruitsList]
print(newExList) #['OLMA', 'SHAFTOLI', 'PERSIK']

# We can set the outcome to whatever you like
newExList = ['hello' for x in fruitsList]
print(newExList) #['hello', 'hello', 'hello']

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Return "apple" instead of "olma"
newExList = [x if x!="olma" else "apple" for x in fruitsList]
print(newExList) #['apple', 'shaftoli', 'persik']

