# Django Admin - Include Member

# Include Member
# To include the Member model in the admin interface, we have to tell Djnago that this model should be visible in the
# admin interface. This is done in a file called admin.py, and is located in your app's folder, which in our case is
# the members folder.

# Open it, and it should look like this
from django.contrib import admin
# Register your models here

# Insert a couple of lines here to make the Member model visible in the admin page:

after Register