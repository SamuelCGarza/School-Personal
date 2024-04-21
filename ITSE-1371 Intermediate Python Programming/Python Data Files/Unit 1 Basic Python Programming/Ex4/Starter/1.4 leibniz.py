# Write your code below:
#importing math library for math.pi
import math

#Prompt and read the number of iterations from the user.
numOfIterations = int(input("Enter the number of iterations: "));

#declare and initialize the variables.
Pi_div_four = 0;
iterationCounter = 1;

#iterate the for loop.
for i in range(1,numOfIterations+1):
    #Check the if value is odd.
    if(i % 2 != 0):
        #Compute the value of Pi_div_four.
        Pi_div_four = Pi_div_four + 1 /iterationCounter;
    #value is even
    else:
        #Compute the value of Pi_div_four.
        Pi_div_four = Pi_div_four - 1 /iterationCounter;
    #increase the current iterationCounter by 2.
    iterationCounter = iterationCounter + 2;

#compute the value of pi.
Pi_value = Pi_div_four*4;
#displaying the  Pi_value alongside math.pi for comparison.
print(Pi_value,math.pi,sep='\n')
