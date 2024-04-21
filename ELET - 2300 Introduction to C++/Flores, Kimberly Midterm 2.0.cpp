#include <iostream>
#include <cstdlib>
using namespace std;

int main() {

    int firstNum;
    int secondNum; 
    int thirdNum;
    int userInput; 

    cout << "Do you want to play jackpot? (0 = no, 1 = yes): ";
    cin >> userInput;

    // Loop to generate random numbers between 1 and 7, and check if they are equal
    while (userInput != 0) {
        
        srand(time(0));
        firstNum = (rand() % 7) + 1;
        secondNum = (rand() % 7 )+ 1;
        thirdNum = (rand() % 7) + 1;

        cout << "Numbers " << firstNum << " " << secondNum << " " << thirdNum << endl;

        if ((firstNum == secondNum) && (secondNum == thirdNum)) {
            if ((firstNum == 7) && (secondNum == 7) && (thirdNum == 7)) {
                cout << "You won the jackpot! You won 100 dollars." << endl << endl;
            } else {
                cout << "Three equal numbers. You won 20 dollars." << endl << endl;
            }
        } 
        else if ((firstNum == secondNum) || (secondNum == thirdNum) || (firstNum == thirdNum) || (secondNum == thirdNum)) {
            cout << "Two equal numbers. You won 5 dollars." << endl << endl;
        }
        else {
            cout << "No equal numbers. You won 0 dollars." << endl << endl;
        }

        cout << "Do you want to play jackpot? (0 = no, 1 = yes): ";
        cin >> userInput;
    }

    cout << "Thank you for playing!" << endl;

    return 0;
}


