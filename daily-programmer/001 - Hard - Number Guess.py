"""
Challenge #1  [Hard] Number Guess.

Description

we all know the classic "guessing game" with higher or lower prompts. lets do a role reversal; you create a program that will guess numbers between 1-100, and respond appropriately based on whether users say that the number is too high or too low. Try to make a program that can guess your number based on user input and great code!

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
import random

#Sloppy but works. TODO - tidy up / refactor
a = 1
while a == 1:
    number = raw_input("Please enter a number between 1-100 >")
    number = int(number)
    if number > 100 or number < 1:
        print "Invalid selection"
    else:
        a = 2

top = 100
bottom = 1
x = 1
guesser = 0

def guessing(top, bottom):
    guess = random.randint(bottom,top)
    return guess

while x == 1:
    guesser = guessing(top,bottom)
    if guesser == number:
        break
    print "Ok, I'm going to try and guess you number!"
    print "My guess was %d, which was wrong. Is your number higher or lower?" %(guesser)   
    refine = raw_input("Higher or Lower h/l:  ")
    if refine == "h":
        bottom = guesser
    if refine == "l":
        top = guesser

print "My guess of %d was right! \n\n\n Thanks for plaing." %(number)
