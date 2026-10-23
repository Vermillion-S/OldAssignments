/*

    Maxwell Cunningham - Systems Programming

    Assignment 8

*/

#include <stdio.h>

int main(int argc, char const *argv[])
{
    // Initialize variables
    int age; // age integer
    float height; // height floating point number
    double GPA; // GPA double [long float]
    char grade; // Grade Character

    // Input integer (%d)
    printf("Enter your age: ");
    scanf("%d",&age);

    // Input Float (%f)
    printf("Enter your height: ");
    scanf("%f",&height);

    // Input Double (%lf)
    printf("Enter your GPA: ");
    scanf("%lf",&GPA);

    // Input Character (%c)
    printf("Enter your grade: ");
    scanf(" %c",&grade);

    // Output Variable Data
    printf("\n--- Student Information ---\n");
    printf("Age: %d\n", age); // Print age
    printf("Height: %f\n", height); // Print height
    printf("GPA: %lf\n", GPA); // Print GPA
    printf("Grade: %c", grade); // Print Grade
    
    return 0;
}