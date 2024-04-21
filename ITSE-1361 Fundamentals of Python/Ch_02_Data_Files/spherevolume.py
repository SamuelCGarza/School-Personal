"""
File: spherevolume.py
Computes and prints the volume of a sphere, given its radius as input.
"""

import math

radius = float(input("Enter the radius of the sphere: "))
volume = 4 // 3 * math.pi * radius ** 3
print("The volume of the sphere is", volume)
