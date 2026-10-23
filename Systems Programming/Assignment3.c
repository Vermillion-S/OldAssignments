#include <stdio.h>
#include <ctype.h>
// Maxwell Cunningham Assingment 3
int main(int argc, char const *argv[])
{
    // Variables
    int age;
    float gpa;
    char grade;
    
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
    
    // Input Grade (Between A - F)
    do {
        printf("Enter your grade: ");
        scanf(" %c", &grade);
    while (getchar() != '\n');
    } while((toupper(grade) < 'A' || toupper(grade) > 'F'));
    
    // Output formatted input
    printf("\n--- Student Information ---\n");
    printf("Age: %d\n", age);
    printf("GPA: %.2f\n", gpa);
    printf("Grade: %c\n", grade);
    return 0;
}
