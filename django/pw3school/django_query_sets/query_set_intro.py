# Django Query Set

# A QuerySet is a collection of data from a database.

# A QuerySet is  built up as list of objects.
# QuerySet makes it easier to get the data you actually need, by allowing you to filter and oreder the data at an early
# stage.

# Querying Data
# In views.py we have a view for testing called testing where we will test different queries
# ".all()" method to get all records and fields of the Member model

# .views.py file

from django.http import HttpResponse
from django.template import loader
from .models import Member


def testing(request):
    mydata = Member.objects.all()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))


# The object is placed in a variable called mydata, and it sent to the template via the context objects as mymembers,and
# looks like this
"""
<QuerySet [
  <Member: Member object (1)>,
  <Member: Member object (2)>,
  <Member: Member object (3)>,
  <Member: Member object (4)>,
  <Member: Member object (5)>
]>
"""

# As you can see, our Member model contains 5 records, and are listed inside the QuerySet as 5 objects
# In the template you can use the "mymembers "  object to generate content

# template.html

"""
<table border='1'>
  <tr>
    <th>ID</th>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  {% for x in mymembers %}
    <tr>
      <td>{{ x.id }}</td>
        <td>{{ x.firstname }}</td>
      <td>{{ x.lastname }}</td>
    </tr>
  {% endfor %}
</table>
"""


