"""
Challenge #034  [Easy] square sum.

Description

A very basic challenge:
In this challenge, the
input is are : 3 numbers as arguments
output: the sum of the squares of the two larger numbers.

Your task is to write the indicated challenge.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
def squaresum(a, b, c):
    l=[a,b,c]
    l.sort()
    result = (l[1]**2) + (l[2]**2)
    return result

#Test
print squaresum(3,2,1)

