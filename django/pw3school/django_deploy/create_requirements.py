# Deploy Django - Create Requirements

# Lock in Dependencies

"""
When you create a Django application, there are some Python packages that your project depends on.
Django itself is a Python package, and we have to make sure that the server where we deploy our project also has the
Django package installed, and all the other packages your project requires.

Luckily there is a command for this as well, just run this command in the command view:
"""

# py -m pip freeze > requirements.txt

# The result of the above command, is a file called requirements.txt being created in the project
# The file contains  all the packages that this project depends on: with this content:

# Note: You can create this file on your own, and insert the packages manually,
# just make sure you get all the packages your project depends on, and you must name the file requirements.txt

# Now the hosting provider knows which packages to install when we deploy our project.
# But Elastic Beanstalk needs more information, go to the next chapter to create an "EB" config file
