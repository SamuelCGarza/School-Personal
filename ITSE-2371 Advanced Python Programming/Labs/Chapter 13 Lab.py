def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
    
    
def userInput():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
        except ValueError:
            print("Please enter a valid number")
        
        try:
            num2 = int(input("Enter the second number: "))
        except ValueError:
            print()
            
        try:
            if num1 <= num2:
                print("First number must be greater than second number. Please try again. ")
                return
            else:
                result = gcd(num1, num2)
                print(f"The GCD of {num1} and {num2} is {result}")
                print()
        except UnboundLocalError:
            print("You have entered one or more invalid inputs. Please try again.")
            print()
            
        return
                
                
def getAnswer():
    return str(input("Continue? (y/n): " )).lower()


    
def main():
    print()
    print("Greatest Common Divisor Calculator")
    print()
    
    userInput()
    
    answer = getAnswer()
    
    while answer != "y" and answer != "n":
        print("Invalid response, please answer y or n. ")
        answer = getAnswer()

    while answer == "y":
        userInput()
        answer = getAnswer()
        
    if answer == "n":
        print("Bye!")
    
    
        
        
if __name__ == "__main__":
    main()
    
    