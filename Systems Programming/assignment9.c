#include <stdio.h>

/*

    Maxwell Cunningham - Systems Programming

    Assignment 9
    
*/ 



int main(int argc, char const *argv[])
{
    // Array Length variable
    // Saving it externally to be reused for interative looping
    int arrayLength = 5;

    // Initializing the array to contain 5 integer objects
    int Array[arrayLength];

    int i; // loop counter variable

    // Input loop
    printf("Enter 5 integers:\n");
    // for each slot in the array...
    for (i = 0; i < arrayLength; i++) {
        // take a user inputted value and submit it into the array value
        scanf("%d", &Array[i]); 
    }

    // Sum, largest value, and smallest value variables
    
    // Set currentSmallest to an arbitrarally large value 
    // so it is replaced by the first array value
    int sum = 0, currentLargest = 0, currentSmallest = __INT32_MAX__;

    // Loop through array elements
    printf("\nArray elements:\n");
    for (i = 0; i < arrayLength; i++) {
        // Save array element to a new variable for convenience
        int num = Array[i];

        printf("%d ", num); // print array element

        sum += num; // Add current array element to our sum
        
        // Check if it is larger than our current Largest value
        if (num > currentLargest) {
            // If so make it the new current Largest
            currentLargest = num;
        }

        // Check if it is smaller than our current Smallest value
        if (num < currentSmallest) {
            // If so make it the new current Smallest
            currentSmallest = num;
        }
    }

    // Calculate average (Sum / number of values)
    float average = (float)sum / arrayLength;

    // Print our array statisitics
    printf("\n\n");
    printf("Sum = %d\n", sum); // Print sum
    printf("Average = %.2f\n", average); // Print average
    printf("Largest = %d\n", currentLargest); // Print Largest value
    printf("Smallest = %d\n", currentSmallest); // Print Smallest Value

    return 0;
}