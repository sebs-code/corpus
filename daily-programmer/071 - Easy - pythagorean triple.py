"""
Challenge #071  [Easy] pythagorean triple.

Description

If a right angled triangle has three sides A, B and C (where C is the 
hypothenuse), the pythagorean theorem tells us that A2 + B2 = C2

When A, B and C are all integers, we say that they are a pythagorean triple. 
For instance, (3, 4, 5) is a pythagorean triple because 32 + 42 = 52 .

When A + B + C is equal to 240, there are four possible pythagorean triples: 
(15, 112, 113), (40, 96, 104), (48, 90, 102) and (60, 80, 100).

Write a program that finds all pythagorean triples where A + B + C = 504.


Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

limit = 504
for A in range(1, limit):
    for B in range(A, limit):
        C = limit - A - B
        if (A <= B and B <= C) and (A * A + B * B == C * C):
            print (A, B, C)
