"""
Challenge #017  [Easy] Triangles.

Description

write an application which will print a triangle of stars of user-specified height, with each line having twice as many stars as the last. sample output:

@
@@
@@@@

hint: in many languages, the "+" sign concatenates strings.
bonus features: print the triangle in reverse, print the triangle right justified

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
height = raw_input("Enter height of triangle > ")
height = int(height)
count = 0
 
while count < height:
    print "@" * count + "\n"
    count += +1 







