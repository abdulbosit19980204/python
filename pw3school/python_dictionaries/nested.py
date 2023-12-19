# Nested Dictionaries

# A dictionary can contain dictionaries, this is called nested dictionaries

# Creat a dictionary that contain  dicitonaries
thisNestedDict = {
    "car1": {
        "model": "BMW X7",
        "price": 650000,
        "color": "black"
    },
    "car2": {
        "model": "Ferrari",
        "price": 50000,
        "color": "black"
    },
    "car1": {
        "model": "Damas",
        "price": 6000,
        "color": "black"
    },
}

# Or If you want to add  three dictionaries into  a new dictionary
car1 = {
    "year": 2023,
    "luk": False
}
car2 = {
    "year": 2015,
    "luk": False
}
car3 = {
    "year": 2022,
    "luk": True
}

thisNestedDict = {
    "car1": car1,
    "car3": car2,
    "car3": car3,
}
print(thisNestedDict)

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary

print(thisNestedDict["car1"]["year"])  # 2023
