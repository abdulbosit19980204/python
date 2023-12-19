# Copy a Dictionary

# You can't copy a dictionary simply by typing dict2=dict1, because: dict2 will only be reference to dict1,
# and changes made in dict1 will automatically also be made in dict2

# There are ways to make a copy, one way is to use the built-in Dictionary method copy()

# Make a copy of a dictionary with the copy() method
thisDict ={
    "firstName": "John",
    "lastName": "Doe",
    "age":25,
    "city": "New York"
}

copiedDict = thisDict.copy()
print(copiedDict) #{'firstName': 'John', 'lastName': 'Doe', 'age': 25, 'city': 'New York'}
thisDict["city"] = "Berlin"
copiedDict["city"] = "Pekin"
print(copiedDict)
print(thisDict)

# Another way to make a copy is to use the built-in function dict()
# Make a copy of dictionary with  the dict() function

secCopiedDict = dict(copiedDict)
print(secCopiedDict.items()) #dict_items([('firstName', 'John'), ('lastName', 'Doe'), ('age', 25), ('city', 'Pekin')])
