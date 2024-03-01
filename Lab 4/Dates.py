import datetime as dt
# 1
a = dt.date.today() - dt.timedelta(5)
print('Current Date :',dt.date.today())
print('5 days before Current Date :', a)

# 2
print ("Today: ", dt.date.today())
print("Yesterday: ", dt.date.today() - dt.timedelta(1))
print("Tomorrow: ", dt.date.today() + dt.timedelta(1))

# 3

import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print()
print(dt)
print()

# 4
from datetime import datetime, time

def date_diff_in_Seconds(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()

print((date_diff_in_Seconds(date2, date1)))
