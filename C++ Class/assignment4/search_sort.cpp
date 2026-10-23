#include <iostream>

using namespace std;

// Search algorithms
int linearSearch(int[], int, int);
int binarySearch(int[], int, int);

// Sorting algorithms
void bubbleSort(int[], int);
void selectionSort(int[], int);

void swap(int &, int &);

int main()
{
    int size, choice, target;
    // Initialize The array
    cout << "Length of List: ";
    cin >> size;
    int arr[size];

    // Take user input for array
    cout << "Enter Values: ";
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }

    // Choosing Sorting Algorithm
    cout << "Sorting method: \n1. Bubble Sort \n2. Selection Sort\nEnter choice (1/2): ";
    cin >> choice;
    
    if (choice == 1)
        bubbleSort(arr, size);
    else if (choice == 2)
        selectionSort(arr, size);
    else {
        cout << "Invalid choice!";
        return 1;
    }
    // Print Sorted Array
    cout << "Sorted array: ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    // Select Target
    cout << "Enter target number to search: ";
    cin >> target;
    // Select Search Algorithm
    cout << "Choose search method: \n1. Linear Search \n2. Binary Search Sort\nEnter choice (1/2): ";
    cin >> choice;
    
    int result; // Initialize result variable

    if (choice == 1)
        result = linearSearch(arr, size, target);
    else if (choice == 2)
        result = binarySearch(arr, size, target);
    else {
        cout << "Invalid choice!";
        return 1;
    }
    // -1 means result was not found
    if (result != -1)
        cout << "Element found at index: " << result << endl;
    else
        cout << "Element not found." << endl;

    return 0;
}

// Iterates through every index in the array
// and compares it to find the target value
int linearSearch(int arr[], int size, int target) {
    //iterate through the whole array
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) //compare current index with target value
            return i;  // Return index if found
    }
    return -1;  // Return -1 if not found
}

// Finds target value by constantly
// cutting the array in half
int binarySearch(int arr[], int size, int target) {
    // initialize left and right bounds
    int left = 0, right = size - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2; // calculate the current middlepoint
        
        if (arr[mid] == target)
            return mid; // Return index if found
        else if (arr[mid] < target)
            left = mid + 1; // target to the right of the current array
        else
            right = mid - 1; // target is to the left of the current array
    }
    return -1; // Return -1 if not found
}

// Shifts the largest value to the
// end until the array is sorted
void bubbleSort(int arr[], int size) {
    // iterate through whole array
    for (int i = 0; i < size - 1; i++) {
        // cut off last value from next iteration
        for (int j = 0; j < size - i - 1; j++) {
            // if the left value is larger
            // than the right, swap them
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Searches for the smallest value and swaps it 
// with the leftmost index in current iteration
void selectionSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        int minIndex = i;
        //cut off left most value in next every iteration
        for (int j = i + 1; j < size; j++) {
            // if current index is smaller,
            // it is the new minIndex
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        //swap the left value with the smallest current value
        swap(arr[i], arr[minIndex]);
    }
}

// swaps the contents of two variables
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}