# Change Values

# You can change the value of a specific item by referring to its key name
# change the "age"

thisDict = {"firstName": "John", "lastName": "Doe", "age": 35}

print(thisDict)  # {'firstName': 'John', 'lastName': 'Doe', 'age': 35}

# Update Dictionary
# The update() method will update the dictionary with the items from given argument
# The argument must be a dictionary, or an iterable object with key:value pairs
# Update the "firstName" of the Dict by using the update() method

thisDict.update({"firstName": "Jeck"})
print(thisDict) #{'firstName': 'Jeck', 'lastName': 'Doe', 'age': 35}

