# Create Table

# To create a table in MySQL, use the "CREATE TABLE" statement
# Make sure you define the name of the database when you create the connection

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydatabase"
)

mycursor = db.cursor()
# mycursor.execute("CREATE TABLE users (name VARCHAR(255), address VARCHAR(255))")
# if the above code was executed with no errors, you have now successfully created a table

# Check if Table Exsists
# YOu can check if a table exsist by listing all tables in your database with the "show tables" statement
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)

# Primary Key
# When creating a table, you should also create a column with a unique key for each record
# This can be done by defining a Primary key
# We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. String at 1
# and increased by one for each record

# Create primary key when creating the table
# mycursor.execute("CREATE TABLE ntabel (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# If the table already exsist, use the ALTER TABLE keyword

# Create primary key on  an existing table
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
