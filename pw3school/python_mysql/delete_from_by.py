# MySQL Delete from BY

# Delete Record
# You can delete records from an exsiting table by using the "DELTE FROM" statement

# Delete any record where the address is "Mountain 21"

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY address"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

print('*' * 80)

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

# Important: Notice the satatement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table
# Notice the Where clause in the DELETE syntax: The Where clause specifies wich record(s) that should be deleted.
# If you omit the where clause, all records will be deleted

# Prevent SQL Injection
# It is considered a good practise to escape the values of any query, also in delete statements
# This is  to prevent SQL injections, which is a common web hacking technique to destroy or misues your database
# The mysql.connector module uses the placeholder %s to escape values in the delete statement

# Escape values by using the placeholder %s method

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
print('*' * 80)

sql = "DELETE FROM customers WHERE name=%s"
name = ("Viola",)
mycursor.execute(sql, name)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")


