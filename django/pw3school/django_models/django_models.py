# Django Models

# A Django model is a table in your database

# Django Models

# Up until now in this tutorial, output has been static data from Python on HTML templates

# Now we will see how Django allows us to work with data, without having to change or upload files in the process.

# In Django, data is created in objects, called Models, and is actually tables in a database.

# Create Table (Model)

# To create a model, navigate to the "models.py" file in the "/members/" folder

# Open it, and add a "Member" table by creating a "Member class", and describe the table fields in it:

from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    # The first field, firstaname, is a Text field, and will contain the first name if the members
    # The second field, lastname, is also a Text field, with the member's last name

# Both firstname and lastname is set up to have a maximum of 255 characters.

# SQLite Database
# When we created the Django project, we got an empty SQLite database.
# It was created in the my_tennis_club root folder, and has the filename db.sqlite3
# By default, all Models created in the Django project will ve created as tables in this database.

# Migrate

# Now when we have described a Model in the models.py file, we must run a command to catually create the table in the database
# Navigate to the /my_tennis_club/ folder and run this command:
# py manage.py makemigrations members

# Which will result in this output:
#   - Create model Member

# Django creates a file describing the changes and stores the file in the /migrations/ folder

# Note that Django inserts an id filed for your tables, which is an auto increment number
# (first record gets the value 1, the second record 2 etc), this is the default behaviour of Django,
# you can override it by describing your own id field.
# The table is not created yet, you will have to run one more command,
# then Django will create and execute as SQL statement,
# based on the content of the new file in the /migrations/ folder

# Run the migrate command:

# py manage,oy migrate
# Now you have a Member table in your database!

# View SQl

# As a side-note: you can view the SQL statement that were executed from the migration above. All you have to do is to
# run this command, with the migration number:
# py manage.py sqlmigrate members 0001
