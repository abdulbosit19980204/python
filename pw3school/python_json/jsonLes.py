# Pyhton JSON

# JSON is a syntax for storing and exchanging data
# JSON is text, written with JavaScript object notation

# JSON in Python
# Pyhton has a built-in module called json, which can be used to work with JSON data.

# Import the JSON module
import json

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method
# The result will be python dictionary

# Convert from JSON to Python
# Some JSON
x = '{"name":"John","age":22,"city":"New York"}'

# parse x
y = json.loads(x)

# the result is a Python dictionary
print(y["age"])
print(y)

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method

# Convert from Python to JSON
x = {
    "name": "Abdulbosit",
    "surname": "Tuychiev",
    "age": 25
}
# Convert into JSON
y = json.dumps(x)
print(y)  # {"name": "Abdulbosit", "surname": "Tuychiev", "age": 25}

# You can convert Python objects of the following types, into JSON strings
"""
dict
lsit
tuple
string
int
float
True
False
None
"""
# Convert Python objects into JSON strings, and print the values

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# When  you convert from Pythonto JSON, Python objects are converted into the JSON (JavaScript) equivalent
"""
Python	JSON
**************
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
**************
"""

# Convert a Python object containing  all the legal data types
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))
# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentications and line breaks
# The json.dumps() method has parameters to make it easier to read the result

# Use the indent parameter to define the numbers of indents
json.dumps(x, indent=4)
print(json.dumps(x, indent=4))

# You can also define the sperators, default value is (",",":"), which means using a comma and a space to sperate each object
# and a colon and a space to separate keys from values

# use the seperators parameter to change the default seperator
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Order the Result
# The json.dumps() method has parameters to order the keys in the result
# Use the sort_keys parameter to specify if the result should be sorted or not
y= json.dumps(x, indent=4, sort_keys=True)
print(y)

