"""
Challenge #021  [Easy] Same Digits.

Description

Input: a number
Output : the next higher number that uses the same set of digits. Repeat digits
count as one digit (e.g 22 is 2).

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""


def samedigits(n):
    start = int(n) + 1
    while True:
        if set(str(n)) == set(str(start)):
            break
        else:
            start += +1
    print "Next highest number containing the same digits is: %d" %(start)

#Test
samedigits(1224662)
