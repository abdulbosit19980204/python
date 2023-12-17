# Loop Tuples

# Loop through a tuple
# You can loop through the tuple items by using a for lop

# Iterate through the items and print the values
thisTuple = (1,2,3,4,5,6,7,8,9)
for i in thisTuple:
    print(i, end=" ") #1 2 3 4 5 6 7 8 9

# Loop throught the index numbers
# You can also loop through the tuple items by referring to their index number
# Use the range() and len() function to create a suitable iterable
thisFruitTuple = ("apple", "banana", "cherry", "orange", "pear" )
for i in range(len(thisFruitTuple)):
    print(thisFruitTuple[i], end=" ") #apple banana cherry orange pear


# Using While loop
thisTuple = ("apple", "banana", "cherry", "orange")
i=0
while i <len(thisTuple):
    print(thisTuple[i], end=" ") #apple banana cherry orange
    i+=1

