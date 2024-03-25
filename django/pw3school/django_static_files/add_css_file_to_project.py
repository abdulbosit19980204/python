# Add CSS file to the Project

# The Project - My Tennis Club

# If you have followed the steps in the entire Django tutorial, you will have my_tennis_club project on you computer,
# with 5 members:
# We want to add a stylesheet to this project, and put it in the "mystaticfiles" folder

# The name of the CSS file is your choice, we call it "mystyles.css" in this project
# Open the CSS file and insert the CSS styles

# Modify the Master Template
# Now you have a css file, the next step will be to include this file in the master template:

# Check settings.py
# Make sure your settings.py file contains a "STATICFILES_DIRS" list with a reference to the mystaticfiles folder
# on the root directory, and that you have specified a "STATICFILES_ROOT" folder

STATIC_ROOT = BASE_DIR / 'productionfiles'

STATIC_URL = 'static/'

# Add this in your settings.py file:
STATICFILES_DIRS = [
    BASE_DIR / 'mystaticfiles'
]

# Collect Static Files
# Every time you make a change in a static file, you must run the collectstatic command to make the changes take effect:

# py manage.py collectstatic

# If you have executed the command earlier in the project, Django will prompt you with a question:
# Type 'yes'. This will update any changes done in the static files, and give you this result:

