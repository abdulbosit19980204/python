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