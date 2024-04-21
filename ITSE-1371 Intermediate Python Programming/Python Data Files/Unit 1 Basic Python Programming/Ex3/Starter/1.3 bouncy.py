# Write your code below:
height = float(input("Enter the height from which the ball is dropped: "))
index = float(input("Enter the bounciness index of the ball: "))
bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
distance = height

for i in range (bounces - 1):
    height = height * index
    distance = distance + 2 * height
    """height *= index
    distance += 2 * height"""

distance = distance + height * index
#distance += height * index 


print("Total distance traveled is: " + str(distance) + " units.")
