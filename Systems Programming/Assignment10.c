/*

    Maxwell Cunningham - Systems Programming

    Assignment 10

*/


#include <stdio.h>

// Function Prototypes
int add(int,int);
int subtract(int, int);
int multiply(int, int);
void displayMessage(void);

// Main execution
int main(int argc, char const *argv[])
{
    // Initialize two integer variables for user input
    // along with variables to store the returned
    // values of the function calls
    int num1, num2, sum, difference, product;

    // Display the welcome message
    displayMessage();

    // Input for num1
    printf("Enter first number: ");
    scanf("%d", &num1);

    // Input for num2
    printf("Enter second number: ");
    scanf("%d", &num2);
    
    // Call add() function and print the output
    sum = add(num1, num2);
    printf("\nSum = %d\n", sum);

    // Call subtract() function and print the output
    difference = subtract(num1, num2);
    printf("Difference = %d\n", difference);

    // Call multiply() function and print the output
    product = multiply(num1, num2);
    printf("Product = %d\n", product);

    return 0;
}

// Function Definitions

// Addition function (Takes two integers and returns their sum)
int add(int num1, int num2) {
    return num1 + num2;
}

// Subtraction function (Takes two integers and returns their difference)
int subtract(int num1, int num2) {
    return num1 - num2;
}

// Multiplication function (Takes two integers and returns their product)
int multiply(int num1, int num2) {
    return num1 * num2;
}

// Displays a welcome message to the terminal
void displayMessage() {
    printf("Welcome to the Functions Program!\n\n");
}