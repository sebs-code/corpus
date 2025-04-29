"""
Challenge #018  [Easy] Teleconverter.

Description

Often times in commercials, phone numbers contain letters so that they're easy
to remember (e.g. 1-800-VERIZON). Write a program that will convert a phone
number that contains letters into a phone number with only numbers and the
appropriate dash. Click here to learn more about the telephone keypad.

Example Execution: Input: 1-800-COMCAST Output: 1-800-266-2278

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

def teleconverter():
    a ={'a': 2, 'c': 2, 'b': 2, 'e': 3, 'd': 3, 'g': 4, 'f': 3,
        'i': 4, 'h': 4, 'k': 5, 'j': 5, 'm': 6, 'l': 5, 'o': 6,
        'n': 6, 'q': 7, 'p': 7, 's': 7, 'r': 7, 'u': 8, 't': 8,
        'w': 9, 'v': 8, 'y': 9, 'x': 9, 'z': 9, '-':'-', ' ':' '}
        
    numb = str.lower(raw_input('Enter phone number?: '))
    numbers=''
    for i in numb:
        if i in ('1','2','3','4','5','6','7','8','9','0'):
            numbers +=i
        elif i in a:
            numbers +=str(a[i])
        else:
            numbers = 'You input a symbol!'
            
    print numbers 

teleconverter()



