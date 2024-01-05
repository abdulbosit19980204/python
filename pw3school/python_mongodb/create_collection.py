# MongoDB Create Collection

# A Collection in MongoDB is the same as a table in SQL database

# Creating a Collection
# To create a collection in MongoDB, use database object and specify the name of the collection you want to create
# MongoDB will create the collection if it doesn't exist

# Create a collection called "customers"
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]

# Important: In MongoDB, a collection is not created until it gets content

# MongoDB waits until you have inserted a document before it actually creates the collection

# Check IF collection Exist
# Remember: In MongoDB, a collection is not created until it gets content, so if your first time creating a collection, you should
# complete the next chapter(create document) before you check if the collection exsist

# You can check if a collection exist in a database by listining all collections

# Return a list of all collections in your database
print(db.list_collection_names())

# Or you can check a specific collection by name
# Check if the "customers" collection exist

collist = db.list_collection_names()
if "customers" in collist:
    print("The collection is exist")


