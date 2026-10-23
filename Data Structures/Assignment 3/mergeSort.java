public class mergeSort {
    //
    public static void merge(int[] ar1, int[] ar2, int[] temp) {
        int c1 = 0, c2 = 0, c3 = 0;

        // incriment each element of the 2 arrays
        while (c1 < ar1.length && c2 < ar2.length) {
            // compare elements
            // and add them based on compared size
            if (ar1[c1] < ar2[c2]) {
                temp[c3++] = ar1[c1++];
            } else {
                temp[c3++] = ar2[c2++];
            }
        }

        // add left over elements

        while (c1 < ar1.length) {
            temp[c3++] = ar1[c1++];
        }

        while (c2 < ar2.length) {
            temp[c3++] = ar2[c2++];
        }        
    }
    // merge sort is recursive so we have to put it in its own fucntion
    public static void MergeSort(int[] array) {
        if (array.length > 1) {
            // split array in half recursively

            int[] firstHalf = new int[array.length / 2];
            System.arraycopy(array, 0, firstHalf, 0, array.length / 2);
            MergeSort(firstHalf);

            int secondLength = array.length - (array.length / 2);
            int[] secondHalf = new int[secondLength];
            System.arraycopy(array, array.length / 2, secondHalf, 0, secondLength);
            MergeSort(secondHalf);

            // remerge the arrays, sorting as you go
            merge(firstHalf, secondHalf, array);
        }
    }
}
