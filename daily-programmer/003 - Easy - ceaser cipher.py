"""
Challenge #3  [Easy] Ceaser Cipher.

Description

Welcome to cipher day!
write a program that can encrypt texts with an alphabetical caesar cipher. 
This cipher can ignore numbers, symbols, and whitespace.

for extra credit, add a "decrypt" function to your program!

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

phrase = str(input("Please enter your phrase:\n> "))
shift = int(input("Please enter a shift value:\n> "))
encoded = ""

for t in phrase:
    val = ord(t)
    if val >= 97 and val <=122:
        x = val + shift
        if x > 122:
            x = x % 122 + 96
    elif val >= 65 and val <= 90:
        x = val + shift
        if x > 90:
            x = x % 90 + 64
    else:
        x = val
    encoded = encoded + chr(x)
print(encoded)    


