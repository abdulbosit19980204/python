# Django For Tag

# For Loops
# A for loop is used for iterating over a sequence, like looping over times in an array, a list, or a dictionary.

# Example
# Loop through the items of a list
"""
{% for i in  fruits %}
    <h1>{{i}}</h1>
{% endfor %}
"""

# Loop through a list of dictionaries
"""
{% for x in cars %}
    <h1>{{ x.brand }}</h1>
    <p>{{ x.model }}</p>
    <p>{{ x.year }}</p>
{% endfor %}
"""

# Reversed
# The "reversed" keyword is used when you want to do the loop in reversed order.

"""
{% for x in members reversed %}
    <h1>{{x.id}}</h1>
    <p>
        {{x.firstname}}
        {{x.lastname}}
    </p>
{% endfor %}
"""

# Empty
# The "empty" keyword can be used if you want to do something special if the object is empty
"""
<ul>
    {% for x in emptytestobject %}
        <li>{{ x.firstname }}</li>
    {% empty %}
        <li>No members</li>
    {% endfor %}
</ul>
"""

# The "empty" keyword can also  be used if the object does not exist:
"""
<ul>
  {% for x in myobject %}
    <li>{{ x.firstname }}</li>
  {% empty %}
    <li>No members</li>
  {% endfor %}
</ul> 
"""

# Loop Variables
# Django has some variables that are available for you inside a loop

"""
* forloop.counter
* forloop.counter
* forloop.first
* forloop.last
* forloop.parentloop
* forloop.revcounter
* forloop.revcounter0
"""

# forloop.counter
# The current iteration, starting at 1.
"""
<ul>
  {% for x in fruits %}
    <li>{{ forloop.counter }}</li>
  {% endfor %}
</ul> 
"""

# forloop.counter0
# The current iteration, starting at 0.
"""
<ul>
  {% for x in fruits %}
    <li>{{ forloop.counter0 }}</li>
  {% endfor %}
</ul> 
"""

# forloop.first
# Allows you to test if the loop is on its first iteration

# Example
# Draw a blue background for the first iteration of the loop.
"""
<ul>
  {% for x in fruits %}
    <li
      {% if forloop.first %}
        style='background-color:lightblue;'
      {% endif %}
    >{{ x }}</li>
  {% endfor %}
</ul>
"""


# forloop.last
# Allows you to test if the loop is on its last iteration
# forloop.revcounter - The current iteration if you start at the end and count backwards, ending up at 1.
# forloop.revcounter0 - The current interation if you start at the end and count backwards, ending up at 0.
