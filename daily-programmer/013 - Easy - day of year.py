"""
Challenge #013  [Easy] Day of year.

Description

Find the number of the year for the given date. For example, january 1st would be 1, and december 31st is 365.

for extra credit, allow it to calculate leap years, as well.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

import datetime
date = raw_input("Please enter a date (mm/dd/yyyy): ")
date = str(date)
try:
    day = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%j')
    print day 
except:
    print "Invalid date format"






