# MySQL Limit

# Limit the result
# You can limit the number of records returned from the query, by using the "LIMIT " Statement
# Select the first 5 records from the "customers" table:
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="mydatabase"
)

cursor = db.cursor()
sql = "select * from customers limit 5"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)
print('*' * 50)
# Start From Another position
# If you want to return five records, starting from the third record, you can use the "OFFSET" keyword

# Start from position 3, and return 5 records

sql = "SELECT * FROM customers limit 5 offset 2"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)
