#include <stdio.h>

/*
    Maxwell Cunningham
    Feb 26 2026

    Assignment 5 Submission
    Each function represents its own task
*/

void task1() {
    // Double variables
    double a,b,c;
    
    // Take Input
    printf("Intput 3 floats: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    // Calculate Doubles
    double E1 = (a + b) * c;
    double E2 = a + (b * c);
    double E3 = (a / b) + c;
    double E4 = (int)a / (int)b;
    double E5 = (double)((int)a) / (int)b;
    
    // Display Formatted Results
    printf("E1: %.2lf\n", E1);
    printf("E2: %.2lf\n", E2);
    printf("E3: %.2lf\n", E3);
    printf("E4: %lf\n", E4);
    printf("E5: %lf\n", E5);
}

/* Task 2
   For int x=7 y=3, z=2; ...
        1) x + y * z = 13
            Multiplication is done before addition; 3 * 2 = 6; 6 + 7 = 13
        
        2) (x + y) * z = 20
            Parentheses are done first; 7 + 3 = 10; 10 * 2 = 20 
        
        3) x / y * z = 4
            Integers discard remainders when dividing; 7 / 3 = 2.33333, 
            (or in this case just 2), and 2 * 2 = 4
        
        4) x % y + z = 2
            Modulo results in the remainder of the division; 
            7 / 3 has a remainder of 1; 1 * 2 = 2
        
        5) x == y || z > 1 = 1
            7 does not equal 3, so its false; 2 is greater than 1, 
            so it is true, leaving us with the expression false || true. 
            || is an or operator, so if one expression is true, then the 
            entire expression is true. So the result is true (or 1)
*/ 

// Scholarship calculation
void task3() {

    // Declare Input variables
    int age; 
    double gpa;
    int has_discipline_case;

    // input Age
    printf("input age: ");
    scanf("%d", &age);

    // Input Gpa
    printf("input GPA: ");
    scanf("%lf", &gpa);

    do
    {
        // Input discipline case
        printf("input if student has a discipline case (0 for no 1 for yes): ");
        scanf("%d", &has_discipline_case);
      
      // Verify input
    } while (has_discipline_case != 0 && has_discipline_case != 1);
    

    // Eligability Calculation
    printf("Eligible: ");
    if (age > 18 && gpa >= 3.0 && has_discipline_case == 0) {
        printf("Yes"); // Pass result
    } else {
        printf("No"); // fail result
    }

    // Scholarship Calculation
    printf("\nScholarship: ");
    if (gpa >= 3.7 && age <= 25) {
        printf("Yes\n"); // Pass Result
    } else {
        printf("No\n"); // Fail Result
    }
}

// Bitwise Flags and masks
void task4() {
    // Flag variable
    unsigned int flags;
    
    // Input flag
    do
    {
        printf("Input (0 - 15): ");
        scanf("%u", &flags);
    } while (flags < 0 || flags > 15);

    // Checks if a bit position is 1 using the
    // Formula: "number & (1 << bit_position_to_check)"
    // Returns non-zero value on pass
    // variables store the result as 0 or 1
    int IS_STUDENT = (flags & (1 << 0)) > 0;
    int IS_EMPLOYEE = (flags & (1 << 1)) > 0;
    int HAS_PARKING = (flags & (1 << 2)) > 0;
    int HAS_LIBRARY_ACCESS = (flags & (1 << 3)) > 0;

    // Prints flag status (0 = No, 1 = Yes)
    printf("IS_STUDENT: %s\n", (IS_STUDENT) ? "Yes" : "No");
    printf("IS_EMPLOYEE: %s\n", (IS_EMPLOYEE) ? "Yes" : "No");
    printf("HAS_PARKING: %s\n", (HAS_PARKING) ? "Yes" : "No");
    printf("HAS_LIBRARY_ACCESS: %s\n", (HAS_LIBRARY_ACCESS) ? "Yes" : "No");

    // Calculates access level
    // Since flags are either 0 or 1,
    // it can be used to mask whether we add a value
    int access_level = (10 * HAS_LIBRARY_ACCESS) 
                     + (5 * HAS_PARKING) 
                     + (3 * IS_EMPLOYEE) 
                     + (1 * IS_STUDENT);

    // Print Access Level
    printf("Access Level: %d\n", access_level);
}

void task5() {
    double num, den;

    printf("Input Numerator then Denomenator: ");
    scanf("%lf %lf", &num, &den);

    // If the denominator is not 0, perform and print the division
    // Else print "Division by zero"
    (den !=0) ? printf("Result: %lf", num / den) : printf("Division by zero");
}

/*  Task 6
    
    All of the below examples overlap both incrimenting and 
    assignment operators. Best practice dictates that a line of code 
    should only have one side effect, to prevent undefined behavior.

    1)	x =	x++ + 5; 
    Rewrite as x++; 
               x += 5;

    2)	y =	++y + y++;
    Rewrite as ++y; 
               y++;
    
    3)	z =	(a++) + (a++);
    Rewrite as a++; 
               z = a; 
               a++; 
               z += a;
*/

int main(int argc, char const *argv[])
{
    task1();
    task3();
    task4();
    task5();
    return 0;
}
