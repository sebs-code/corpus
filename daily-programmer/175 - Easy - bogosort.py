"""
COUNTING THE DAYS UNTIL...

Challenge #175 [Easy] Bogosort

A bogo sort is a purposefully inefficient algorithm for sorting a sequence. Today we will be using this for strings to test for equality.

Given a scrambled string N and another string M. You must sort N so that it matches M. After it has been sorted, it must output how many iterations it took to complete the sorting.


solution by Sebastan David Lees (sebastian@incerto.net).
"""
import random

def bogosort(string1, string2):
    permutations = 0
    while string1 != string2:
        l = list(string1)
        random.shuffle(l)
        string1 = ''.join(l)
        permutations += +1
    print "%s Iterations" %(permutations)

bogosort("elhlo","hello")    
