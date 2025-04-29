# -*- coding: UTF-8 -*-

"""
Challenge #026  [Easy] Consequtive Duplicates.

Description

you have a string "ddaaiillyypprrooggrraammeerr". We want to remove all the consecutive duplicates and put them in a separate string, which yields two separate instances of the string "dailyprogramer".

use this list for testing:

input: "balloons"
expected output: "balons" "lo"
input: "ddaaiillyypprrooggrraammeerr"
expected output: "dailyprogramer" "dailyprogramer"
input: "aabbccddeded"
expected output: "abcdeded" "abcd"
input: "flabby aapples"
expected output: "flaby aples" "bap"

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

def duplicates(string):
    singles = []
    doubles = []
    string  = list(string)
    for x in range(0, len(string)-1):
        if string[x] == string [x + 1]:
            doubles.append(string[x])
        else:
            singles.append(string[x])
    singles.append(string[len(string)-1])
    print singles
    print doubles

duplicates("balloons")
duplicates("ddaaiillyypprrooggrraammeerr")
duplicates("aabbccddeded")
