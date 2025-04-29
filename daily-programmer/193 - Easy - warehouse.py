"""
Challenge #193  [Easy] A cube, a ball and a cylinder walk into a warehouse.

Description

An international shipping company is trying to figure out how to manufacture 
various types of containers. Given a volume they want to figure out the 
dimensions of various shapes that would all hold the same volume.

Input:

A volume in cubic meters.
Output:

Dimensions of containers of various types that would hold the volume.
The following containers are possible.

Cube
Ball (Sphere)
Cylinder
Cone

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""
import math

volume = raw_input("Enter volume (cubic meters) > ")
volume = int(volume)

#cube calculation
cube = round(volume ** (1.0/3.0), 2)
cube = str(cube)

#Sphere calculation
sphere = round((3*(volume/(4*3.1459))) ** 0.3333, 2)
sphere = str(sphere)

#cylinder calculation (assumes radius is 2m)
cylinder = round(volume / (3.1459*(2**2)), 2) 

#cone calculation (assumes radius is 2m)
cone = round(3*(volume/(3.1459*(2**2))),2)

print "Cube: %sm width, %sm high, %sm tall" %(cube, cube, cube)
print "Sphere: " + sphere + "m Radius"
print "Cylinder: %sm height, 2m radius" %(cylinder)
print "Cone: %sm height, 2m radius" %(cone)


