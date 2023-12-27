# Python File Handling

# File handling is an important part of any web application
# Python has several functions for creating, reading , updating and deleting files

# File Handling
# The key function for working with files is open() function
# The open() function takes two parameters: filename and mode
# There are four different methods (modes) for opening file
# "r" - Read - Default value. Open a file for reading, error if the file does not exsist
# "a" - Append. - Opens a file for appending, creats the file if it does not exsist
# "w" - Write. - Opens s file for writing. creates the file if it does not exsist
# "x" - Create. - Creates the specified file, returns an error if the file exsist

# In addition, you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode. (e.g images)

# Syntax
# To open a file for reading its enough to specify the filename
# f= open("demo.tx") the code is the same as f=open("demo.tx","rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them
# Note: Make sure the file exsist, or else you will get an error