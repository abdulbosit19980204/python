# Introduction to PostgreSQL

# Database Engines
# Django comes with a SQLite database which is greate for testing and dubugging at the beggining of project.
# However, it is not very suitable for production.
# Django also support these database engines:
"""
 *PostgreSQL
 *MariaDB
 *MySQL
 *Oracle
"""

# We will take a closer look at the PostgreSQL database engine

# PostgreSQL

# PostgreSQL database is an open source relational database, which should cover most demands you have when creating
# a database for a Django project.

# It has a good reputation, it is reliable, and it perform well under most circumstances.
# We will add a PostgreSQL database to our Django project.
# To be able to use PostgreSQL in Django we have to install a package called "psycopg2".


# Install psyconpg2
# Type this command in the command line to install the package. Make sure you are still inn the virtual environment:

# pip install psycopg2-binary

# The psyconpg2 package is a driver that is necessary for PostgreSQL to work in python.
# We also need a server where we can host the database.
