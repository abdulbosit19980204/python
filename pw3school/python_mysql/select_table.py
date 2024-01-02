# MySQL select from

# To select from a table in MySQL, use the "SELECT" statement
# Select all records from the "customer" table, and display the result
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for row in myresult:
    print(row)

# Note: We use the fetchall() method, which fetches all rows from the last executed statement

# Selecting columns
# To select only some of the columns in a table, use the SELECT statement followed by the column name(s)
# Select only the name and address columns

sql = "SELECT name FROM customers"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    print(row)


# Using the fetchone() Method
# If you are only interested in one row, you can use the fetchone() method
# The fetchone() method will return the first row of the result
sql = "SELECT * FROM customers"
mycursor.execute(sql)
myresult = mycursor.fetchone()
print("myresult: ", myresult)
