# Django If tag

# If Statement

# An if statement evaluates a variable and executes a block of code if the value is true.
"""
{% if greeting == 1 %}
    <h1>Hello</h1>
{% endif %}
"""

# Elif

# The elif  keyword says "if the previous conditions were not true, then try this condition".
"""
{% if greeting == 1 %}
    <h1>Hello</h1>
{% elif greeting == 2%}
    <h1>Welcome</h1>
{% endif %}
"""

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.
"""
{% if greeting == 1 %}
  <h1>Hello</h1>
{% elif greeting == 2 %}
  <h1>Welcome</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %} 
"""

# Operators

# The above examples uses the == operator, which is used to check if a variable is equal to a value, but there are many
# other operators you can use, or you can even drop the operator if you just want to check if a variable is not empty

"""
{% if greeting %}
  <h1>Hello</h1>
{% endif %} 
"""

"""
== - is equal to.
!= - is not equal to.
< - less than.
<= - Is less than or, equal to
>= - Is greater than, or equal to.


"""

# and
# To check if more than one condition is true
"""
{% if greeting == 1 and day == "Friday" %}
  <h1>Hello Weekend!</h1>
{% endif %} 
"""
# Or

# To check if one of the conditions is true
# And/or - Combine and or
"""
{% if greeting == 1 and day == "Friday" or greeting == 5 %}
"""
# Parentheses are not allowed in if statements in Django, so when you combine "and" and or operators, it is important to
# know that parentheses are added for "and" but not for or
# Meaning that the above example is ready by the interpreter like this:
"""
{% if (greeting == 1 and day == "Friday") or greeting == 5 %}
"""
# in
# To check if a certain items is present in an object

"""
{% if 'Banana' in fruits %}
  <h1>Hello</h1>
{% else %}
  <h1>Goodbye</h1>
{% endif %} 
"""

# not in

# To check if a certain item is not present in an object.

"""
{% if 'Banana' not in fruits %}
    <h1>Hello</h1>
{% else %}
    <h1>Goodbye</h1>
{% endif %}
"""

# is

# Check if two objects are the same
# This operator "is" different from the "==" operator, because the == operator check the values of two objects,
# but the "is" checks the identity of two objects.
# In the view, we have two objects, x and y, with the same values:

# views.py

from django.http import HttpResponse
from django.template import loader


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'x': ['Apple', 'Banana', 'Cherry'],
        'y': ['Apple', 'Banana', 'Cherry']
    }

    return HttpResponse(template.render(context, request))


# The two objects have the same value, but is it the same object?
"""
{% if x is y %}
    <h1>Yes</h1>
{% else %}
    <h1>No</h1>
{% endif %}
"""

# Let us try the same example with the == operator instead:
"""
{% if x==y %}
    <h1>Yes</h1>
{% else %}
    <h1>No</h1>
{% endif %}
"""


# How can two objects be the same? Well, if you have two objects that points to the same object, then the is operator
# evaluates to true:
# We will demonstrate this by using the "{% with %}" tag, which allows us to create variables in the template.
"""
{% with var1=x var2=x %}
    {% if var1 is var2 %}
    <h1>Yes</h1>
    {% else %}
    <h1>No</h1>
    {%endif%}
{%endwith%}
"""