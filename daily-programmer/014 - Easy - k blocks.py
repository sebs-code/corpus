"""
Challenge #014  [Easy] K Blocks.

Description

Input: list of elements and a block size k or some other variable of your choice
Output: return the list of elements with every block of k elements reversed, 
starting from the beginning of the list.

For instance, given the list 12, 24, 32, 44, 55, 66 and the block size 2, the 
result is 24, 12, 44, 32, 66, 55.

your name is (blank), you are (blank) years old, and your username is (blank)

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
lst = [1, 2, 3, 4, 5, 6]
place = 2
 
def extract(lst, place):
    result = []
    for i in range(place):
        result.append(lst.pop())
    result.reverse()
    return result
 
def populate(lst, place):
    result = []
    while len(lst) > 0:
        result.extend(extract(lst, place))
    result.reverse()
    return result

#Test
print populate(lst, place)

