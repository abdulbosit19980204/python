# Add Dictionary items

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisDict = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 35
}

thisDict["gender"] = "male"
print(thisDict)  # {'firstName': 'John', 'lastName': 'Doe', 'age': 35, 'gender': 'male'}

# Update Dictionary
# The update() method will update the dictionary with the items from a given argument.
# If the item doesn't exist, it will be added

thisDict["salary"] =10000
print(thisDict) #{'firstName': 'John', 'lastName': 'Doe', 'age': 35, 'gender': 'male', 'salary': 10000}
