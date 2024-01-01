# Python MySQL Create Database
# To create a database in MySQL, use the "Create Database" statement
# create a database named "mydatabase":
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)
mycursor = mydb.cursor()
"""
mycursor.execute("CREATE DATABASE mydatabase")
"""

# If the above code was executed with no errors, you have successfully created a database

# Check if the database Exsist
# You can check if a database exsist by listing all databases  in your system by using the "SHOW DATABASES" statement
# Return a list of your system's databases


mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

# Or you can  try to access the database when making the connection
# Try connecting to the database "mydatabase"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydatabase"
)
# mycursor = mydb.execute("SELECT * FROM mydatabase")

# If the database does not exist, you will get an error
