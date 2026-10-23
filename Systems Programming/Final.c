/*

    Maxwell Cunningham
    Systems Programming
    Final Project: Student Record Management System in C
    05/08/2026

*/

#include <stdio.h>
#include <string.h>

// Function Headers
void addStudent();
void displayAllRecords();
float calculateAverageScore();
float findHighestScore();
float findLowestScore();
void searchStudent(int);
void clearbuffer();

// Tracks the index location of the next available entry
int entrycrawler = 0;

// Global Data arrays (Data of the Same entry will have the same Index)
int students_ID[50]; // student id
char students_Name[50][50]; // student name
int students_Age[50]; // student age
float students_Score[50]; // student score

// main input loop for menu
int main(int argc, char const *argv[])
{   
    int escape = 0; // Excape Case Boolean
    
    // Program Loop
    do
    {
        // Variable for Menu Input
        int choice;
        
        // Menu Display
        printf("Menu Options\n");
        printf("1. Add Student Records\n");
        printf("2. Display All Student Records\n");
        printf("3. Calculate Average Score\n");
        printf("4. Find Highest Score\n");
        printf("5. Find Lowest Score\n");
        printf("6. Search by Student ID\n");
        printf("7. Exit\n");
        printf(">> ");

        // User input
        if (scanf("%d", &choice) == 1) {} else {
            printf("Invalid Datatype\n");
            clearbuffer(); 
            continue;
        }

        // Menu Options
        switch (choice)
        {
        case 1: // Add Student Records

            // Call Add student function
            addStudent();
            break;
        
        case 2: // Display All Student Records

            // Skip if no Student Entries
            if (entrycrawler == 0) {
                printf("Ensure there is at least 1 entry to calculate from\n\n");
                break;
            }

            // Call Display All Records Function
            displayAllRecords();

            break;

        case 3: // Calculate Average Score

            // Skip if no Student Entries
            if (entrycrawler == 0) {
                printf("Ensure there is at least 1 entry to calculate from\n\n");
                break;
            }

            // Call Average Function and print result
            float average = calculateAverageScore();
            printf("Average Score: %.2f\n", average);

            break;
        case 4: // Find Highest Score

            // Skip if no Student Entries
            if (entrycrawler == 0) {
                printf("Ensure there is at least 1 entry to calculate from\n\n");
                break;
            }

            // Call Highest Score Function and print result
            float max = findHighestScore();
            printf("Highest Score: %.2f\n", max);

            break;

        case 5: // Find Lowest Score

            // Skip if no Student Entries
            if (entrycrawler == 0) {
                printf("Ensure there is at least 1 entry to calculate from\n\n");
                break;
            }

            // Call Lowest Score Function and print result
            float min = findLowestScore();
            printf("Lowest Score: %.2f\n", min);

            break;

        case 6: // Search Student By ID
            
            // Skip if no Student Entries
            if (entrycrawler == 0) {
                printf("Ensure there is at least 1 entry to calculate from\n\n");
                break;
            }

            // Take Id INput
            int id; // Input Variable
            printf("Submit Student ID: ");
            if (scanf("%d", &id) == 1) {} else {
                printf("Invalid Datatype\n");
                clearbuffer(); 
                continue;
            }

            // Call Searc Student Function with passed input variable
            searchStudent(id);
            break;

        case 7: // Exit Case

            escape = 1; // Set Exit flag
            break;

        default: // Bad Input Case
            
            // Just continue the loop
            break;
        }
      
    } while (escape != 1); // Loop until Exit Flag == 1
    
    return 0; // terminate program
}

