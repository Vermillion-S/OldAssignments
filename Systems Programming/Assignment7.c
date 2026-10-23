#include <stdio.h>

/*
    Assignment 7

    Maxwell cunningham

    03/13/2026

    The code uses loops in two distinct ways: iteration and validation. 
    Several tasks involve performing a task several times, 
    with only slight changes to the values being used. Loops allow the same logic 
    to be used several times until a condition is fulfilled, whether that be an 
    increment value reaching a certain threshold or an input value matching a 
    specified condition (task 4).

    */

// Prints integers from 1 to 20
void task1() {


    // Instantiates the variable "i" and performs an operation using it until
    // it reaches a certain threshold, incrimenting the looping variable each time
    for (int i = 1; i <= 20; i++)
    {   
        // Prints the current i value
        printf("%d ",i);
    }
    printf("\n"); // newline to separate task results
}

// Takes a number, and adds all previous positive integers to it
void task2() {
    // Variables
    int number, sum = 0;

    // Take an inputted value
    printf("Enter a Number: ");
    scanf("%d", &number);

    // While the number is still greater than 0..
    while (number >= 1) {
        sum += number; // add the number to the running total
        number--; // decriment the number
    }

    // Print the sum
    printf("Sum = %d\n", sum);
}

// Creates a multiplication table (1-10) for a given value
void task3() {
    // Input variable
    int num;

    // Take input for int
    printf("Enter a Number: ");
    scanf("%d", &num);

    // Loop from 1 to 10
    for (int i = 1; i <= 10; i++)
    {
        // Print the equation for the input and the given loop of i
        printf("%d x %d = %d\n", num, i, num * i);
    }
    
}

// Guessing game
void task4() {
    int guess; // input variable
    int secret = 8; // number to guess

    // Execute once before loop
    do
    {
        // Take user input
        printf("Guess the Number: ");
        scanf("%d", &guess);

        // Compare input to the secret value
        if (guess != secret)
        {
            // Fail message
            printf("Wrong! Try again.\n");
        }
        
    } while (guess != secret); // loop on failure
    
    // Escape loop on correct guess
    printf("Correct!\n"); // success message
}

// Execute
int main(int argc, char const *argv[])
{
    task1();
    task2();
    task3();
    task4();
    return 0;
}
