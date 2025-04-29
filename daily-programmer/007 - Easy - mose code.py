"""
Challenge #007  [Easy] Morse Code.

Description

Write a program that can translate Morse code in the format of ...---...
A space and a slash will be placed between words. ..- / --.-
For bonus, add the capability of going from a string to Morse code.
Super-bonus if your program can flash or beep the Morse.
This is your Morse to translate:

.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','..-','.--','-..-','-.--','--..','/']
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def morse_alpha(str):
    str = str.split()
    str = map(lambda x: alpha[morse.index(x)], str)
    return ''.join(str)

def alpha_morse(str):
    str = map(lambda x: morse[alpha.index(x)], str)
    return ' '.join(str)

print "enter 1 for morse->normal or 2 for normal->morse"
input = raw_input('>')

if input == '1':
    print "enter string to translate morse->normal"
    str = raw_input('>')
    print morse_alpha(str)

elif input == '2':
    print "enter string to translate normal->morse"
    str = raw_input('>')
    print alpha_morse(str)

else:
    print "invalid input"
