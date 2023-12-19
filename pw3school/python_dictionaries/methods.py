# Dictionary Methods
# Python has  a set of built-in methods that you can use on dictionaries

# clear()
# copy()
# fromkeys() -  Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)  # {'key1': 0, 'key2': 0, 'key3': 0}
# get() - get vs key names ? get returns None and key name returns Error
# items()
# keys()
# pop() - remove with the specified key
# popitem() -remove key and value from back
# setdefault() - Returns the value of the specified key. IF the key doesn't exsist: insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x) #Mustang

# update()
# values()
