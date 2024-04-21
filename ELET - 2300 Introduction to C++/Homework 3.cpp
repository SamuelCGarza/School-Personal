#include <iostream>
using namespace std;

// Function to check if a number is prime
bool isPrime(int num) { 
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0)
            return false;
    }
    return true;
}

int main() {
    int n1;
    int n2;

    // Loop until user enters a negative number
    while (true) { 
        cout << "Enter two positive integers: ";
        cin >> n1 >> n2;

        // If either n1 or n2 is less than or equal to 0, terminate the program
        if (n1 <= 0 || n2 <= 0) { 
            cout << "Program terminated, goodbye!" << endl;
            break;
        }

        // If n2 is smaller than n1, ask for input again
        if (n2 <= n1) { 
            cout << "Please enter a second number smaller than the first." << endl;
            continue;
        }

        // Print prime numbers between n1 and n2
        cout << "Prime numbers between " << n1 << " and " << n2 << " are: ";
        for (int i = n1; i <= n2; i++) { 
            if (isPrime(i)) {
                cout << i << " ";
            }
        }
        cout << endl;
    }
    return 0; 
}
