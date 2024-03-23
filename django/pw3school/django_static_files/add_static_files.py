# Django - Add Static File

# Create Static Folder
# When building web applications, you probably want  to add some static files like images or css file.
# Start by creating  a folder named "static" in your project, the same place where you created the templates folder.
# The name of the folder has to be static.
# Add a CSS file in the static folder, the name is your choice, we will call it "myfirst.css" in this example:

# Modify the Template
"""
Now you have a CSS file, with some CSS styling. The next step will be to include this file in a HTML template:
Open the HTML file and add the following:
"""
# {% load static %}
# And:
# <link rel="stylesheet" href="{% static 'myfirst.css' %}">


# Choose Debug=False
"""
For the rest of this tutorial, we will run with DEBUG=False, even in development, because that is the best wat to learn
how to work with Django.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

"""
# ALLOWED_HOSTS

"""
When using DEBUG=False you have to specify which host name(s) are allowed to host your work. You could choose.
'127.0.0.1' or 'localhost' which both represents the address of your local machine.

We choose '*', which means any address are allowed to host this site. This should be change into a real domain name 
when you deploy your project to a public server.
"""

# Didn't Work?
# That is right, the example still does not work.
# You will have install a third-party library in order to handle static files.
# There are many alternatives, we will show you how to use a Python library called "WhiteNoise" in the next chapter.
