# Django - Global Static files

# Add a Global CSS File


# We have learned how to add a static file in the application's static folder, and how to use it in the application
# But what if other applications in your project wants to use the file?

# Then we have to create a folder on the root directory and put the file(s) there.
# It is not enough to create a static folder in the root directory, and Django will fix the rest.We have to tell Django
# where to look for these static files.
# Start by creating a folder on the project's root level, this folder can be called whatever you like, I will call it
# "mystaticfiles" in this tutorial.

# Modify Settings

# You will have to tell Django to also look for static files in the "mystaticfiles" folder in the root directory, this is
# done in the settings.py file.

# Add a STATICFILES_DIRS list:
# settings.py file
STATIC_ROOT = BASE_DIR / 'productionfiles'

STATIC_URL = 'static/'

# Add this in your settings.py file:
STATICFILES_DIRS = [
    BASE_DIR / 'mystaticfiles'
]

# In the STATICFILES_DIRS list, you can list all the directories where Django should look for static files.
# The BASE_DIR keyword represent the root directory of the project and together with the / "mystaticfiles", it means the
# mystaticfiles folder in the root directory.

# Search Order
# If you have files with the same name, Djnago will use the first occurence of the file. The search starts in the
# directories listed in STATICFILES_DIRS, using the order you have provided. Then, if the file is not found, the
# search continues in the static folder of each application

# Modify the Template
# Now you have a global CSS file for the entire project, which can be accessed from all your applications.
# To use it in a template, use the same syntax as you did for the myfirst.css file
# Begin the template with the {% load static %}
# And refer to the file like this: <link rel="stylesheet" href="{% static 'myglobal.css' %}">

# Didn't work
# That is correct. You need to collect the static files once again.

# Collect Static Files
# Run the collectstaic command to collect the new static file.
# py manage.py collectstaic

