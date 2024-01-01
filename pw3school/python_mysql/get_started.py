# Python MySQL
# Python can be used in database application
# One of the most popular databases in MySQL
from pip._internal.distributions import installed

# Install MySQL Driver
# Python needs a mysql driver to access the MySQl database
# Download and install "MySQL Connector": python -m pip install mysql-connector-python

# Test MySQL Connector
# To test in the installation was successful, or of you already have "MySQL connector" installed, create a Python page with
# the following content
import mysql.connector
# if the above code was executed with  no errors. "MySQl connector" is installed and ready to be used

# Create a connection
# Start by creating a connection to the database
# Use the username and password from your MySQL database

import mysql

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234"
)
print(mydb)

# Now we can start querying the database using SQL statements
