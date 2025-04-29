"""
Challenge #203  [Easy] The start of something big

Description

All great things start with something small. Sometimes people don't even realise what goes into making a 'small' thing.

A popular story is linked above about a group of graphics programmers who create a rendering engine in some amount of time. After some time HR came to see what the programmers had accomplished. They responded by showing a black triangle on a tv.

HR was less than impressed (understandle for a non techie) but it goes to show the natural evolution of a program. What they didn't realise is that the programmers have created their base engine and can now easily add and extend on top of it.

Maybe you can follow similar steps?

Challenge

On your screen, display a square.
You may use any libraries available to you.
The square may be of any size and of any colour.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

w = 5
h = 5
 
print '+' + '=' *(w-2) + '+' + '\n' + ('|' + " " * (w - 2) + '|' + '\n' ) * (h-2) + '+' + '=' *(w-2) + '+'
