"""
Challenge #041  [Easy] Box Text.

Description

Write a program that will accept a sentence as input and then output that sentence surrounded by some type of an ASCII decoratoin banner.

Sample run:
Enter a sentence: So long and thanks for all the fish

Output
*****************************************
*                                       *
*  So long and thanks for all the fish  *
*                                       *
*****************************************

Bonus: If the sentence is too long, move words to the next line.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

def box(text):
    a = len(text)
    b = ("*" * (a+4)) + "\n"
    c = ("* " + " "*a + " *") + "\n"
    d = "* " + text + " *" + "\n"
    print b,c,d,c,b

#Text
box("Do you like cheese?")
    



