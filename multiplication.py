# Write a function that prints a multiplication table to the screen.
# For example, the output for n=5 should look like:-

# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

def multiplication(n):
    """
    [[], [], []]
    """

    output = []

    for x in range(1, n+1):
        output.append([y*x for y in range(1, n+1)]) 

    return output


output = multiplication(5)

for row in output:
    
    line = ''
    for item in row:
        item = str(item)
        line += ' ' + item if len(item) > 1 else '  ' + item

    print(line)




    