# Django prepare Template

# Create Template

# After creating Models, with the fields and data we want in them, it is time to display the data in a web page
# Start by creating an HTML file named all_members.html and place it in the /templates/ folder

# all_members.html file

"""

<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>

<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }} {{ x.lastname }}</li>
  {% endfor %}
</ul>

</body>
</html>
"""

# Do you see the {% %} brackets inside the HTML document?

# They are Django Tags, telling Django to perform some programming logic inside these brackets
# You will learn more about Django Tags in our Django Tags chapter

# Modify View

# Next we need to make the model data available in the template. This is done in the view
# In the view we have to import the Member model, and send it to the template like this.

# views.py file

from django.template import loader

from .models import Member


def mebers(request):
    mymembers = Member.objects.all().values()
    template - loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


# The members views does the following

# Creates a mymembers object with all the values of the Member model
# Loads the all_members.html template.
# Creates an object containing the mymembers object
# Sends the object to the template
# Outputs the HTML that is rendered by the template.

# The Result

# We have created an example so that you can use see the result
# Start the server by navigating to the /my_tennis_club/ folder and execute this command

" py manage.py runserver"

# In the browser window, type 127.0.0.1:8000/members/ in the address bar.

