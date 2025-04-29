"""
Challenge #016  [Easy] String Duplicates.

Description

Hi folks! We are in the midst of discussing how this subreddit will go about 
but for now how about we just concentrate on challenges!

Write a function that takes two strings and removes from the first string any 
character that appears in the second string. For instance, if the first string 
is "Daily Programmer" and the second string is "aeiou" the result is 
"DlyPrgrmmr".

note: the second string has [space] so the space between "Daily Programmer" 
is removed.

edit: if anyone has any suggestions for the subreddit, kindly post it in the 
feedback thread posted a day before. It will be easier to assess. Thank you.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

string1 = "dailyprogrammer"
string2 = "aeiou"
duplicates = [x for x in string1 if x not in string2]

print duplicates
