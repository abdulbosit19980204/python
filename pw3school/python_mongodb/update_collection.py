# MongoDB Update

# Update Collection
# You can update a record, or document as it is called in MongoDB, by using the update_one() method
# The first parameter of the update_one() method is a query object defining which document to update

# Note: IF the query finds more than one record, only the first occurence is updated.

# The second parameter is an object defining the new values of the document

# Change the address from "Valley 345" to "Canyon 123"

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}
mycol.update_one(myquery, newvalues)

for i in mycol.find():
    print(i)
print("***" * 50)
# Update Many
# To update all documents that meets the criteria of the query, use the update_many() method
# Update all documents where the address starts with the letter "S"
myquery = {"address": {"$regex": "^S"}}
newvalues = {"$set": {"address": "Minnie"}}
x = mycol.update_many(myquery, newvalues)
for i in mycol.find():
    print(i)

