# Python Delete File

# Delete a File
# To delete a file you must import the OS module, and run its os.remove() function

# Remove the file "myfile.txt"
# import os
# os.remove('myfile.txt')

# Check if file exsist

# To avoid getting an error, you might want to check if the file exsist before you try to delete it
# Check if file exsist, then delete it
import os
if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print("The file doesn't exist")

# Delete Folder
# To delete folder an entire folder, use the os.rmdir() method
# os.rmdir("mydir")

# Note: You can only remove empty folder