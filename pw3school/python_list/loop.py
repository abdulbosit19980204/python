# Loop List

# You can loop through the list items by using a for loop:

thisLoopList = [1,2,3,4,5,6]
for x in thisLoopList:
    print(x, end=" ") #1 2 3 4 5 6


#Loop through the index Numbers
# We can also loop through the list items by referring to theis index number
# Use the range() and len() functions to create a suitable iterable.

thisIndexList =[1,2,3,4,5,6,7]
for i in range(len(thisIndexList)):
    print(thisIndexList[i], end=" ") #1 2 3 4 5 6 1 2 3 4 5 6 7

# using a While Loop
# You can loop through the list items by using a while loop
"""
 Use the len() function to determine  the length of the list then start at 0 and 
 loop your way through the list, then start at 0 and loop your way through the list items by refering 
 to their indexes.
 
 Remember to increase the index by 1 after each iteration
 
"""

thisWhileList = [1,2,3,4,5,6,7]
i=0
while i < len(thisWhileList):
    print(thisWhileList[i], end=" ") #1 2 3 4 5 6 7
    i = i+1

# Looping Using List Comprehesion
# List Comprehension offers the shortest syntax for looping through list:

thisCompList = [11,55,22,44,66,77,33]
[print(x, end=" ") for x in thisCompList] #11 55 22 44 66 77 33
