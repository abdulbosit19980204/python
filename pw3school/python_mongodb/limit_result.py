# MongoDB Limit

# Limit Result
# To limit the result in MongoDB, we use the limit() method
# The limit() method takes one parameter, a number defining how many documents to return
# Consider you have a "customers" collections

# Limit the result to only return 5 documents
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]
result = collection.find().limit(5)
for i in result:
    print(i)

