# MySQL Where
# Select with a filter
# When selecting records from a table , you can filter the selection by using the "WHERE" statement
# Select record(s) where the adress is "New York": result

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address='Andijon'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

# Wildcard Character
# You can also select the records that starts, includes, or ends with a given letter or phrase
# Use the % to represent wildcard characters

sql = "SELECT * FROM customers WHERE address LIKE '%New%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

# Prevent SQL INJECTION
# When query values are provided by the user, you should escape the values
# This is to prevent SQL Injection, which is a common web hacking technique to destroy or misuse your database
# The mysql.connector module has methods to escape query values
# Escape query values by using the placeholder %s method
sql = "SELECT * FROM customers WHERE address=%s"
adr = ("Yellow Garden 2",)
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

