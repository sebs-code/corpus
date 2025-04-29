"""
Challenge #047  [Easy] Ceaser Cipher.

Description

our task today is to implement one of the oldest ciphers known, the so-called 
Caesar cipher (or Caesar shift, as it is sometimes called). It works like 
this: 

for every letter you want to encrypt, you shift it some number of places down 
the alphabet to get the letter in the cipher.

So, for instance, in a Caesar cipher with a shift of 3, "A" becomes "D", 
"B" becomes "E", "C" becomes "F", and so on. At the end of the alphabet it 
wraps around, so "W" becomes "Z", "X" becomes "A", "Y" becomes "B" and "Z" 
becomes "C". If you encrypt "Hello" with a shift of 3, you get "Khoor".
One interesting thing about this cipher is that you can use the same algorithm 
to decode a cipher as you can to encode it: if you wish to decrypt some text 
that has been Caesar-shifted 6 places, you simply shift it another 20 places 
to get back the original text. For example, if you encrypt "Daily programmer" 
with a shift of 6 you get "Jgore vxumxgsskx", and if you encrypt "Jgore 
vxumxgsskx" with a shift of 20 you get "Daily programmer".

Implement the cipher and encrypt a bit of text of your choice!
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


