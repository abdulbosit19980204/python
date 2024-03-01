# Django Admin - Create User


# Create User
# To be able to log into the admin application, we need to create a user
# This is done by typing this command in the command view

"py manage.py createsuperuser"

# which will give this propmt: Username:

# Here you must enter: username, email address, (you can just pick a fake e-mail address), and password

# Now run server
"py manage.py runserver"

# In the borwser window, type 127.0.0.1:8000/admin/ in the address bar
# And fill in the form with the correct username and password


# Missing Model
# The Members model is missing, as it should be, you have to tell Djnago which models that should be visible in the admin
# interface. You will learn how to include the Members model in the next chapter

