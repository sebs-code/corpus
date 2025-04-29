# -*- coding: UTF-8 -*-

"""
Challenge #039  [Easy] Fizz Buzz.

Description

You are to write a function that displays the numbers from 1 to an input parameter n, one per line, except that if the current number is divisible by 3 the function should write "Fizz" instead of the number, if the current number is divisible by 5 the function should write "Buzz" instead of the number, and if the current number is divisible by both 3 and 5 the function should write “FizzBuzz” instead of the number.
For instance, if n is 20, the program should write 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, and Buzz on twenty successive lines.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

def fizzbuzz(n):
    n = int(n)
    for x in range(0, n):
        if x % 3 == 0:
            print "Fizz"
        elif x % 5 == 0:
            print "Buzz"
        else:
            print x

fizzbuzz(200)
