# Django Add Link to Details

# Details Template

# The next step in our web page will be to add a Details page, where we can list more details about a specific member.
# Start by creating a new template called details.html

# details.html file

"""
<!DOCTYPE html>
<html>

<body>

<h1>{{ mymember.firstname }} {{ mymember.lastname }}</h1>

<p>Phone: {{ mymember.phone }}</p>
<p>Member since: {{ mymember.joined_date }}</p>

<p>Back to <a href="/members">Members</a></p>

</body>
</html>
"""

# Add Link in all-members template
# The list in all_members.html should be clickable, and take you to the details page with the ID of the member you clicked on

# all_members.html file

"""
<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>
  
<ul>
  {% for x in mymembers %}
    <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }}</a></li>
  {% endfor %}
</ul>

</body>
</html>
"""

# Create new View
# Then create a new view in the views.py file, that will deal with incoming requests to the /details/ url:

# views.py file

"""
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().value()
    template = loader.get_template('all_members.html')
    context = {
    'mymembers':mymembers
    }
    return HttpResponse(template.render(context, request))
    

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mymember':mymember
    }
    return HttpResponse(template.render(context, request))
"""

# The details view does the following:
"""
    *Gets the id as an argument
    *Uses the id to locate the correct record in the Member table
    *loads the details.html template
    *Creates an object containing the member
    *Sends the object to the template
    *Outputs the HTML that is rendered by the template.
    
"""

# Add URLs

# Now we need to make sure that the /details/ url points to the correct view, with id as a parameter.
# Open the urls.py file and add the details view to the urlpatterns list

# urls.py file

"""
from django.urls import path
from . import views

urlpatterns = [
    path('members/',views.members, name ='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
"""

# You have to start server again with the runserver command, if the server is down

"py manage.py runserver"

