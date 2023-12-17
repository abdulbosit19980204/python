# Join Tuples

# To join two or more tuples you can use the + operator
numbersTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
fruitsTuple = ('apple', 'banana', 'orange', 'pear')
print(fruitsTuple+numbersTuple) #('apple', 'banana', 'orange', 'pear', 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator

fruitsTuple = ('apple', 'banana', 'pear')
numbersTuple = (1, 2, 3, 4)
print(fruitsTuple*2) #('apple', 'banana', 'pear', 'apple', 'banana', 'pear')
print(numbersTuple*2) #(1, 2, 3, 4, 1, 2, 3, 4)

