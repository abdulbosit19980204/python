# Python DateTime

# A date in python is not a data type of its own, but we can import a module named datetime to work with dates as date objects
# Import the datetime module and display the current date

import datetime

x = datetime.datetime.now()
print(x)  # 2023-12-25 14:17:13.037659

# Date Output

# When we execute the code from the example above the result will be:
# 2023-12-25 14:17:13.037659

# The date contains year, month, day, hour, minute, second and microsecond
# The datetime modules has many methods to return information about the date object
# Here are a few examples, you will learn more about them later in this chapter

# Return the year and name of weekday
x = datetime.datetime.now()
print(x.year)  # 2023
print(x.strftime("%A"))  # Monday

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module
# The  datetime() class requires three paremetrs to create a date: year,month, day
# Create a date object
x = datetime.datetime(2021, 11, 22)
print(x)  # 2021-11-22 00:00:00

# The datetime() class also takes parametrs for time and timezone(hour, minute, second, microsecond, tzone)
# but they are optional and has a default value of 0, (None for timezone)

# The strftime() method
# The datetime object has a method for formatting date objects into readable string
# The method is called strftime(), and takes one parametr, format, to specify the fromat of the returned string

# Display the name of the month
x = datetime.datetime(2021, 11, 22)
print(x.strftime("%B"))  # November
# A reference of all the legal format codes
x = datetime.datetime.now()
print(x.strftime("%H:%M"))


