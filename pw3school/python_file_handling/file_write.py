# Python File Write
# Write to and Exsiting File
# To wirte to an exsiting file, you must add a parameter to the open() function
# "a" - Append. - will append to the end of the file
# "w" - Write -will overwrite any exsisting content

# Open the file "demofile2.txt" and append content to the file
f = open("demofile2.txt", "a")
f.write("New lines are adding")
f.close()
f = open("demofile2.txt")
print(f.read())
# New lines are adding

# Open the file "demofile3.txt" and overwrite the content

f = open("demofile3.txt", "w")
f.write("New lines are adding and overwrite")
f.close()
f = open("demofile3.txt")
print(f.read())  # New lines are adding and overwrite

# Note: The "w" method will overwrite the entire file

# Create a new file
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - create - will create a file, returns an error if the file exsist
# "a" - Append - will create a file if the specified files does not exsist
# "w" - Write - will create a file  if the specified file does not exsist

# Create a file called "myfile.txt"
f = open("myfile.txt", "x")
