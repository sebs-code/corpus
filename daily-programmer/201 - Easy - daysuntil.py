"""
COUNTING THE DAYS UNTIL...

Challenge #201 /r/dailyprogrammer

Sometimes you wonder. How many days I have left until.....Whatever date you are curious about. Maybe a holiday. Maybe a vacation. Maybe a special event like a birthday.
So today let us do some calendar math. Given a date that is in the future how many days until that date from the current date?

The date you want to know about in 3 integers. I leave it to you to decide if you want to do yyyy mm dd or mm dd yyyy or whatever. For my examples I will be using yyyy mm dd. Your solution should have 1 comment saying what format you are using for people reading your code. (Note you will need to convert your inputs to your format from mine if not using yyyy mm dd).


solution by Sebastan David Lees (sebastian@incerto.net).
"""
import datetime

"Basic function to calcualte days by creating two time deltas and subtracting.
def daysuntil(date):
    date = datetime.datetime.strptime(date, "%d/%m/%y")
    now = datetime.datetime.now()
    days = abs((date-now).days)
    print "There are %s days until %s" %(days, date)

daysuntil("20/02/15")    
