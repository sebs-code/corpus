"""
**********************
Quick Sort Algorithm *
**********************

The quick sort algorithm is a recursive function that uses a divdide and
conquer strategy to order  a list of items.

A quick sort first selects a value, which is called the pivot value (this can
be any item o the list). The pivot value is used to split the list at the split
point, which is the point at we we recursively call the quicksort function.

"""

def quickSort(yourlist):
    quickSortHelper(yourlist, 0, len(yourlist)-1)

def quickSortHelper(yourlist, first, last):
    if first < last:
        splitpoint = partition(yourlist, first, last)

        quickSortHelper(yourlist, first, splitpoint-1)
        quickSortHelper(yourlist, splitpoint+1, last)

def partition(yourlist, first, last):
    pivotvalue = yourlist[first]
    leftmark = first +1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and yourlist[leftmark] <= pivotvalue:
            leftmark = leftmark +1

        while yourlist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = yourlist[leftmark]
            yourlist[leftmark] = yourlist[rightmark]
            yourlist[rightmark] = temp

    temp = yourlist[first]
    yourlist[first] = yourlist[rightmark]
    yourlist[rightmark] = temp
    return rightmark

#Testing it out
yourlist = [23,33,1,12,3,6,8,76,879,6,55,3,345,6,34,67,87,66,4,22,4,6,776]
quickSort(yourlist)
print yourlist
