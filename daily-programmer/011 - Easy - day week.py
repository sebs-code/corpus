"""
Challenge #011  [Easy] Day of the week.

Description

The program should take three arguments. The first will be a day, the second will be month, and the third will be year. Then, your program should compute the day of the week that date will fall on.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

import datetime
date = raw_input("Please enter a date (mm/dd/yyyy): ")
date = str(date)
try:
    day = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%A')
    print day 
except:
    print "Invalid date format"




