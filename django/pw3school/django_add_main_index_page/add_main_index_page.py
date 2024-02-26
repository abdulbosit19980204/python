# Django Add Main Index Page

# Main Index Page

# Our project needs a main page

# The main page will be the landing page when someone visits  the root folder of the project.

# Now, you get an error when visiting the root folder of your project:
# 127.0.0.1:8000/

# Start by creating a template called main.html

# Main

"""
{% extends "master.html" %}

{% block title %}
  My Tennis Club
{% endblock %}


{% block content %}
  <h1>My Tennis Club</h1>

  <h3>Members</h3>

  <p>Check out all our <a href="members/">members</a></p>

{% endblock %}
"""

# Create a New View

# Then create a new view called main, that will deal with incoming requests to root of the project:
"""
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
    'mymembers':mymembers,
    }
    return HttpResponse(template.render(context, request))
    
def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mymember':mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    
"""

# The main view does the following
"""
    * loads the main.html template.
    * Outputs the HTML that is rendred by the template.
"""

# Add URL

# Now we need to make sure that the role url points to the correct view.
# Open the urls.py file and the main view to the urlpatterns list:

# urls.py file

"""
from django.urls import path
from . import views

urlpatterns=[
    path('', views.main, name='main'),
    path('members/', views.members, name='members')
    path('members/details/<int:id>', views.details, name='details')
]
"""

# Add Link Bacl to Main

# The members page is missing a link back to the main page, so let us add that in the all_members.html template,
# in the content block:

# all_members.html file

"""
{% extends "master.html" %}

{% block title %}
  My Tennis Club - List of all members
{% endblock %}


{% block content %}

  <p><a href="/">HOME</a></p>

  <h1>Members</h1>
  
  <ul>
    {% for x in mymembers %}
      <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
    {% endfor %}
  </ul>
{% endblock %}
"""
