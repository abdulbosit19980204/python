# Django Add Master Template

# The extends Tag

# In the previous pages we created two templates, one for listing all members, and one for details about a member.
# The templates have a set of HTML code that are the same for both templates.

# Django provides a way of making a "parent template" that you can include in all pages to do the stuff that is the same
# in all pages.

# Start by creating a template called master.html, with all the necessary HTML elements

# master.html file
"""
<!DOCTYPE html>
<html>
    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        {% block content%}
        {% endblock %}
    </body>
</html>
"""

# Do you see Django block Tag inside the <title> element, and the <body> element?

# They are placeholders, telling Django to replace this block with content from other sources.

# Modify Templates
# Now the two templates (all_members.html and details.html) can use this master.html template
# This is done by including the master template with the {% extends %} tag, and inserting a title block and a content block:

# Members

# all_members.html file
"""
{% extends "master.html" %}
{% block title %}
    My Tennis Club - List of all members
{% endblock %}

{% block content%}
    <h1>Members</h1>
    <ul>
        {% for x in mymembers %}
            <li>
                <a href = 'details/{{x.id}}'>{{x.firstname}}{{x.lastname}}</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
"""

# Details

# details.html file

"""
{% extends "master.html" %}
{% block title %}
    Details about {{mymember.firstname}} {{mymember.lastname}}
{% endblock %}

{% block content %}
    <h1>{{mymember.firstname}} {{mymember.lastname}}</h1>
    <p>Phone {{mymember.phone}}</p>
    <p><a></a></p>
{% endblock %}
"""

# If the server is down, you have to start it again with the runserver command:
