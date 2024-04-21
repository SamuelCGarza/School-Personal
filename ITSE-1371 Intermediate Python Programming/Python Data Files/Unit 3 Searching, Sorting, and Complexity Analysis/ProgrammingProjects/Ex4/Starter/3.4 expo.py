"""
File: expo.py
Project 3.4

Defines a function to raise a number to a given power.
Computational complexity: 
"""

def expo(base, exponent):
    # Base case: exponent is 0
    if exponent == 0:
        return 1
    
    # Recursive case: exponent is odd
    elif exponent % 2 == 1:
        return base * expo(base, exponent - 1)
    
    # Recursive case: exponent is even
    else:
        half_power = expo(base, exponent // 2)
        return half_power * half_power
   
def main():
    """Tests with powers of 2."""
    for exponent in range (5):
        print(exponent, expo(2, exponent))

if __name__ == "__main__":
    main()    
