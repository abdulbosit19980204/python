# Django Insert Data

# Add Records

# The Members table created in the previous chapter is empty
# We will use the Python interpreter (Python Shell) to add some members to it.

# To open a Python shell, type this command
# py manage.py shell

# Now we are in the shell, the result should be something like this:
# At the bottom, after the three >>> write the following:

# >>> from members.models import Member

# Hit [enter] and write this to look at the empty Member table:

# >>> Member.objects.all()
# This should be give you an empty QuerySet object, like this:
# <QuerySet []>

# A QuerySet is a collection of data from a database.

# Add a record to the table, by executing these two lines:
# >>> member = Member(firstname='Emil', lastname='Refines')
# >> member.save()

# Execute this command to see if the Member table got a member:
# >>> Member.objects.all().values()

# Add Multiple Records
# You can add multiple records by making a list of Member objects, and execute .save() on each entry:
"""
>>> member1 = Member(firstname='Tobias', lastname='Refsnes')
>>> member2 = Member(firstname='Linus', lastname='Refsnes')
>>> member3 = Member(firstname='Lene', lastname='Refsnes')
>>> member4 = Member(firstname='Stale', lastname='Refsnes')
>>> member5 = Member(firstname='Jane', lastname='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
>>>   x.save()
"""

# Now there are 4 members in the Member table: