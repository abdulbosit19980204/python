# MySQL Drop Table
# Delete a table
# you can delete an exsiting table by using drop table statement

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user='root',
    password='1234',
    database='mydatabase'
)

cursor = db.cursor()
sql = "SELECT * FROM customers ORDER BY name"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)

sql = "SHOW TABLES"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)

# Delete the table 'customers'
# sql = "DROP TABLE users "
# cursor.execute(sql)
# db.commit()

# Drop only if Exist

# If the table you want to delete is already deleted, or for any other reason doesn't exist, you can use the IF EXISTS
# keyword to avoid getting an error
# Delete the table "users" if it exsist
sql = "DROP TABLE IF EXISTS users"
cursor.execute(sql)
db.commit()

