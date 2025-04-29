"""
Challenge #023  [Easy] Split Lists.

Description

Input: a list

Output: Return the two halves as different lists.

If the input list has an odd number, the middle item can go to any of the list.
Your task is to write the function that splits a list in two halves.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
mylist = ["red","blue","green","orange","black","apple","carrot","potato",
            "bag","slippers","pipe"]

def splitlist(listing):
    halfway = len(listing)/2
    first = [x for x in listing[:halfway]]
    second = [x for x in listing[halfway:]]
    print first, second
    

#Test
splitlist(mylist)
