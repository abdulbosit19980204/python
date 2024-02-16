# import  datetime
#
# year = datetime.datetime.now().year
# old = int(input())
# print(year-old)
#

import datetime
inHour=int(input())
inMin= int(input())

hour = datetime.datetime.now().hour
min = datetime.datetime.now().minute
print(abs(hour-inHour),":",abs(min-inMin))
