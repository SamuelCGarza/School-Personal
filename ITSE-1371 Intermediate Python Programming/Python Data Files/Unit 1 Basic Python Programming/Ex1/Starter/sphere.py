import math 
radius = float(input("Enter the sphere's radius: "))
dia = radius*2
cir = math.pi*2*radius
s_area = math.pi*4*radius**2
vol = (4/3)*math.pi*radius**3

print("Diameter     : " +str(dia))
print("Circumference: " +str(cir))
print("Surface area : " +str(s_area))
print("Volume       : " +str(vol))

