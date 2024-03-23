# Djnago QuerySet - Filter

# QuerySet Filter
# The filter() method is used to filter your search, and allows you to return only the rows that matches the search term.
# As we learned in the previous chapter, we can filter on field name likes this:

# Return only the records where the firstname is 'Emil':
mydata = Member.objects.filter(firstname='Emil').values()

# In SQL, the above statement would be written like this

# SELECT * FROM members WHERE firstname = 'Emil';

# AND
# The filter() method takes the arguments as **kwargs (keyword arguments) so you can filter on more than one filed by
# separating them by a comma.

# Return records where lastname is 'Refsnes' and id is 2
mydata = Member.objects.filter(lastname='Refsnes', id=2).values()

# In SQL, the above statement would be written like this:

# SELECT * FROM members WHERE lastname = 'Refsnes' AND id = 2;

# OR
"""
To return records where firstname is Emil or firstname is Tobias (meaning: returning records that matches either query,
not necessarily both) is not as easy as the AND example above.

We can use multiple filter() methods, separated by a pipe | character. The result will merge into one model.
"""

mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()

# Another common method is to import and use Q expressions:

# Return records where firstname is either "Emil" or Tobias":
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q


def testing(request):
    mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))


# In SQL, the above statement would be written like this
# SELECT * FROM members WHERE firstname = 'Emil' OR firstname = 'Tobias';

# Field Lookups

# Django has its own way of specifying SQL statements and "where" clauses.
# To make specifies where clauses in Django, use "Field lookups"
# Field lookups are keywords that represents specifies SQL keywords.

"Use the __startswith keyword:"

.filter(firstname__startswith='L');
# Is the same as the SQL statement:
# WHERE firstname LIKE 'L%'

# Field Lookups Syntax
# All Field lookup keywords must be specified with the fieldname, followed  by two(__) underscore characters and the keyword
# In our Member model, the statement would be written like this
mydata = Member.objects.filter(firstname__startswith='L').values()

