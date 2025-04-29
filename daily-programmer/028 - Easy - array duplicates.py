"""
Challenge #028  [Easy] Array Duplicates.

Description

The array duplicates problem is when one integer is in an array for more than once.
If you are given an array with integers between 1 and 1,000,000 or in some other interval and one integer is in the array twice. How can you determine which one?
Your task is to write code to solve the challenge.
Note: try to find the most efficient way to solve this challenge.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

list = [5,56,77,88,90,45,23,34,6,56,34,12,34,675,77,77,1,2,98,9,43,23,1]

duplicates = set([x for x in list if list.count(x) > 1])

for x in duplicates:
    print x
