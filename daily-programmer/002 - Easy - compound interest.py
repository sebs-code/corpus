"""
Challenge #1  [Easy] Compound Interest.

Description

Hello, coders! An important part of programming is being able to apply your 
programs, so your challenge for today is to create a calculator application 
that has use in your life. It might be an interest calculator, or it might be
something that you can use in the classroom. For example, if you were in
physics class, you might want to make a F = M * A calc.
  
EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!

Solution

Solution by Sebastian David Lees (sebastian@incerto.net)
"""

# Compund Interest Calculator

start = raw_input("Enter starting amount: ")
start = int(start)

term = raw_input("Enter number of years: ")
term = int(term)

interest = raw_input("Enter annual interest rate: ")
interest = float(interest)

amount = start * (1 + interest) ** term

print """ Start amount: %d \n Term: %d years \n Annual Interest Rate: %d \n
 Final Amount: %d """ %(start, term, interest, amount)




