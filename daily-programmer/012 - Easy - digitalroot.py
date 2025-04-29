"""
SUM DEM DIGITS (aka Digital Root)

Challenge 12 /r/dailyprogrammer

As a crude form of hashing function, Lars wants to sum the digits of a number.
Then he wants to sum the digits of the result, and repeat until he have only
one digit left. He learnt that this is called the digital root of a number,
but the Wikipedia article is just confusing him.

Can you help him implement this problem in your favourite programming language?
It is possible to treat the number as a string and work with each character at
a time. This is pretty slow on big numbers, though, so Lars wants you to at
least try solving it with only integer calculations (the modulo operator may
prove to be useful!).

solution by Sebastan David Lees (sebastian@incerto.net).
"""

def digitalroot(n):
    if n < 10:
        return n
    return n % 10 + digitalroot( n // 10)

#Test
print digitalroot(123456)
