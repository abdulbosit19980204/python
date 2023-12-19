# Python Dictionaries


# Dictionary
# Dictionaries are used to store data key:value pairs.
# A dictionaries is a collection which is ordered*, changeable and do not allow duplicates

# Dictionaires are written with curly barkets, and have keys and values

thisDict = {
    "firstName": "John",
    "lastName": "Doe",
    "birthDate": "11-01-1998",
    "email": "example@gmail.com"
}

print(thisDict)  # {'firstName': 'John', 'lastName': 'Doe', 'birthDate': '11-01-1998', 'email': 'example@gmail.com'}

# Dictionary Items

# Dictionary items are ordered and changable, and does not allow duplicates
# Dictionary items are presented in key:value pairs, and can be referred to by using key name

print(thisDict["firstName"])  # John

# Ordered and Unordered
# When we say that dictionaries are ordered, it means that the items have a defined order, and that oreder will not change
# Unordered means that the items does not have a deifined order, you cannot refer to an item by using an index

# Changabel
# Dictionaries are changable, meaning that we can change, add or remove items after the dicrionary has been created

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key

# Duplicate values will overwrite exsisting values
thisDict = {
    "firstName": "John",
    "lastName": "Doe",
    "birthDate": "11-01-1998",
    "email": "example@gmail.com",
    "firstName": "Jeck"
}
print(thisDict)  # {'firstName': 'Jeck', 'lastName': 'Doe', 'birthDate': '11-01-1998', 'email': 'example@gmail.com'}

# Dictionary Length
# To determine how many items a dictionary has, use the len() function
print(len(thisDict))  # 4

# Ditionary Items - Data Types
# The values in dictionary items can be of any data types
thisTypedDict = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 25,
    "salary": 225.52,
    "cars": ["Jeep", "BMW", "Bugatti"]
}

print(thisTypedDict)

# The dict() constructor
# It is also possible to use the dict() constructor to make a dictionary

thisMadeDict = dict(name="Abdulbosit", age=25, salary=2254, country="Uzbeksitan")
print(thisMadeDict)  # {'name': 'Abdulbosit', 'age': 25, 'salary': 2254, 'country': 'Uzbeksitan'}


