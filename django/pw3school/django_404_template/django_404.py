# Django 404 (page not found)

# Page Not found

# If you try to access a page that doesn't exist( a 404 error), Django directs you to a built-in view that handles
# 404 errors. We will learn hot to customize this chapter, but first, just try to request a page that does not exsist.

# In the browser window, type 127.0.0.1:8000/massdas/ in the address bar
# You will get one of two result

# 1. Not Found message
# 2. Page Not Found python error

# If you got the first result, you got directed to the built-in Django 404 tamplate

# If you got the second result, then DEBUG is set to True in your setting, and you must set it to False to get directed
# to the 404 template

# This is done in the setting.py file, which is located in the project folder, in our case the my_tennis_club folder,
# where you also have to specify the host name from where your project runs from.

# Set the debug property to False, and allow the project to run from your local host
"""
.
.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
.
.
"""

# Important

"""
When DEBUG = False, Django requires you to specify the hosts you will allow this Django project to run from. 
In production, this should be replaced with a proper domain name

ALLOWED_HOSTS = ['yourdomain.com']


"""

# Customize the 404 Template

# Django will look for a file named 404.html in the templates folder, and display it when there is a 404 error.

# If no such file exists, Django shows the "Not Found" that you saw in the example above.
# To customize this message, all you have to do is to create a file in the templates folder and name it 404.html, and
# fill it with whatever you want

# 404.html file

"""
<!DOCTYPE html>
<html>
<title>Wrong address</title>
<body>

<h1>Ooops!</h1>

<h2>I cannot find the file you requested!</h2>

</body>
</html>
"""


