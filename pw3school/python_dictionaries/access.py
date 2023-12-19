# Access Dictionary Items
# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2023
}
print(thisDict["model"])  # Mustang

# There is also a method called get() that will give you the same result:
# Get the value of the "model" key
x = thisDict.get("brand")
print(x)  # Ford

# Get Keys
# The keys() method will return a list of all the keys in the dictionary
x = thisDict.keys()
print(x)  # dict_keys(['brand', 'model', 'year'])

# Get Values
# The values() method will return a list of all the values in the dictionary
x = thisDict.values()
print(x)  # dict_values(['Ford', 'Mustang', 2023])

# Add a new item to the orginal dictionary, and see that the values list gets updated as well

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2023,
}
x = car.values()
print("Car before update => ", x)  # Car before update =>  dict_values(['Ford', 'Mustang', 2023])
car["color"] = "Black"
x = car.values()
print("Car after update => ", x)  # Car after update =>  dict_values(['Ford', 'Mustang', 2023, 'Black'])

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list
x = car.items()
print(x)  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2023), ('color', 'Black')])

# Check if Key Exsist
# To determine if a specified key is present in a dictionary use the in keyword

if "model" in car:
    print(car.get("model")) #Mustang
else:
    print("No model")
