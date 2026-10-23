#include <iostream>
#include <limits>

using namespace std;

int main()
{
    // initialize variable for user input
    int input;

    // take user input
    cout << "Insert an integer: ";

    // if the input is not an integer, end the program
    if (!(cin >> input))
    {
        cout << "invalid input" << endl;
        return 0;
    }

    // if it is less than zero, than it is negative
    if (input < 0)
    {
        cout << "The integer is negative" << endl;
    }

    // if it is greater than zero, then it is positive
    else if (input > 0)
    {
        cout << "The integer is positive" << endl;
    }

    // if it is neither of the previous 2, then it is 0
    else
    {
        cout << "The integer is 0" << endl;
    }

    // Switch case for even/odd; 
    // After dividing by an even number,
    switch (int value = input % 2; value)
    {

    // if the remainder is zero, then it is even, 
    case 0:
        cout << "The Integer is even" << endl;
        break;

    // otherwise it is odd
    default:
        cout << "The Integer is odd" << endl;
        break;
    }
    
    return 0;
}
