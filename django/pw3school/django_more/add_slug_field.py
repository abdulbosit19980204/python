# Django Slug Field

# What is Slug?

# Have you ever seen url's that look like this:

# w3schools.com/django/learn-about-slug-field

# The "learn-about-slug-field" part is a slug.

# It is a description containing only letters, hyphens, numbers or underscores.
# It is often used in url's to make them easier to read, but also to make them more search engine friendly.

# Url without Slug
# If you have followed our Django Project created in this tutorial, you will have a small Django project.
# To add slug

# Modify the models.py File
# Start by adding a new field in the database.
# Open the models.py file and add a fielf called slug with the data type SlugField:

# models.py
slug = models.SlugField(default="", null=False)
# This is a change in the Model's Structure, and therefore we have to make a migration to tell Django that it has to
# update the database.

# py manage.py makemigrations

# Add the migrate command:
# py manage.py migrate

# Change Admin
# Now we have a new field in the database, but we also want this field to be updated automatically
# when we set the firstname or lastname of a memeber

# This can be done with a built-in Django feature called prepopulated_fields where you specify the field you want to
# prepopulated, and a tuple with the fields you want to populate it with

# This is done in the admin.py file

from django.contrib import admin
from .models import Member


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)
    prepopulated_fields = {"slug": ("firstname", "lastname")}


admin.site.register(Member, MemberAdmin)

# Modify Template

# Now we can replace the ID field with the slug field through the project
# Start with the all_members.html template, where we have a link to the details page:

"""
{% extends "master.html" %}

{% block title %}
  My Tennis Club - List of all members
{% endblock %}


{% block content %}
  <div class="mycard">
    <h1>Members</h1>
    <ul>
      {% for x in mymembers %}
        <li onclick="window.location = 'details/{{ x.slug }}'">{{ x.firstname }} {{ x.lastname }}</li>
      {% endfor %}
    </ul>
  </div>
{% endblock %}
"""
