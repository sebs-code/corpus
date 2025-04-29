"""
Challenge #029  [Easy] Palindrome Detector.

Description

A Palindrome is a sequence that is the same in reverse as it is forward.
I.e. hannah, 12321.

Your task is to write a function to determine whether a given string is 
palindromic or not.

Bonus: Support multiple lines in your function to validate Demetri Martin's 
224 word palindrome poem.

Thanks to _lerp for submitting this idea in /r/dailyprogrammer_ideas!

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""


def ispalindrome(n):
    if str(n) == str(n[::-1]):
        print "Is a palindrome"
    else:
        print "Is not a palindrome"
        
#Test
ispalindrome("121")
ispalindrome("ppoopp")
ispalindrome("123")
ispalindrome("people")
        
