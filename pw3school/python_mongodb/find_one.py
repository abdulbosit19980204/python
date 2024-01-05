# MongoDB Find
# In MongoDB we use the find() and find_one() methods to find data in a collection
# Just like the Select statement is used to find data in a table in a MySQL database

# Find One
# To select data from a collection in MongoDB, we can use the find_one() method
# The find_one() method returns the first occurence in the selection

# Find the first document in the customers collections
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["mydatabase"]
mycol = mydb["customers"]
result = mycol.find_one({"name": "John"})
print(result)  # {'_id': ObjectId('659757c329ae471c4c174cf8'), 'name': 'John', 'address': 'Highway 37'}

# Find All

# To select data from a table in MongoDB, we can also use the find() method
# The find() method returns all occurences in the selection
# The first parameter of the find() method is a query object. In this example we use an ampty query object, which select all
# documents in the collection
result = mycol.find()
for i in result:
    print(i)
print('*' * 80)
# Return only Some Fields
# The second parameter of the find() method is an object describing which fields to include in the result
# This parameter is optional, and if omitted, all fields will be included in the result

for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

# You are not allowed to specify both 0 and 1 values  in the same object (except if one of the fields is the _id field)
# If you specify a field with the value 0, all other fields get the value 1, and vice versa

# This example will exclude "address" from the result:
for x in mycol.find({}, {"address": 0}):
    print(x)

# You get an error if you  specify both 0 and 1 values in the same object (expect if one of the fields is the _id filed)
# for x in mycol.find({}, {"name": 1, "address": 0}):
#     print(x)
