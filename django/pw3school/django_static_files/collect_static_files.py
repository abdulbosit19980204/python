# Django - Collect Static Files

# Handle Static Files
# Static files in your project, like stylsheets, JavaScripts, and images, are not handled automatically by Django when
# DEBUG=False

# When Debug=True, this worked fine, all we had to do was to put them in the static folder of the application
# When Debug = False, static files have to be collected and put in a specified folder before we can use it.

# Collect Static Files
# To collect all necessary static files for your project, start by specifying a STATIC_ROOT property in the settings.py
# file. This specifies a folder where you want to collect your static files.
# You can call the folder whatever you like, we will call it "productionfiles".
# settings.py file

STATIC_ROOT = BASE_DIR / 'productionfiles'

STATIC_URL = 'static/'

# You could manually create this folder and collect and put all static files of your project into this folder, but
# Djnago has a command that do this for you.

# py manage.py collectstatic

# which will produce this result
# 131 static files copied to 'C:\Users\your_name\myworld\my_tennis_club\productionfiles'.
