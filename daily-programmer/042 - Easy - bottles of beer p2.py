"""
Challenge #042  [Easy] Bottles of beer p2.

Description

write a program that will print the song "99 bottles of beer on the wall".
for extra credit, do not allow the program to print each loop on a new line.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

#Note script won't run until dict completed to 100 integers.

num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
            #etc....
            
for x in range (99, -1, -1):
    if x > 0:
        print """%s bottles of beer on the wall, %s bottles of beer. You take one 
        down and pass it around, %s bottles of beer on the wall.\n""" %(num2words1[x],
        num2words1[x],num2words1[x-1])




