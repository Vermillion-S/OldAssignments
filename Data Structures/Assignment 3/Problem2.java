import java.util.Random;

public class Problem2 {
    //create a randomized array
    public static int[] randArray(int size) {
        // initialize array
        int[] array = new int[size];
        // create rng generator
        Random rand = new Random();

        // iterate through array and add a random number
        for (int i = 0; i < size; i++) {
            array[i] = rand.nextInt(1000);
        }
        // return the array
        return array;
    }
    // Selection Sort Algorithm
    public static long SelectionSortTime(int[] array) {
        long startTime = System.nanoTime();

        int n = array.length;
        for (int i = 0; i < n-1; i++) {
            int minIndex = i;
            for (int j = i+1; j < n; j++) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = array[minIndex];
            array[minIndex] = array[i];
            array[i] = temp;
        }
        long endTime = System.nanoTime();

        return endTime - startTime;
    }
    // bubble sort algorithm
    public static long BubbleSortTime(int[] arr) {
        long startTime = System.nanoTime();
        boolean swapped;
        int i,j,temp;
        int n = arr.length;
        
        for (i = 0; i < n - 1; i++) {
            swapped = false;
            for (j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    
                    // Swap arr[j] and arr[j+1]
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // If no two elements were
            // swapped by inner loop, then break
            if (swapped == false)
                break;
        }
            
        long endTime = System.nanoTime();

        return endTime - startTime;
    }

    // Merge Sort Algorithm
    public static long MergeSortTime(int[] array) {
        long startTime = System.nanoTime();
        
        mergeSort.MergeSort(array);
        
        long endTime = System.nanoTime();

        return endTime - startTime;
    }
    
    // Quick Sort Algorithm
    public static long QuickSortTime(int[] array) {
        long startTime = System.nanoTime();
        quickSort.qSort(array, 0, array.length-1);
        long endTime = System.nanoTime();

        return endTime - startTime;
    }

    
    public static void main(String[] args) {
        System.out.printf("%-9s | %-20s %-20s %-20s %-20s%n","Array Size", "Selection Sort","Bubble Sort","Merge Sort","Quick Sort");
        System.out.println("----------------------------------------------------------------------------------------");
        
        int arraySize = 50000;
        System.out.printf(" %-9s | %-20s %-20s %-20s %-20s%n",
        arraySize,
        SelectionSortTime(randArray(arraySize)), 
        BubbleSortTime(randArray(arraySize)),
        MergeSortTime(randArray(arraySize)),
        QuickSortTime(randArray(arraySize)));

        arraySize = 100000;
        System.out.printf(" %-9s | %-20s %-20s %-20s %-20s%n",
        arraySize,
        SelectionSortTime(randArray(arraySize)), 
        BubbleSortTime(randArray(arraySize)),
        MergeSortTime(randArray(arraySize)),
        QuickSortTime(randArray(arraySize)));

        arraySize = 150000;
        System.out.printf(" %-9s | %-20s %-20s %-20s %-20s%n",
        arraySize,
        SelectionSortTime(randArray(arraySize)), 
        BubbleSortTime(randArray(arraySize)),
        MergeSortTime(randArray(arraySize)),
        QuickSortTime(randArray(arraySize)));

        arraySize = 200000;
        System.out.printf(" %-9s | %-20s %-20s %-20s %-20s%n",
        arraySize,
        SelectionSortTime(randArray(arraySize)), 
        BubbleSortTime(randArray(arraySize)),
        MergeSortTime(randArray(arraySize)),
        QuickSortTime(randArray(arraySize)));
        
        arraySize = 250000;
        System.out.printf(" %-9s | %-20s %-20s %-20s %-20s%n",
        arraySize,
        SelectionSortTime(randArray(arraySize)), 
        BubbleSortTime(randArray(arraySize)),
        MergeSortTime(randArray(arraySize)),
        QuickSortTime(randArray(arraySize)));

        arraySize = 300000;
        System.out.printf(" %-9s | %-20s %-20s %-20s %-20s%n",
        arraySize,
        SelectionSortTime(randArray(arraySize)), 
        BubbleSortTime(randArray(arraySize)),
        MergeSortTime(randArray(arraySize)),
        QuickSortTime(randArray(arraySize)));
        
        
    }
}
