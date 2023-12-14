# Copy list
"""

You can't copy a list simply by typing list2=list1, because: list2 will only be a reference to list1
 and changes made in list11
will automatically also be made in list2

There are ways to make a copy, one way is to use the built-in List method copy()
"""

thisCopiableList =[1,5,77,11,55,2,3]
thisCopiedList = thisCopiableList.copy()
print(thisCopiedList) #[1, 5, 77, 11, 55, 2, 3]

# Another way to make a copy is to use the built-in method list()
thisListMethod = list(thisCopiedList)
print(thisListMethod) #[1, 5, 77, 11, 55, 2, 3]
