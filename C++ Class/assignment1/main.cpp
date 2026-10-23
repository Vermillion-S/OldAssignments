#include <iostream>

using namespace std;

int main() {
    string name;
    int age;

    // Prompt the user to enter their name
    cout << "Enter your name: ";
    cin >> name;

    // Prompt the user to enter their age
    cout << "Enter your age: ";
    cin >> age;

    // Display the greeting message
    cout << "Hello, " << name << "! You are " << age << " years old." << endl;

    return 0;
}
