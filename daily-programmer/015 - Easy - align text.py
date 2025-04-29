"""
Challenge #015  [Easy] Align Text.

Description

Write a program to left or right justify a text file.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

#Python 3.0

import sys

with open(sys.argv[1]) as f:
    for line in f.readlines():
        if sys.argv[2].lower() == '-l':
            print ('{:<' + sys.argv[3] + '}').format(line.lstrip().rstrip())
        elif sys.argv[2].lower() == '-r':
            print ('{:>' + sys.argv[3] + '}').format(line.lstrip().rstrip())



