import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Jimmy", "China town")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, " data added, ID: ", mycursor.lastrowid)
