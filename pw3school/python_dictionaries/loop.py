# Loop Dictionaries

# You can loop through a dictionary by using a for loop
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the
# values as well

thisDict = {"name": "John", "age": 22, "city": "New York"}

# Print all key names in the Dictionary, one by one
for x in thisDict:
    print(x, end=" ")  # name age city

# Print all values in the dictionary, one by one
for x in thisDict:
    print(thisDict[x], end=" ")  # John 22 New York

# You can also use the values method to return values of a dictionary
for x in thisDict.values():
    print(x, end=" ")  # John 22 New York

# You can use the keys() method to return the keys of a dictionary
for x in thisDict.keys():
    print(x, end=" ") #name age city

# Loop through  both keys and values, by using the items()
for x,y in thisDict.items():
    print(x, y, end=" ") #name John age 22 city New York
