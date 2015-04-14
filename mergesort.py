"""
**********************
Merge Sort Algorithm *
**********************

Merge sort is a famous 'Divide and COnquer' algorithm, and is also recursive.

Merge sort recursively splits a list in half, until it only has lists on single
itmes (sorted by default). It then performs a merge operation on those items,
and appends them to the original list in order.

"""

def mergeSort(yourlist):
    print "Part 1: recursively splitting list"
    if len(yourlist) > 1:
        midpoint = len(yourlist)//2
        lefthalf = yourlist[:midpoint]
        righthalf = yourlist[midpoint:]

        #Recursive functionality of mergesort here
        mergeSort(lefthalf)
        mergeSort(righthalf)

        #By this point, the list has been seperated into indiviudal items.
        #The rest of the code now concerns re-assembling those item into
        #the original list, in order.

        print "reassembling list"
        x = 0
        y = 0
        z = 0

        while x < len(lefthalf) and y < len(righthalf):
            if lefthalf[x]<righthalf[y]:
                yourlist[z]=lefthalf[x]
                x = x+1

            else:
                yourlist[z] = righthalf[y]
                y = y+1
            z = z+1

        while x < len(lefthalf):
            yourlist[z] = lefthalf[x]
            x = x+1
            z = z+1

        while y < len (righthalf):
            yourlist[z] = righthalf[y]
            y = y+1
            z = z+1

#Testing it out
yourlist = [22,1,45,6,44,73,8,24,33,90,9,68]
mergeSort(yourlist)
print yourlist
