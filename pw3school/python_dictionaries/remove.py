# Removing Items
# There are several methods to remove items from a dictionary

# The pop() method removes the item with the specified key name
thisDict = {
    "firstName": "John",
    "lastName": "Doe",
    "email": "xxnn@mm.hh"
}

thisDict.pop("email")
print(thisDict)  # {'firstName': 'John', 'lastName': 'Doe'}

# The popitem() method removes the last inserted item
thisDict.popitem()
print(thisDict)  # {'firstName': 'John'}

# The del keyword removes the item with the specified key name
thisDict["lastName"] = "Jim"
thisDict["gender"] = "male"

del thisDict["firstName"]
print(thisDict)  # {'lastName': 'Jim', 'gender': 'male'}

# The del keyword can also delete the dictionary completly
del thisDict
# print(thisDict)  # NameError: name 'thisDict' is not defined

# The clear() method empties the dictionary
thisDict={
    "firstName": "John",
    "lastName": "Doe",
    "email": "xxnn@mm"
}
thisDict.clear()
print(thisDict) #{}