// Adds a new student record to our arrays based on user input
void addStudent() {

    // Input Variables

    int id; // Student Id
    char name[50]; // Student Name
    int age; // Student age
    float score; // Student score
    
    // Input ID
    printf("Enter Student ID: ");
    if (scanf("%d", &id) == 1) {} else {
        // wrong datatype case
        printf("Invalid Datatype\n");
        clearbuffer(); 
        return;
    }

    clearbuffer();

    // Input Student Name
    // Using fgets to include spaces
    printf("Enter Student Name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = 0; // Strip newline character

    // Input Student Age
    printf("Enter Student Age: ");
    if (scanf("%d", &age) == 1) {} else {
        // wrong datatype case
        printf("Invalid Datatype\n");
        clearbuffer(); 
        return;
    }

    // Input Test Score
    printf("Enter Student Score: ");
    scanf("%f", &score);

    // Length of ID array
    int length = sizeof(students_ID) / sizeof(students_ID[0]);
    int i; // loop iterator

    // Check if more entries can be added
    if (entrycrawler == length) {
        // Exit if not
        printf("Reached maximum limit of entries\n\n");
        return;
    }

    // Check if test score is valid
    if (score > 100.0 || score < 0.0) {
        // Error case
        printf("Please submit a valid test score\n\n");
        clearbuffer();
        return;
    }

    // Add new Entry

    // skip id comparison if this is the first entry
    if (entrycrawler == 0) {

        students_ID[0] = id; // submit id
        strcpy(students_Name[0], name); // submit name
        students_Age[0] = age; // submit age
        students_Score[0] = score; // submit score
        entrycrawler++; // incriment entry crawler variable

        return; // exit function early
    }

    // Check for duplicate IDs up to the last submitted entry
    for (i = 0; i <= entrycrawler; i++) {
        // if duplicate exits...
        if (students_ID[i] == id) {
            // Exit
            printf("Student id already exits\n");
            return;
        }
    }

    // Set index for entries
    int loc = entrycrawler;

    students_ID[loc] = id; // submit id
    strcpy(students_Name[loc], name); // submit name
    students_Age[loc] = age; // submit age
    students_Score[loc] = score; // submit score

    entrycrawler++; // incriment entry crawler variable
   
}

// Displays all student records formatted
void displayAllRecords() {

    int i; // loop iterator

    // loop through all used enries
    for (i = 0; i < entrycrawler; i++) {

        // Display student information
        printf("Student ID: %d\n", students_ID[i]);
        printf("Student Name: %s\n", students_Name[i]);
        printf("Student Age: %d\n", students_Age[i]);
        printf("Student Score: %.2f\n\n", students_Score[i]);
    
    }
}

// Calculates the average of all submitted test scores
float calculateAverageScore() {

    float count = 0.0; // running total
    int i; // loop iterator
    
    // Loop through all score entries
    for (i = 0; i < entrycrawler; i++) {

        // add score to running total
        count += students_Score[i]; 

    }

    // Return average (total divided by number of entries)
    return (count / (float)entrycrawler);
}

// Finds and returns the highest test score
float findHighestScore() {

    float currentHighests = 0.0; // variable for highest score found
    int i; // loop iterator
    
    // Loop through all score entries
    for (i = 0; i < entrycrawler; i++) {

        // if the score is higher than our previous highest recorded score...
        if(students_Score[i] > currentHighests) {
            
            // make it the new highest
            currentHighests = students_Score[i];

        }
    }

    // return the highest score
    return currentHighests;
}

// Finds and returns the lowest test score
float findLowestScore() {

    float currentLowest = 100.00; // variable for lowest score found
    int i; // loop iterator
    
    // loop through all score entries
    for (i = 0; i < entrycrawler; i++) {
        
        // if the score is lower than our previous lowest recorded score...
        if(students_Score[i] < currentLowest) {

            // make it the new lowest
            currentLowest = students_Score[i];

        }
    }
    
    // return the lowest score
    return currentLowest;
}

// Looks through entries for a matching id, and print related information
void searchStudent(int id) {

    int i; // loop iterator
    // Look through all ids

    for (i = 0; i <= entrycrawler; i++) {
        // if the index has the id...
        if (students_ID[i] == id) {

            // print other entries for that index
            printf("Student Name: %s\n", students_Name[i]); // print name
            printf("Student Age: %d\n", students_Age[i]); // print age
            printf("Student Score: %.2f\n\n", students_Score[i]); // print score
            
            return; // exit function since we found what we wanted

        }
    }

    // If we don't find a match, say so
    printf("Student does not exist\n\n");
    return;
}

// To prevent subsequent effects of erronious inputs
void clearbuffer() {
    // Clear newline from the buffer
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}