# Django Template Variables

# Template Variables
# In Djnago templates, you can render variables by putting them inside {{ }} brakets:

# templates/template.html

# <h1>Hello {{firstname}}, how are you? </h1>

# Create Variable in View

# The variable firstname in the example above was sent to the template via a view:
# views.py

from djnago.http import HttpResponse
from django.template import loader


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'firstname': 'Linus',
    }
    return HttpResponse(template.render(context, request))


# As you can see in the view above, we create an object named context and fill it with data, and send it as the
# first parameter in the template.render() function.

# Create Variables in Template
# You can also create variables directly in the template, by using the {% with %} template tag.
# The variable is available until the {% endwith %} tag appears:
"""
{% with firstname ="Tobias" %}
<h1>Hello {{firstname}}, how are you?</h1>
{% endwith %}

"""

# Data From a Model
# The example above showed an easy approach on how to create and use variables in a template.
# Normally, most of the external data you want to use in a template, comes from a model.  We have created a model in the
# previous chapters, called Member, which we will use in many examples in the next chapters of this tutorial
# To get data from the Member model, we will have to import it in the views.py file, and extract data from it in the view:

# views.py file
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member


def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

# Now we can use the data in the template:

"""
<ul>
{% for x in mymembers %}
<li>
{{x.firstname}}
</ly>
{% endfor %}
</ul>
"""