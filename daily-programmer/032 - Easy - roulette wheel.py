"""
Challenge #032  [Easy] Roulette Wheel.

Description

lets simulate a roulette wheel!

a program that takes as input your bet, and gives as output how much you won, 
with the appropriate probability

write a program that will take a players bet and output the resulting spin and 
payout. try using an american roulette wheel (which has the 00 slot) to add a 
slight twist. and try to incorporate as many complex bets as you can to.
 
Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

from random import randint

def basicroulette(bet, choice):
    bet = int(bet)
    choice = int(choice)
    if choice > 36:
        print "invalid choice"
    else:
        winner = randint(0, 36)
        print "The winning number is %d\n" %(winner)
        if winner == choice:
            print "Congratulations you have won $%d" %(bet*35)    
        else:
            print "Sorry - better luck next time!"

#Poor Y / N error handling - obiovusly not for stable release. To test only.
x = True
while x is True:
    choice = raw_input("Please select a number: ")
    bet = raw_input("How much do you want to bet: $")
    basicroulette(bet, choice)
    repeat = raw_input("Play again? (Y / N)")
    if repeat == "N":
        x = False  
        
