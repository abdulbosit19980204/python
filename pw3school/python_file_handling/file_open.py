# Python File Open

# Open a file on the Server
# Assume we have the following file, located in the same folder as Python

# To open the file, use the built-in open() function
# The open() function returns a file object, which has a read() method for reading the content of the file
f = open("demofile.txt")
print(f.read())
"""
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
"""

# If the file is located in a different location, you will have to specify the file path, like this
# Open a file on different location
f = open("D:\\coding\\python\\pw3school\\python_try_except\\demofile.txt", "r")
print(f.read())

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return

# Return the 5 first characters of the file
f = open("demofile.txt", "r")
print(f.read(5))  # Hello

# Read lines
# You can return one line by using the readline() method
f = open("demofile.txt", "r")
print(f.readline())  # Hello! Welcome to demofile.txt

# By calling readline() two times, you can read the two first lines
f=open("demofile.txt", "r")
print(f.readline())
print(f.readline())
"""
Hello! Welcome to demofile.txt

This file is for testing purposes.
"""
# By looping through the lines of the file, you can read the whole file, line by line
f=open("demofile.txt","r")
for x in f:
    print(x)
"""
Hello! Welcome to demofile.txt

This file is for testing purposes.

Good Luck!
"""

# Close Files
# It is a good practice to always close the file when you are done with it
# Close the file when you are finish with it
f=open("demofile.txt","r")
print(f.readlines()) #['Hello! Welcome to demofile.txt\n', 'This file is for testing purposes.\n', 'Good Luck!']
f.close()
