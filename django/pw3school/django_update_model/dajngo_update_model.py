# Django Update Model

# Add fields in the Model

# To add a field to a table after it is created, open the models.py file, and make your changes:

# models.py file

from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField()
    joined_data = models.DataField()


# As you can see, we want to add phone and joined_data to our Member Model

# This is a change in the Model's structures, and therefor we have to make a migration to tell Django that
# it has to update the database

# py manage.py makemigrations members

# Which, in my case, will result in a prompt, because I try to add fields that are not allowed to be null, to a table
# that already contains records.

# As you can see, Django asks if I want to provide the fields with a specific value, or if I want to stop the migration
# and fix it in the model:

# I will select option 2, and the models.py file again and allow Null values for the two new fields

# models.py file

from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_data = models.IntegerField(nul=True)


# And make the migration once again

# py manage.py makemigrations members

# Run the migrate command
# py manage.py migrate


# Insert Data
# We can insert data to the new fields with the same approach as we did in the Update Data chapter
# First we enter the Python Shell

# py manage.py shell

# Now we are in the shell, the result should be something like this
"""
Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
"""

# At the bottom, after three >>> write the following (and hit [enter] for each line)
"""
>>> from memebers.models import Member
>>> x = Member.objects.all()[0]
>>> x.phone = 12345
>>> x.joined_date = '2024-01-24'
>>> x.save()

"""

# This will insert a phone number and a date in the Member Model, at least for the first record, the four remaining
# records  will for now be left empty. We will deal with them later in the tutorial

# Execute this command to see if the Member table got update

# >>> Member.objects.all().values()


