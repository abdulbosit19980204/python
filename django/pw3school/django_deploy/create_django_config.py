# Deploy Django - django.config

# Provider - Specific Settings
# We have chosen AWS as our hosting provider, and Elastic Beanstalk as a service to deploy the Django project, and it
# has some specific requirements.

# .ebextensions Folder
# It requires that you create a folder on the root lever of your project called ".ebextensions"

# Create django.confid File
# In the .ebextensions folder, create a file called django.config:

# Open the file and insert these settings:
".ebextensions/django.config:"
"""
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: my_tennis_club.wsgi:application
"""
# Note: These steps are specific for AWS and Elastic beanstalk, but every provider has some provider-specific settings.

# The next step is to wrap all the dependencies into one .zip file, which you will learn in the next chapter
