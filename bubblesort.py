'''
*****************************************
BUBBLE SORT                             *
*****************************************

Implementation of a bubble sort algorithm in python.

The bubble sort makes multiple passes through a list. On each pass it compares
adjacent items and exchanges those which are out of order. In this fashion
items in the list 'bubble up' to where they belong.

e.g:
    Starting with an unordered list:

    [23,34,66,1,2,87,4,9,67,93,44]

    First pass:
    Starting with the first pass, the first two items on the list will be
    compared and switched if the first number is higher than the second. If the
    second number is higher than the first, no switch will occur. This process
    is repeated along the list until the first pass is complete. This process
    repeats itself  in multiple passes until the entire list is sorted.

    So for our first pass:

    [23, 34] = No exchange
    [34, 66] = No exchange
    [66, 1 ] = Exchange
    [66, 2]  = Exchange
    [66, 87] = No exchange
    [87, 4 ] = Exchange
    [87, 9 ] = Exchange
    [87, 67] = Exchange
    [87, 93] = No exchange
    [93, 44] = Exchange

    So after our first pass we end up with:

    [23,34,1,2,66,4,9,67,87,44,93]

    Note that at the start of the first pass, there are always n -1 pairs
    pairs of items in a list that need to be compared, where n is the length of
    the list. This increased to n-2, n-3 ... with each pass of the list.
'''

def bubblesort(yourlist):
    #step to reduce length of pairs by -1 on each pass.
    for passnumber in range(len(yourlist)-1,0,-1):
        for i in range(passnumber):
            if yourlist[i] > yourlist[i+1]:
                #temporary placeholder for second value.
                temp = yourlist[i]
                yourlist[i] = yourlist[i+1]
                yourlist[i+1] = temp

# Testing it out
yourlist = [23,54,6,99,8,133,24,33,54,66,456,51,52,19,8,77,5,23,25,29]
bubblesort(yourlist)
print (yourlist)

