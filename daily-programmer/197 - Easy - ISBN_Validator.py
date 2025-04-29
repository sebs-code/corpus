"""
Challenge #197 [Easy] ISBN Validator

Description

ISBN's (International Standard Book Numbers) are identifiers for books.
Given the correct sequence of digits, one book can be identified out of
millions of others thanks to this ISBN. But when is an ISBN not just a
random slurry of digits? That's for you to find out.

Bonus
Write an ISBN generator. That is, a programme that will output a valid ISBN
number (bonus if you output an ISBN that is already in use :P )

Solution
SOlution by Sebastian David Lees (sebastian@incerto.net)
"""
import random

def ISBNValidator(number):
    number = str(number)
    number = number.replace("-","")
    number = number.replace(" ","")

    if len(number)!=10:
        print "Invalid ISBN number"
        return False

    multiplicationfactor = 10
    total = 0

    for i in number:
        i= int(i)
        total += (i * multiplicationfactor)
        multiplicationfactor += -1

    if total % 11 == 0:
        print "valid ISBN number"
        return True

    else:
        print "Invalid ISBN number"
        return False

def ISBNGenerator():
    ISBNvalid = False
    while ISBNvalid == False:
        ISBNnumber = random.randint(1000000000,9999999999)
        if ISBNValidator(ISBNnumber):
            ISBNvalid = True
            print "Your ISBN number is %s" % ISBNnumber
#Testing
ISBNValidator("0-7475-3269-9") # Should be True
ISBNValidator(1234567892) # Should be False
ISBNValidator("2345839057") # Should be False
ISBNGenerator()





