# Django QuerySet - GetData

# Get Data
# There are different methods to get data from a model into a QuerySet.
# The values() Method

# The values() method allows you to return each objects as a Python dictionary, with the names and values as key/value
mydata = Member.objects.all().values()

# Return Specific Columns
# The values_list() method allows you to return only the columns that you specify.
# Return only the firstname columns:
mydata = Member.objects.values_list('firstname')

# Return Specific Rows
# You can filter the search to only return specific  rows/records, by using the "filter()" method.
mydata = Member.objects.filter(firstname='Emil').values()

