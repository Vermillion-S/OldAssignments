#include <stdio.h>
#include <ctype.h>
// Maxwell Cunningham Assingment 3
int main(int argc, char const *argv[])
{
    // Variables
    char fName[30], lName[30]; // First Name & Last name
    int age; // Age int
    float gpa; // Gpa float
    
    // Input Firstname
    do {
        printf("Enter First Name: ");
        scanf("%s", &fName);
    } while (getchar() != '\n');

    // Input Lastname
    do {
        printf("Enter Last Name: ");
        scanf("%s", &lName);
    } while (getchar() != '\n');

    // Input age (Must be a positive integer)
    do {
        printf("Enter your age: ");
        scanf("%d", &age);
        while (getchar() != '\n');
    } while(age < 0);
    
    // Input GPA (between 0.0 - 5.0)
    do {
        printf("Enter your GPA: ");
        scanf("%f", &gpa);
        while (getchar() != '\n');
    } while(gpa < 0.0 || gpa > 5.0);
    
    
    // Output formatted input
    printf("\n===== Student Information =====\n");
    // Print First and Last Name Together
    printf("Name: %s %s\n", fName, lName);
    // Print Age
    printf("Age : %d years old\n", age);
    // 2 decimal precision
    printf("GPA : %.2f\n", gpa);
    printf("===============================");
    return 0;
}
