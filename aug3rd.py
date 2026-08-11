#datetime--->date,time module functionalities

import datetime
#print(dir(datetime))
from datetime import datetime
a = datetime.now()
print(a)
print(type(a))
#based on above datetime object we can extract seperately as below
d = datetime.now()
print(d.date())
da=d.day
m=d.month
y=d.year
print(f'Today is{da}-{m}-{y}')
g=datetime.today()
print(g)
print(type(g))
h=g.weekday()
print(h)
k=g.isoweekday()
print(k)
l = g.time()
print(l)
#stringformatting-->convert dateime to string
print(g.strftime('%W')) #number of days in this month
print(g.strftime('%M'))
print(g.strftime("%m"))
print(g.strftime("%w"))

#we can create a datetime object
b = datetime(2026,8,15)
print(b)
print(type(b))
c = datetime(day=16,month=9,year=2026,hour=10,minute=30)
print(c)
print(type(c))
print(dir(datetime))
#accept input from-->convert to datetime object-->return the string format(part day,month name)
d,m,y = map(int,input("enter the values:").split(','))
print(d,m,y)
d_obj = datetime(y,m,d)
print(d_obj)
print(f'Today is {d_obj.strftime("%A")}')
print(f'The month is {d_obj.strtime("%B")}')

#strptime()-->stringpointoftime-->datetime-->str format
#timedelta-->handling time difference
from datetime import datetime,timedelta
f = datetime.now()
print(f)
print(type(f))
d_obj = datetime.strptime("26-12-1993","%d-%m-%Y")
#print(d_obj)
#print(d_obj.strftime('That day was %A'))
print(f)
print(d_obj)
#days,hours,minutes,seconds
diff = timedelta(days=5,hours=10)
print(diff)

print(f-diff)
print(f + timedelta(hours=5,minutes=30))
d = f+timedelta(hours=5,minutes=30)
print(d)
print(f'Future date is {d+timedelta(days=5,hours=10)}')

#time-->time fuctionalities
import time
print(dir(time))
print(time.tzname)
print(time.ctime())
print(time.localtime())
d_obj = time.localtime()
y = d_obj.tm_year
month = d_obj.tm_mon
day = d_obj.tm_mday
print(f"Date is {day}--{month}--{y}")
