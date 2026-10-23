#include <stdio.h>

int main(int argc, char const *argv[])
{
    
    // Number Variables
    int a, b, c;

    // Take user input
    printf("Enter 3 Integers: ");
    scanf("%d %d %d", &a, &b, &c);

    // Formatted table
    // Print formatting works with the following structure
    // %[flags][width][.precision][length]specifier
    printf("\n-----------------\n");
    printf("Number 1 : %5d\n", a);
    printf("Number 2 : %5d\n", b);
    printf("Number 3 : %5d\n", c);
    printf("-----------------");
    return 0;
}
