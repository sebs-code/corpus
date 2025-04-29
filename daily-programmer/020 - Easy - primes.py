"""
Challenge #020  [Easy] Primes.

Description

create a program that will find all prime numbers below 2000

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

primes = [x for x in range(2,2001) if all(x%c for c in range(2,x))]
print primes
