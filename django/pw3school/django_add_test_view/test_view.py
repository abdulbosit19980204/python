# Django Add Test View

# Test View

# When testing different aspects of Django, it can be a good idea to have somewhere to test code without destroying
# the main project

# This is optional off course, but if you like to follow all steps in this tutorial, you should add a test view that is
# exactly like the one we create below


# Add View

# Start by adding a view called "testing" in the views.py file

# views.py file from app

from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context=context))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render)


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context=context))


# URLs
# We have to make sure that incoming urls to /testing/ will be redirected to the testing view
# This is done in the urls.py file in the members folder

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.mebers, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]

# Test Template

# We also need a template where we can play around with
# You might noticed that there was a reference to a template in the testing view?

# Create a template called "template.html" in the templates folder:

# Open the template.html file and insert the following

"""
<!DOCTYPE html>
<html>
<body>

{% for x in fruits %}
  <h1>{{ x }}</h1>
{% endfor %}

<p>In views.py you can see what the fruits variable looks like.</p>

</body>
</html>
"""

