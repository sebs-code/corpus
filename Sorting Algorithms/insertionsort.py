"""
*******************************
Insertion Sort Algorithm      *
*******************************

The Insertion Sort algorithm works by maintaining a secondary list of sorted
items at the beginning of the main list.

That algorithm makes multiple passes through the list to be sorted. On each pass
an additional item is added to the sublist (in order). This may involve shifting
an item in the sublist to allow room for the new item.

On the first pass, we assume that the first item in the list is alread sorted.
Therefore, there is always len(list)-1 items to sort through, increasing by 1
each pass n-2, n-3...

For example:

    Curly braces represent the sublist (sorted list).

    Starting point:

    [{23,}46,1,34,97,55,432,12,11,34,56,7
    [{23,46}1,34,97,55,432,12,11,34,56,7] First pass
    [{1,23,46}34,97,55,432,12,11,34,56,7] Second Pass
    [{1,23,34,46}97,55,432,12,11,34,56,7] Third Pass
    [{1,23,34,46,97,}55,432,12,11,34,56,7] Four Pass
    [{1,23,34,46,55,97,}432,12,11,34,56,7] Fith Pass
    [{1,23,34,46,55,97,432}12,11,34,56,7] Sixth Pass
    [{1,12,23,34,46,55,97,432}11,34,56,7] Seventh Pass
    [{1,11,12,23,34,46,55,97,432}34,56,7] Eigth Pass
    [{1,11,12,23,34,34,46,55,97,432}56,7] Ninth Pass
    [{1,11,12,23,34,34,46,55,56,97,432}7] Tenth Pass
    [{1,7,11,12,23,34,34,46,55,56,97,432}] Eleventh Pass

"""

def insertionSort(yourlist):
    for i in range (1, len(yourlist)):
        currentvalue = yourlist[i]
        position = i

        while position > 0 and yourlist[position-1] > currentvalue:
            yourlist[position] = yourlist[position-1]
            position = position -1

        yourlist[position] = currentvalue

#Testing it out
yourlist = [23,46,1,34,97,55,432,12,11,34,56,7]
insertionSort(yourlist)
print yourlist


