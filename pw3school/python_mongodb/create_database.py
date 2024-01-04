# Python MongoDB Create Database

# Creating Database
# To create  a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct
# ip address and the name of the database you want to create

# MongoDb will create the database if it doesn't exsist, and make a connection to it

# Create a database called "mydatabase"
import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#
# mydb = myclient["mydatabase"]

# Important: In MongoDB, a database is not created until it gets content!

# MongoDB waits until you have created a collection (table), with a least one document (record) before it actually creates
# the database (and collection).

# Check if Database Exsist

# Remember: In MongoDB, a database is not created until it gets content, so if this is your first time creating a database
# you should complete the next two chapters( create collection and create document) before you check if the database exsist

# You can check if a database exist by listening all database in you system
# Return a list of your system's databases
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_names())

# Or you can check a specific database by name
# Check if "mydatabase" exists
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("Database is exist")
else:
    mydb = myclient["mydatabase"]
    print(mydb)