"""
Challenge #005  [Easy] Login.

Description

Your challenge for today is to create a program which is password protected,
and wont open unless the correct user and password is given.
For extra credit, have the user and password in a seperate .txt file.
for even more extra credit, break into your own program :)

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
username = raw_input("Username > ")
password = raw_input("Password > ")

username = str(username)
password = str(password)

with open("005 - Easy - login.txt", "rb") as f:
    f = f.read().replace('\n', '')
    if username and password in f:
        print "access granted"
    
    else:
        print "access denied"




