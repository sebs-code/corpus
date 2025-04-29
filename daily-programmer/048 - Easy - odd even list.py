"""
Challenge #048  [Easy] Odd Even List.

Description

Take an array of integers and partition it so that all the even integers in 
the array precede all the odd integers in the array. Your solution must take 
linear time in the size of the array and operate in-place with only a constant 
amount of extra space.

Your task is to write the indicated function.

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

list = [1,6,4,77,65,3,4,23,5,4,9,90,87,6,4,3,22,3,444,56,634,2,1,32,55,6]

def oddeven(list):
    odd = [x for x in range(len(list)) if x % 2 == 0]
    even = [x for x in range(len(list)) if x % 2 != 0]
    result = even + odd
    return result

print oddeven(list)

