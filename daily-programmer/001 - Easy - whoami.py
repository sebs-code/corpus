"""
Challenge #1  [Easy] Who am I?.

Description

create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:

your name is (blank), you are (blank) years old, and your username is (blank)

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
name = raw_input("What is your name? > ")
age = raw_input("What is your age? > ")
username = raw_input("What is your username? > ")

print """So let me get this staight. Your name is %s, you are %s years old and 
your username is %s.""" %(name, age, username)




