# Connect to Database

# Modify Settings

# To make Django able to connect to your database, you have to specify it in the DATABASES tuple in the settings.py file
# Before, it looked like this.

# SQLite settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Now you should change it to look like this:
# PostgreSQL settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'masteruser',
        'PASSWORD': '12345678',
        'HOST': 'w3-django-project.cdxmgq9zqqlr.us-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}

# The values will be different for your project.

# Engine?
# As you can see in the settings.py file, we insert postgresql instead of sqlite

# Name?
# The database doesn't have a name, but you have to assign one in order to access the database
# If no name is given, the provider accepts 'postgres' as the name of the database

# Username and Password?
# Insert the username and password that you specified when you created the database.

# Host? Port?
# As you can see in the settings.py file, we insert postgresql instead of sqlite, and insert the username and password
# that we specified when we created the database.

# The HOST and PORT can be found under the "Connectivity & security" section in the RDS instance. They are described as
# "Endpoint" and "port"

# Migrate
# Once we have done the changes in settings.py we must run a migration in on virtual environment, before the changes will
# take place

# py manage.py migrate

