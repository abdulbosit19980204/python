# Django Templates

# Templates

# In the Django Intro page, we learned that the result should be in HTML, and it should be created in a template,
# so let's do that.

# Create a "templates" folder inside the "members" folder, and create a HTML file named "myfirst.html"

# Modify the View

# Open the "views.py" file and replace the "members" view with this

from django.http import HttpResponse
from django.template import loader


def members(request):
    template = loader.get_template('myfirst-html')
    return HttpResponse(template.render())


# Change Setting

# To be able to work with more complicated stuff than "Hello World", We have to tell Djagno that a new app is created.
# This is done in the setting.py file in the my_tennis_club folder.
# Look up the INSTALLED_APPS[] list and add the members app like this

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members'
]
