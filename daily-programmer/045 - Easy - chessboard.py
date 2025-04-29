"""
Challenge #045  [Easy] Chessboard.

Description

Your challenge today is to write a program that can draw a checkered grid 
(like a chessboard) to any dimension. For instance, a 3 by 8 board might look
 like this:
 
*********************************
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*********************************
*###*   *###*   *###*   *###*   *
*###*   *###*   *###*   *###*   *
*###*   *###*   *###*   *###*   *
*********************************
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*********************************

Yours doesn't have to look like mine, you can make it look any way you want (now that I think of it, mine looks kinda bad, actually). Also try to make it scalable, so that if you want to make a 2 by 5 board, but with bigger squares, it would print out:

*******************************
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*******************************
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*******************************

Have fun!

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

Height = raw_input("Enter height > ")
Width = raw_input("Enter width > ")
Height = int(Height)
Width = int(Width)

piece = ["********","*   *###","*   *###","*   *###"]

for x in range(0, Height):
    for i in piece:
        print (i*Width) + "*"
print "********" * Width + "*"
