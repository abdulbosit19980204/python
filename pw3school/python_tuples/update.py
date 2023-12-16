# Update Tuples
# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangable, or immutable as it also is called.
#  But there is a workround
# You can convert the tuple into s list

thisTuple=("apple","banana","cherry","tomato")
y=list(thisTuple)
y[-1] = "kiwi"
thisTuple = tuple(y)
print(thisTuple) #('apple', 'banana', 'cherry', 'kiwi')

# Add items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple

# 1. Convert into a list
thisTuple = ("apple","banana","cherry","olma")
y=list(thisTuple)
y.append("kiwi")
thisTuple =tuple(y)
print(thisTuple) #('apple', 'banana', 'cherry', 'olma', 'kiwi')

# 2.Add tuple to a tuple
thisTuple=(1,2,3,4,5,6,7,8,9)
y=(55,)
thisTuple+=y
print(thisTuple) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 55)

# Remove Items
# You cannot remove items in a tuple
# Convert the tuple into a list, remove "apple", and convert it back into a tuple
thisTuple=("apple","banana","kiwi","cherry","olma")
y=list(thisTuple)
y.remove('kiwi')
thisTuple=tuple(y)
print(thisTuple) #('apple', 'banana', 'cherry', 'olma')

# Or you can delete the tuple completly:
thisTuple=("apple","banana","kiwi","cherry","olma")
del thisTuple
print(thisTuple) #this will raise an error because the tuple no longer exists
