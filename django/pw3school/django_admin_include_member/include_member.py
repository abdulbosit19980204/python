# Django Admin - Include Member

# Include Member
# To include the Member model in the admin interface, we have to tell Djnago that this model should be visible in the
# admin interface. This is done in a file called admin.py, and is located in your app's folder, which in our case is
# the members folder.

# Open it, and it should look like this
from django.contrib import admin
# Register your models here

# Insert a couple of lines here to make the Member model visible in the admin page:

# Register your models here.
admin.site.register(Member)



# Change Display
# In the list in the screenshot, we see Member object(1) , Member object(2) etc. which might not be the data you
# wanted to be displayed in the list
# It would be better to display "firstname" and "lastname" instead.
# This can easily be done changing some settings in the models.py and / or the admin.py files.
# You will learn more about this in the next chapter
