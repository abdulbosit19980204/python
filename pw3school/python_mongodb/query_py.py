# MongoDB Query
# Filter The Result
# When finding documents in a collection, you can filter the result by using a query object
# The first argument of the find() method is a query object, and is used to limit the search

# Find documents with the address "Park Lane 38"
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['mydatabase']
collection = db['customers']
myquery = {"address": "Park Lane 38"}
mydoc = collection.find(myquery)

for x in mydoc:
    print(x)

# Advanced Query
# To make advanced queries you can use modifiers as values in the query object
# E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the
# greater than modifier: {"$gt":"S"}

# Find documents where the address starts with the letter "S" or higher
myquery = {"address": {"$gt": "S"}}
mydoc = collection.find(myquery)
print("#" * 81)
for x in mydoc:
    print(x)

print("#" * 81)

# Filter with Regular Expressions
# You can also use regular expressions as modifier
# Regular expressions can only be used to query strings

# To find only the documents where the "address" field starts with the letter "S" use the regular expression {"$regex":"^S"}
# Find documents where the address starts with the letter "S"
myquery = {"address": {"$regex": "^S"}}
mydoc = collection.find(myquery)
for x in mydoc:
    print(x)
