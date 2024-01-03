# MySQL order by
# Sort the Result

# Use the ORDER BY statement  to sort the result in ascending or descending order
# The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='1234',
    database='mydatabase'
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    print(row)
print('*' * 50)
# Order by desc
# Use the DESC keyword to sort the result in a descending order
# Sort the result reverse alphabetically by name
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    print(row)
