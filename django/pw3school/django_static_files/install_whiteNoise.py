# Django - Installing WhiteNoise

# White Noise
# Django does not have a built-in solution for serving static files, at least not in production when "DEBUG" has to be
# "False"
# We have to use a third-party solution to accomplish this
# In this tutorial we will use WhiteNoise, which is a Python library, built for serving static files.

# Install WhiteNoise
# To install WhiteNoise in your virtual environment, type the command below.

# pip install whitenoise

# Modify Settings
# To make Django aware of you wanting to run  WhiteNoise,
# you have to specify it in the "MIDDLEWARE" list in settings.py file:

# settings.py file

"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
].

"""

# Collect Static Files
# There are one more action you have to perform before you can serve the static file from the example in the
# previous chapter. You have to collect all static files and put them into one specified folder. You will learn
# how in the next chapter.
