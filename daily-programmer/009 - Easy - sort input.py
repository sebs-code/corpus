"""
Challenge #009  [Easy] Sort Input.

Description

write a program that will allow the user to input digits, and arrange them in 
numerical order. For extra credit, have it also arrange strings in alphabetical order.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
list = []
for x in range (10):
    number = raw_input("Enter a number: ")
    list.append(number)

list = [int(x) for x in list]    
list.sort()

print list



