#include <iostream>
using namespace std;

int main() {

    int n1;  
    int n2;
    int i;
    bool isPrime;

    // Loop to keep program running while true
    while (true) {   
        cout << "Enter two positive integers: ";
        cin >> n1 >> n2;

        // If integers are less than or equal to 0 terminate program
        if (n1 <= 0 || n2 <= 0) {    
            cout << "Program terminated, goodbye!" << endl;
            break;
        }

        // If n2 is less than or equal to n1, prompt user to enter a second number smaller than the first
        if (n2 <= n1) {               
            cout << "Please enter a second number smaller than the first." << endl;
            continue;
        }

        
        cout << "Prime numbers between " << n1 << " and " << n2 << " are: ";
        
        // Loop to find prime numbers between n1 and n2
        for (int num = n1; num <= n2; num++) {
            isPrime = true;
            if (num <= 1) {
                isPrime = false;
            }
            else {
                for (i = 2; i * i <= num; i++) {
                    if (num % i == 0) {
                        isPrime = false;
                        break;
                    }
                }
            }
            if (isPrime) {
                cout << num << " ";
            }
        }
        cout << endl;
    }
    return 0;
}