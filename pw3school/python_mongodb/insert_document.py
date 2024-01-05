# MongoDB Insert Document

# A document in MongoDB is the same as a record in SQL databases

# Insert Into Collection
# TO insert a record, or document as it is called in Mongodb, into a collection, we use the insert_one() method
# The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each fields
# in the document you want to insert

# Insert a record in the "customers" collection
import pymongo
from pymongo.results import InsertOneResult, InsertManyResult

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]
mydict = {"name": "John", "address": "Highway 37"}
x = collection.insert_one(mydict)

# Return the _id Field
# The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the
# inserted document

# Insert another record in the "customers" collection, and return the value of the _id field
mydict = {"name": "Peter", "address": "Lowstreet 27"}
x = collection.insert_one(mydict)
print(x.inserted_id)

# If you don't specify an _id field, then MongoDB will add one for you and assign a unique id for each docuement
# In the example above no _id field was specified, so MongoDB assigned a unique _id for the record(document)

# Insert Multiple Documents
# To insert multiple documents into collection in MongoDB, we use the insert_many() method
# The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert
mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]
x = collection.insert_many(mylist)
print(x.inserted_ids)

# The insert_many() method returns a InsertManyResult object, which has a property, inserted_ids, that holds the ids of
# the inserted documents

# Insert Multiple Documents, with Specified IDs
# If you don't want MongoDB to assign unique ids for you document, you can specify the _id field when you insert the docuemtns
# Remember that the values has to be unique. Two documents cannot have the same _id
# mylist = [
#     {"_id": 1, "name": "John", "address": "Highway 37"},
#     {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#     {"_id": 3, "name": "Amy", "address": "Apple st 652"},
#     {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
#     {"_id": 5, "name": "Michael", "address": "Valley 345"},
#     {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#     {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
#     {"_id": 8, "name": "Richard", "address": "Sky st 331"},
#     {"_id": 9, "name": "Susan", "address": "One way 98"},
#     {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#     {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
#     {"_id": 12, "name": "William", "address": "Central st 954"},
#     {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
#     {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
# x = collection.insert_many(mylist)
# print(x.inserted_ids)
