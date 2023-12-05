#Slicing

# You can return a range of  characters by using the slice syntax
# Specify the start index and the end index, sperated by a colon,  to return  a part of the string

a="Hello world"
print(a[2:5]) #llo
# The first character has index 0

# Slice from the start
# By leaving out the start to position 5 (not included)
print(a[:5]) #Hello

# Slice to the end
print(a[2:]) #llo world

# Negative indexing
# Use negative indexes to start the slice from the end of the string:
print(a[-5:-2]) #wor


