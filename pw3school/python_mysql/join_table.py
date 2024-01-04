# MySQL Join

# Join Two or More Tables
# You can combine  rows from two or more  tables, based on a related column betwen them by using a JOIN statement
# consider you have a "users"  table and a "products" table
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user='root',
#     password='1234',
#     database='mydatabase'
# )
#
# cursor = mydb.cursor()

# Create the products table
# cursor.execute("CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT)")

# Insert data into the products table
# sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
# val = [
#     ("Apple", 10000),
#     ("Banana", 15200),
#     ("Peach", 50000),
#     ("Pineapple", 100000),
#     ("Cherry", 150000),
# ]
#
# cursor.executemany(sql, val)
# mydb.commit()
#
# print(cursor.rowcount, "record inserted.")

# sql = "ALTER TABLE customers ADD fav int "
# sql = "INSERT INTO customers (fav) VALUES (%s)"
# sql = "DELETE FROM customers WHERE id=(%s)"
# sql = "UPDATE customers SET fav = %s WHERE id = %s"
# val = [
#     (4, 11),
#     (2, 12),
#     (1, 13),
#     (4, 14),
# ]
# cursor.executemany(sql, val)
# mydb.commit()

# These two tables can be combined by using customers' fav field and product's id fields:

# Join users and products  to see  the name of the users favourite product

# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user='root',
#     password='1234',
#     database='mydatabase'
# )
# cursor = mydb.cursor()
# sql = ("SELECT customers.name AS customer, products.name AS favourite, FROM customers INNER JOIN products ON customers.fav = products.id")
#
# cursor.execute(sql)
# results = cursor.fetchall()
# for row in results:
#     print(row)

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  customers.name AS customer, \
  products.name AS favorite \
  FROM customers \
  INNER JOIN products ON customers.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
print('*' * 80)
# Note: You can use JOIN instead of INNER JOIN. They will both give the same result

# LEFT JOIN
# In the example above, Hannah, and Michael were exclude from the result, that is because INNER JOIN only shows the
# records where there is a match

# If you want to show all users, even if they don't have a favourite product, use the LEFT JOIN statement
# Select all users and their favourite product:
sql = "SELECT \
  customers.name AS customer, \
  products.name AS favorite \
  FROM customers \
  LEFT JOIN products ON customers.fav = products.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print('*' * 80)

# RIGHT JOIN
# If you want to return all products, and the customers who have them as their favorite, even if no user have them
# as their favourite, use the RIGHT JOIN statement

# Sellect all products, and the user(s) who have them as their favourite
sql = "SELECT \
  customers.name AS customer, \
  products.name AS favorite \
  FROM customers \
  RIGHT JOIN products ON customers.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("Products")
for x in myresult:
    print(x)
print('*' * 80)

