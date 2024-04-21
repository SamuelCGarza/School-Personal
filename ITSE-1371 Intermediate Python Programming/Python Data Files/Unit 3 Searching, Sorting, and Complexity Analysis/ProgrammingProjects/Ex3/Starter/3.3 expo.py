"""
File: expo.py
Project 3.3
Defines a function to raise a number to a given power.
"""

def expo(base, exponent):
    """Raises base to exponent."""
    result = 1
    # Handle negative exponents by taking the reciprocal of the base
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    for _ in range(exponent):
        result *= base
    return result
 
   
def main():
    """Tests with powers of 2."""
    for exponent in range (5):
        print(exponent, expo(2, exponent))

if __name__ == "__main__":
    main()    
