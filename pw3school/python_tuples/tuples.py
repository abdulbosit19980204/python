# Python Tuples
# from builtins import function

myTuple = ("apple","banana","cherry")
print(myTuple)

# Tuples are used to store multiple items in a single variable.

# A tuple is a collection which is ordered and unchangable.

# Tuples are written with round brackets.

thisTuple = ("apple","banana","cherry","persik")
print(thisTuple)

# Tuple items are ordred, unchangable, and allow duplicate values.

# Ordered
# When we say that tuples are ordred, it means that the items have defined ordred, and that order will not change.

# Unchagable
# Tuples are unchangable, meaning that we cannot change, add or remove items after the tuples has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value

thisTuple = ("apple","banana","apple","banana","apple")
print(thisTuple)

# Tuple length
# To determine how many items a tuple has, use the len() function:
thisTuple = ("apple","banana","orange","orange","orange")
print(len(thisTuple)) #5

# Create Tuple with one Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple
thisString=("apple")
thisOneItemTuple=("apple",)
print(type(thisString)) #<class 'str'>
print(type(thisOneItemTuple)) #<class 'tuple'>

# Tuple items - Data Types
# Type items can be of any data type:

# String, int and boolean data types:
tuple1 = ("olma","behi","gilos")
tuple2=(1,2,3,4,5,6,7,8,9)
tuple3=(True,False,True,False)
print(tuple3) #(True, False, True, False)

# A tuple can contain different data types
tupleDif = ("a",11,"b",11.22,True)
print(tupleDif) #('a', 11, 'b', 11.22, True)

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple
thisList= ["apple","banana","dsm"]
thisConstructorTuple = tuple(thisList)
print(thisConstructorTuple) #('apple', 'banana', 'dsm')
