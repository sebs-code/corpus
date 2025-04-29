"""
Challenge #22  [Easy] Merge Lists.

Description

Write a program that will compare two lists, and append any elements in the 
second list that doesn't exist in the first.

input: ["a","b","c",1,4,], ["a", "x", 34, "4"]
output: ["a", "b", "c",1,4,"x",34, "4"]

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

list1 = ["a","b","c",1,4,]
list2 = ["a", "x", 34, "4"]
list3 = set(list1 + list2)

print list3




