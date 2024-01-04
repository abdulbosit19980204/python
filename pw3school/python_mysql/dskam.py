import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "SELECT name FROM customers"
sql2 = "SELECT id FROM customers"
mycursor.execute(sql)
result = mycursor.fetchall()
mycursor.execute(sql2)
ids = mycursor.fetchall()
print(ids)
# plt.bar(ids, result)
# # plt.title(result)
# plt.show()
x = []
t=[]
for i in ids:
    x.append(int(list(i)[0]))
for j in result:
    t.append(str(list(j)))
print(t)
plt.bar(x,t)
plt.show()