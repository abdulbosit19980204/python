# Django Admin - Set Fields to Display

# Make the list Display More Reader  - Friendly
# When you display a Model as a list, Django displays each record as the string representation of the record object,
# which in our case is "Member object (1)", "Member object(2)" etc.:

# To change this to more reader-friendly format, we have two choices:
#     1. Change the string representation function, __str__() of the Member Model
#     2. Set the list_details property of the Member Model

# Change the String Representation Function
# To change the string representation, we have to define the __str__() function of the Member Model in models.py like this:

# models.py file
from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

# Defining our own __str__() function is not a Django feature, it is how to change the string
# representation of objects in Python

# Set list_display
# We can control the fields to display by specifying them in a list_display property in the admin.py file.

