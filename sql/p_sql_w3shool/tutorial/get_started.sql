-- PostgreSQL Get Started

-- Connect to the Database

-- If you have followed the steps from the Install PostgreSQL page, you now have a PostgreSQL database on you computer.
There
are several ways to connect to the database, we will look at two ways in this tutorial.
      SQL Shell(psql)
      pgAdmin 4

Both of them comes with the installation of PostgreSQL

      SQL Shell(psql)
SQL shell is a terminal based program where you can write and execute SQL syntax in the command-line terminal.

OPEN SQL Shell (psql)

You will find the SQL Shell(psql) tool in the start menu under PostgreSQL on windows

1. "Server name" - Insert the "name" of the server (default = localhost)
2. "Databse" - The suggested "database" is [postgres], which is correct, press [Enter] to accept
3. "Port" - The suggested port is [5432], which is the correct, at least in my case, press [Enter] to accept
4. "User name" - The suggested username is [postgres]
5. "Password" -  Enter the password you chose when you installed the PostgreSQL database

RESULT = The result is "postgres=#" when you have succesfully connected to the database!

Execute SQL Statements

Once you have connected to the database, you can start executing SQL statements.
Our database is empty, so we cannot query any tables yet, but we can check the version with this SQL statement:

SELECT version()

To insert SQL statements in the SQL Shell command, just write them after the "postgres=#" command and press [Enter]


Remember the Semicolon
Note: Always end SQL statements with a semicolon ";"

SQL Shell waits for the semicolon and executes all lines as one SQL statement.
A  multiple lines SQL statement is not executed before we include a semicolon at the end.



