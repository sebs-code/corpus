"""
Challenge #027  [Easy] Year Century.

Description

Write a program that accepts a year as input and outputs the century the year belongs in (e.g. 18th century's year ranges are 1701 to 1800) and whether or not the year is a leap year. Pseudocode for leap year can be found here.

Sample run:
Enter Year: 1996
Century: 20
Leap Year: Yes
Enter Year: 1900
Century: 19
Leap Year: No

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

year=int(raw_input('enter a year:'))
if year % 100 == 0:
    x = year/100
    print'Century: %d' % x
else:
    y=(year/100)+1
    print'Century: %d' % y

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print'Leap year: Yes'
        else:
            print'Leap year: No'
    else:
        print'Leap year: Yes'
else:
    print'Leap year: No'
