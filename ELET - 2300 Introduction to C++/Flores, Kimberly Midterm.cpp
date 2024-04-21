
#include <iostream>
#include <string>
using namespace std;

// Progarm stimulates a jackpot machine
int main()
{ // Declare variables
    int wantToPlay;
    int randomNum1;
    int randomNum2;
    int randomNum3;

    while (wantToPlay != 0) // Loop to ask user if they want to play again
    {
        cout << "Do you ant to play jackpot? (0 = no, 1 = yes): " << endl;
        cin >> wantToPlay;

        if (wantToPlay == 1)
        { // Initialize weather user wants to play or not

            randomNum1 = rand() % 8; // Generating 3 random numbers from 0-7
            randomNum2 = rand() % 8;
            randomNum3 = rand() % 8;

            cout << "Numbers " << randomNum1 << " " << randomNum2 << " " << randomNum3 << endl; // Output random numbers

            if (randomNum1 == 7 && randomNum1 == randomNum2 && randomNum2 == randomNum3)
            { // Assign prize with conditions
                cout << "Jackpot! "
                     << "You won 100 dollars" << endl; // Output prize
            }
                else if (randomNum1 == randomNum2 && randomNum2 == randomNum3 && randomNum1 == randomNum3)
                 {
                cout << "Three equal numbers! You won 20 dollars" << endl;
                  }
                 else if (randomNum1 == randomNum2 || randomNum2 == randomNum3 || randomNum1 == randomNum3)
                 {
                cout << "Two equal numbers! You won 5 dollars" << endl;
                }   
            else
            {
                cout << "No prize" << endl;
            }
        }
    
        if (wantToPlay == 0)
        {
            cout << "Thank you for playing!";
        }
    }
        return 0;
    }
