public class quickSort {
    // find the pivot point of the array
    public static int partition(int[] array, int first, int last) {
        int pivot = array[first], low = first + 1, high = last;

        // Start from different ends of the array
        while (high > low) {
            // Incriment up
            while (low <= high && array[low] <= pivot) {
                low++;
            }
            // Incriment down
            while (low <= high && array[high] > pivot) {
                high--;
            }
            // swap elements based on size
            if (high > low) {
                int temp = array[high];
                array[high] = array[low];
                array[low] = temp;
            }
        }

        while (high > first && array[high] >= pivot) {
            high--;
        }

        // return pivot point
        if (pivot > array[high]) {
            array[first] = array[high];
            array[high] = pivot;
            return high;
        } else {
            return first;
        }
    }
    public static void qSort(int[] array, int first, int last) {
        if (last > first) {
            // find middle point and swap elements along them
            int pivot = partition(array, first, last);
            // repeat for each half of the array
            qSort(array, first, pivot -1);
            qSort(array, pivot + 1, last);
        }
    }
}
