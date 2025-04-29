"""
Challenge #008  [Easy] Bottles of beer.

Description

write a program that will print the song "99 bottles of beer on the wall".
for extra credit, do not allow the program to print each loop on a new line.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
for x in range (99, -1, -1):
    if x > 0:
        print """%d bottles of beer on the wall, %d bottles of beer. You take one 
        down and pass it around, %d bottles of beer on the wall.\n""" %(x,x,x-1)




