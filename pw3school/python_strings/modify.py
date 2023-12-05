#Modify Strings

# Python has  a set of built-in methods that you can use on strings

# Upper-case

a="hello world"
print(a.upper()) #HELLO WORLD

# Lower case
a="HellO"
print(a.lower()) #hello

# Remove whitespace
# The stripe() method removes any white space from the beginning or the end

a="  Hello I am Abdulbosit  "
print(a.strip()) #"Hello I am Abdulbosit"

# Replace string
# The replace() method replace a string with another string
a="Helllo I am abdublbosit"
print(a.replace("Helllo", "Hello")) #Hello I am abdublbosit

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

a="Hello I am Abdulbosit. I am form Andijon"
print(a.split(".")) #['Hello I am Abdulbosit', ' I am form Andijon']
print(a.split(" ")) #['Hello', 'I', 'am', 'Abdulbosit.', 'I', 'am', 'form', 'Andijon']

