# MySQL Update table

# Update Table
# You can update existing records in a table by using the "UPDATE" statement


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydatabase"
)

cursor = db.cursor()
sql = "SELECT * FROM customers ORDER BY address"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)

# Overwrite the address column from "Valley 345" to "Canyon 123"

sql = " UPDATE customers SET address='Canyon 123' WHERE address='Valley 345'"
cursor.execute(sql)
db.commit()
print(cursor.rowcount, "record(s) affected")

# Important: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table
# Notice the Where clause in the Update syntax: The where clause specifies which record or records that should be updated
# if you omit the where clause, all records will be updated!

# Prevent SQL Injection
# It is considered a good practise to escape the values of any query, also in update statements
# This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database
# The mysql.connector module uses the placeholder %s to escape values in the delete statement


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydatabase"
)
cursor = db.cursor()
sql = "SELECT * FROM customers ORDER BY address"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)
print('*' * 80)

# Escape values by using the placeholder %s method

sql = "UPDATE customers SET address=%s WHERE address=%s"
val = ("Valley 345", "Canyon 123")
cursor.execute(sql, val)
db.commit()
print(cursor.rowcount, "record(s) affected")
