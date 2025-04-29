"""
Challenge #4  [Easy] Password Generator.

Description

You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
from random import randint

def passwordGen(length, no):
    no = int(no)
    x = 0
    while x < no:
        password = ""
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                    "p","q","r","s","t","u","v","w","x","y","z",]
        
        for i in range(length/2):
            i = alphabet[randint(0,23)]
            password += str(i)
            
        for i in range(length/2):
            i = randint(0,9)
            password += str(i)
            
        print password
        x += +1
        
plength = raw_input("Please select password length >> ")
plength = int(plength)
no = raw_input("Please select no. of passwords to generate >> ")
no = int(no)
passwordGen(plength, no)

