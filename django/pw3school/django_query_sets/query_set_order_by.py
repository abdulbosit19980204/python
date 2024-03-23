# Django QuerySet - Oreder By

# Order By
# To sort QuerySets, Django uses the "order_by()" method:

# Order the result alphabetically by firstname:
mydata = Member.objects.all().order_by('firstname').values()

# In SQL, the above statement would be written like this:
# SELECT * FROM members ORDER BY firstname;

# Descending Order
# By default, the result is sorted ascending (the lowest value first), to change the  direction to descending
# (the highest value first), use the minus sign (NOT), "-" in fornt of the field name:

# Order the result firstname descending
mydata = Member.objects.all().order_by('-firstname').values()

# SELECT * FROM members ORDER BY firstname DESC;

# Multiple Order Bys
# To order by more than one field, separate the fieldnames with a comma in the order_by() method:

# Order the result first by lastname ascending, then descending on id:
mydata = Member.objects.all().order_by('lastname', '-id').values()
# SELECT * FROM members ORDER BY lastname ASC, id DESC;
