#Import necessary modules.
import math

#Declare variables and perform arithmetic. 
radius = float(input("Enter the sphere's radius: "))
sphereDiameter = 2 * radius 
sphereCircumference = 2 * math.pi * radius
sphereSurfaceArea = 4 * math.pi * radius * radius
sphereVolume = (4/3) * math.pi * radius * radius * radius

#Output.
print("Diameter     : " + str(sphereDiameter))
print("Circumference: " + str(sphereCircumference))
print("Surface area : " + str(sphereSurfaceArea))
print("Volume       : " + str(sphereVolume))
