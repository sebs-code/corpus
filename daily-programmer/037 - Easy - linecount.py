"""
Challenge #37  [Easy] Line Count.

Description

write a program that takes
input : a file as an argument
output: counts the total number of lines.
for bonus, also count the number of words in the file.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

lines = sum(1 for line in open("037 - Easy - linecount.txt"))
print lines

