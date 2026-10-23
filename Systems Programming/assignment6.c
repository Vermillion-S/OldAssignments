#include <stdio.h>

// Maxwell Cunningham | Assignment 6
// 03/05/2026

// Checks whether an inputted integer is even or odd
void task1() {
    int input_int;

    // Take Int input
    printf("[Task1]\nInput an integer: ");
    scanf("%d", &input_int);

    // Check condition
    // Even numbers should have no remainder when divided by 2
    if (input_int % 2 == 0) {
        printf("%d is EVEN\n\n", input_int); // Even output
    } else {
        // If not even, then od
        printf("%d is ODD\n\n", input_int); // Odd Output
    }
}

// Takes an number grade and converts into a letter grade 
void task2() {
    int grade_input; // grade variable

    do
    {   // Take Input
        printf("[Task2]\nInput a nunber grade (0-100): ");
        scanf("%d", &grade_input);
    } while (grade_input < 0 || grade_input > 100); // Loop condition for input validation
    
    printf("The letter grade is : ");

    if (grade_input >= 90) { // Grade A Condition
        printf("A\n\n"); // Grade A Result
    } else if (grade_input >= 80) { // Grade B Condition
        printf("B\n\n");        // Grade B Result
    } else if (grade_input >= 70) { // Grade C Condition
        printf("C\n\n");        // Grade C Result
    } else if (grade_input >= 60) { // Grade D Condition
        printf("D\n\n"); // GRade D Result
    } else {
        printf("F\n\n"); // Grade F Result
    }
}

// Menu based calculator
void task3() {
    // Menu variable for selection
    int menu_selection;
    
    // Variables for calculation
    float input_float_1, input_float_2, result; 
    
    // Print Menu
    printf("[Task3]\nChoose an operation you'd like to do:\n");
    printf("1.) Addition\n2.) Subtraction\n3.) Multiplication\n4.) Division\n\n>> ");

    // Menu Selection
    scanf("%d",&menu_selection);

    // Menu Logic
    switch (menu_selection)
    {
    // Addition Case
    case 1:
        // Take input
        printf("Input 2 Numbers to add: ");
        scanf("%f %f", &input_float_1, &input_float_2);

        result = input_float_1 + input_float_2; // add
        // Print output
        printf("[Result] %.2f + %.2f = %.2f\n\n", input_float_1, input_float_2, result);
        break;
    // Subtraction Case
    case 2:
        // Take input
        printf("Input 2 Numbers to Subtract (The second number will subtract the first): ");
        scanf("%f %f", &input_float_1, &input_float_2);

        result = input_float_1 - input_float_2; // Subtract
        // Print output
        printf("[Result] %.2f - %.2f = %.2f\n\n", input_float_1, input_float_2, result);
        break;
    // Multiplication Case
    case 3:
        // Take input
        printf("Input 2 Numbers to multiply: ");
        scanf("%f %f", &input_float_1, &input_float_2);

        result = input_float_1 * input_float_2; // Multiply
        // Print output
        printf("[Result] %.2f x %.2f = %.2f\n\n", input_float_1, input_float_2, result);
        break;
    // Division Case
    case 4:
        // Take input
        printf("Input 2 Numbers to divide (numerator then denominator): ");
        scanf("%f %f", &input_float_1, &input_float_2);

        // Check second number variable
        // To preven divide-by-zero-error
        if (input_float_2 == 0.0) {
            printf("Divide by Zero Error\n\n");
        } else {
            // Calculate After Validating
            result = input_float_1 / input_float_2; // Divide
            // Print output
            printf("[Result] %.2f / %.2f = %.2f\n\n", input_float_1, input_float_2, result);
        }
        break;
    default:
        // Bad option
        printf("Please Select a Valid Menu Option\n\n");
        task3(); // Recursively call task
        break;
    }
}

// Leap year calculator
void task4() {
    int year; // Year variable

    // Take Input
    printf("[Task4]\nSelect a year to evaluate: ");
    scanf("%d", &year);

    // Divisible by 4 AND not divisible by 100
    // OR divisible by 400
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
        printf("%d is a leap year", year); // pass result
    } else {
        printf("%d is NOT a leap year", year); // fail result
    }
}

int main(int argc, char const *argv[])
{
    // Run Tasks
    task1();
    task2();
    task3();
    task4();
    return 0;
}
